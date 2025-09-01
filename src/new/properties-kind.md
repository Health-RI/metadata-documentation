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
      <td><a href="https://www.w3.org/TR/vcard-rdf/#d4e891">formatted name</a></td>
      <td>The formatted text corresponding to the name of the object.</td>
      <td><code>vcard:fn</code></td>
      <td>NA</td>
      <td><code>xsd:string</code></td>
      <td>Provide the full name of the contact point, such as the name of a person or department responsible for communication.</td>
      <td>1</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vcard-rdf/#d4e183">has email</a></td>
      <td>To specify the electronic mail address for communication with the object.</td>
      <td><code>vcard:hasEmail</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>When naming a contact point, this information needs to be further specified with additional information, i.e., an email address. This email address does not need to be a direct contact to the person responsible for the management of the data, it could be a generic information email. The email address has to be provided starting with <code>mailto:</code> prefix. <br> For example: <code>mailto:info@example.com</code> / <code>mailto:jane.doe@example.com</code></td>
      <td>1</td>
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
      <td><a href="https://www.w3.org/TR/vcard-rdf/#d4e605">contact page</a></td>
      <td>To specify a uniform resource locator associated with the object.</td>
      <td><code>vcard:hasURL</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>A webpage that either allows to make contact (i.e. a webform) or the information contains how to get into contact.</td>
      <td>0..*</td>
    </tr>
  </tbody>
</table>
