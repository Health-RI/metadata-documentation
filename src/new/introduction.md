# Introduction # {#introduction}

## Scope and Current State of the Schema
Building on the [1st version of the metadata schema](https://github.com/Health-RI/health-ri-metadata/tree/master), version 2 aims to incorporate both [DCAT-AP NL](https://geonovum.github.io/DCAT-AP-NL30/) and the (yet-to-be-finalized) [HealthDCAT-AP](https://healthdcat-ap.github.io/), along with Health-RI-specific requirements for the [National Health Data Catalogue](https://catalogus.healthdata.nl/). It introduces several health-related properties (marked in blue in the UML diagram below), with suggested or required controlled vocabularies where applicable.

**Important Note:** HealthDCAT-AP has not yet been officially finalized and remains subject to change. Once its official release is published, Health-RI will reevaluate compatibility with HealthDCAT-AP. This version is based on the draft dated *16-12-2024*. In that draft, the cardinalities of HealthDCAT-AP vary depending on different access rights (public, restricted, non-public). For now, compliance is ensured with the [open version](https://healthdcat-ap.github.io/OPEN%20DATA%20HealthDCAT-AP%203.0.0.drawio.png), using its UML diagram for reference.

Additionally, several **ELSI**-related metadata fields, as [gathered](https://health-ri.atlassian.net/wiki/spaces/HA/pages/469893133/Metadata+rondom+gebruiksvoorwaarden+en+authenticatie+autorisatie+en+ELSI+aspecten#Catalogus) by the Health-RI ELSI team, have been included in this version 2. These fields are not mandatory but will be evaluated upon implementation in the catalogue.

To indicate the **nature of the data** (e.g., whole genome sequencing or questionnaire data), we propose using `healthdcatap:healthTheme`. For **synthetic data**, use `dct:type` with the required controlled vocabulary in the `dcat:Dataset` class.

Several classes from [DCAT-AP NL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/) and draft [HealthDCAT-AP](https://healthdcat-ap.github.io/) have been included but not further specified for Health-RI yet. This includes the **DataService** class, meaning that these classes can be used but are not yet tailored to specific dataholder needs for the National Health Data Catalogue.

  
## Used Prefixes
<table> 
  <caption></caption> 
  <thead> 
    <tr> 
      <th>Prefix</th> 
      <th>Namespace IRI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>adms</td> 
      <td>http://www.w3.org/ns/adms#</td> 
    </tr> 
    <tr> 
      <td>dcat</td> 
      <td>http://www.w3.org/ns/dcat#</td> 
    </tr> 
    <tr> 
      <td>dcatap</td> 
      <td>http://data.europa.eu/r5r/</td> 
    </tr> 
    <tr> 
      <td>dct</td> 
      <td>http://purl.org/dc/terms/</td> 
    </tr> 
    <tr> 
      <td>dpv</td> 
      <td>https://w3id.org/dpv#</td> 
    </tr> 
    <tr> 
      <td>dqv</td> 
      <td>https://www.w3.org/TR/vocab-dqv/</td> 
    </tr> 
    <tr> 
      <td>eli</td> 
      <td>http://data.europa.eu/eli/ontology#</td> 
    </tr> 
    <tr> 
      <td>foaf</td> 
      <td>http://xmlns.com/foaf/0.1/</td> 
    </tr> 
    <tr> 
      <td>owl</td> 
      <td>http://www.w3.org/2002/07/owl#</td> 
    </tr> 
    <tr> 
      <td>rdf</td> 
      <td>http://www.w3.org/1999/02/22-rdf-syntax-ns#</td> 
    </tr> 
    <tr> 
      <td>rdfs</td> 
      <td>http://www.w3.org/2000/01/rdf-schema#</td> 
    </tr> 
    <tr> 
      <td>skos</td> 
      <td>http://www.w3.org/2004/02/skos/core#</td> 
    </tr> 
    <tr> 
      <td>spdx</td> 
      <td>http://spdx.org/rdf/terms#</td> 
    </tr> 
    <tr> 
      <td>time</td> 
      <td>http://www.w3.org/2006/time#</td> 
    </tr> 
    <tr> 
      <td>vcard</td> 
      <td>http://www.w3.org/2006/vcard/ns#</td> 
    </tr> 
    <tr> 
      <td>xsd</td> 
      <td>http://www.w3.org/2001/XMLSchema#</td> <br>
    </tr> 
    <tr>
      <td>healthdcatap</td> 
      <td>To Be Determined </td> 
    </tr> 
  </tbody> 
</table>

## Overview and Diagram
An overview of the metadata schema core is presented in the UML diagram below. This UML diagram showcases primary classes (entities), excluding detailed definitions such as `rdfs:label` and `rdfs:comment`. Each block represents a class and lists its attributes (properties). Where properties reference another class, their range is displayed in pink font.

If a class is linked to another class with a closed arrow, it inherits all properties from the other class (e.g., `dcat:Dataset` inherits from `dcat:Resource`). Other arrows represent relationships, including their types (e.g., `dcat:Dataset` connects to a `dcat:DatasetSeries` via `dcat:inSeries`), along with cardinalities (e.g., `dcat:Dataset` connects to zero or more `dcat:DatasetSeries`). **Mandatory relationships** are marked with dark labels, while **recommended relationships** use a lighter color.

The UML diagram separates **main classes** from **supporting classes**. While relationships between main classes are indicated by arrows, supporting class relationships are not visually connected via arrows to maintain clarity in the diagram. Instead, they can be deduced from the pink-colored property ranges listed per class.

Properties derived from draft [HealthDCAT-AP](https://healthdcat-ap.github.io/) (mostly within the `dcat:Dataset` class) are marked blue.

A tabular overview of all classes and properties—including their range, cardinality, controlled vocabulary (if applicable), and usage notes—is provided below. A reference sheet containing this information can be found [here](Documents/Metadata_CoreGenericHealth_v2.xlsx). This sheet also documents property histories (compared to v1 of the Health-RI core metadata schema) and specifies the origins of new constraints (whether they stem from DCAT-AP v3, DCAT-AP NL, or HealthDCAT-AP).

## UML of the Profile (Version 2)
<a href="https://raw.githubusercontent.com/Health-RI/metadata-documentation/main/src/new/images/HRI_metadata_p2.png" target="_blank">
  <img src="https://raw.githubusercontent.com/Health-RI/metadata-documentation/main/src/new/images/HRI_metadata_p2.png" alt="Health-RI Metadata Diagram"">
</a>

For usage notes regarding this profile please refer to the next section.

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

 Filling in recommended properties increases the richness and maturity of your dataset’s metadata, making it more useful and FAIR‑compliant over time.

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


- **Add recommended properties when possible** – This improves FAIRness, user experience, and increases the overall maturity of your metadata.


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