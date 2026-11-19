# Saved specifications and release guide

Each `vX.Y.Z/` folder contains a generated HTML specification and the images it needs. These snapshots preserve access to the documentation used with a particular schema version when the latest page changes.

For the latest specification and citation guidance, see the [repository overview](../README.md). For source editing, table generation, local builds, and validation, see the [maintainer guide](../src/README.md).

## Saved versions

| Version | Committed HTML | Published location after deployment |
|---------|----------------|-------------------------------------|
| v2.0.3 | [Saved specification](v2.0.3/index.html) | [Read v2.0.3](https://health-ri.github.io/metadata-documentation/releases/v2.0.3/) |
| v2.1.0 | [Release preparation snapshot](v2.1.0/index.html) | [v2.1.0 location](https://health-ri.github.io/metadata-documentation/releases/v2.1.0/) |

The v2.1.0 snapshot is still a preparation copy. Set the actual publication date and regenerate it from the final sources before publication. Its saved HTML must include any final narrative or navigation changes; generating a separate preview does not update the snapshot.

## Prepare and save a version

Run commands from the repository root. The example below illustrates preparing v2.2.0 after v2.1.0 has been published; substitute the intended version and its actual previous release.

1. Update the workbook and other sources for the intended release. If property source material changes, regenerate its tables, selecting the input explicitly:

   ```bash
   python src/python/Excel_To_Html.py --excel src/excel/HealthRI_v2.2.0.xlsx
   ```

2. Update the publication metadata in `index.bs`:

   | Field | Example for v2.2.0 |
   |-------|--------------------|
   | `Status Text` | `Health-RI metadata schema v2.2.0.` |
   | `Date` | Actual publication date |
   | `URL` and `Canonical URL` | `https://w3id.org/health-ri/metadata/docs/v2.2.0` |
   | `Previous Version` | `https://w3id.org/health-ri/metadata/docs/v2.1.0` |
   | `TR` | Keep `https://w3id.org/health-ri/metadata/docs` |

   Keep the UML heading and diagram reference in `src/chapter/4-introduction.md` consistent with the version. Review `CITATION.cff` so its version, publication status, and citation URL describe the released specification.

3. Register version access before building the snapshot:

   - Add the new version to the saved versions table in this guide.
   - Keep the latest-specification link in the root `README.md`, and add the outgoing release to its previous-specification links.
   - Use `https://health-ri.github.io/metadata-documentation/releases/vX.Y.Z/` for a saved HTML specification. Versioned PIDs use `https://w3id.org/health-ri/metadata/docs/vX.Y.Z`; verify that the separately maintained w3id redirects resolve to the intended saved version before publication. A generic version redirect rule, once active, does not need a new rule for each release.

4. Generate the snapshot and copy its images while preserving relative paths. For example, in PowerShell:

   ```powershell
   New-Item -ItemType Directory -Force releases/v2.2.0/src/images | Out-Null
   bikeshed spec index.bs releases/v2.2.0/index.html
   Copy-Item src/images/* releases/v2.2.0/src/images/
   ```

   Include any other local assets required by the generated HTML at the paths it references. Keep existing published version folders and their assets unchanged; future releases receive their own folders.

5. Open the saved `index.html` and check its text, property tables, navigation, publication metadata, and images. Confirm that local assets are copied into the version folder and do not depend on changing source files. Run the [local validation commands](../src/README.md#build-and-validate-locally).

6. Commit the final source changes, regenerated property tables when applicable, and the saved version folder together. Review the differences before merging through the release branch into upstream `main`.

## Publication and verification

The [publication workflow](../.github/workflows/publish.yml) builds the latest page. After a push to upstream `main`, it also copies the committed `releases/` folders and current `src/images/` to GitHub Pages, retaining existing site files. It does not regenerate saved HTML or property tables.

After publication, verify:

- the latest specification at `https://health-ri.github.io/metadata-documentation/`;
- the new version's saved HTML and images;
- previous specifications and their images;
- the latest and version-specific w3id documentation URLs.

## If changes are not visible

- Check the GitHub Actions workflow runs and confirm the publication steps completed successfully.
- Confirm the changes reached upstream `main`; pushes to a working branch or fork do not publish the upstream site.
- Check the `gh-pages` branch for the latest page and saved version files.
- Confirm that the intended `releases/vX.Y.Z/index.html` and its images were regenerated and committed; a preview build alone does not update them.
- Check w3id redirects separately if a persistent URL resolves incorrectly.
- Refresh the page and clear the browser cache if necessary.
