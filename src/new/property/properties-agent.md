<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Property label</th>
      <th>Definition</th>
      <th>Property URI</th>
      <th>Range</th>
      <th>Cardinality</th>
      <th>Usage note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>country</td>
      <td>Spatial characteristics of the resource.</td>
      <td>dct:spatial</td>
      <td>dct:Location (IRI)</td>
      <td>0..n</td>
      <td>Use the appropriate term from the EU authority table. Example for the Netherlands: http://publications.europa.eu/resource/authority/country/NLD</td>
    </tr>
    <tr>
      <td>email</td>
      <td>A email address via which contact can be made. This property SHOULD be used to provide the email address of the Agent, specified using fully qualified mailto: URI scheme [ RFC6068 ]. The email SHOULD be used to establish a communication channel to the agent.</td>
      <td>foaf:mbox</td>
      <td>rdfs:Resource&nbsp;&nbsp;(IRI)</td>
      <td>1</td>
      <td>It is preferred to provide a general email address of the appropriate institution or department instead of a personal email address, even if an individual is described with this instance of foaf:Agent.\nThis protects their privacy and enables contact about the resource even after the individual has left the institution.\n\nThe email address has to be provided starting with mailto: prefix.\nFor example: mailto:info@example.com</td>
    </tr>
    <tr>
      <td>identifier</td>
      <td>An unambiguous reference to the resource within a given context.</td>
      <td>dct:identifier</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>Specify the entity (person or organization) by providing an identifier. We recommend using an ORCID identifier for a person or ROR identifier for organization. Dutch governmenta organization are listed in TOOI. If these are not available, you can use ISNI, or Wikidata or any other identifier you may have. If you have multiple identifiers, you should provide them all.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>A name for some thing.</td>
      <td>foaf:name</td>
      <td>rdfs:Literal</td>
      <td>1..n</td>
      <td>This property refers to the given name of the entity. Example: Jane Doe (for a person) and Radboudumc (for an organization). This property can be repeated for different versions of the name (e.g. the name in different languages).</td>
    </tr>
    <tr>
      <td>publisher note</td>
      <td>A description of the publisher activities.</td>
      <td>healthdcatap:publishernote</td>
      <td>rdfs:Literal</td>
      <td>0..1</td>
      <td>This property can be repeated for parallel language versions of the publisher notes. Example: "Sciensano is a research institute and the national public health institute of Belgium. It is a so-called federal scientific institution that operates under the authority of the federal minister of Public Health and the federal minister of Agriculture of Belgium."@en</td>
    </tr>
    <tr>
      <td>publisher type</td>
      <td>A type of organisation that makes the Dataset available.</td>
      <td>healthdcatap:publishertype</td>
      <td>skos:Concept (IRI)</td>
      <td>0..1</td>
      <td>Current status: Specifically for the health domain, a controlled vocabulary is being developed to include commonly recognised health publishers. This vocabulary is currently under development. Version 1.0 includes the following types: Academia-ScientificOrganisation, Company, IndustryConsortium, LocalAuthority, NationalAuthority, NonGovernmentalOrganisation, NonProfitOrganisation, PrivateIndividual, RegionalAuthority, StandardisationBody and SupraNationalAuthority. These should use the following URL: http://purl.org/adms/publishertype/[type].</td>
    </tr>
    <tr>
      <td>type</td>
      <td>The nature or genre of the resource.</td>
      <td>dct:type</td>
      <td>skos:Concept (IRI)</td>
      <td>0..1</td>
      <td>This property should be filled using ADMS vocabulary (http://purl.org/adms/publishertype/1.0)</td>
    </tr>
    <tr>
      <td>URL</td>
      <td>A homepage for some thing.</td>
      <td>foaf:homepage</td>
      <td>rdfs:Resource (IRI)</td>
      <td>1</td>
      <td>Provide the URL of the page containing contact information, such as a contact form or details for reaching out. If a specific contact page is unavailable, the main website of the Agent is sufficient.</td>
    </tr>
  </tbody>
</table>