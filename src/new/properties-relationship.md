### [Relationship](https://w3c.github.io/dxwg/dcat/#Class:Relationship)

An association class for attaching additional information to a relationship between DCAT Resources. <br><br>
`Usage note`: This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [had role](https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole) | The function of an entity or agent with respect to another entity or resource. | `dcat:hadRole` | [IANA Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml) <br> or [ISO Codelist](https://standards.iso.org/iso/19115/resources/Codelists/gml/DS_AssociationTypeCode.xml) | `skos:Concept (IRI)` | Specify, ideally with a value from the linked controlled vocabulary, the nature of the relationship between the linked resources. <br> Example: `http://www.iana.org/assignments/relation/related` | 1..\* |
| [relation](https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole) | A related resource. | `dct:relation` | NA | `rdfs:Resource (IRI)` | This property establishes the link between the described and the related resources. The value of this property is the IRI of the related resource. | 1..\* |

#### Recommended Properties

There are currently no recommended properties for this class.
