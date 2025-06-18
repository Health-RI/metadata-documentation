### [Attribution](https://www.w3.org/ns/prov#Attribution)

Attribution is the ascribing of an entity to an agent. <br><br>
`Usage note`: This class is instantiated by the property "qualified attribution".

#### Mandatory Properties

There are currently no mandatory properties for this class.

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [agent](https://www.w3.org/TR/2013/REC-prov-o-20130430/#p_agent) | The prov:agent property references an prov:Agent which influenced a resource. | `prov:agent` | NA | `foaf:Agent` | This property points to another instance of class `foaf:Agent`. | 0..1 |
| [role](https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole) | The function of an entity or agent with respect to another entity or resource. | `dcat:hadRole` | [Codelist CI_RoleCode](https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml) | `rdfs:Resource (IRI)` | Choose one of the roles as listed in the controlled vocabulary. Note that for HealthDCAT-AP, the list of roles might be extended in the future. <br> Example: `https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml#processor` | 0..1 |
