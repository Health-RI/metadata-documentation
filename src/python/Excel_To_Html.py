"""
Generate HTML bikeshed  Excel files from Health-RI metadata Excel.

This script converts the Health-RI metadata Excel file to Bikeshed-flavored Markdown -compatible
format that can be rendered: pre-processor source document (containing only the actual spec content, plus several shorthands for linking to terms and other things) into a final spec document, with appropriate boilerplate, bibliography, indexes, etc all filled in. imported into SHACLPlay for SHACL shape editing.
"""

import traceback
from pathlib import Path
import pandas as pd
import json
import re

# Helper functions for link injection
def linkify_property_label(row, links):
    label = row.get("Property label")
    uri = row.get("Property URI")

    # Safety
    if not isinstance(label, str) or not isinstance(uri, str):
        return label

    # Ignore class IRIs like "dcat:Dataset (IRI)"
    if "(IRI)" in uri:
        return label

    # If URI found in canonicalLinks → make label clickable
    if uri in links["canonicalLinks"]:
        url = links["canonicalLinks"][uri]
        return f'<a href="{url}">{label}</a>'

    return label

import re

def linkify_usage_note(value):
    if isinstance(value, str):
        return re.sub(
            r"controlled vocabulary",
            '<a href="#controlled-vocabularies">controlled vocabulary</a>',
            value,
            flags=re.IGNORECASE
        )
    return value


# Configuration
# EXCEL_FILE_PATH = "./inputs/filename.xlsx"
EXCEL_FILE_PATH = "../excel/HealthRI_v2.0.2.xlsx"
FOLDER_NAME = "property"
OUTPUT_PATH = Path("../") / FOLDER_NAME

def main():
    """Main conversion function."""
    print("=" * 80)
    print("HTML Generator")
    print("=" * 80)
    print()

    # Create output directory
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    # Initialize converter
    # print(f"Loading template from {TEMPLATE_PATH}...")
    # print(f"Loading prefixes from {EXCEL_FILE_PATH}...")
    #converter = SHACLPlayConverter(TEMPLATE_PATH, Path(EXCEL_FILE_PATH))

    # Read the classes sheet to get configuration for each class
    print(f"Reading classes configuration from {EXCEL_FILE_PATH}...")
    classes_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='classes')
    print(f"  Found {len(classes_df)} classes to process")
    print()

    # STEP 3: Load link registry
    LINKS_FILE = Path(__file__).parent / "links.json"

    with open(LINKS_FILE, "r", encoding="utf-8") as f:
        links = json.load(f)

    # For now, just print what we loaded (so we know it works)
    print("Loaded link registry with:")
    print(" -", len(links["prefixes"]), "prefixes")
    print(" -", len(links["canonicalLinks"]), "canonical links")
    print(" -", len(links["rawURLs"]), "raw URLs")


    # Process each class
    for idx, class_row in classes_df.iterrows():
        sheet_name = class_row['sheet_name']
        ontology_name = class_row['class_URI']
        target_class = class_row['SHACL_target_ontology_name']
        description = class_row.get('description', None)

        print(f"Processing {sheet_name} class...")
        print(f"  Ontology: {ontology_name}")
        print(f"  Target: {target_class}")

        try:
            # Read the class sheet from Health-RI Excel
            class_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=sheet_name)
            class_df = class_df[[
                "Property label",
                "Definition",
                "Property URI",
                "Range",
                "Cardinality",
                "Usage note",
                "Controlled vocabluary (if applicable)"
            ]]

            # REMOVE empty rows (this fixes your NaN rows problem!)
            class_df = class_df.dropna(how="all")

            print(f"  Loaded {len(class_df)} properties")
            print("COLUMNS FOUND:")
            for col in class_df.columns:
                print(repr(col))

            # Extract class name
            class_name = ontology_name.split(":")[-1]

            # Load output file name and path
            output_file = OUTPUT_PATH / f"properties-{sheet_name.lower()}.html"


### apply toepassen hier
            ## Convert NaN to None for description
            if pd.isna(description):
                description = None
            if not description or str(description).strip().lower() in ("NA", "nan", "none"):
                description = None

            print(f"  ✓ Generated {output_file}")
            print()

            # Show DataFrame (optional)
            print(class_df)

            # Make ONLY the Property label clickable
            class_df["Property label"] = class_df.apply(
                lambda row: linkify_property_label(row, links),
                axis=1
            )

            # Make "controlled vocabulary" clickable inside Usage note
            def enhance_usage_note(row):
                value = row["Usage note"]

                if (
                        pd.notna(row["Controlled vocabluary (if applicable)"]) and
                        isinstance(value, str)
                ):
                    return (
                            value
                            + ' For this specific case please refer to the '
                            + '<a href="#controlled-vocabularies">controlled vocabularies</a>.'
                    )

                return value

            class_df["Usage note"] = class_df.apply(enhance_usage_note, axis=1)


            class_df = class_df.drop(columns=["Controlled vocabluary (if applicable)"])

            # Replace Excel newlines with <br> for proper HTML rendering
            class_df = class_df.replace(r'\n', '<br>', regex=True)

            # Write to output file with escape disabled
            class_df.to_html(output_file, index=False, escape=False)



        except Exception as e:
            print(f"  ✗ Error processing {sheet_name}: {e}")
            traceback.print_exc()
            print()

    print("=" * 80)
    print("Conversion complete!")
    print(f"Output files written to {OUTPUT_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()