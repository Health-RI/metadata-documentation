"""
Generate HTML bikeshed  Excel files from Health-RI metadata Excel.

This script converts the Health-RI metadata Excel file to Bikeshed-flavored Markdown -compatible
format that can be rendered: pre-processor source document (containing only the actual spec content, plus several shorthands for linking to terms and other things) into a final spec document, with appropriate boilerplate, bibliography, indexes, etc all filled in. imported into SHACLPlay for SHACL shape editing.
"""

import traceback
from pathlib import Path
import pandas as pd

# Configuration
# EXCEL_FILE_PATH = "./inputs/filename.xlsx"
EXCEL_FILE_PATH = "../excel/Metadata_CoreGenericHealth_v2_Harm.xlsx"
FOLDER_NAME = "test-property"
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

    # Process each class
    for idx, class_row in classes_df.iterrows():
        sheet_name = class_row['sheet_name']
        ontology_name = class_row['ontology_name']
        target_class = class_row['target_ontology_name']
        description = class_row.get('description', None)

        print(f"Processing {sheet_name} class...")
        print(f"  Ontology: {ontology_name}")
        print(f"  Target: {target_class}")

        try:
            # Read the class sheet from Health-RI Excel
            class_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=sheet_name)
            class_df = class_df[["Property label","Definition","Property URI","Range","Cardinality","Usage note"]]
            print(f"  Loaded {len(class_df)} properties")
            print("COLUMNS FOUND:")
            for col in class_df.columns:
                print(repr(col))

            # Extract class name
            class_name = ontology_name.split(":")[-1]

            # Load output file name and path
            output_file = OUTPUT_PATH / f"properties-{sheet_name.lower()}.md"


### apply toepassen hier
            ## Convert NaN to None for description
            if pd.isna(description):
                description = None
            if not description or str(description).strip().lower() in ("NA", "nan", "none"):
                description = None

            print(f"  ✓ Generated {output_file}")
            print()
            print(class_df)

            # Write to output file
            class_df.to_html(output_file, index=False)


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