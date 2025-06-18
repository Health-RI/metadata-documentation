
### [Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)

An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme. <br><br>
`Usage note`: This class is instantiated by the property "other identifier".

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [notation](https://www.w3.org/2009/08/skos-reference/skos.html#notation) | A string that is an identifier in the context of the identifier scheme referenced by its datatype. | `skos:notation` | NA | `rdfs:Literal` | The value of this property is the alternative identifier of the dataset, next to the one indicated in the dct:identifier property. | 1 |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [schema agency](https://www.w3.org/ns/legacy_adms#schemaAgency) | The name of the agency that issued the identifier. | `adms:schemaAgency` | NA | `rdfs:Literal` | NA | 0..1 |
