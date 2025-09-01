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
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url">access URL</a></td>
      <td>A URL of the resource that gives access to a distribution of the dataset. E.g., landing page, feed, SPARQL endpoint.</td>
      <td><code>dcat:accessURL</code></td>
      <td>NA</td>
      <td><code>IRI</code></td>
      <td>Add a link that points to where the dataset can be found. If it's hosted in a Data Repository, include the link to its entry. For datasets not in a repository (like registries), but still available for secondary use, provide a link to an access request form or a webpage with instructions for accessing the data.</td>
      <td>1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.bytesize">byte size</a></td>
      <td>The size of a Distribution in bytes.</td>
      <td><code>dcat:byteSize</code></td>
      <td>NA</td>
      <td><code>xsd:nonNegativeInteger</code></td>
      <td>Describes the size of the distribution (the actual file) in bytes, and is therefore expressed as a non-negative integer. If the actual size is not know, it can be estimated.</td>
      <td>1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/format">format</a></td>
      <td>The file format, physical medium, or dimensions of the resource.</td>
      <td><code>dct:format</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/file-type">EU Vocabularies File Type Authority List</a></td>
      <td><code>dct:MediaType or Extent</code></td>
      <td>This property can be used to describe a media format in more detail than <code>media type</code> (using IANA media type) when needed. Instances of this property should use a URL, e.g., from the <a href="https://publications.europa.eu/resource/authority/file-type">File Type vocabulary</a>. For instance, for mzML files, the value of this property could be: <code>http://edamontology.org/format_3244</code></td>
      <td>1</td>
      <td><code>http://publications.europa.eu/resource/authority/file-type/TSV</code></td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/license">license</a></td>
      <td>A legal document giving official permission to do something with the resource.</td>
      <td><code>dct:license</code></td>
      <td><a href="https://definities.geostandaarden.nl/dcat-ap-nl/nl/">Geonovum licence list</a></td>
      <td><code>dct:LicenseDocument</code></td>
      <td>For public data, use a Creative Commons (CC) license (see <a href="https://definities.geostandaarden.nl/dcat-ap-nl/nl/">Geonovum options</a>). For most National Health Data Catalogue distributions, where data is not public, use the 'not open' license from Geonovum and specify data reuse agreements in the <code>dct:rights</code> property.</td>
      <td>1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/rights">rights</a></td>
      <td>Information about rights held in and over the resource.</td>
      <td><code>dct:rights</code></td>
      <td>NA</td>
      <td><code>dct:RightsStatement</code></td>
      <td>A statement that concerns all rights not addressed in fields <code>license</code> or <code>access rights</code>. In case of not open data (as specified in the <code>dct:licence</code> property), further agreements regarding data reuse (e.g., Data Transfer Agreement, DTA) should be stated in this property. <br> The rights statement should be a free-text statement placed at a web-accessible location such that the value of this property is the IRI pointing to that statement. <br> Current status: This recommendation on how to state data transfer/reuse conditions will be piloted in 2025.</td>
      <td>1</td>
      <td>NA</td>
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
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service">access service</a></td>
      <td>A data service that gives access to the distribution of the dataset</td>
      <td><code>dcat:accessService</code></td>
      <td>NA</td>
      <td><code>dcat:DataService</code></td>
      <td>This property links the distribution class to the corresponding data service(s).</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#applicableLegislation">applicable legislation</a></td>
      <td>The legislation that is applicable to this resource.</td>
      <td><code>dcatap:applicableLegislation</code></td>
      <td>NA</td>
      <td><code>eli:LegalResource</code></td>
      <td>The legislation that mandates the creation or management of the Distribution.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://spdx.org/rdf/spdx-terms-v2.2/#d4e1930">checksum</a></td>
      <td>The checksum property provides a mechanism that can be used to verify that the contents of a file or package have not changed.</td>
      <td><code>spdx:checksum</code></td>
      <td>NA</td>
      <td><code>spdx:Checksum</code></td>
      <td>The checksum is related to the downloadURL. This property makes use of the <code>spdx:Checksum</code> class, which itself has two properties to indicate checksum algorithm and checksum value (see <a href="linkto:checksum">Checksum</a> class for further details).</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.compressionformat">compression format</a></td>
      <td>The compression format of the distribution in which the data is contained in a compressed form, e.g., to reduce the size of the downloadable file.</td>
      <td><code>dcat:compressFormat</code></td>
      <td><a href="http://www.iana.org/assignments/media-types/media-types.xhtml">IANA Media Types</a></td>
      <td><code>dct:MediaType</code></td>
      <td>It MUST be expressed using a media type as defined in the official register of media types managed by <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">IANA</a>.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/description">description</a></td>
      <td>An account of the resource.</td>
      <td><code>dct:description</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Provide specific details about the distribution here, complementing the description of the related Dataset. This field can be repeated for different language versions of the description.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://xmlns.com/foaf/spec/#term_page">documentation</a></td>
      <td>A homepage for some thing.</td>
      <td><code>foaf:page</code></td>
      <td>NA</td>
      <td><code>foaf:Document (IRI)</code></td>
      <td>This page can contain additional information about the distribution.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url">download URL</a></td>
      <td>The URL of the downloadable file in a given format. E.g., CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.</td>
      <td><code>dcat:downloadURL</code></td>
      <td>NA</td>
      <td><code>IRI</code></td>
      <td>If the dataset is openly accessible and available in a repository, you can directly include a link to the downloadable file here.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/language">language</a></td>
      <td>A language of the resource.</td>
      <td><code>dct:language</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/language">EU Vocabularies Language Authority List</a></td>
      <td><code>dct:LinguisticSystem (IRI)</code></td>
      <td>Indicates the natural language used in the Distribution, indicated with a value from the EU controlled vocabulary. Not all distributions might have a language, for example, imaging data. <br> Note that here the Health-RI model diverges from DCAT-AP NL, which allows a maximum of 1 language per Distribution. The Health-RI model allows multiple languages in the same Distribution.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/conformsTo">linked schemas</a></td>
      <td>An established standard to which the described resource conforms.</td>
      <td><code>dct:conformsTo</code></td>
      <td>NA</td>
      <td><code>dct:Standard (IRI)</code></td>
      <td>This property SHOULD be used to indicate the model, schema, ontology, view, or profile to which this representation of a dataset conforms, in a machine-readable form. This is generally a complementary concern to the media-type or format. Use a reference to the official publication of the respective schema.</td>
      <td>0..*</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type">media type</a></td>
      <td>The media type of the distribution as defined by IANA. [<a href="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types">IANA-MEDIA-TYPES</a>].</td>
      <td><code>dcat:mediaType</code></td>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types">IANA media types</a></td>
      <td><code>IRI</code></td>
      <td>Use the specified vocabularies, prioritizing <a href="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types">IANA media types</a> whenever possible. If unavailable, consider other ontologies, such as <a href="https://bioportal.bioontology.org/ontologies/ZONMW-GENERIC/?p=classes&conceptid=http%3A%2F%2Fpurl.org%2Fzonmw%2Fgeneric%2F10105">ZonMw generic terms</a>, to describe the format. If IANA media types do not sufficiently describe the format, use "format" to describe it in more detail.</td>
      <td>0..1</td>
      <td><code>https://www.iana.org/assignments/media-types/text/csv</code></td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/modified">modification date</a></td>
      <td>Date on which the resource was changed.</td>
      <td><code>dct:modified</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>NA</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.packagingformat">packaging format</a></td>
      <td>The package format of the distribution in which one or more data files are grouped together, e.g., to enable a set of related files to be downloaded together.</td>
      <td><code>dcat:packageFormat</code></td>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#bib-iana-media-types">IANA media types</a></td>
      <td><code>dct:MediaType</code></td>
      <td>It SHOULD be expressed using a media type as defined in the official register of media types managed by IANA.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/issued">release date</a></td>
      <td>Date of formal issuance of the resource.</td>
      <td><code>dct:issued</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>The date the dataset distribution was issued.</td>
      <td>0..1</td>
      <td>NA</td>
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
      <td><a href="https://www.w3.org/ns/legacy_adms#status">status</a></td>
      <td>The status of the Asset in the context of a particular workflow process.</td>
      <td><code>adms:status</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/distribution-status">EU Vocabularies Distribution Status Authority List</a></td>
      <td><code>skos:Concept</code></td>
      <td>It MUST take one of the values: Completed, Deprecated, Under Development, Withdrawn, from the provided controlled vocabulary.</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution.temporalresolution">temporal resolution</a></td>
      <td>Minimum time period resolvable in the dataset.</td>
      <td><code>dcat:temporalResolution</code></td>
      <td>NA</td>
      <td><code>xsd:duration</code></td>
      <td>If applicable, this property indicates the minimum time period resolvable in the dataset distribution, expressed in <code>xsd:duration</code> format (see for more information <a href="https://www.w3schools.com/xml/schema_dtypes_date.asp">here</a>)</td>
      <td>0..1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/title">title</a></td>
      <td>A name given to the resource.</td>
      <td><code>dct:title</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>A title given to the distribution. This property can be repeated to provide names in parallel languages.</td>
      <td>0..*</td>
      <td>Data Access Request of Healthy Brain study</td>
    </tr>
  </tbody>
</table>
