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

## Release management ## {#release-management}

Changes to the Health-RI metadata schema are tracked in the [model repository](https://github.com/Health-RI/health-ri-metadata). Enhancement proposals are assessed by the metadata modeling group as described in the [contribution guide](https://github.com/Health-RI/health-ri-metadata/blob/develop/CONTRIBUTING.md#i-want-to-suggest-enhancements). Published schema versions are recorded in the [model releases](https://w3id.org/health-ri/metadata/releases), with changes described in the corresponding changelog.

The technical specification is maintained in the documentation repository. Before publication, maintainers update its version and publication date, regenerate property tables when the Excel source changes, and build and validate the HTML. Each published specification and its images are saved in a versioned folder, retaining earlier specifications for future reference. The [publication instructions](https://github.com/Health-RI/metadata-documentation/blob/v2.1/README.md#publication) describe these steps.

When adopting a schema version, use the corresponding specification and consult that version's model changelog to identify changes affecting your metadata.

