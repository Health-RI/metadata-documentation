## [Agent](http://xmlns.com/foaf/spec/#term_Agent)

Any entity carrying out actions with respect to the (Core) entities Catalogue, Datasets, Data Services and Distributions. <br><br>
`Usage note`: A person or organisation that is associated with the catalogue or dataset. This class is instantiated in these classes whenever the range is `foaf:Agent`.

 

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
      <td><a href="http://xmlns.com/foaf/spec/#term_mbox">email</a></td>
      <td>An email address via which contact can be made. This property SHOULD be used to provide the email address of the Agent, specified using fully qualified mailto: URI scheme linkto:macro: (RFC6068). The email SHOULD be used to establish a communication channel to the agent.</td>
      <td><code>foaf:mbox</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>It is possible to provide the email address of the appropriate institution or department if no personal email address can be provided. <br>The email address has to be provided starting with <code>mailto:</code> prefix. <br> For example: mailto:info@example.com / mailto:jane.doe@example.com</td>
      <td>1</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/identifier">identifier</a></td>
      <td>A unique identifier of the agent.</td>
      <td><code>dct:identifier</code></td>
      <td>ORCID: (<a href="https://orcid.org/">https://orcid.org/</a>) <br> ROR: (<a href="https://ror.org/">https://ror.org/</a>) <br> ISNI: (<a href="https://isni.org/page/search-database/">https://isni.org/page/search-database/</a>) <br> TOOI: (<a href="https://standaarden.overheid.nl/tooi/waardelijsten/">https://standaarden.overheid.nl/tooi/waardelijsten/</a>) <br> Wikidata: (<a href="https://www.wikidata.org/">https://www.wikidata.org/</a>)</td>
      <td><code>rdfs:Literal</code></td>
      <td>Specify the entity (person or organisation) by providing an identifier. We recommend using an ORCID identifier for a person or ROR identifier for an organisation. Dutch governmental organisations are listed in TOOI. If these are not available, you can use ISNI, or Wikidata or any other identifier you may have. If you have multiple identifiers, you should provide them all.</td>
      <td>1..*</td>
    </tr>
    <tr>
      <td><a href="http://xmlns.com/foaf/spec/#term_name">name</a></td>
      <td>A name for some thing.</td>
      <td><code>foaf:name</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>This property refers to the given name of the entity. Example: Jane Doe (for a person) and Radboudumc (for an organisation). This property can be repeated for different versions of the name (e.g. the name in different languages).</td>
      <td>1..*</td>
    </tr>
    <tr>
      <td><a href="http://xmlns.com/foaf/spec/#term_homepage">URL</a></td>
      <td>A homepage for some thing.</td>
      <td><code>foaf:homepage</code></td>
      <td>NA</td>
      <td><code>rdfs:Resource</code></td>
      <td>Provide the URL of the page containing contact information, such as a contact form or details for reaching out. If a specific contact page is unavailable, the main website of the Agent is sufficient.</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

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
      <td><a href="http://purl.org/dc/terms/spatial">country</a></td>
      <td>Country of the agent.</td>
      <td><code>dct:spatial</code></td>
      <td><a href="https://publications.europa.eu/resource/authority/country">EU Vocabularies Country Authority List</a></td>
      <td><code>dct:Location</code></td>
      <td>Use the appropriate term from the EU authority table. Example for the Netherlands: <code>http://publications.europa.eu/resource/authority/country/NLD</code></td>
      <td>0..*</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.publishernote">publisher note</a></td>
      <td>A property used to provide additional context about a publisher.</td>
      <td><code>healthdcatap:publisherNote</code></td>
      <td>NA</td>
      <td><code>rdfs:Literal</code></td>
      <td>This property can be repeated for parallel language versions of the publisher's notes. Example: "Sciensano is a research institute and the national public health institute of Belgium. It is a so-called federal scientific institution that operates under the authority of the federal minister of Public Health and the federal minister of Agriculture of Belgium."@en</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="https://healthdcat-ap.github.io/#Dataset.publishertype">publisher type</a></td>
      <td>A category (type) of organisation that makes the Dataset available</td>
      <td><code>healthdcatap:publisherType</code></td>
      <td>NA</td>
      <td><code>skos:Concept</code></td>
      <td>A <a href="https://raw.githubusercontent.com/SEMICeu/ADMS-AP/master/purl.org/ADMS_SKOS_v1.00.rdf">controlled vocabulary</a> is provided, denoting commonly recognised health publishers. <em>Current status</em>: Specifically for the health domain, a controlled vocabulary is being developed to include commonly recognised health publishers. This vocabulary is currently under development. Version 1.0 includes the following types: Academia-ScientificOrganisation, Company, IndustryConsortium, LocalAuthority, NationalAuthority, NonGovernmentalOrganisation, NonProfitOrganisation, PrivateIndividual, RegionalAuthority, StandardisationBody and SupraNationalAuthority. These should use the following URL format: <em><code>http://purl.org/adms/publishertype/[type]</code></em>.</td>
      <td>0..1</td>
    </tr>
    <tr>
      <td><a href="http://purl.org/dc/terms/type">type</a></td>
      <td>A type of the agent that makes the Catalogue or Dataset available.</td>
      <td><code>dct:type</code></td>
      <td><a href="https://raw.githubusercontent.com/SEMICeu/ADMS-AP/master/purl.org/ADMS_SKOS_v1.00.rdf">ADMS Agent Type</a></td>
      <td><code>skos:Concept</code></td>
      <td>NA</td>
      <td>0..1</td>
    </tr>
  </tbody>
</table>

