### Mandatory Properties

<table> 
  <thead> 
    <tr> 
      <th>Property name</th> 
      <th>Definition</th> 
      <th>URI</th> 
      <th>Controlled Vocabulary</th> 
      <th>rdfs:Range</th> 
      <th>Usage Note</th> 
      <th>Cardinality</th> 
      <th>Example</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/accessRights">access rights</a></td> 
      <td>Information about who accesses the resource or an indication of its security status.</td> 
      <td><code>dct:accessRights</code></td> 
      <td><a href="http://publications.europa.eu/resource/authority/access-right">EU Vocabularies Access Rights Authority List</a></td> 
      <td><a href="http://publications.europa.eu/resource/authority/access-right">Rights Statement (IRI)</a></td> 
      <td>Information that indicates whether the Dataset is publicly accessible, has access restrictions, or is not public. It is foreseen that one of the three options has to be used: <code>public</code>, <code>restricted</code>, <code>non-public</code>. <br> - Open Data (Public): The dataset is available under general open data rules, such as those covered by the High Value Datasets Implementing Regulation. <br> - Protected Data (Restricted): The dataset contains protected data and is accessible only under specific conditions, as outlined in regulations like the Data Governance Act. <br> - Sensitive Data (Non public): The dataset includes resources that may contain sensitive or personal information, falling under regulations such as the EHDS Regulation. <br><br> Since most data contain personal information, these datasets will need to take the value 'non-public' for the access rights property.</td> 
      <td>1</td> 
      <td><code>http://publications.europa.eu/resource/authority/access-right/RESTRICTED</code></td> 
    </tr> 
    <tr> 
      <td><a href="http://data.europa.eu/r5r/applicableLegislation">applicable legislation</a></td> 
      <td>The legislation that is applicable to this resource.</td> 
      <td><code>dcatap:applicableLegislation</code></td> 
      <td>NA</td> 
      <td><code>eli:LegalResource</code></td> 
      <td>The ELI of the EHDS was published in March 2025 and can now be included as the applicable legislation mandating that the dataset has to be made public. <br> For health datasets, the value must include the ELI of the <a href="http://data.europa.eu/eli/reg/2025/327/oj">EHDS Regulation</a>. <br> As multiple legislations may apply to the resource, the maximum cardinality is not limited. <br><br> While the applicable legislation indicates which legislation mandates the publication of the dataset, the legal basis property (also in Datasets) described the legal basis for initial collection and processing of (personal) data.</td> 
      <td>1..*</td> 
      <td>NA</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point">contact point</a></td> 
      <td>Relevant contact information for the cataloged resource.</td> 
      <td><code>dcat:contactPoint</code></td> 
      <td>NA</td> 
      <td><code>vcard:Kind</code></td> 
      <td>This property points to a contact point (department or person) that can answer questions about the dataset. Details on how to describe these are provided under class <code>vcard:Kind</code>. <br>Whenever possible, use <strong>general contact information</strong> (for example from a department) instead of contact information of an individual.</td> 
      <td>1</td> 
      <td>mailto: <code>data-access-committee@xumc.nl</code> <br> with the name Data Access Committee of the x UMC (see <a href="linkto:kind">vcard:Kind</a>)</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/creator">creator</a></td> 
      <td>An entity responsible for making the resource.</td> 
      <td><code>dct:creator</code></td> 
      <td>NA</td> 
      <td><code>foaf:Agent</code></td> 
      <td>This property points to a person (known as <code>Agent</code>) responsible for generating the dataset. In most cases, this should be the project’s Principal Investigator, provided they consent to being listed in the catalogue. If not, the associated department or institute may be specified instead.</td> 
      <td>1..*</td> 
      <td>Jip Fictief, Inez Maginary, Fabio Abricated for name of <code>foaf:Agent</code></td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/description">description</a></td> 
      <td>An account of the resource.</td> 
      <td><code>dct:description</code></td> 
      <td>NA</td> 
      <td><code>rdfs:Literal</code></td> 
      <td>Brief description of the dataset. You can repeat this property in multiple languages.</td> 
      <td>1..*</td> 
      <td>Collection of physiological data of Healthy Brain Study participants. This collection includes measurements via biowearables for heart rate, oxygenation, systolic and diastolic measures and stress levels.</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/identifier">identifier</a></td> 
      <td>An unambiguous reference to the resource within a given context.</td> 
      <td><code>dct:identifier</code></td> 
      <td>NA</td> 
      <td><code>rdfs:Literal</code></td> 
      <td>Please see the latest usage recommendations on <a href="https://health-ri.atlassian.net/wiki/spaces/FSD/pages/1084751895/Recommendations+for+filling+in+the+dct+identifier+field+for+Dataset">this page</a>.</td> 
      <td>1</td> 
      <td><code>https://doi.org/10.34894/ZLOYOJ</code></td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/ns/dcat#keyword">keyword</a></td> 
      <td>A keyword or tag describing the resource.</td> 
      <td><code>dcat:keyword</code></td> 
      <td>NA</td> 
      <td><code>rdfs:Literal</code></td> 
      <td>Add keywords to increase dataset discoverability. You can include keywords in different languages, submitting each keyword as a separate entry.</td> 
      <td>1..*</td> 
      <td>Physiological measures, Heart Rate, Stress Measures</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/publisher">publisher</a></td> 
      <td>An entity responsible for making the resource available.</td> 
      <td><code>dct:publisher</code></td> 
      <td>NA</td> 
      <td><code>foaf:Agent</code></td> 
      <td>This property identifies the organisation or individual responsible for making the dataset available. For datasets, this is typically the employer of the data creators. In simple cases, the dataset publisher may be the same as the catalog publisher. In more complex settings, such as when datasets come from multiple institutions within a consortium, the consortium should be listed as the publisher where possible. If no formal consortium can be specified, provide the information of the contributing organizations or individuals under <code>dct:creator</code> instead. For more details, refer to the <a href="linkto:agent">Agent</a> class.</td> 
      <td>1</td> 
      <td>Radboud University Medical Center; identifier <code>https://ror.org/05wg1m734</code> (see foaf: Agent)</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme">theme</a></td> 
      <td>A main category of the resource. A resource can have multiple themes.</td> 
      <td><code>dcat:theme</code></td> 
      <td><a href="http://publications.europa.eu/resource/authority/data-theme">Dataset Theme Vocabulary</a></td> 
      <td><code>skos:Concept</code></td> 
      <td>This property should use a controlled vocabulary. In the Health Data Catalogue, all datasets will use the theme <a href="http://publications.europa.eu/resource/authority/data-theme/HEAL">HEAL</a>, but additional values from the same vocabulary are allowed.</td> 
      <td>1..*</td> 
      <td><code>http://publications.europa.eu/resource/authority/data-theme/HEAL</code></td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/title">title</a></td> 
      <td>A name given to the resource.</td> 
      <td><code>dct:title</code></td> 
      <td>NA</td> 
      <td><code>rdfs:Literal</code></td> 
      <td>Provide a unique title for your Dataset, which can be repeated in multiple languages.</td> 
      <td>1..*</td> 
      <td>Healthy Brain Study - Physiological Data</td> 
    </tr> 
  </tbody> 
</table>


### Recommended Properties 

<table>
  <thead>
    <tr>
      <th>Property name</th>
      <th>Definition</th>
      <th>URI</th>
      <th>Controlled Vocabulary</th>
      <th>rdfs:Range</th>
      <th>Usage Note</th>
      <th>Cardinality</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.analytics">analytics</a></td>
      <td>An analytics distribution of the dataset.</td>
      <td><code>healthdcatap:analytics</code></td>
      <td>NA</td>
      <td><code>dcat:Distribution</code></td>
      <td>Publishers are encouraged to provide URLs pointing to document repositories where users can access or request associated resources such as technical reports of the dataset, quality measurements, usability indicators,... Note that HealthDCAT-AP mentions also API endpoints or analytics services, but these would not be Distributions but rather DatasetServices.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.hascodevalues">code values</a></td>
      <td>Health classifications and their codes associated with the dataset.</td>
      <td><code>healthdcatap:hasCodeValues</code></td>
      <td>NA</td>
      <td><code>skos:Concept</code></td>
      <td>Inside this property, you can provide the coding system of the dataset in the form of <a href="https://www.wikidata.org/">wikidata</a> URI (example: <code>https://www.wikidata.org/entity/P494</code> for ICD-10 ID) and the URI of the value that describes the dataset (example: <code>https://icd.who.int/browse10/2019/en#/Y59.0</code> for viral vaccines)</td>
      <td>0..*</td>
      <td><code>https://www.wikidata.org/entity/P494</code> for ICD-10 ID and <code>https://icd.who.int/browse10/2019/en#/Y59.0</code> for viral vaccines</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.hascodingsystem">coding system</a></td>
      <td>Coding systems in use (ex: ICD-10-CM, DGRs, SNOMED-CT, ...).</td>
      <td><code>healthdcatap:hasCodingSystem</code></td>
      <td>NA</td>
      <td><code>dct:Standard (IRI)</code></td>
      <td>This property provides information on which coding systems are in use inside your dataset. For this, <a href="https://www.wikidata.org/">wikidata</a> URIs must be used.</td>
      <td>0..*</td>
      <td><code>https://www.wikidata.org/entity/P494</code> (ICD-10 ID)</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/conformsTo">conforms to</a></td>
      <td>An established standard to which the described resource conforms.</td>
      <td><code>dct:conformsTo</code></td>
      <td>NA</td>
      <td><code>dct:Standard (IRI)</code></td>
      <td>If your data conforms to an established standard or specification, use this property to indicate which one. The <a href="https://www.wikidata.org/">wikidata</a> URI of the specification must be used.</td>
      <td>0..*</td>
      <td><code>https://www.wikidata.org/wiki/Q19597236</code> for FHIR</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution">distribution</a></td>
      <td>An available distribution of the dataset.</td>
      <td><code>dcat:distribution</code></td>
      <td>NA</td>
      <td><code>dcat:Distribution</code></td>
      <td>Metadata element used as a key link to the class Distribution.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://xmlns.com/foaf/spec/#term_page">documentation</a></td>
      <td>A page or document about this thing.</td>
      <td><code>foaf:page</code></td>
      <td>NA</td>
      <td><code>foaf:Document (IRI)</code></td>
      <td>The value of this property is the IRI directing to the webpage or document about the dataset.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/accrualPeriodicity">frequency</a></td>
      <td>The frequency with which items are added to a collection.</td>
      <td><code>dct:accrualPeriodicity</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/frequency">EU Vocabularies Frequency Authority List</a></td>
      <td><code>skos:Concept</code></td>
      <td>"The value of this property should be the IRI from the listed controlled vocabulary, indicating the frequency at which the dataset is updated.</td>
      <td>0..1</td>
      <td><code>http://publications.europa.eu/resource/authority/frequency/WEEKLY</code></td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/spatial">geographical coverage</a></td>
      <td>Spatial characteristics of the resource.</td>
      <td><code>dct:spatial</code></td>
      <td>
        EU Vocabularies Lists: <br>
        <a href="http://publications.europa.eu/resource/authority/continent/">Continents</a> <br>
        <a href="http://publications.europa.eu/resource/authority/country">Countries</a> <br>
        <a href="http://publications.europa.eu/resource/authority/place/">Places</a> <br>
        OR <br>
        <a href="http://sws.geonames.org/">Geonames</a> OR <br>
        <a href="https://vocabs.cbs.nl/nl/">CBS Classificaties en begrippen</a>
      </td>
      <td><code>dct:Location</code></td>
      <td>The EU Vocabularies Name Authority Lists must be used for continents, countries and places that are in those lists; if a particular location is not in one of the mentioned Named Authority Lists, Geonames URIs must be used. For districts or neighborhoods in NL, the Dutch vocab can be used. However, it might in many cases be desirable to keep the geographical coverage broader (e.g. indicating that NL is covered), to not expose detailed information of subject's locations.</td>
      <td>0..*</td>
      <td><code>http://publications.europa.eu/resource/authority/place/NLD_AMS</code></td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_has_version">has version</a></td>
      <td>This resource has a more specific, versioned resource.</td>
      <td><code>dcat:hasVersion</code></td>
      <td>NA</td>
      <td><code>dcat:Dataset</code></td>
      <td>Indicate the dataset which is the other version of the current dataset.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.healththeme">health theme</a></td>
      <td>A category of the Dataset or tag describing the Dataset.</td>
      <td><code>healthdcatap:healthTheme</code></td>
      <td>NA</td>
      <td><code>skos:Concept</code></td>
      <td>This property is a structured way to tag the dataset with different health themes. This could include, for example, the specific disease the dataset is about. More details can be provided, if desirable, in the keywords' property. *Current status*: the HealthDCAT-AP working group is currently exploring is other sources (ontologies, thesauri) can be used for this, next to <a href="https://www.wikidata.org/">Wikidata</a>.</td>
      <td>0..*</td>
      <td><code>https://www.wikidata.org/wiki/Q58624061</code></td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series">in series</a></td>
      <td>A dataset series of which the dataset is part.</td>
      <td><code>dcat:inSeries</code></td>
      <td>NA</td>
      <td><code>dcat:DatasetSeries</code></td>
      <td>This property points to which Dataset Series the Dataset is part of.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/isReferencedBy">is referenced by</a></td>
      <td>A related resource that references, cites, or otherwise points to the described resource.</td>
      <td><code>dct:isReferencedBy</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>The value of this property is the IRI of the doi to the publication or other related resource.</td>
      <td>0..*</td>
      <td><code>https://doi.org/10.1186/s13690-021-00709-x</code></td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/language">language</a></td>
      <td>A language of the resource.</td>
      <td><code>dct:language</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/language">EU Vocabularies Language Named Authority List</a></td>
      <td><code>dct:LinguisticSystem</code></td>
      <td>The language of the Dataset. For this property, the values from the EU Vocabularies Languages Named Authority List must be used. If your Dataset contains multiple languages, this property can be repeated.</td>
      <td>0..*</td>
      <td><code>http://publications.europa.eu/resource/authority/language/NLD</code></td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.haslegalbasis">legal basis</a></td>
      <td>Indicates use or applicability of a Legal Basis.</td>
      <td><code>dpv:hasLegalBasis</code></td>
      <td><a href="https://w3c.github.io/dpv/2.0/dpv/modules/legal_basis.html#vocab-legal-basis">DPV Taxonomy</a></td>
      <td><code>dpv:LegalBasis</code></td>
      <td>The legal basis can be provided as a value from the dpv taxonomy (see Controlled vocabulary column). <br><br>While the applicable legislation indicates which legislation mandates the publication of the dataset, the legal basis property described the legal basis for initial collection and processing of (personal) data. <br> Example value for this property could be: dpv:Consent.</td>
      <td>0..*</td>
      <td><code>dpv:Consent</code></td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.maxtypicalage">maximum typical age</a></td>
      <td>Maximum typical age of the population within the dataset.</td>
      <td><code>healthdcatap:maxTypicalAge</code></td>
      <td>NA</td>
      <td><code>xsd:nonNegativeInteger</code></td>
      <td>The approximate maximum age of subjects in the dataset, if applicable. Approximate age is given to protect potentially sensitive information of subjects in the dataset.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.mintypicalage">minimum typical age</a></td>
      <td>Minimum typical age of the population within the dataset.</td>
      <td><code>healthdcatap:minTypicalAge</code></td>
      <td>NA</td>
      <td><code>xsd:nonNegativeInteger</code></td>
      <td>The approximate minimum age of subjects in the dataset, if applicable. Approximate age is given to protect potentially sensitive information of subjects in the dataset.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/modified">modification date</a></td>
      <td>Date on which the resource was changed.</td>
      <td><code>dct:modified</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>This property indicates changes to the dataset, not the metadata record. An absent value may mean the resource hasn't changed since publication, the modification date is unknown, or the resource is continuously updated.</td>
      <td>0..1</td>
      <td>2024-06-04T13:36:10.246Z</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.numberofrecords">number of records</a></td>
      <td>Size of the dataset in terms of the number of records.</td>
      <td><code>healthdcatap:numberOfRecords</code></td>
      <td>NA</td>
      <td><code>xsd:nonNegativeInteger</code></td>
      <td>Number of records inside a Dataset.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.numberofuniqueindividuals">number of unique individuals</a></td>
      <td>Number of records for unique individuals.</td>
      <td><code>healthdcatap:numberOfUniqueIndividuals</code></td>
      <td>NA</td>
      <td><code>xsd:nonNegativeInteger</code></td>
      <td>This property is not mandatory, since not all datasets might include data from individuals.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.otheridentifier">other identifier</a></td>
      <td>Links a resource to an adms:Identifier class.</td>
      <td><code>adms:identifier</code></td>
      <td>NA</td>
      <td><code>adms:Identifier</code></td>
      <td>Examples for secondary identifiers are <code>MAST/ADS</code>, <code>DataCite</code>, <code>DOI</code>, <code>EZID</code> or <code>W3ID</code> (if not used for the original identifier). This property makes use of another, small class: <code>adms:Identifier</code>, where you provide the identifier and the name of the identifier schema (e.g., DOI).</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.haspersonaldata">personal data</a></td>
      <td>Indicates association with Personal Data.</td>
      <td><code>dpv:hasPersonalData</code></td>
      <td><a href="https://w3c.github.io/dpv/2.0/pd/">DPV Taxonomy</a></td>
      <td><code>dpv:PersonalData</code></td>
      <td>The different types of personal information that are collected in the dataset can be indicated with this property. Values can be picked from the dpv taxonomy (see controlled vocabulary column). <br>For example: dpv-pd:Gender.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.populationcoverage">population coverage</a></td>
      <td>A definition of the population within the dataset.</td>
      <td><code>healthdcatap:populationCoverage</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>This field is a free text description of the population covered in the dataset.</td>
      <td>0..*</td>
      <td>Adults aged 18–65 diagnosed with type 2 diabetes in the Netherlands between 2015 and 2020</td>
    </tr>
    <tr>
      <td><a href="https://w3c.github.io/dpv/2.0/dpv/#dfn-haspurpose">purpose</a></td>
      <td>Indicates association with Purpose.</td>
      <td><code>dpv:hasPurpose</code></td>
      <td><a href="https://w3c.github.io/dpv/2.1/dpv/#vocab-purposes">DPV Taxonomy Purposes</a></td>
      <td><code>dpv:Purpose</code></td>
      <td>One (or many) category or sub-category of the purposes can be chosen from the taxonomy provided by dpv (see the controlled vocabulary column). <br> Example value could be: dpv:ResearchAndDevelopment.</td>
      <td>0..*</td>
      <td><code>dpv:ResearchAndDevelopment</code></td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/prov-o/#qualifiedAttribution">qualified attribution</a></td>
      <td>Attribution is the ascribing of an entity to an agent.</td>
      <td><code>prov:qualifiedAttribution</code></td>
      <td>NA</td>
      <td><code>prov:Attribution</code></td>
      <td>This property makes use of another small class (<code>prov:Attribution</code>). There, you can choose one of the roles as listed in the controlled vocabulary and link that to a specific Agent (expressed with <code>foaf:Agent</code>). Note that for HealthDCAT-AP, the list of roles might be extended in the future. <br>Example: <code>https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor</code> <br><br> Use this property if you would like to indicate the <strong>funder</strong> of the (research project that resulted in creation of the) dataset. <br>The value for role then becomes: <code>https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#funder</code>"</td>
      <td>0..*</td>
      <td>See Usage Note</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Dataset.qualifiedrelation">qualified relation</a></td>
      <td>Link to a description of a relationship with another resource.</td>
      <td><code>dcat:qualifiedRelation</code></td>
      <td>NA</td>
      <td><code>dcat:Relationship</code></td>
      <td>This property makes use of another small class (<code>dcat:Relationship</code>), in which you can indicate the related resource (via its identifier) and the nature of the relation (based on a controlled vocabulary, which is described in the information of the class).</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dqv/#dqv:hasQualityAnnotation">quality annotation</a></td>
      <td>Refers to a quality annotation.</td>
      <td><code>dqv:hasQualityAnnotation</code></td>
      <td>NA</td>
      <td><code>dqv:QualityCertificate</code></td>
      <td>This property makes use of another small class (<code>dqv:QualityCertificate</code>), in which you indicate the IRI of the quality certificate, linked to the described resource (via the identifier of the dataset). See that class for more information.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/issued">release date</a></td>
      <td>Date of formal issuance of the resource.</td>
      <td><code>dct:issued</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>This property should point to the first known date of issuance, such as the publication date in a data repository.</td>
      <td>0..1</td>
      <td>2023-12-10T13:16:10.246Z</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.retentionPeriod">retention period</a></td>
      <td>A temporal period in which the dataset is available for secondary use.</td>
      <td><code>healthdcatap:retentionPeriod</code></td>
      <td>NA</td>
      <td><code>dct:PeriodOfTime</code></td>
      <td>This property makes use of the class <code>dct:PeriodOfTime</code>, in which a start and end date should be provided.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.sample">sample</a></td>
      <td>Links to a sample of an Asset (which is itself an Asset).</td>
      <td><code>adms:sample</code></td>
      <td>NA</td>
      <td><code>dcat:Distribution</code></td>
      <td>This property makes use of the <code>dcat:Distribution</code> class to describe a sample distribution of the dataset, which can be anonymized or synthetic data, or the data dictionary provided in <code>CSVW format</code>. This is currently further developed by the TEHDAS2 program. More information can be <a href="https://healthdcat-ap.github.io/#sample-distribution">found here.</a></td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/source">source</a></td>
      <td>A related resource from which the described resource is derived.</td>
      <td><code>dct:source</code></td>
      <td>NA</td>
      <td><code>dcat:Dataset</code></td>
      <td>Indicate the dataset on which this described dataset is based.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-adms/#adms-status">status</a></td>
      <td>The status of the Asset in the context of a particular workflow process.</td>
      <td><code>adms:status</code></td>
      <td><a href="https://publications.europa.eu/resource/authority/dataset-status">EU Vocabularies Dataset Status Named Authority List</a></td>
      <td><code>skos:Concept</code></td>
      <td>This property makes use of a controlled vocabulary to indicate the status of the described dataset.</td>
      <td>0..1</td>
      <td><code>http://publications.europa.eu/resource/authority/dataset-status/COMPLETED</code></td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/temporal">temporal coverage</a></td>
      <td>Temporal characteristics of the resource.</td>
      <td><code>dct:temporal</code></td>
      <td>NA</td>
      <td><code>dct:PeriodOfTime</code></td>
      <td>The start and end date of the period that the dataset covers. This property makes use of a small class: Period of Time, in which a start and end date can be given.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/temporalResolution">temporal resolution</a></td>
      <td>Minimum time period resolvable in the dataset.</td>
      <td><code>dcat:temporalResolution</code></td>
      <td>NA</td>
      <td><code>xsd:duration</code></td>
      <td>If the dataset is a time-series, this should correspond to the spacing of items in the series. For other kinds of dataset, this property will usually indicate the smallest time difference between items in the dataset. The time period has to be provided in the <code>xsd:duration</code> format.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/type">type</a></td>
      <td>The nature or genre of the resource.</td>
      <td><code>dct:type</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/dataset-type">EU Vocabularies Dataset Type Named Authority List</a></td>
      <td><code>skos:Concept</code></td>
      <td>A recommended controlled vocabulary data-type is foreseen. Health datasets with personal information must use 'personal data'. This list supports dataset categorization for the EU Open Data Portal. Currently, 'PERSONAL_DATA' is not included in the EU vocabulary and cannot be filled out.</td>
      <td>0..*</td>
      <td><code>http://publications.europa.eu/resource/authority/dataset-type/PERSONAL_DATA</code></td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Dataset.version">version</a></td>
      <td>The version indicator (name or identifier) of a resource.</td>
      <td><code>dcat:version</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Suggested practice: track major_version.minor_version. Register a new identifier for major changes (e.g., 1.0.0 for an unchanged dataset).</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/ns/legacy_adms#versionNotes">version notes</a></td>
      <td>A description of changes between this version and the previous version of the Asset.</td>
      <td><code>adms:versionNotes</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Provide a short description of changes made to the dataset from the previous version.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/prov-o/#wasGeneratedBy">was generated by</a></td>
      <td>Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.</td>
      <td><code>prov:wasGeneratedBy</code></td>
      <td>NA</td>
      <td><code>prov:Activity</code></td>
      <td>NA</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>
