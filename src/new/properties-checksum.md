## [Checksum](https://spdx.org/rdf/terms/#d4e2091)

A value that allows the contents of a file to be authenticated. <br><br>
`Usage note`: This class is instantiated by properties in other classes that have the range `spdx:Checksum`.

 

### Mandatory Class Properties

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
      <td><a href="https://spdx.org/rdf/terms/#algorithm">algorithm</a></td>
      <td>Identifies the algorithm used to produce the subject Checksum.</td>
      <td><code>spdx:algorithm</code></td>
      <td><a href="https://spdx.org/rdf/terms/#d4e2129">Checksum Algorithm members</a></td>
      <td><code>spdx:ChecksumAlgorithm</code></td>
      <td>Choose one member of the checksum algorithm members as indicated on the webpage linked in the Controlled Vocabulary column.</td>
      <td>1</td>
    </tr>
    <tr>
      <td><a href="https://spdx.org/rdf/terms/#checksumValue">checksum value</a></td>
      <td>The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.</td>
      <td><code>spdx:checksumValue</code></td>
      <td>NA</td>
      <td><code>xsd:hexBinary</code></td>
      <td>NA</td>
      <td>1</td>
    </tr>
  </tbody>
</table>


### Recommended Class Properties 

There are currently no recommended properties for this class.
