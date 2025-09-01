# Supportive Classes # {#classes-supportive}
**Supportive Classes** provide additional context and metadata. They enhance discoverability.

## Mandatory

### [Agent](http://xmlns.com/foaf/spec/#term_Agent)
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Agent</td> 
      <td>Any entity carrying out actions with respect to the (Core) entities Catalogue, Datasets, Data Services and Distributions.</td> 
      <td>A person or organisation that is associated with the catalogue or dataset. This class is instantiated in these classes whenever the range is `foaf:Agent`.</td> 
      <td>foaf:Agent</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-agent.md
</pre>

### [Kind](https://www.w3.org/TR/vcard-rdf/#d4e1819)
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Kind</td> 
      <td>A description following the vCard specification.</td> 
      <td>Used to describe contact information for Dataset and DatasetSeries. This class is instantiated in these classes whenever the range is `vcard:Kind`.</td> 
      <td>vcard:Kind</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-kind.md
</pre>

## Recommended 

### [Attribution](https://www.w3.org/ns/prov#Attribution) 
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Attribution</td> 
      <td>Attribution is the ascribing of an entity to an agent.</td> 
      <td>This class is instantiated by the property "qualified attribution" (`prov:qualifiedAttribution`) in other classes. Use this class to describe any Agent (other than publisher or creator) that has some form of responsibility for the resource. Within the class, this Agent is described with an instance of `foaf:Agent`, and the role is chosen from a controlled vocabulary. This class can be used to indicate the funding agent that provided funding for the dataset.</td> 
      <td>prov:Attribution</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-attribution.md
</pre>

### [Checksum](https://spdx.org/rdf/terms/#d4e2091)
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Checksum</td> 
      <td>A value that allows the contents of a file to be authenticated.</td> 
      <td>This class is instantiated by properties in other classes that have the range `spdx:Checksum`.</td> 
      <td>spdx:Checksum</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-checksum.md
</pre>

### [Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Identifier</td> 
      <td>An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme.</td> 
      <td>This class is instantiated by the property "other identifier" (`adms:identifier`) in other classes. Use this class to provide any additional identifier to the resource or dataset that is not the primary identifier provided in `dct:identifier`.</td> 
      <td>adms:Identifier</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-identifier.md
</pre>

### [Period of time](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Periodoftime) 
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Period of Time</td> 
      <td>An interval of time that is named or defined by its start and end dates.</td> 
      <td>This class is instantiated by properties in other classes that have the range `dct:PeriodOfTime`.</td> 
      <td>dct:PeriodOfTime</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-period-of-time.md
</pre>

### [Quality certificate](https://www.w3.org/TR/vocab-dqv/#dqv:QualityCertificate)
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Quality Certificate</td> 
      <td>An annotation that associates a resource (especially, a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules.</td> 
      <td>This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.</td> 
      <td>dqv:QualityCertificate</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-quality-certificate.md
</pre>


### [Relationship](https://w3c.github.io/dxwg/dcat/#Class:Relationship)
<table> 
  <thead> 
    <tr> 
      <th>Class name</th> 
      <th>HealthDCAT-AP Definition</th> 
      <th>Usage Note</th> 
      <th>URI</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Relationship</td> 
      <td>An association class for attaching additional information to a relationship between DCAT Resources.</td> 
      <td>This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary.</td> 
      <td>dcat:Relationship</td> 
    </tr> 
  </tbody> 
</table>

<pre class=include>
path: src/new/style-tables2.md
</pre>

<pre class=include>
path: src/new/properties-relationship.md
</pre>