#### Mandatory Properties

<table> 
  <thead> 
    <tr> 
      <th>Property label</th> 
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
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point">contact point</a></td> 
      <td>Relevant contact information for the cataloged resource.</td> 
      <td><code>dcat:contactPoint</code></td> 
      <td>NA</td> 
      <td><code>vcard:Kind</code></td> 
      <td>This property points to a contact point (department or person) that can answer questions about the catalogue. Details on how to describe these are provided under class <code>vcard:Kind</code>. <br> Whenever possible, use <strong>general contact information</strong> (for example from a department) instead of contact information of an individual.</td> 
      <td>1</td> 
      <td>TBD</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset">dataset</a></td> 
      <td>A dataset that is listed in the catalog.</td> 
      <td><code>dcat:dataset</code></td> 
      <td>NA</td> 
      <td><code>dcat:Dataset</code></td> 
      <td>Each catalog contains one or more datasets. This property serves to link datasets to a catalogue. Therefore, a dataset is always contained inside a catalogue.</td> 
      <td>1..*</td> 
      <td>TBD</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/description">description</a></td> 
      <td>An account of the resource.</td> 
      <td><code>dct:description</code></td> 
      <td>NA</td> 
      <td><code>rdfs:Literal</code></td> 
      <td>Briefly describe the catalog and what it contains. You can repeat this in multiple languages.</td> 
      <td>1..*</td> 
      <td>This catalogue describes the core metadata of AUMC Inflammatory Bowel Disease datasets. <br> This catalogue describes breast cancer imaging, clinical and omics datasets.</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/publisher">publisher</a></td> 
      <td>An entity responsible for making the resource available.</td> 
      <td><code>dct:publisher</code></td> 
      <td>NA</td> 
      <td><code>foaf:Agent</code></td> 
      <td>The organisation or individual that is the holder of the intellectual property rights of a dataset. For more details about the publisher, see the class [Agent]linkto:agent).</td> 
      <td>1</td> 
      <td>name: Radboud University Medical Center <br> identifier: <code>https://ror.org/05wg1m734</code> <br> (see class foaf: Agent)</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/title">title</a></td> 
      <td>A name given to the resource.</td> 
      <td><code>dct:title</code></td> 
      <td>NA</td> 
      <td><code>rdfs:Literal</code></td> 
      <td>Provide a unique title for your catalog, which can be repeated in multiple languages.</td> 
      <td>1..*</td> 
      <td>Healthy Brain Study</td> 
    </tr> 
  </tbody> 
</table>

#### Recommended Properties 

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
      <td>NA</td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog">catalog</a></td> 
      <td>A catalog that is listed in the catalog.</td> 
      <td><code>dcat:catalog</code></td> 
      <td>NA</td> 
      <td><code>dcat:Catalog</code></td> 
      <td>For certain research projects, multiple catalogs may need to be organized in a nested manner. This property serves to connect the different catalogs with each other.</td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#creator">creator</a></td> 
      <td>An entity responsible for making the resource.</td> 
      <td><code>dct:creator</code></td> 
      <td>NA</td> 
      <td><code>foaf:Agent</code></td> 
      <td>Note that the Health-RI model diverges from DCAT-AP NL here, which reduces the maximum number of creators to 1. The Health-RI model allows the specification of multiple creators of a catalogue.</td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/spatial">geographical coverage</a></td> 
      <td>Spatial characteristics of the resource.</td> 
      <td><code>dct:spatial</code></td> 
      <td>EU Vocabularies Lists: <br> 
        <a href="http://publications.europa.eu/resource/authority/continent">Continents</a> <br> 
        <a href="http://publications.europa.eu/resource/authority/country">Countries</a> <br> 
        <a href="http://publications.europa.eu/resource/authority/place">Places</a> <br> 
        OR <br> 
        <a href="http://sws.geonames.org/">Geonames</a> OR <br> 
        <a href="https://vocabs.cbs.nl/nl/">CBS Classificaties en begrippen</a> 
      </td> 
      <td><code>dct:Location</code></td> 
      <td>The EU Vocabularies Name Authority Lists must be used for continents, countries and places that are in those lists; if a particular location is not in one of the mentioned Named Authority Lists, Geonames URIs must be used. For districts or neighbourhoods in NL, the Dutch vocab can be used.</td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/hasPart">has part</a></td> 
      <td>A related resource that is included either physically or logically in the described resource.</td> 
      <td><code>dct:hasPart</code></td> 
      <td>NA</td> 
      <td><code>dcat:Catalog</code></td> 
      <td>Use this property to establish another catalogue in this catalogue. <br> Note that deeply nested structures should be avoided, and can currently not be displayed in the National Health Data Catalogue.</td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="http://xmlns.com/foaf/spec/#term_homepage">home page</a></td> 
      <td>A homepage for some thing.</td> 
      <td><code>foaf:homepage</code></td> 
      <td>NA</td> 
      <td><code>foaf:Document</code></td> 
      <td>The home page of the catalogue, if available.</td> 
      <td>0..1</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/language">language</a></td> 
      <td>A language of the resource.</td> 
      <td><code>dct:language</code></td> 
      <td><a href="http://publications.europa.eu/resource/authority/language">EU Vocabularies Language Authority List</a></td> 
      <td><code>dct:LinguisticSystem</code></td> 
      <td>The value of this property must be an IRI from the provided controlled vocabulary. <br> For example: <code>http://publications.europa.eu/resource/authority/language/NLD</code></td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/license">licence</a></td> 
      <td>A legal document giving official permission to do something with the resource.</td> 
      <td><code>dct:license</code></td> 
      <td><a href="https://definities.geostandaarden.nl/dcat-ap-nl/nl/">Geonovum licence list</a></td> 
      <td><code>dct:LicenseDocument</code></td> 
      <td>The licence under which the catalogue (with resource description) is made available. In the description of distributions and data services, the licences of that resources are taken up.</td> 
      <td>0..1</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/modified">modification date</a></td> 
      <td>Date on which the resource was changed.</td> 
      <td><code>dct:modified</code></td> 
      <td>NA</td> 
      <td><code>xsd:dateTime</code></td> 
      <td>NA</td> 
      <td>0..1</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/issued">release date</a></td> 
      <td>Date of formal issuance of the resource.</td> 
      <td><code>dct:issued</code></td> 
      <td>NA</td> 
      <td><code>xsd:dateTime</code></td> 
      <td>NA</td> 
      <td>0..1</td> 
    </tr> 
    <tr> 
      <td><a href="http://purl.org/dc/terms/rights">rights</a></td> 
      <td>Information about rights held in and over the resource.</td> 
      <td><code>dct:rights</code></td> 
      <td>NA</td> 
      <td><code>dct:RightsStatement</code></td> 
      <td>The rights statement should be a free-text statement placed at a web-accessible location such that the value of this property is the IRI pointing to that statement.</td> 
      <td>0..1</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service">service</a></td> 
      <td>A service that is listed in the catalog.</td> 
      <td><code>dcat:service</code></td> 
      <td>NA</td> 
      <td><code>dcat:DataService</code></td> 
      <td>Some datasets may have real-time Data Services (e.g., Beacon API counting individuals). IT teams should define the relationship between the catalog and the Data Service via this property. While crucial for interoperability, this property is not relevant for end-users to collect.</td> 
      <td>0..*</td> 
    </tr>
    <tr> 
      <td><a href="http://purl.org/dc/terms/temporal">temporal coverage</a></td> 
      <td>Temporal characteristics of the resource.</td> 
      <td><code>dct:temporal</code></td> 
      <td>NA</td> 
      <td><code>dct:PeriodOfTime</code></td> 
      <td>Use this property, if applicable to the catalogue, to indicate a time period the catalogue spans.</td> 
      <td>0..*</td> 
    </tr> 
    <tr> 
      <td><a href="https://www.w3.org/ns/dcat#themeTaxonomy">themes</a></td> 
      <td>A main category of the resource. A resource can have multiple themes.</td> 
      <td><code>dcat:themeTaxonomy</code></td> 
      <td>NA</td> 
      <td><code>skos:ConceptScheme</code></td> 
      <td>This property refers to a knowledge organisation system used to classify the Catalogue's Datasets. It must have at least the value <code>NAL:data-theme</code> as this is the mandatory controlled vocabulary for <code>dcat:theme</code>.</td> 
      <td>0..*</td> 
    </tr> 
  </tbody> 
</table>


