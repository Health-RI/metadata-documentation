## Classes # {#classes-classtext} 
The Health-RI metadata schema is based on DCAT-AP 3.0, which defines a set of classes and properties for describing datasets, services, and related resources. To make the model easier to apply and interoperable across catalogues, the schema distinguishes between: To achieve this, the schema organizes its structure around two types of classes: **Main Classes** and **Supportive Classes**.

The Health‑RI metadata schema builds on [DCAT‑AP 3.0](https://semiceu.github.io/DCAT-AP/releases/3.0.0/), a European application profile for describing datasets, services, and related resources. To make the model easier to apply and to ensure interoperability across catalogues, the schema organises its structure around two complementary types of classes:

- **Main Classes** – the core entities that form the core of the catalogue.
- **Supportive Classes** – contextual entities that provide detail to the main classes.

## Usage Notes on Schema / Mapping
This application profile follows DCAT-AP 3.0 and it separates classes into main and supportive groups to keep the model interoperable. Supportive classes are included because they form the range of properties used by the main classes [additional requirements to properties for the entity.]

Main classes are the core entities in the catalogue. They are divided into those with mandatory properties for conformance and those that are recommended for richer metadata. This is how to use those classes:


Main classes in this profile:
- **Catalog**
- **Dataset**
- **Data Service**
- **Dataset Series**
- **Distribution**.

- The main classes are [Catalog](#catalog), [Dataset](#dataset), [Data Service](#data-service), [Dataset Series](#dataset-series), [Distribution](#distribution)


Supportive classes in this profile:
- **Agent**
- **Kind**
- **Attribution**
- **Checksum**
- **Identifier**
- **Period of time**
- **Relationship**
- **Quality certificate**

- The supporting classes are [Agent](#agent), [Kind](#kind), [Attribution](#attribution), [Checksum](#checksum), [Identifier](#identifier), [Period of time](#period-of-time), [Relationship](#relationship), [Quality certificate](#quality-certificate)

This separation helps modularize metadata and makes it easier to reuse supporting elements across multiple datasets or services.
- Start with main classes – Identify the datasets, services, and distributions you need to describe.
- Link supportive classes – Use them wherever the profile specifies a property range (e.g., publisher → Agent).
- Always fill mandatory properties – This ensures your metadata is valid and interoperable.
- Add recommended properties when possible – This improves FAIRness and user experience, and increases the overall maturity of your metadata.
- Reuse supportive entities – If the same Agent or Identifier appears in multiple records, reference it rather than duplicating it.

The following sections describe each class in detail, including its role in the schema, its mandatory and recommended properties, and examples of how to populate them.



**Notes on the metadata schema / mapping**:
- We discriminate between main and supporting classes, and within each group between mandatory and recommended classes.
- Certain properties (e.g. `dct:publisher`, `dct:creator`, `dct:contactPoint`) in several of the main classes refer to the supporting classes (e.g. [`foaf:Agent`](#agent), [`vcard:Kind`](#kind)). When used, these properties will instantiate new instances of the specific supporting classes for each usage. This means that, for example, the `dct:publisher` and `dct:creator` can instantiate [`foaf:Agent`](#agent) at two separate times with different content (organisation vs. person).
- It is possible that not all main classes of the metadata schema are necessary to describe your data or the structure of your data. For example, [DataService](#data-service) or [DatasetSeries](#dataset-series) might not apply to all datasets described/onboarded in the National Health Data Catalogue.
- The power of [DCAT](https://www.w3.org/TR/vocab-dcat-3/) is that it is flexible in use, giving a data holder the ability to reflect the structure of their data by using the different classes.
- We aim to collect mapping examples from different data sources [here](https://health-ri.atlassian.net/wiki/spaces/FSD/folder/736985095). Currently, this collection only holds mapping examples to v1 though.
- Please visit Confluence for general information about the [metadata schema](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279281676/4A+Metadata+mapping) and [metadata mapping](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734/Mapping+tutorial).


## Class Properties ## {#properties-classtext} 
The main classes and supportive classes together form the Health-RI data catalogue Application Profile. The properties and their associated constraints that apply in the context of this profile, and the range of properties are listed below.
