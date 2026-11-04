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

Version numbers communicate compatibility:

- **Major:** backward-incompatible changes that may require updates to existing metadata or implementations.
- **Minor:** backward-compatible extensions and improvements.
- **Patch:** backward-compatible technical corrections or documentation improvements that preserve the schema’s meaning and validation outcomes.

Draft versions may change during development. A **release candidate** (such as `-rc.1`) is feature frozen for testing and may receive bug fixes before final release.

Major and minor releases undergo conceptual review, technical validation, and implementer testing to assess semantic correctness, consistency between the specification and validation shapes, and practical usability before approval.
