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
      <td>contact page</td>
      <td>To specify a uniform resource locator associated with the object.</td>
      <td>vcard:hasURL</td>
      <td>rdfs:Resource&nbsp;&nbsp;(IRI)</td>
      <td>0..n</td>
      <td>A webpage that either allows to make contact (i.e. a webform) or the information contains how to get into contact.</td>
    </tr>
    <tr>
      <td>has email</td>
      <td>To specify the electronic mail address for communication with the object.</td>
      <td>vcard:hasEmail</td>
      <td>rdfs:Resource&nbsp;&nbsp;(IRI)</td>
      <td>1</td>
      <td>When naming a contact point this information needs to be further specified with additional information, i.e., an email address. This email address does not need to be a direct contact to the person responsible for the management of the data, it could be a generic information email.\nThe email address has to be provided starting with mailto: prefix.\nFor example: mailto:info@example.com / mailto: jane.doe@example.com</td>
    </tr>
    <tr>
      <td>formatted name</td>
      <td>The formatted text corresponding to the name of the object.</td>
      <td>vcard:fn</td>
      <td>xsd:string</td>
      <td>1</td>
      <td>Provide the full name of the contact point, such as the name of a person or department responsible for communication.</td>
    </tr>
  </tbody>
</table>