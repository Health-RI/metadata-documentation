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
      <td>had role</td>
      <td>The function of an entity or agent with respect to another entity or resource.</td>
      <td>dcat:hadRole</td>
      <td>skos:Concept (IRI)</td>
      <td>1..n</td>
      <td>Specify, ideally with a value from the linked controlled vocabulary, the nature of the relationship between the linked resources.\nExample: http://www.iana.org/assignments/relation/related</td>
    </tr>
    <tr>
      <td>relation</td>
      <td>A related resource.</td>
      <td>dct:relation</td>
      <td>rdfs:Resource (IRI)</td>
      <td>1..n</td>
      <td>This property establishes the link between the described and the related resources. The value of this property is the IRI of the related resource.</td>
    </tr>
  </tbody>
</table>