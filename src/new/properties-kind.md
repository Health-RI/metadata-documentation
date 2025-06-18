### [Kind](https://www.w3.org/TR/vcard-rdf/#d4e1819)

A description following the vCard specification. <br><br>
`Usage note`: Used to describe contact information for [Dataset](linkto:dataset) and [Dataset Series](linkto:dataset-series). This class is instantiated in these classes whenever the range is `vcard:Kind`.

#### Mandatory Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [formatted name](https://www.w3.org/TR/vcard-rdf/#d4e891) | The formatted text corresponding to the name of the object. | `vcard:fn` | NA | `xsd:string` | Provide the full name of the contact point, such as the name of a person or department responsible for communication. | 1 |
| [has email](https://www.w3.org/TR/vcard-rdf/#d4e183) | To specify the electronic mail address for communication with the object. | `vcard:hasEmail` | NA | `rdfs:Resource` | When naming a contact point, this information needs to be further specified with additional information, i.e., an email address. This email address does not need to be a direct contact to the person responsible for the management of the data, it could be a generic information email. The email address has to be provided starting with `mailto:` prefix. <br> For example: `mailto:info@example.com` / `mailto:jane.doe@example.com` | 1 |

#### Recommended Properties

| **Property name** | **Definition** | **URI** | **Controlled Vocabulary** | **rdfs:Range** | **Usage Note** | **Cardinality** |
| --- | --- | --- | --- | --- | --- | --- |
| [contact page](https://www.w3.org/TR/vcard-rdf/#d4e605) | To specify a uniform resource locator associated with the object. | `vcard:hasURL` | NA | `rdfs:Resource` | A webpage that either allows to make contact (i.e. a webform) or the information contains how to get into contact. | 0..\* |
