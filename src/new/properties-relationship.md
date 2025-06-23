## [Relationship](https://w3c.github.io/dxwg/dcat/#Class:Relationship)

An association class for attaching additional information to a relationship between DCAT Resources. <br><br>
`Usage note`: This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary.

 

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
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole">had role</a></td>
      <td>The function of an entity or agent with respect to another entity or resource.</td>
      <td><code>dcat:hadRole</code></td>
      <td>
        <a href="https://www.iana.org/assignments/link-relations/link-relations.xhtml">IANA Link Relations</a> <br>
        or <a href="https://standards.iso.org/iso/19115/resources/Codelists/gml/DS_AssociationTypeCode.xml">ISO Codelist</a>
      </td>
      <td><code>skos:Concept (IRI)</code></td>
      <td>Specify, ideally with a value from the linked controlled vocabulary, the nature of the relationship between the linked resources. <br> Example: <code>http://www.iana.org/assignments/relation/related</code></td>
      <td>1..*</td>
    </tr>
    <tr>
      <td><a href="https://www.w3.org/TR/vocab-dcat-3/#Property:relationship_hadRole">relation</a></td>
      <td>A related resource.</td>
      <td><code>dct:relation</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource (IRI)</code></td>
      <td>This property establishes the link between the described and the related resources. The value of this property is the IRI of the related resource.</td>
      <td>1..*</td>
    </tr>
  </tbody>
</table>

### Recommended Attributes 

There are currently no recommended properties for this class.
