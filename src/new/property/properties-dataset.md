<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Property label</th>
      <th>Definition</th>
      <th>Property URI</th>
      <th>Range</th>
      <th>Cardinality</th>
      <th>Usage note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>access rights</td>
      <td>Information about who access the resource or an indication of its security status.</td>
      <td>dct:accessRights</td>
      <td>dct:RightsStatement (IRI)</td>
      <td>1</td>
      <td>Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public. It is foreseen that one of the three options have to be used: public, restricted, non-public.\n&nbsp;&nbsp;&nbsp;&nbsp;Open Data (Public): The dataset is available under general open data rules, such as those covered by the High Value Datasets Implementing Regulation.\n&nbsp;&nbsp;&nbsp;&nbsp;Protected Data (Restricted): The dataset contains protected data and is accessible only under specific conditions, as outlined in regulations like the Data Governance Act.\n&nbsp;&nbsp;&nbsp;&nbsp;Sensitive Data (Non public): The dataset includes resources that may contain sensitive or personal information, falling under regulations such as the EHDS Regulation.\n\nSince most data contain personal information, these datasets will need to take the value 'non-public' for the access rights property.</td>
    </tr>
    <tr>
      <td>analytics</td>
      <td>An analytics distribution of the dataset.</td>
      <td>healthdcatap:analytics</td>
      <td>dcat:Distribution (IRI)</td>
      <td>0..n</td>
      <td>Publishers are encouraged to provide URLs pointing to document repositories where users can access or request associated resources such as technical reports of the dataset, quality measurements, usability indicators,... Note that HealthDCAT-AP mentions also API endpoints or analytics services, but these would not be Distriutions but rather DatasetServices.</td>
    </tr>
    <tr>
      <td>applicable legislation</td>
      <td>The legislation that is applicable to this resource.</td>
      <td>dcatap:applicableLegislation</td>
      <td>eli:LegalResource (IRI)</td>
      <td>1..n</td>
      <td>The ELI of the EHDS was published in March 2025 and can now be included as the applicable legislation mandating that the dataset has to be made public.\nFor health datasets, the value must include the ELI of the EHDS Regulation (http://data.europa.eu/eli/reg/2025/327/oj).\nAs multiple legislations may apply to the resource the maximum cardinality is not limited.\n\nWhile the applicable legislation indicates which legislation mandates the publication of the dataset, the legal basis property (also in Datasets) described the legal basis for initial collection and processing of (personal) data.</td>
    </tr>
    <tr>
      <td>code values</td>
      <td>Health classifications and their codes associated with the dataset</td>
      <td>healthdcatap:hasCodeValues</td>
      <td>skos:Concept (IRI)</td>
      <td>0..n</td>
      <td>Inside this property, you can provide the coding system of the dataset in the form of wikidata URI (example: https://www.wikidata.org/entity/P494 for ICD-10 ID) and the URI of the value that describes the dataset (example: https://icd.who.int/browse10/2019/en#/Y59.0 for viral vaccines)</td>
    </tr>
    <tr>
      <td>coding system</td>
      <td>Coding systems in use (ex: ICD-10-CM, DGRs, SNOMED=CT, ...)</td>
      <td>healthdcatap:hasCodingSystem</td>
      <td>dct:Standard (IRI)</td>
      <td>0..n</td>
      <td>This property provides informatio on which coding systems are in use inside your dataset. For this, wikidata URIs must be used.</td>
    </tr>
    <tr>
      <td>conforms to</td>
      <td>An established standard to which the described resource conforms.</td>
      <td>dct:conformsTo</td>
      <td>dct:Standard (IRI)</td>
      <td>0..n</td>
      <td>If your data conforms to an established standard or specification, use this property to indicate which one. The wikidata URI of the specification must be used. Example: https://www.wikidata.org/wiki/Q19597236 for FHIR.</td>
    </tr>
    <tr>
      <td>contact point</td>
      <td>Relevant contact information for the cataloged resource.</td>
      <td>dcat:contactPoint</td>
      <td>vcard:Kind</td>
      <td>1</td>
      <td>This property points to a contact point (department or person) that can answer questions about the dataset. Details on how to describe these are provided under class vcard:Kind.\nWhenever possible, use a general contact information (for example from a department) instead of contact information of an individual.</td>
    </tr>
    <tr>
      <td>creator</td>
      <td>An entity responsible for making the resource.</td>
      <td>dct:creator</td>
      <td>foaf:Agent</td>
      <td>1..n</td>
      <td>This property points to a person (known as Agent) responsible for generating the dataset. In most cases, this should be the project’s Principal Investigator, provided they consent to being listed in the catalogue. If not, the associated department or institute may be specified instead.</td>
    </tr>
    <tr>
      <td>description</td>
      <td>An account of the resource.</td>
      <td>dct:description</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>Brief description of the dataset. You can repeat this property in multiple languages. Example: ''Collection of physiological data of Healthy Brain Study participants. This collection includes measurements via biowearables for heart rate, oxygenation, systolic and diastolic measures and stress levels.''</td>
    </tr>
    <tr>
      <td>distribution</td>
      <td>An available Distribution for the Dataset.</td>
      <td>dcat:distribution</td>
      <td>dcat:Distribution (IRI)</td>
      <td>0..n</td>
      <td>Metadata element used as a key link to the class Distribution.</td>
    </tr>
    <tr>
      <td>documentation</td>
      <td>A page or document about this thing.</td>
      <td>foaf:page</td>
      <td>foaf:Document (IRI)</td>
      <td>0..n</td>
      <td>The value of this property is the IRI directing to the web-page or document about the dataset.</td>
    </tr>
    <tr>
      <td>frequency</td>
      <td>The frequency with which items are added to a collection.</td>
      <td>dct:accrualPeriodicity</td>
      <td>skos:Concept (IRI)</td>
      <td>0..1</td>
      <td>The value of this property should be the IRI from the listed controlled vocabulary indicating the frequency at which the dataset is updated.\nFor example: http://publications.europa.eu/resource/authority/frequency/WEEKLY</td>
    </tr>
    <tr>
      <td>geographical coverage</td>
      <td>Spatial characteristics of the resource.</td>
      <td>dct:spatial</td>
      <td>dct:Location (IRI)</td>
      <td>0..n</td>
      <td>The EU Vocabularies Name Authority Lists must be used for continents, countries and places that are in those lists; if a particular location is not in one of the mentioned Named Authority Lists, Geonames URIs must be used. For districts or neighbourhoods in NL, the Dutch vocab can be used. However, it might in many cases be desirable to keep the geographical coverage broader (eg. indicating that NL is covered), to not expose detailed information of subject's locations.</td>
    </tr>
    <tr>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>has version</td>
      <td>This resource has a more specific, versioned resource.</td>
      <td>dcat:hasVersion</td>
      <td>dcat:Dataset (IRI)</td>
      <td>0..n</td>
      <td>Indicate the dataset which is the other version of the current dataset.</td>
    </tr>
    <tr>
      <td>health theme</td>
      <td>A category of the Dataset or tag describing the Dataset.</td>
      <td>healthdcatap:healthTheme</td>
      <td>skos:Concept (IRI)</td>
      <td>0..n</td>
      <td>This property is a structured way to tag the dataset with different health themes. This could include, for example, the specific disease the dataset is about. More details can be provided, if desirable, in the keywords property. Current status: the HealthDCAT-AP working group is currently exploring is other sources (ontologies, thesauri) can be used for this, next to Wikidata. To access Wikidata, click on the link in the controlled vocabulary column and search for your desired theme there.</td>
    </tr>
    <tr>
      <td>identifier</td>
      <td>An unambiguous reference to the resource within a given context.</td>
      <td>dct:identifier</td>
      <td>rdfs:Literal</td>
      <td>1</td>
      <td>Current status: Health-RI is currently working on a strategy for persistant identifiers for, among other things, datasets. Until a solid solution has been found, we propose the following temporary solution:\nIf your data is published in a repository, fill in with the provided DOI (Example: https://doi.org/10.34894/ZLOYOJ). If not, use the identifier of the dataset as generated in the FAIR data point (FDP). Ensure that metadata is updated if your situation changes.</td>
    </tr>
    <tr>
      <td>in series</td>
      <td>A dataset series of which the dataset is part.</td>
      <td>dcat:inSeries</td>
      <td>dcat:DatasetSeries (IRI)</td>
      <td>0..n</td>
      <td>This property points to which Dataset Series the Dataset is part of.</td>
    </tr>
    <tr>
      <td>is referenced by</td>
      <td>A related resource that references, cites, or otherwise points to the described resource.</td>
      <td>dct:isReferencedBy</td>
      <td>rdfs:Resource (IRI)</td>
      <td>0..n</td>
      <td>The value of this property is the IRI of the doi to the publication or other related resource.\nFor example: https://doi.org/10.1186/s13690-021-00709-x</td>
    </tr>
    <tr>
      <td>keyword</td>
      <td>A keyword or tag describing the resource.</td>
      <td>dcat:keyword</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>Add keywords to increase dataset discoverability. You can include keywords in different languages, submitting each keyword as a separate entry. Example: Physiological measures, Heart Rate, Stress Measures.</td>
    </tr>
    <tr>
      <td>language</td>
      <td>A language of the resource.</td>
      <td>dct:language</td>
      <td>dct:LinguisticSystem (IRI)</td>
      <td>0..n</td>
      <td>The language of the Dataset. For this property, the values from the EU Vocabularies Languages Named Authority List must be used. If your Dataset contains multiple languages, this property can be repeated.</td>
    </tr>
    <tr>
      <td>legal basis</td>
      <td>Indicates use or applicability of a Legal Basis.</td>
      <td>dpv:hasLegalBasis</td>
      <td>dpv:LegalBasis (IRI)</td>
      <td>0..n</td>
      <td>The legal basis can be provided as a value from the dpv taxonomy (see Controlled vocabulary column).\n\nWhile the applicable legislation indicates which legislation mandates the publication of the dataset, the legal basis property described the legal basis for initial collection and processing of (personal) data.\n\nExample value for this property could be: dpv:Consent</td>
    </tr>
    <tr>
      <td>maximum typical age</td>
      <td>Maximum typical age of the population within the dataset</td>
      <td>healthdcatap:maxTypicalAge</td>
      <td>xsd:nonNegativeInteger</td>
      <td>0..1</td>
      <td>The approximate maximum age of subjects in the dataset, if applicable. Approximate age is given to protect potentially sensitive information of subjects in the dataset.</td>
    </tr>
    <tr>
      <td>minimum typical age</td>
      <td>Minimum typical age of the population within the dataset</td>
      <td>healthdcatap:minTypicalAge</td>
      <td>xsd:nonNegativeInteger</td>
      <td>0..1</td>
      <td>The approximate minimum age of subjects in the dataset, if applicable. Approximate age is given to protect potentially sensitive information of subjects in the dataset.</td>
    </tr>
    <tr>
      <td>modification date</td>
      <td>Date on which the resource was changed.</td>
      <td>dct:modified</td>
      <td>xsd:dateTime</td>
      <td>0..1</td>
      <td>This property indicates changes to the dataset, not the metadata record. An absent value may mean the resource hasn't changed since publication, the modification date is unknown, or the resource is continuously updated.</td>
    </tr>
    <tr>
      <td>number of records</td>
      <td>Size of the dataset in terms of the number of records</td>
      <td>healthdcatap:numberOfRecords</td>
      <td>xsd:nonNegativeInteger</td>
      <td>0..1</td>
      <td>Number of records inside a Dataset.</td>
    </tr>
    <tr>
      <td>number of unique infividuals</td>
      <td>Number of records for unique individuals.</td>
      <td>healthdcatap:numberOfUniqueIndividuals</td>
      <td>xsd:nonNegativeInteger</td>
      <td>0..1</td>
      <td>This property is not mandatory, since not all datasets might include data from individuals.</td>
    </tr>
    <tr>
      <td>other identifier</td>
      <td>Links a resource to an adms:Identifier class.</td>
      <td>adms:identifier</td>
      <td>adms:Identifier</td>
      <td>0..n</td>
      <td>Examples for secondary identifiers are MAST/ADS, DataCite, DOI, EZID or W3ID (if not used for the original identifier). This property makes use of another, small class: adms:Identifier, where you provide the identifier and the name of the identifier schema (eg. DOI).</td>
    </tr>
    <tr>
      <td>personal data</td>
      <td>Indicates association with Personal Data.</td>
      <td>dpv:hasPersonalData</td>
      <td>dpv:PersonalData (IRI)</td>
      <td>0..n</td>
      <td>The different types of personal information that are collected in the dataset can be indicated with this property. Values can be picked from the dpv taxonomy (see controlled vocabulary column).\nFor example: dpv-pd:Gender</td>
    </tr>
    <tr>
      <td>population coverage</td>
      <td>A definition of the population within the dataset</td>
      <td>healthdcatap:populationCoverage</td>
      <td>rdfs:Literal</td>
      <td>0..n</td>
      <td>This field is a free text description of the population covered in the dataset. For example, "Adults aged 18–65 diagnosed with type 2 diabetes in the Netherlands between 2015 and 2020".</td>
    </tr>
    <tr>
      <td>publisher</td>
      <td>An entity responsible for making the resource available.</td>
      <td>dct:publisher</td>
      <td>foaf:Agent</td>
      <td>1</td>
      <td>This property identifies the organisation or individual responsible for making the dataset available. For datasets, this is typically the employer of the data creators. In simple cases, the dataset publisher may be the same as the catalog publisher. In more complex settings, such as when datasets come from multiple institutions within a consortium, the consortium should be listed as the publisher where possible. If no formal consortium can be specified, provide the information of the contributing organizations or individuals under dct:creator instead. For more details, refer to the Agent class.</td>
    </tr>
    <tr>
      <td>purpose</td>
      <td>Indicates association with Purpose.</td>
      <td>dpv:hasPurpose</td>
      <td>dpv:Purpose (IRI)</td>
      <td>0..n</td>
      <td>One (or many) category or sub-category of the purposes can be chosen from the taxonomy provided by dpv (see controlled vocabulary column).\nExample value could be: dpv:ResearchAndDevelopment.</td>
    </tr>
    <tr>
      <td>qualified attribution</td>
      <td>Attribution is the ascribing of an entity to an agent.</td>
      <td>prov:qualifiedAttribution</td>
      <td>prov:Attribution</td>
      <td>0..n</td>
      <td>This property makes use of another small class (prov:Attribution). There, you can choose one of the roles as listed in the controlled vocabulary and link that to a specific Agent (expressed with foaf:Agent). Note that for HealthDCAT-AP, the list of roles might be extended in the future.\nExample: https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor\n\nUse this property if you would like to indicate the funder of the (research project that resulted in creation of the) dataset.\nThe value for role then becomes: https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#funder</td>
    </tr>
    <tr>
      <td>qualified relation</td>
      <td>Link to a description of a relationship with another resource.</td>
      <td>dcat:qualifiedRelation</td>
      <td>dcat:Relationship</td>
      <td>0..n</td>
      <td>This property makes use of another small class (dcat:Relationship), in which you can indicate the related resource (via its identifier) and the nature of the relation (based on a controlled vocabulary, which is described in the information of the class).</td>
    </tr>
    <tr>
      <td>quality annotation</td>
      <td>Refers to a quality annotation.</td>
      <td>dqv:hasQualityAnnotation</td>
      <td>dqv:QualityCertificate</td>
      <td>0..n</td>
      <td>This property makes use of another small class (dqv:QualityCertificate), in which you indicate the IRI of the quality certificate, linked to the described resource (via the identifier of the dataset). See that class for more information.</td>
    </tr>
    <tr>
      <td>release date</td>
      <td>Date of formal issuance of the resource.</td>
      <td>dct:issued</td>
      <td>xsd:dateTime</td>
      <td>0..1</td>
      <td>This property should point to the first known date of issuance, such as the publication date in a data repository. Example: 2023-12-10T13:16:10.246Z.</td>
    </tr>
    <tr>
      <td>retention period</td>
      <td>A temporal period which the dataset is available for secondary use.</td>
      <td>healthdcatap:retentionPeriod</td>
      <td>dct:PeriodOfTime</td>
      <td>0..1</td>
      <td>This property makes use of the class dct:PeriodOfTime, in which a start and end date should be provided.</td>
    </tr>
    <tr>
      <td>sample</td>
      <td>Links to a sample of an Asset (which is itself an Asset).</td>
      <td>adms:sample</td>
      <td>dcat:Distribution (IRI)</td>
      <td>0..n</td>
      <td>This property makes use of the dcat:Distribution class to describe a sample distribution of the dataset, which can be anonymized or synthetic data, or the data dictionary provided in CSVW format. This is currently further developed by the TEHDAS2 program. More information can be found here: https://healthdcat-ap.github.io/#sample-distribution</td>
    </tr>
    <tr>
      <td>source</td>
      <td>A related resource from which the described resource is derived.</td>
      <td>dct:source</td>
      <td>dcat:Dataset (IRI)</td>
      <td>0..n</td>
      <td>Indicate the dataset on which this described dataset is based.</td>
    </tr>
    <tr>
      <td>status</td>
      <td>The status of the Asset in the context of a particular workflow process.</td>
      <td>adms:status</td>
      <td>skos:Concept (IRI)</td>
      <td>0..1</td>
      <td>This property makes use of a controlled vocabulary to indicate the status of the described dataset.\nFor example: http://publications.europa.eu/resource/authority/dataset-status/COMPLETED</td>
    </tr>
    <tr>
      <td>temporal coverage</td>
      <td>Temporal characteristics of the resource.</td>
      <td>dct:temporal</td>
      <td>dct:PeriodOfTime</td>
      <td>0..n</td>
      <td>The start and end date of the period that the dataset covers. This property makes use of a small class: Period of Time, in which a start and end date can be given.</td>
    </tr>
    <tr>
      <td>temporal resolution</td>
      <td>Minimum time period resolvable in the dataset.</td>
      <td>dcat:temporalResolution</td>
      <td>xsd:duration</td>
      <td>0..1</td>
      <td>If the dataset is a time-series, this should correspond to the spacing of items in the series. For other kinds of dataset, this property will usually indicate the smallest time difference between items in the dataset. The time period has to be provided in the xsd:duration format.</td>
    </tr>
    <tr>
      <td>theme</td>
      <td>A main category of the resource. A resource can have multiple themes.</td>
      <td>dcat:theme</td>
      <td>skos:Concept (IRI)</td>
      <td>1..n</td>
      <td>This property should use a controlled vocabulary. In the Health Data Catalogue, all datasets will use the theme 'HEAL' (http://publications.europa.eu/resource/authority/data-theme/HEAL), but additional values from the same vocabulary are allowed.</td>
    </tr>
    <tr>
      <td>title</td>
      <td>A name given to the resource.</td>
      <td>dct:title</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>Provide a unique title for your Dataset, which can be repeated in multiple languages. Example: Healthy Brain Study - Physiological Data</td>
    </tr>
    <tr>
      <td>type</td>
      <td>The nature or genre of the resource.</td>
      <td>dct:type</td>
      <td>skos:Concept (IRI)</td>
      <td>0..n</td>
      <td>A recommended controlled vocabulary data-type is foreseen. Health datasets with personal information must use 'personal data'. This list supports dataset categorization for the EU Open Data Portal. Currently, 'PERSONAL_DATA' is not included in the EU vocabulary and cannot be filled out.</td>
    </tr>
    <tr>
      <td>version</td>
      <td>The version indicator (name or identifier) of a resource.</td>
      <td>dcat:version</td>
      <td>rdfs:Literal</td>
      <td>0..1</td>
      <td>Suggested practice: track major_version.minor_version. Register a new identifier for major changes (e.g., 1.0.0 for an unchanged dataset).</td>
    </tr>
    <tr>
      <td>version notes</td>
      <td>A description of changes between this version and the previous version of the Asset.</td>
      <td>adms:versionNotes</td>
      <td>rdfs:Literal</td>
      <td>0..n</td>
      <td>Provide a short description of changes made to the dataset from the previous version.</td>
    </tr>
    <tr>
      <td>was generated by</td>
      <td>Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.</td>
      <td>prov:wasGeneratedBy</td>
      <td>prov:Activity (IRI)</td>
      <td>0..n</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>