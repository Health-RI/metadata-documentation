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
      <td>applicable legislation</td>
      <td>The legislation that is applicable to this resource.</td>
      <td>dcatap:applicableLegislation</td>
      <td>eli:LegalResource (IRI)</td>
      <td>0..n</td>
      <td>The legislation that mandates the creation or management of the Dataset Series.</td>
    </tr>
    <tr>
      <td>contact point</td>
      <td>Relevant contact information for the cataloged resource.</td>
      <td>dcat:contactPoint</td>
      <td>vcard:Kind</td>
      <td>1..n</td>
      <td>This property points to a contact point (department or person) that can answer questions about the dataset series. Details on how to describe these are provided under class vcard:Kind.\nWhenever possible, use a general contact information (for example from a department) instead of contact information of an individual.</td>
    </tr>
    <tr>
      <td>description</td>
      <td>An account of the resource.</td>
      <td>dct:description</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>Briefly describe the dataset series in the catalog. You can repeat this in multiple languages.</td>
    </tr>
    <tr>
      <td>frequency</td>
      <td>The frequency with which items are added to a collection.</td>
      <td>dct:accrualPeriodicity</td>
      <td>skos:Concept (IRI)</td>
      <td>0..1</td>
      <td>The frequency of a dataset series is not equal to the frequency of the dataset in the collection.</td>
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
      <td>modification date</td>
      <td>Date on which the resource was changed.</td>
      <td>dct:modified</td>
      <td>xsd:dateTime</td>
      <td>0..1</td>
      <td>This is not equal to the most recent modified dataset in the collection of the dataset series.</td>
    </tr>
    <tr>
      <td>publisher</td>
      <td>An entity responsible for making the resource available.</td>
      <td>dct:publisher</td>
      <td>foaf:Agent</td>
      <td>0..1</td>
      <td>The publisher of the dataset series may not be the publisher of all datasets.&nbsp;&nbsp;E.g. a digital archive could take over the publishing of older datasets in the series.</td>
    </tr>
    <tr>
      <td>release date</td>
      <td>Date of formal issuance of the resource.</td>
      <td>dct:issued</td>
      <td>xsd:dateTime</td>
      <td>0..1</td>
      <td>The moment when the dataset series was established as a managed resource. This is not equal to the release date of the oldest dataset in the collection of the dataset series.</td>
    </tr>
    <tr>
      <td>temporal coverage</td>
      <td>Temporal characteristics of the resource.</td>
      <td>dct:temporal</td>
      <td>dct:PeriodOfTime</td>
      <td>0..n</td>
      <td>When temporal coverage is a dimension in the dataset series then the temporal coverage of each dataset in the collection should be part of the temporal coverage. In that case, an open ended value is recommended, e.g. after 2012.</td>
    </tr>
    <tr>
      <td>title</td>
      <td>A name given to the resource.</td>
      <td>dct:title</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>Provide a unique title for your Dataset Series, which can be repeated in multiple languages.</td>
    </tr>
  </tbody>
</table>