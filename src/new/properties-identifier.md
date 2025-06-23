## [Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)

An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme. <br><br>
`Usage note`: This class is instantiated by the property "other identifier".

 

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://www.w3.org/2009/08/skos-reference/skos.html#notation">notation</a></td>
      <td>A string that is an identifier in the context of the identifier scheme referenced by its datatype.</td>
      <td><code>skos:notation</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>The value of this property is the alternative identifier of the dataset, next to the one indicated in the dct:identifier property.</td>
      <td>1</td>
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
      <td><a href="https://www.w3.org/ns/legacy_adms#schemaAgency">schema agency</a></td>
      <td>The name of the agency that issued the identifier.</td>
      <td><code>adms:schemaAgency</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>NA</td>
      <td>0..1</td>
    </tr>
  </tbody>
</table>

