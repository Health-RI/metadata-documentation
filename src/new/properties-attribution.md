## [Attribution](https://www.w3.org/ns/prov#Attribution)

Attribution is the ascribing of an entity to an agent. <br><br>
`Usage note`: This class is instantiated by the property "qualified attribution".

 

### Mandatory Class Properties

There are currently no mandatory properties for this class.

### Recommended Class Properties 

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
      <td><a href="https://www.w3.org/TR/2013/REC-prov-o-20130430/#p_agent">agent</a></td>
      <td>The prov:agent property references an prov:Agent which influenced a resource.</td>
      <td><code>prov:agent</code></td>
      <td>NA</td>
      <td><code>foaf:Agent</code></td>
      <td>This property points to another instance of class <code>foaf:Agent</code>.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole">role</a></td>
      <td>The function of an entity or agent with respect to another entity or resource.</td>
      <td><code>dcat:hadRole</code></td>
      <td><a href="https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml">Codelist CI_RoleCode</a></td>
      <td><code>rdfs:Resource (IRI)</code></td>
      <td>Choose one of the roles as listed in the controlled vocabulary. Note that for HealthDCAT-AP, the list of roles might be extended in the future. <br> Example: <code>https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor</code></td>
      <td>0..1</td>
    </tr>
  </tbody>
</table>
