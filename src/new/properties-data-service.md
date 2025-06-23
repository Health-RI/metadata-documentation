## [Data Service](http://www.w3.org/ns/dcat#DataService)

A collection of operations that provides access to one or more datasets or data processing functions. <br><br>
`Usage note`: A Data service offers the possibility to access and query the data of one (or several datasets) through operations. It offers more extensive possibilities to access the data than the [Distribution](linkto:distribution) through a variety of potential actions. An example of a Data Service is a [Beacon API](https://docs.genomebeacons.org/) to query genomics data.

 

### Mandatory Attributes

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
      <td>Information that indicates whether the Dataset is publicly accessible, has access restrictions, or is not public. This property is required to adopt one of the predefined values listed in the Access Rights Named Authority List provided by the Publications Office. This designation informs data users whether the dataset is considered open data or is classified as non-public.</td>
      <td>1</td>
      <td>For non-public data, use the value: <code>http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC</code></td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point">contact point</a></td>
      <td>Relevant contact information for the cataloged resource.</td>
      <td><code>dcat:contactPoint</code></td>
      <td>NA</td>
      <td><code>vcard:Kind</code></td>
      <td>This property points to a contact point (department or person) that can answer questions about the data service. Details on how to describe these are provided under class <code>vcard:Kind</code>. <br> Whenever possible, use <strong>general contact information</strong> (for example from a department) instead of contact information of an individual.</td>
      <td>1</td>
      <td>mailto: <code>data-access-committee@xumc.nl</code> <br> with the name Data Access Committee of the x UMC (see <code>vcard:Kind</code>)</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/description">description</a></td>
      <td>An account of the resource.</td>
      <td><code>dct:description</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Briefly describe the data service provided. You can repeat this description in multiple languages.</td>
      <td>1..*</td>
      <td>A data service that provides API access to real-time electrocardiogram (ECG) monitoring data for clinical research applications.</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description">end point description</a></td>
      <td>A description of the services available via the end-points, including their operations, parameters, etc.</td>
      <td><code>dcat:endpointDescription</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>Provides technical documentation that explains how to access and interact with the data service’s endpoint.</td>
      <td>1</td>
      <td>TBD</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url">end point URL</a></td>
      <td>The root location or primary endpoint of the service (a Web-resolvable IRI).</td>
      <td><code>dcat:endpointURL</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>Provide the URL of the endpoint that users can interact with to access the data service. This should be a direct link to the service's endpoint, such as an API URL, SPARQL endpoint, or similar.</td>
      <td>1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/identifier">identifier</a></td>
      <td>An unambiguous reference to the resource within a given context.</td>
      <td><code>dct:identifier</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Provide a unique identifier for the data service. This could be a globally unique and persistent identifier, such as a DOI, URN, or UUID. If no persistent identifier is available, you may use the accessURL or endpointURL as the identifier, provided it is stable and unique to the service.</td>
      <td>1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/license">licence</a></td>
      <td>A legal document giving official permission to do something with the resource.</td>
      <td><code>dct:license</code></td>
      <td><a href="https://definities.geostandaarden.nl/dcat-ap-nl/nl/">Geonovum licence list</a></td>
      <td><code>dct:LicenseDocument</code></td>
      <td>For public data, use a Creative Commons (CC) license (see <a href="https://definities.geostandaarden.nl/dcat-ap-nl/nl/">Geonovum options</a>). For most National Health Data Catalogue data services, where data is not public, use the 'not open' license from Geonovum and specify data reuse agreements in the <code>dct:rights</code> property.</td>
      <td>1</td>
      <td>NA</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/publisher">publisher</a></td>
      <td>An entity responsible for making the resource available.</td>
      <td><code>dct:publisher</code></td>
      <td>NA</td>
      <td><code>foaf:Agent</code></td>
      <td>The organisation or individual responsible for making the data service available. In the context of data services, the publisher is typically the organisation that manages or provides access to the service. For details, see the class <a href="linkto:agent">Agent</a>.</td>
      <td>1</td>
      <td>name: Radboud University Medical Center <br> identifier: <code>https://ror.org/05wg1m734</code> <br> (see class foaf: Agent)</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme">theme</a></td>
      <td>A main category of the resource. A resource can have multiple themes.</td>
      <td><code>dcat:theme</code></td>
      <td><a href="https://publications.europa.eu/resource/authority/data-theme">EU Vocabularies Theme Authority List</a></td>
      <td><code>skos:Concept</code></td>
      <td>This property should use the <a href="https://publications.europa.eu/resource/authority/data-theme">controlled vocabulary</a>. In the Health Data Catalogue, most data services will use <code>NAL:data-theme</code> 'HEAL', but additional values from the same vocabulary are allowed.</td>
      <td>1..*</td>
      <td><code>https://publications.europa.eu/resource/authority/data-theme/HEAL</code></td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/title">title</a></td>
      <td>A name given to the resource.</td>
      <td><code>dct:title</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>NA</td>
      <td>1..*</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>


### Recommended  Attributes

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#applicableLegislation">applicable legislation</a></td>
      <td>The legislation that is applicable to this resource.</td>
      <td><code>dcatap:applicableLegislation</code></td>
      <td>NA</td>
      <td><code>eli:LegalResource</code></td>
      <td>TBA</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/conformsTo">application profile</a></td>
      <td>An established standard to which the described resource conforms.</td>
      <td><code>dct:conformsTo</code></td>
      <td>NA</td>
      <td><code>dct:Standard</code></td>
      <td>The standards referred here SHOULD describe the Data Service and not the data it serves. The latter is provided by the dataset with which this Data Service is connected. For instance, the data service adheres to the OGC WFS API standard, while the associated dataset adheres to the <a href="https://knowledge-base.inspire.ec.europa.eu/index_en">INSPIRE</a> Address data model.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/creator">creator</a></td>
      <td>An entity responsible for making the resource.</td>
      <td><code>dct:creator</code></td>
      <td>NA</td>
      <td><code>foaf:Agent</code></td>
      <td>Note that the Health-RI model diverges from DCAT-AP NL here, which reduces the maximum number of creators to 1. The Health-RI model allows the specification of multiple creators of a data service.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/format">format</a></td>
      <td>The file format, physical medium, or dimensions of the resource.</td>
      <td><code>dct:format</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/file-type">EU Vocabularies File Type Authority List</a></td>
      <td><code>dct:MediaType or Extent</code></td>
      <td>The term from the authority table should be used.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="https://semiceu.github.io/DCAT-AP/r5r/releases/3.0.0/#hvdCategory">HVD Category</a></td>
      <td>A data category defined in the High Value Dataset Implementing Regulation.</td>
      <td><code>dcatap:hvdCategory</code></td>
      <td>NA</td>
      <td><code>skos:Concept</code></td>
      <td>NA</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/ns/dcat#keyword">keyword</a></td>
      <td>A keyword or tag describing the resource.</td>
      <td><code>dcat:keyword</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>NA</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_landing_page">landing page</a></td>
      <td>A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.</td>
      <td><code>dcat:landingPage</code></td>
      <td>NA</td>
      <td><code>foaf:Document</code></td>
      <td>It is intended to point to a landing page at the original data service provider, not to a page on a site of a third party, such as an aggregator.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/language">language</a></td>
      <td>A language of the resource.</td>
      <td><code>dct:language</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/language">EU Vocabularies Language Authority List</a></td>
      <td><code>dct:LinguisticSystem</code></td>
      <td>Indicates the natural language used in the data service, indicated with a value from the <a href="https://publications.europa.eu/resource/authority/language">EU controlled vocabulary</a>.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/modified">modification date</a></td>
      <td>Date on which the resource was changed.</td>
      <td><code>dct:modified</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>This property indicates the date of the last changes to the dataset, not the metadata record. An absent value may mean the resource hasn't changed since publication, the modification date is unknown, or the resource is continuously updated.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="https://docs.geostandaarden.nl/dcat/dcat-ap-nl30/#dataservice-other-identifier">other identifier</a></td>
      <td>Links a resource to an <code>adms:Identifier</code> class.</td>
      <td><code>adms:identifier</code></td>
      <td>NA</td>
      <td><code>adms:Identifier</code></td>
      <td>NA</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/rights">rights</a></td>
      <td>Information about rights held in and over the resource.</td>
      <td><code>dct:rights</code></td>
      <td>NA</td>
      <td><code>dct:RightsStatement</code></td>
      <td>NA</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset">serves dataset</a></td>
      <td>A collection of data that this data service can distribute.</td>
      <td><code>dcat:servesDataset</code></td>
      <td>NA</td>
      <td><code>dcat:Dataset</code></td>
      <td>This property connects the Data Service class to its corresponding dataset(s), ensuring every data service links to at least one <code>dcat:Dataset</code>. While essential for metadata implementation teams on each node, it's less relevant for researchers to collect.</td>
      <td>0..*</td>
    </tr>
  </tbody>
</table>
