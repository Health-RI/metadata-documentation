#### Mandatory Properties

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
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point">contact point</a></td>
      <td>Relevant contact information for the cataloged resource.</td>
      <td><code>dcat:contactPoint</code></td>
      <td>NA</td>
      <td><code>vcard:Kind</code></td>
      <td>This property points to a contact point (department or person) that can answer questions about the dataset series. Details on how to describe these are provided under class <code>vcard:Kind</code>. <br> Whenever possible, use <strong>general contact information</strong> (for example from a department) instead of contact information of an individual.</td>
      <td>1..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/description">description</a></td>
      <td>An account of the resource.</td>
      <td><code>dct:description</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Provide a brief description of the dataset series in the catalog. You can repeat this in multiple languages.</td>
      <td>1..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/title">title</a></td>
      <td>A name given to the resource.</td>
      <td><code>dct:title</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>Provide a unique title for your Dataset Series. It can be provided in multiple languages.</td>
      <td>1..*</td>
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
      <td><a href="http://data.europa.eu/r5r/applicableLegislation">applicable legislation</a></td>
      <td>The legislation that is applicable to this resource.</td>
      <td><code>dcatap:applicableLegislation</code></td>
      <td>NA</td>
      <td><code>eli:LegalResource</code></td>
      <td>The legislation that mandates the creation or management of the Dataset Series.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/accrualPeriodicity">frequency</a></td>
      <td>The frequency with which items are added to a collection.</td>
      <td><code>dct:accrualPeriodicity</code></td>
      <td><a href="http://publications.europa.eu/resource/authority/frequency">EU Vocabularies Frequency Authority List</a></td>
      <td><code>skos:Concept</code></td>
      <td>The frequency of a dataset series is not equal to the frequency of the dataset in the collection.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/spatial">geographical coverage</a></td>
      <td>Spatial characteristics of the resource.</td>
      <td><code>dct:spatial</code></td>
      <td>
        EU Vocabularies Lists: <br>
        <a href="http://publications.europa.eu/resource/authority/continent">Continents</a> <br>
        <a href="http://publications.europa.eu/resource/authority/country">Countries</a> <br>
        <a href="http://publications.europa.eu/resource/authority/place">Places</a> <br>
        OR <br>
        <a href="http://sws.geonames.org/">Geonames</a> OR <br>
        <a href="https://vocabs.cbs.nl/nl/">CBS Classificaties en begrippen</a>
      </td>
      <td><code>dct:Location</code></td>
      <td>The EU Vocabularies Name Authority Lists must be used for <a href="https://publications.europa.eu/resource/authority/continent/">continents</a>, <a href="https://publications.europa.eu/resource/authority/country">countries</a>, and <a href="https://publications.europa.eu/resource/authority/place/">places</a> that are in those lists. If a particular location is not in one of the mentioned Named Authority Lists, <a href="https://sws.geonames.org/">Geonames URIs</a> must be used. For districts or neighbourhoods in NL, the <a href="https://vocabs.cbs.nl/nl/">Dutch vocab</a> can be used. However, it might in many cases be desirable to keep the geographical coverage broader (e.g., indicating that NL is covered) to avoid exposing detailed information about the subjects' locations.</td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/modified">modification date</a></td>
      <td>Date on which the resource was changed.</td>
      <td><code>dct:modified</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>This does not correspond to the most recently modified dataset in the collection of the dataset series.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/publisher">publisher</a></td>
      <td>An entity responsible for making the resource available.</td>
      <td><code>dct:publisher</code></td>
      <td>NA</td>
      <td><code>foaf:Agent</code></td>
      <td>The publisher of the dataset series may not be the publisher of all datasets. E.g., a digital archive could take over the publishing of older datasets in the series.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/issued">release date</a></td>
      <td>Date of formal issuance of the resource.</td>
      <td><code>dct:issued</code></td>
      <td>NA</td>
      <td><code>xsd:dateTime</code></td>
      <td>This refers to the moment when the dataset series was established as a managed resource. This is not equal to the release date of the oldest dataset in the collection of the dataset series.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/temporal">temporal coverage</a></td>
      <td>Temporal characteristics of the resource.</td>
      <td><code>dct:temporal</code></td>
      <td>NA</td>
      <td><code>dct:PeriodOfTime</code></td>
      <td>When temporal coverage is a dimension in the dataset series, then the temporal coverage of each dataset in the collection should be part of the temporal coverage. In that case, an open-ended value is recommended, e.g., after 2012.</td>
      <td>0..*</td>
    </tr>
  </tbody>
</table>
