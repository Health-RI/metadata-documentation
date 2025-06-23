## [Quality certificate](https://www.w3.org/TR/vocab-dqv/#dqv:QualityCertificate)

An annotation that associates a resource (especially a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules. <br><br>
`Usage note`: This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.

 

### Mandatory Attributes

There are currently no mandatory properties for this class.

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
      <td><a href="https://www.w3.org/TR/annotation-vocab/#hastarget">target</a></td>
      <td>The relationship between an Annotation and its Target.</td>
      <td><code>oa:hasTarget</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource (IRI)</code></td>
      <td>This property has to be filled with the same value as the <code>dct:identifier</code> of the dataset described, in order to link the quality certificate to that dataset. [See also the example in HealthDCAT-AP.](https://healthdcat-ap.github.io/#dqvhasqualityannotation)</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/annotation-vocab/#hasbody">body</a></td>
      <td>The object of the relationship is a resource that is a body of the Annotation.</td>
      <td><code>oa:hasBody</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource (IRI)</code></td>
      <td>IRI pointing to the location where the quality certificate can be found.</td>
      <td>0..1</td>
    </tr>
  </tbody>
</table>

