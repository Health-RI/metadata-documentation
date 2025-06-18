
### [Checksum](https://spdx.org/rdf/terms/#d4e2091)

A value that allows the contents of a file to be authenticated. <br><br>
`Usage note`: This class is instantiated by properties in other classes that have the range `spdx:Checksum`.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [algorithm](https://spdx.org/rdf/terms/#algorithm) | Identifies the algorithm used to produce the subject Checksum. | `spdx:algorithm` | [Checksum Algorithm members](https://spdx.org/rdf/terms/#d4e2129) | `spdx:ChecksumAlgorithm` | Choose one member of the checksum algorithm members as indicated on the webpage linked in the Controlled Vocabulary column. | 1 |
| [checksum value](https://spdx.org/rdf/terms/#checksumValue) | The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm. | `spdx:checksumValue` | NA | `xsd:hexBinary` | NA | 1 |

#### Recommended Properties

There are currently no recommended properties for this class.
