## Classes # {#classes-classtext} 
The Health-RI metadata schema is based on DCAT-AP 3.0, which defines a set of classes and properties for describing datasets, services, and related resources. To make the model easier to apply and interoperable across catalogues, the schema distinguishes between: To achieve this, the schema organizes its structure around two types of classes: **Main Classes** and **Supportive Classes**.



# Classes # {#classes-classtext}

The Health‑RI metadata schema builds on [DCAT‑AP 3.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/), a European application profile for describing datasets, services, and related resources. To make the model easier to apply and to ensure interoperability across catalogues, the schema organises its structure around two complementary types of classes:

- **Main Classes** – the core entities that form the core of the catalogue.
- **Supportive Classes** – contextual entities that provide detail to the main classes.

## Usage Notes on Schema / Mapping

**Main classes in this profile:**
- `Catalog`
- `Dataset`
- `Dataset Series`
- `Data Service`
- `Distribution`

**Supportive classes in this profile:**
- `Agent`
- `Kind`
- `Attribution`
- `Checksum`
- `Identifier`
- `Period of time`
- `Relationship`
- `Quality certificate`

**Key points for implementers:**
- Certain properties (e.g., `dct:publisher`, `dct:creator`, `dct:contactPoint`) have values that are instances of supportive classes (e.g., `foaf:Agent`, `vcard:Kind`).
- Not all classes will apply in every case — for example, `Dataset Series` or `Data Service` may not be relevant for all datasets.
- DCAT‑AP is intentionally flexible: you can model metadata to fit your needs while still meeting the profile’s conformance requirements.
- Where DCAT‑AP specifies **mandatory** properties, these **must** be provided for conformance. **Recommended** properties should be provided when available to improve discovery and reuse.
- Controlled vocabularies listed in DCAT‑AP section 10.2 **must** be used for the relevant properties; additional domain‑specific vocabularies may be used to add value.

## Understanding the schema

This application profile uses DCAT‑AP 3.0’s core concepts to describe:

- Data catalogues (`Catalog`)
- Datasets (`Dataset`)
- Dataset series (`Dataset Series`)
- Data services (`Data Service`)
- Distributions of datasets (`Distribution`)

These are the **main classes** — the primary records that users search for and interact with.  

**Supportive classes** are included because they form the *range* (value type) of certain properties in the main classes. For example, a dataset’s `dct:publisher` property points to an `Agent`, and a distribution’s `spdx:checksum` property points to a `Checksum`. By defining these supportive classes explicitly, the profile ensures that such linked details are described consistently and can be reused across records.

## Understanding the schema
This application profile follows DCAT-AP 3.0 to describe data catalogues, datasets, dataset series, data services, and their distributions. It separates classes into main and supportive groups to keep the model interoperable. Supportive classes are included because they form the range (value type) of properties used by the main classes [additional requirements to properties for this entity.]. This section explains how to use those classes.



## Practical guidance

- **Start with main classes** – Identify the datasets, services, and distributions you need to describe.
- **Link supportive classes** – Use them wherever the profile specifies a property range (e.g., publisher → Agent).
- **Always fill mandatory properties** – This ensures your metadata is valid and interoperable.
- **Add recommended properties when possible** – This improves FAIRness and user experience.
- **Reuse supportive entities** – If the same Agent or Identifier appears in multiple records, reference it rather than duplicating it.

---

The following sections describe each class in detail, including its role in the schema, its mandatory and recommended properties, and examples of how to populate them.




## Usage Notes on Schema / Mapping
- Main classes include: **Catalog**, **Dataset**, **Data Service**, **Dataset Series**, **Distribution**.
- Supporting classes include: **Agent**, **Kind**, **Attribution**, **Checksum**, **Identifier**, **Period of time**, **Relationship**, **Quality certificate**.
- Certain properties (e.g., `dct:publisher`, `dct:creator`, `dct:contactPoint`) refer to supporting classes (e.g., `foaf:Agent`, `vcard:Kind`). These properties instantiate new instances each time they are used.
- Not all metadata schema classes may be necessary for describing your dataset. For example, **DataService** or **DatasetSeries** might not apply to every dataset in the National Health Data Catalogue.
- DCAT's flexibility enables data holders to structure their metadata according to their needs.
- Mapping examples from various data sources have been collected for reference.
- Further information on the metadata schema and guidance on metadata mapping is available.