# Permanent Urls # {#permanent-urls}

To support long-term [FAIR (Findable, Accessible, Interoperable, and Reusable)](https://www.go-fair.org/fair-principles/) access to Health-RI metadata schema resources, we provide persistent URLs using the [W3ID](https://w3id.org/) system. These permanent identifiers improve the **findability** and **accessibility** of the related artifacts.
The following links distinguish the published specification from the metadata model and its SHACL sources:

**Specification**

- **Published specification:** [w3id.org/health-ri/metadata/docs](https://w3id.org/health-ri/metadata/docs)
- **Documentation repository:** [w3id.org/health-ri/metadata/docs/git](https://w3id.org/health-ri/metadata/docs/git)

**Metadata model and SHACL resources**

- **Model repository:** [w3id.org/health-ri/metadata/git](https://w3id.org/health-ri/metadata/git)
- **SHACL source files:** [development branch](https://github.com/Health-RI/health-ri-metadata/tree/develop/Formalisation%28shacl%29)

**Metadata model releases**

- **Latest model release:** [w3id.org/health-ri/metadata/releases/latest](https://w3id.org/health-ri/metadata/releases/latest)
- **All model releases:** [w3id.org/health-ri/metadata/releases](https://w3id.org/health-ri/metadata/releases)
- **Specific model release:**
  - Use the following pattern to reference a specific versioned model release: `https://w3id.org/health-ri/metadata/releases/{version}`.
  - For example: [w3id.org/health-ri/metadata/releases/v1.0.1](https://w3id.org/health-ri/metadata/releases/v1.0.1)

**Project Homepage**

**Main page:** [w3id.org/health-ri/metadata](https://w3id.org/health-ri/metadata)

## Versioning and releases ## {#versioning-and-releases}

When implementing the Health-RI metadata schema, use the specification, SHACL validation shapes, and supporting artifacts associated with the same schema version. Check the version’s release status before adopting it. Published versions and their release notes are available through the [metadata model releases](https://w3id.org/health-ri/metadata/releases).

### Version numbers and compatibility ### {#version-numbers-and-compatibility}

The release process uses semantic versioning to communicate the intended compatibility of changes:

<table class="larger-font">
  <thead>
    <tr>
      <th scope="col">Release type</th>
      <th scope="col">Meaning</th>
      <th scope="col">What users should consider</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Major</strong></td>
      <td>Backward-incompatible schema changes.</td>
      <td>Review the changes and migration guidance to identify necessary adjustments to metadata and implementations.</td>
    </tr>
    <tr>
      <td><strong>Minor</strong></td>
      <td>Backward-compatible extensions and improvements.</td>
      <td>Review the new capabilities and any implementation guidance relevant to their adoption.</td>
    </tr>
    <tr>
      <td><strong>Patch</strong></td>
      <td>Backward-compatible technical corrections or documentation improvements that preserve the schema’s meaning and metadata validation outcomes.</td>
      <td>Consult the release notes to understand the correction and its relevance to your implementation.</td>
    </tr>
  </tbody>
</table>

Draft versions may change during development. A **release candidate**, identified by a suffix such as `-rc.1`, is feature frozen for testing. Bug fixes may result in subsequent candidates, such as `-rc.2`, before final release.

### Review and validation ### {#release-review-and-validation}

The release process requires major and minor releases to undergo conceptual review, internal technical validation, testing by external implementers, and formal approval. These activities check that the schema addresses the agreed requirements and that its specification, diagram, SHACL shapes, and test data are consistent. Patch releases follow a lighter review and approval process.

Consult the release notes and changelog for the changes introduced by a particular version, known issues, and migration guidance where required. The [modelling decision log](https://github.com/Health-RI/health-ri-metadata/blob/develop/Documents/V2_decisionLog.md) provides the rationale for recorded Health-RI-specific modelling choices.

### Implementation in the catalogue ### {#catalogue-implementation-status}

Schema publication is coordinated with planned implementation in the National Health Data Catalogue. A schema version may therefore be available before all corresponding catalogue functionality is deployed.

When relying on a particular feature, consult the implementation notes in this specification and the catalogue onboarding guidance. In particular, inclusion of a property in the schema does not by itself establish that the property is supported in catalogue search, filtering, or display.
