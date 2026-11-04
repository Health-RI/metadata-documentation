# Introduction # {#introduction}

## Scope and Current State of the Schema ## {#scope-and-current-state-of-the-schema}

Version 2.1.0 of the Health-RI metadata schema defines metadata for describing health data resources in the [National Health Data Catalogue](https://catalogus.healthdata.nl/). It draws on [DCAT-AP NL](https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/) and the [OPEN variant of the HealthDCAT-AP draft dated December 16, 2024](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-6/), with documented Health-RI-specific adaptations.

This version expands Dataset descriptions with data domains (`edam:has_topic`), measurement techniques (`schema:measurementTechnique`), health conditions of interest (`hri:healthConditionOfInterest`), and anatomical coverage (`hri:anatomicalLocationCovered`). It also adds alternative dataset names, landing pages, provenance statements, and [CSVW variable descriptions](#csvw-variables) using Table Group, Table, and Column.

Selected property requirements are relaxed compared with version 2.0.3. The class and property tables in this specification define the applicable ranges, cardinalities, and usage requirements for version 2.1.0. An overview of the changes is available in the [model changelog](https://github.com/Health-RI/health-ri-metadata/blob/testing/CHANGELOG.md#v210).

CSVW variable descriptions are included for testing purposes. Their current implementation status in the National Health Data Catalogue is explained in the [CSVW Variables section](#csvw-variables).

## Used Prefixes ## {#used-prefixes}
<table class="larger-font">
  <thead>
    <tr>
      <th>Prefix</th>
      <th>Namespace IRI</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>adms</td><td>http://www.w3.org/ns/adms#</td></tr>
    <tr><td>csvw</td><td>http://www.w3.org/ns/csvw#</td></tr>
    <tr><td>dcat</td><td>http://www.w3.org/ns/dcat#</td></tr>
    <tr><td>dcatap</td><td>http://data.europa.eu/r5r/</td></tr>
    <tr><td>dct</td><td>http://purl.org/dc/terms/</td></tr>
    <tr><td>dpv</td><td>https://w3id.org/dpv#</td></tr>
    <tr><td>pd</td><td>https://w3id.org/dpv/pd#</td></tr>
    <tr><td>dqv</td><td>http://www.w3.org/ns/dqv#</td></tr>
    <tr><td>edam</td><td>http://edamontology.org/</td></tr>
    <tr><td>eli</td><td>http://data.europa.eu/eli/ontology#</td></tr>
    <tr><td>foaf</td><td>http://xmlns.com/foaf/0.1/</td></tr>
    <tr><td>hri</td><td>https://w3id.org/health-ri/metadata-vocabulary#</td></tr>
    <tr><td>oa</td><td>http://www.w3.org/ns/oa#</td></tr>
    <tr><td>owl</td><td>http://www.w3.org/2002/07/owl#</td></tr>
    <tr><td>prov</td><td>http://www.w3.org/ns/prov#</td></tr>
    <tr><td>rdf</td><td>http://www.w3.org/1999/02/22-rdf-syntax-ns#</td></tr>
    <tr><td>rdfs</td><td>http://www.w3.org/2000/01/rdf-schema#</td></tr>
    <tr><td>schema</td><td>https://schema.org/</td></tr>
    <tr><td>skos</td><td>http://www.w3.org/2004/02/skos/core#</td></tr>
    <tr><td>spdx</td><td>http://spdx.org/rdf/terms#</td></tr>
    <tr><td>time</td><td>http://www.w3.org/2006/time#</td></tr>
    <tr><td>vcard</td><td>http://www.w3.org/2006/vcard/ns#</td></tr>
    <tr><td>xsd</td><td>http://www.w3.org/2001/XMLSchema#</td></tr>
    <tr><td>healthdcatap</td><td>http://healthdataportal.eu/ns/health#</td></tr>
  </tbody>
</table>

# Overview and Diagram # {#overview-and-diagram}

An overview of the Health-RI metadata schema is presented in the UML diagram below. This UML diagram showcases primary classes (entities), excluding detailed definitions such as `rdfs:label` and `rdfs:comment`. Each block represents a class and lists its attributes (properties). Where properties reference another class, their range is displayed in pink font.

If a class is linked to another class by an arrow with a hollow triangular arrowhead, it inherits all properties from the other class (e.g., `dcat:Dataset` inherits from [`dcat:Resource`](http://www.w3.org/ns/dcat#Resource)). Other arrows represent relationships, including their types (e.g., `dcat:Dataset` connects to a [`dcat:DatasetSeries`](http://www.w3.org/ns/dcat#DatasetSeries) via [`dcat:inSeries`](http://www.w3.org/ns/dcat#inSeries)), along with cardinalities (e.g., `dcat:Dataset` connects to zero or more `dcat:DatasetSeries`). **Mandatory relationships** are marked with dark labels, while **recommended relationships** use a lighter color.

The UML diagram separates **main classes** from **supporting classes**. While relationships between main classes are indicated by arrows, supporting class relationships (except for those between the CSVW Table Group, Table, and Column classes) are not visually connected via arrows to maintain clarity in the diagram. Instead, they can be deduced from the pink-colored property ranges listed per class.

Properties derived from draft [HealthDCAT-AP](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-6/) (mostly within the `dcat:Dataset` class) are marked blue.

A tabular overview of all classes and properties—including their range, cardinality, controlled vocabulary (if applicable), and usage notes—is provided below. A reference sheet containing this information can be found [here](https://github.com/Health-RI/metadata-documentation/blob/v2.1/src/excel/HealthRI_v2.1.0.xlsx). This sheet also documents property histories (compared to v1 of the Health-RI metadata schema) and specifies the origins of new constraints (whether they stem from DCAT-AP v3, DCAT-AP NL, or HealthDCAT-AP).


<!-- Preserve the previous version-specific fragment URL. -->
<div id="uml-class-diagram-v210"></div>
## UML Class Diagram v2.1.0 ## {#uml-class-diagram}

<a href="src/images/HRI_metadata_V2.1.png" target="_blank">
  <img src="src/images/HRI_metadata_V2.1.png"
       alt="Health-RI Metadata Diagram"
       title="diagram"
       style="width: 100%; max-width: 1000px; height: auto;">
</a>

Usage directions for the properties and their associated constraints that apply in the context of this profile, and the range of properties, are listed below.
