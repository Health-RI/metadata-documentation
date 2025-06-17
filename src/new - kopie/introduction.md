 
 ## Introduction
 
 ### Scope and current state of the Health-RI core metadata schema
 
 Building on the [1st version of the metadata schema](https://github.com/Health-RI/health-ri-metadata/tree/master), the scope of the version 2 is to incorporate both [DCAT-AP NL](https://geonovum.github.io/DCAT-AP-NL30/) and the (yet to be finalized) [HealthDCAT-AP](https://healthdcat-ap.github.io/), as well as Health-RI specific requirements / needs for the [National Health Data Catalogue](https://catalogus.healthdata.nl/). It introduces several health-related properties (indicated in blue in the UML diagram below), with (where applicable) suggested or required controlled vocabularies.
 
 Please note that HealthDCAT-AP has currently not officially been finalized and is subject to change and further specification. Once the official release is published, we will reevaluate and make the Health-RI schema compatible with HealthDCAT-AP. The current version of the model is based on the HealthDCAT-AP draft, version of 16-12-2024. In that version, cardinalities of HealthDCAT-AP are dependent on different access rights (public, restricted, non-public). It was decided to be compliant with the [open](https://healthdcat-ap.github.io/OPEN%20DATA%20HealthDCAT-AP%203.0.0.drawio.png) version for now, and cardinalities from that UML diagram of the HealthDCAT-AP specification were used as a reference for compliance checking.
 
 In addition, several **ELSI**-related metadata fields, as [gathered](https://health-ri.atlassian.net/wiki/spaces/HA/pages/469893133/Metadata+rondom+gebruiksvoorwaarden+en+authenticatie+autorisatie+en+ELSI+aspecten#Catalogus) by the Health-RI ELSI team, are included in this version 2 of the Health-RI core metadata schema, although not mandatory. The use of these properties will be explored and evaluated once the new version is implemented in the catalogue.
 
 We propose to indicate the **nature of the data** (e.g. whole genome sequencing data, or questionnaire data) with `healthdcatap:healthTheme`. In case you are describing **synthetic data**, you can use the `dct:type` property with the required controlled vocabulary (including a value for synthetic data) in the `dcat:Dataset` class.
 
 Several classes have been included from [DCAT-AP NL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/) and draft [HealthDCAT-AP](https://healthdcat-ap.github.io/) without further specification so far at Health-RI. This includes the [DataService class](#data-service). Therefore, these classes can be used, but are not yet further modelled to reflect specific needs of dataholders for the National Health Data Catalogue.
 
 ### Used Prefixes
 
 | **Prefix**     | **Namespace IRI**                             |
 | -------------- | --------------------------------------------- |
 | `adms`         | `http://www.w3.org/ns/adms#`                  |
 | `dcat`         | `http://www.w3.org/ns/dcat#`                  |
 | `dcatap`       | `http://data.europa.eu/r5r/`                  |
 | `dct`          | `http://purl.org/dc/terms/`                   |
 | `dpv`          | `https://w3id.org/dpv#`                       |
 | `dqv`          | `https://www.w3.org/TR/vocab-dqv/`            |
 | `eli`          | `http://data.europa.eu/eli/ontology#`         |
 | `foaf`         | `http://xmlns.com/foaf/0.1/`                  |
 | `owl`          | `http://www.w3.org/2002/07/owl#`              |
 | `rdf`          | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
 | `rdfs`         | `http://www.w3.org/2000/01/rdf-schema#`       |
 | `skos`         | `http://www.w3.org/2004/02/skos/core#`        |
 | `spdx`         | `http://spdx.org/rdf/terms#`                  |
 | `time`         | `http://www.w3.org/2006/time#`                |
 | `vcard`        | `http://www.w3.org/2006/vcard/ns#`            |
 | `xsd`          | `http://www.w3.org/2001/XMLSchema#`           |
 | `healthdcatap` | TBD                                           |
 
 ### Overview and Diagram
 
 An overview of the Metadata schema core is presented in the UML diagram depicted below. The UML showcases the primary classes (entities), excluding the detailed definitions such as `rdfs:label` and `rdfs:comment`. Each block denotes a class and comprises a list of its attributes (properties). Where properties connect to another class (the range of the property is another class), this range is stated in pink font.
 If a class is connected to another class by a closed arrow, this indicates that it inherits all properties from the other class. For example, `dcat:Dataset` inherits from `dcat:Resource`. The other arrows represent relations and contain the type of relation, such as `dcat:Dataset` connects to a `dcat:DatasetSeries` via the predicate `dcat:inSeries`, and include the cardinality, such as `dcat:Dataset` can be connected via `dcat:inSeries` to zero or more `dcat:DatasetSeries`. Mandatory relationships are marked with dark labels, recommended relationships with a lighter colour.
 In the UML, we have separated the main classes from supporting classes. Relationships between main classes are indicated with arrows as described above. Relationships with supporting classes are not shown with arrows to keep a better overview in the drawing, but can still be deduced from the pink coloured ranges of the listed properties per class.
 
 Properties that are derived from draft [HealthDCAT-AP](https://healthdcat-ap.github.io/) (mostly in the `dcat:Dataset` class) are marked blue.
 
 Next to the UML, a tabular overview of all classes and properties, including their range, cardinality, controlled vocabulary (if applicable), and usage note, can be found below. The same information can be referred to in [this sheet](Documents/Metadata_CoreGenericHealth_v2.xlsx). In this sheet, we also state the history of each property (compared to v1 of the Health-RI core metadata schema) and the origin of the (new) constraint (whether it is taken from DCAT-AP v3, DCAT-AP NL or HealthDCAT-AP).
 
   UML of the Health-RI core metadata schema diagram (version 2):
 <img src="Images/2.0_plateau2/HRI_metadata_p2.png" alt="diagram" width=800 height=1100 title="diagram">
 
 **Some notes on using the metadata schema / mapping**:
 
 - We discriminate between main and supporting classes, and within each group between mandatory and recommended classes.
 
 - The main classes are [Catalog](#catalog), [Dataset](#dataset), [Data Service](#data-service), [Dataset Series](#dataset-series), [Distribution](#distribution)
 - The supporting classes are [Agent](#agent), [Kind](#kind), [Attribution](#attribution), [Checksum](#checksum), [Identifier](#identifier), [Period of time](#period-of-time), [Relationship](#relationship), [Quality certificate](#quality-certificate)
 
 - Certain properties (e.g. `dct:publisher`, `dct:creator`, `dct:contactPoint`) in several of the main classes refer to the supporting classes (e.g. [`foaf:Agent`](#agent), [`vcard:Kind`](#kind)). When used, these properties will instantiate new instances of the specific supporting classes for each usage.
 This means that, for example, the `dct:publisher` and `dct:creator` can instantiate [`foaf:Agent`](#agent) at two separate times with different content (organisation vs. person).
 
 - It is possible that not all main classes of the metadata schema are necessary to describe your data or the structure of your data. For example, [DataService](#data-service) or [DatasetSeries](#dataset-series) might not apply to all datasets described/onboarded in the National Health Data Catalogue.
 
 - The power of [DCAT](https://www.w3.org/TR/vocab-dcat-3/) is that it is flexible in use, giving a data holder the ability to reflect the structure of their data by using the different classes.
 
 - We aim to collect mapping examples from different data sources [here](https://health-ri.atlassian.net/wiki/spaces/FSD/folder/736985095). Currently, this collection only holds mapping examples to v1 though.
 
 - Please visit Confluence for general information about the [metadata schema](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279281676/4A+Metadata+mapping) and [metadata mapping](https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734/Mapping+tutorial).
 