 
 ## Supporting Classes
 
 ### Mandatory Classes
 
 | **Class name** | **HealthDCAT-AP Definition** | **Usage Note** | **URI** |
 | --- | --- | --- | --- |
 | [Agent](#agent) | Any entity carrying out actions with respect to the (Core) entities Catalogue, Datasets, Data Services and Distributions. | A person or organisation that is associated with the catalogue or dataset. This class is instantiated in these classes whenever the range is `foaf:Agent`. | `foaf:Agent` |
 | [Kind](#kind) | A description following the vCard specification. | Used to describe contact information for Dataset and DatasetSeries. This class is instantiated in these classes whenever the range is `vcard:Kind`. | `vcard:Kind` |
 
 ### Recommended Classes
 
 | **Class name** | **HealthDCAT-AP Definition** | **Usage Note** | **URI** |
 | --- | --- | --- | --- |
 | [Attribution](#attribution) | Attribution is the ascribing of an entity to an agent. | This class is instantiated by the property "qualified attribution" (`prov:qualifiedAttribution`) in other classes. Use this class to describe any Agent (other than publisher or creator) that has some form of responsibility for the resource. Within the class, this Agent is described with an instance of `foaf:Agent`, and the role is chosen from a controlled vocabulary. This class can be used to indicate the funding agent that provided funding for the dataset. | `prov:Attribution` |
 | [Checksum](#checksum) | A value that allows the contents of a file to be authenticated. | This class is instantiated by properties in other classes that have the range `spdx:Checksum`. | `spdx:Checksum` |
 | [Identifier](#identifier) | An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme. | This class is instantiated by the property "other identifier" (`adms:identifier`) in other classes. Use this class to provide any additional identifier to the resource or dataset that is not the primary identifier provided in `dct:identifier`. | `adms:Identifier` |
 | [Period of Time](#period-of-time) | An interval of time that is named or defined by its start and end dates. | This class is instantiated by properties in other classes that have the range `dct:PeriodOfTime`. | `dct:PeriodOfTime` |
 | [Relationship](#relationship) | An association class for attaching additional information to a relationship between DCAT Resources. | This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary. | `dcat:Relationship` |
 | [Quality Certificate](#quality-certificate) | An annotation that associates a resource (especially, a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules. | This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.  | `dqv:QualityCertificate` |
 
 
 