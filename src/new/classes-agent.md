# Classes # {#main-classes}

## Mandatory Terms
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
      <td>Catalog</td> 
      <td>A catalogue or repository that hosts the Datasets or Data Services being described.</td> 
      <td>A catalog that is listed in the National Health Data catalog and contains one or several datasets and/or data services. Used to describe a bundle of datasets (and other resources) under a single title, for example, a collection.</td> 
      <td>dcat:Catalog</td> 
    </tr> 
    <tr> 
      <td>Dataset</td> 
      <td>A conceptual entity that represents the information published.</td> 
      <td>When focusing on health data, a dataset typically contains structured information gathered from a study or research project related to health topics. This might include clinical trial results, public health statistics, patient records, survey data, etc. <br> 
      How the data in a dataset can be accessed is defined in the Distribution, which usually points to the actual data files available for access or download. Datasets are often included in a catalog, which organizes and provides metadata about multiple datasets, making them easier to find and use. The term 'agent' refers to any entity responsible for creating, maintaining, or distributing the dataset.</td> 
      <td>dcat:Dataset</td> 
    </tr> 
    <tr> 
      <td>Agent</td> 
      <td>Any entity carrying out actions with respect to the (Core) entities Catalogue, Datasets, Data Services and Distributions.</td> 
      <td>A person or organisation that is associated with the catalogue or dataset. This class is instantiated in these classes whenever the range is `foaf:Agent`.</td> 
      <td>foaf:Agent</td> 
    </tr> 
    <tr> 
      <td>Kind</td> 
      <td>A description following the vCard specification.</td> 
      <td>Used to describe contact information for Dataset and DatasetSeries. This class is instantiated in these classes whenever the range is `vcard:Kind`.</td> 
      <td>vcard:Kind</td> 
    </tr> 
    <tr> 
  </tbody> 
</table>

## Recommended Terms
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
      <td>Data Service</td> 
      <td>A collection of operations that provides access to one or more datasets or data processing functions.</td> 
      <td>A Data service offers the possibility to access and query the data of one (or several datasets) through operations. It offers more extensive possibilities to access the data than the Distribution through a variety of potential actions.</td> 
      <td>dcat:DataService</td> 
    </tr> 
    <tr> 
      <td>Dataset Series</td> 
      <td>A collection of datasets that are published separately, but share some characteristics that group them.</td> 
      <td>A Dataset Series is a collection of similar datasets that are somehow interrelated but published separately. An example is consecutive datasets split by year and/or datasets separated by location. Instead of being made available in a single dataset, the individual (e.g. yearly) datasets are linked together with the Dataset Series class.</td> 
      <td>dcat:DatasetSeries</td> 
    </tr> 
    <tr> 
      <td>Distribution</td> 
      <td>A physical embodiment of the Dataset in a particular format.</td> 
      <td>Used to describe the different ways that a single dataset can be made available. I.e., it can be downloaded or it can be accessed online in one or more distributions (e.g. one in a downloadable .csv file, another file with an access or query webpage).</td> 
      <td>dcat:Distribution</td> 
    </tr> 
    <tr> 
      <td>Attribution</td> 
      <td>Attribution is the ascribing of an entity to an agent.</td> 
      <td>This class is instantiated by the property "qualified attribution" (`prov:qualifiedAttribution`) in other classes. Use this class to describe any Agent (other than publisher or creator) that has some form of responsibility for the resource. Within the class, this Agent is described with an instance of `foaf:Agent`, and the role is chosen from a controlled vocabulary. This class can be used to indicate the funding agent that provided funding for the dataset.</td> 
      <td>prov:Attribution</td> 
    </tr> 
    <tr> 
      <td>Checksum</td> 
      <td>A value that allows the contents of a file to be authenticated.</td> 
      <td>This class is instantiated by properties in other classes that have the range `spdx:Checksum`.</td> 
      <td>spdx:Checksum</td> 
    </tr> 
    <tr> 
      <td>Identifier</td> 
      <td>An identifier in a particular context, consisting of the string that is the identifier; an optional identifier for the identifier scheme; an optional identifier for the version of the identifier scheme; an optional identifier for the agency that manages the identifier scheme.</td> 
      <td>This class is instantiated by the property "other identifier" (`adms:identifier`) in other classes. Use this class to provide any additional identifier to the resource or dataset that is not the primary identifier provided in `dct:identifier`.</td> 
      <td>adms:Identifier</td> 
    </tr> 
    <tr> 
      <td>Period of Time</td> 
      <td>An interval of time that is named or defined by its start and end dates.</td> 
      <td>This class is instantiated by properties in other classes that have the range `dct:PeriodOfTime`.</td> 
      <td>dct:PeriodOfTime</td> 
    </tr> 
    <tr> 
      <td>Relationship</td> 
      <td>An association class for attaching additional information to a relationship between DCAT Resources.</td> 
      <td>This class is instantiated by the property "qualified relation" (`dcat:qualifiedRelation`) in other classes. Use this class to describe a relationship with another resource or dataset. Within the class, that resource is indicated, as well as the role this resource has in relation to the described one. The role is indicated based on a controlled vocabulary.</td> 
      <td>dcat:Relationship</td> 
    </tr> 
    <tr> 
      <td>Quality Certificate</td> 
      <td>An annotation that associates a resource (especially, a dataset or a distribution) to another resource (for example, a document) that certifies the resource's quality according to a set of quality assessment rules.</td> 
      <td>This class is instantiated by the property "quality annotation" (`dqv:hasQualityAnnotation`) in other classes. Use this class to provide a link between the resource or dataset and an associated quality annotation.</td> 
      <td>dqv:QualityCertificate</td> 
    </tr> 
  </tbody> 
</table>



