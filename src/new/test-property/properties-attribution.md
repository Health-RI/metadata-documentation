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
      <td>agent</td>
      <td>The prov:agent property references an prov:Agent which influenced a resource.</td>
      <td>prov:agent</td>
      <td>foaf:Agent</td>
      <td>0..1</td>
      <td>This property points to another instance of class foaf:Agent.</td>
    </tr>
    <tr>
      <td>role</td>
      <td>The function of an entity or agent with respect to another entity or resource.</td>
      <td>dcat:hadRole</td>
      <td>rdfs:Resource (IRI)</td>
      <td>0..1</td>
      <td>Choose one of the roles as listed in the controlled vocabulary. Note that for HealthDCAT-AP, the list of roles might be extended in the future.\nExample: https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor</td>
    </tr>
  </tbody>
</table>