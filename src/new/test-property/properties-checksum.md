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
      <td>algorithm</td>
      <td>Identifies the algorithm used to produce the subject Checksum.</td>
      <td>spdx:algorithm</td>
      <td>spdx:ChecksumAlgorithm (IRI)</td>
      <td>1</td>
      <td>Choose one member of the checksum algorithm members as indicated on the webpage linked in the Controlled Vocabulary column.</td>
    </tr>
    <tr>
      <td>checksum value</td>
      <td>The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.</td>
      <td>spdx:checksumValue</td>
      <td>xsd:hexBinary</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>