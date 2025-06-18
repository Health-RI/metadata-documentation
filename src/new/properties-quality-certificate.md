
### [Quality certificate](https://www.w3.org/TR/vocab-dqv/#dqv:QualityCertificate)

An annotation that associates a resource (especially a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules. <br><br>
`Usage note`: This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.

#### Mandatory Properties

There are currently no mandatory properties for this class.

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [target](https://www.w3.org/TR/annotation-vocab/#hastarget) | The relationship between an Annotation and its Target. | `oa:hasTarget` | NA | `rdfs:Resource (IRI)` | This property has to be filled with the same value as the `dct:identifier` of the dataset described, in order to link the quality certificate to that dataset. [See also the example in HealthDCAT-AP.](https://healthdcat-ap.github.io/#dqvhasqualityannotation) | 0..1 |
| [body](https://www.w3.org/TR/annotation-vocab/#hasbody) | The object of the relationship is a resource that is a body of the Annotation. | `oa:hasBody` | NA | `rdfs:Resource (IRI)` | IRI pointing to the location where the quality certificate can be found. | 0..1 |
