## Main Classes ## {#classes-main}

### Mandatory Elements
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
  </tbody> 
</table>

### Recommended Elements
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
  </tbody> 
</table>



