
# Core Metadata Schema
<img src="src/images/HRI_Logo.png" alt="HRI Logo" style="width:55%; height:auto;">

## Developer Overview

### Minimal Intro

1. Excel = source
2. Python = transformation
3. Bikeshed = rendering

Output = metadata specification


---

# Quick Start (Most Users)

If you only want to view the specification:

https://health-ri.github.io/metadata-documentation/


---

## Specification

Version **2.0.2** of the Health‑RI core metadata schema for the National Health Data Catalogue, defining key classes, entities, and usage for implementation.


---

## Documentation

Focused on **technical design and usage** (not onboarding or catalogue processes).

Background & onboarding:
- https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279281676  
- https://health-ri.atlassian.net/wiki/spaces/FSD/pages/290291734  
- https://health-ri.atlassian.net/wiki/spaces/FSD/pages/279150593  

**Note:** Frontend implementation is still ongoing.  
Contact: servicedesk@health-ri.nl


---

## Summary

Excel → Python → Bikeshed → HTML
→ Metadata specification output


---

## Status

- [DOI](https://doi.org/10.5281/zenodo.15395604)  
- Repository: https://github.com/Health-RI/health-ri-metadata

# Ways of Working

You can use this project in two ways:

## 1. Local Development (full control)

- Run Python scripts
- Generate property files
- Build full specification locally with Bikeshed
- Recommended for development and maintenance

## 2. GitHub-based Editing (no installation)

- Edit files directly in GitHub
- Commit changes
- GitHub Pages renders the specification automatically

URL:
https://health-ri.github.io/metadata-documentation/


---

# Full Pipeline Overview

excel/HealthRI_v2.0.2.xlsx -> python -> property files -> index.bs -> bikeshed -> index.html


---

# Repository Structure

- chapter/
- class/
- excel/
- images/
- property/
- python/
- table/

---

# Generated Property Files

- properties-adms_identifier
- properties-agent
- properties-attribution
- properties-catalogue
- properties-checksum
- properties-dataservice
- properties-dataset
- properties-datasetseries
- properties-distribution
- properties-kind
- properties-periodoftime
- properties-qualitycertificate
- properties-relationship
- properties-resource

---

# Class Files

- class-agent
- class-attribution
- class-catalog
- class-checksum
- class-data-service
- class-dataset
- class-dataset-series
- class-distribution
- class-identifier
- class-kind
- class-period-of-time
- class-quality-certificate
- class-relationship

---

# Installation Links

- Homebrew: https://brew.sh
- pyenv: https://github.com/pyenv/pyenv#installation
- pipx: https://pipx.pypa.io/stable/
- Bikeshed: https://speced.github.io/bikeshed/#install-final

---

# Install (macOS)

- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- brew install pyenv
- pyenv install 3.12.3
- pyenv global 3.12.3
- brew install pipx
- pipx ensurepath
- pipx install bikeshed
- bikeshed update

---

# Install (Windows)

- pip install pipx
- pipx ensurepath
- pipx install bikeshed
- bikeshed update

---

# Python Requirements

pip install pandas openpyxl

---

# Run Generator

python python/<script>.py

Output:
property/*.html

---

# Build Spec

bikeshed spec index.bs index.html

Validate:

bikeshed --dry-run spec index.bs

---

# IMPORTANT Order

1. Run Python script
2. Check property files
3. Run Bikeshed

---

# Minimal Workflow

1. Clone the repository
2. Edit files
3. Run Python generator (local only)
4. Run Bikeshed (local only)
5. Or commit directly via GitHub

---

# Where to Edit

- Metadata and usage notes (property) -> excel/
- Specification structure -> index.bs
- Text content -> chapter/
- Class descriptions -> class/

---

# GitHub (No Local Install)

Edit directly in GitHub.
Changes will be visible at:

https://health-ri.github.io/metadata-documentation/

Note: updates may take a short time to appear.

---

# Clean Rebuild

Delete:
property/*.html
index.html

Run:
python python/<script>.py
bikeshed spec index.bs index.html

---
