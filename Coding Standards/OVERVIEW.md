# refine.digital development standards

## This single document is the canonical, project-agnostic **Development Standards Framework**.

# Development Standards Framework — single-folder manifest

Put this file (and the sibling files listed below) in a repository called `development-standards` and make it the reference that both humans and AIs (Claude Code, GitHub Actions, bots) read to configure and lint new projects.

---

## 0\. Top-level folder layout (recommended)

```
development-standards/
├─ 00-Development-Standards-Framework.md        # This file (human + AI readable manifesto and manifest)
├─ README.md                            # Quick-start reference for teams
├─ templates/                            # Boilerplate templates to copy into new repos
│  ├─ README-template.md
│  ├─ CONTRIBUTING-template.md
│  ├─ ISSUE_TEMPLATE.md
│  ├─ PULL_REQUEST_TEMPLATE.md
│  ├─ CODE_OF_CONDUCT-template.md
│  └─ .github/workflows/ci-template.yml
├─ configs/                              # Opinionated config snippets to drop-in
│  ├─ editorconfig/.editorconfig
│  ├─ vscode/.vscode-settings.json
│  ├─ prettier/.prettierrc.json
│  ├─ eslint/.eslintrc.json
│  ├─ markdownlint/.markdownlintrc.yml
│  └─ pre-commit/.pre-commit-config.yaml
├─ language-guides/                      # Per-language/style docs + examples
│  ├─ javascript.md
│  ├─ typescript.md
│  ├─ php.md
│  ├─ terraform.md
│  ├─ go.md
│  ├─ sql.md
│  ├─ shell.md
│  ├─ docker.md
│  └─ markdown.md
└─ governance/                           # Policies, access control, release rules
   ├─ naming-conventions.md
   ├─ branching-and-git.md
   ├─ versioning-and-releases.md
   └─ security-and-secrets.md
```

---

## 1\. Purpose & usage

**Purpose:** create consistent, discoverable, automatable rules for all code and infra projects — usable by developers and by automation (formatters, linters, CI). Use these files as templates for new repositories or import key sections into project scaffolding tools.

**How to use:**

* Clone `dev-standards` and copy `templates/*` and `configs/*` into new repo root during repo scaffolding.  
* Enforce via CI (GitHub Actions) and local pre-commit hooks.  
* Keep the central repo authoritative; update language-guides when new widely accepted standards emerge.

---

## 2\. High-level naming & structure rules (governance/naming-conventions.md)

**Repository names**

* Use `kebab-case` for GitHub repo names: `my-service-api`, `billing-worker`.  
* Keep names short (5 words max) and explicit about purpose.

**Folders & files**

* Root-level files: `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, `.gitignore`, `.editorconfig`, `.prettierrc.json` (if JS/TS), `.gitattributes`.  
* Source code under `src/` (or language-native default, e.g. `cmd/` for Go), tests under `test/` or `__tests__/` for JS.

**Branching**

* `main` (protected), `develop` (optional), feature branches named `feature/<short-desc>`, bugfix `bug/<id>-short`, chore `chore/<desc>`.

**Commit messages**

* Use **Conventional Commits**: `type(scope?): subject` (e.g. `feat(auth): add JWT middleware`). This enables changelog automation and dovetails with SemVer.

**Releases**

* Semantic Versioning `MAJOR.MINOR.PATCH`.

(See `governance/branching-and-git.md` and `versioning-and-releases.md` templates.)

---

## 3\. Core files and example contents (copy into `templates/`)

### README-template.md

Include:

* Short description  
* Status / badge (build, coverage)  
* Quick start: prerequisites, install, run, test  
* Contributing & support links  
* License & contact

### CONTRIBUTING-template.md

* How to open issues, PR workflow, code review expectations, CI gating, expected tests, and who approves.

### CODE\_OF\_CONDUCT-template.md

* Use Contributor Covenant (link included in central repo). Include enforcement contact.

### ISSUE\_TEMPLATE.md & PULL\_REQUEST\_TEMPLATE.md

* Structured templates to capture reproduction steps, environment, tests, related issues, and PR checklist (lint, tests, changelog entry, reviewer assignment).

---

## 4\. Editor, formatting & linting (configs/)

### .editorconfig (example)

```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

### .prettierrc.json (example)

```json
{
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5",
  "arrowParens": "always"
}
```

### .eslintrc.json (example for JS/TS projects)

```json
{
  "root": true,
  "env": { "node": true, "es6": true, "browser": true },
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint", "react", "prettier"],
  "rules": {
    "prettier/prettier": ["error"]
  }
}
```

### VS Code settings \- .vscode/settings.json

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true
}
```

### .gitattributes

```
* text=auto
*.sh eol=lf
*.md text
```

### pre-commit (example \- pre-commit or husky \+ lint-staged)

* Use `pre-commit` for multi-language repos or `husky` \+ `lint-staged` for JS-first repos.  
* Hook tasks: run formatters, run linters, run unit-tests (fast subset), prevent secrets (git-secrets).

---

## 5\. Language-specific guidance (language-guides/)

NOTE: each guide has quick checks and automation to enforce: formatters, linters, CI steps.

### JavaScript / TypeScript (language-guides/javascript.md)

* Use Prettier for formatting, ESLint for code quality, TypeScript for typed projects.  
* Choose a style reference (Airbnb or Google) and map to ESLint \+ Prettier. For React, follow Airbnb React/JSX rules.  
* Automate: `npm run lint`, `npm run test`, `npm run build` in CI.  
* Example: extend `airbnb-base`, `plugin:@typescript-eslint/recommended`, and the Prettier plugin.

(Reference: Airbnb style guide, Google JS style guide.)

### PHP (language-guides/php.md)

* Follow **PHP-FIG PSR** standards — PSR-1 \+ PSR-12 for coding style, PSR-4 for autoloading.  
* Use `php-cs-fixer` or `phpcs` configured to PSR-12 in CI.  
* Example rule: class names in `StudlyCaps`, method names in `camelCase`.

(Reference: PHP-FIG PSR-12.)

### Terraform / HCL (language-guides/terraform.md)

* Run `terraform fmt` and `terraform validate` in CI.  
* Use `tflint` and `tfsec` for linting and security scanning.  
* Organize infra into modules, keep variables limited and documented, avoid hard-coded credentials.  
* Use naming scheme for resources and outputs; semantic module versions (tags).

(See HashiCorp recommendations and Gruntwork style guide.)

### Go (language-guides/go.md)

* Use `gofmt`/`gofumpt`, `go vet`, `golangci-lint`.  
* Project layout: `cmd/`, `internal/`, `pkg/`, `api/`, `configs/` (adapted to the project scope).

### Shell scripts (language-guides/shell.md)

* Use `#!/usr/bin/env bash` only when Bash features are required; prefer POSIX `sh` when possible.  
* Always include safety flags: `set -euo pipefail` and trap errors for cleanup.  
* Use `shellcheck` in CI and pre-commit hooks.

### Dockerfiles (language-guides/docker.md)

* Use official base images, multi-stage builds, pin versions where practical, minimize layers and image size.  
* Follow Docker best practices (do not run as root; clear package caches; use `.dockerignore`).

### SQL (language-guides/sql.md)

* Use migrations (Flyway, Liquibase, or native tooling) not ad-hoc `CREATE TABLE` scripts.  
* Naming conventions: `snake_case` for table & column names, `pk_`, `fk_` prefixes for constraints if desired.  
* Keep DDL in `migrations/` with timestamps and ID-based ordering.

### Markdown (language-guides/markdown.md)

* Follow CommonMark/GFM; include a small `markdownlint` config to enforce rules (line length, heading style, no trailing spaces unless code block).

---

## 6\. CI / GitHub Actions (templates/.github/workflows/ci-template.yml)

A single pipeline for lint/test/build that runs when PRs target `main`.

```
name: CI
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      - name: Install
        run: npm ci
      - name: Run linters
        run: npm run lint
      - name: Run tests
        run: npm test -- --coverage

  terraform:
    if: contains(github.event.pull_request.files, '.tf') || github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
      - name: terraform fmt
        run: terraform fmt -check
      - name: tflint
        run: tflint
      - name: tfsec
        run: tfsec .
```

---

## 7\. Security & secrets (governance/security-and-secrets.md)

* **Never** commit secrets. Use secrets managers: HashiCorp Vault, AWS Secrets Manager, GitHub Secrets for CI.  
* Scan history for leaked secrets when onboarding (git-secrets, truffleHog).  
* Add a `SECRETS.md` to describe how to request and rotate secrets.

---

## 8\. Examples / inspiration (governance/refs.md)

Useful canonical references to derive rules from (keep updated):

* PHP-FIG PSR-12 (coding standards for PHP)  
* HashiCorp Terraform style & recommended practices  
* Airbnb JavaScript / React style guide and Google JS style guide  
* Conventional Commits and SemVer for commits/releases  
* Government/large org examples: UK GOV code patterns, US 18F / USDS repositories (see "Design systems" and source code policies)

---

## 9\. Quick automation checklist to onboard a new repo

1. Create repo in kebab-case; add `README.md` from template.  
2. Add `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`.  
3. Add `.editorconfig`, `.gitattributes`, `.prettierrc.json`, `.eslintrc.json` as appropriate.  
4. Add `.github/workflows/ci.yml` from template and enable branch protection on `main` (require PRs, require CI passing, require 1-2 reviewers).  
5. Add pre-commit hooks (install process in CONTRIBUTING.md).  
6. Add CODEOWNERS to route reviews.

---

## 10\. Tailoring & governance process

* Changes to `dev-standards` must be made by PR with two reviewers.  
* Major changes (affecting infra or CI) must be discussed in an RFC (use `docs/rfcs/` folder) and approved by platform leads.

---

## 11\. Machine-readable outputs for AI (short mapping snippet)

AI agents that scaffold repos should read these files (or a machine-friendly JSON derived from them). Example mapping extracted from `00-Dev-Standards-Framework.md`:

```json
{
  "repoNameStyle":"kebab-case",
  "branching":{
    "main":"protected",
    "feature":"feature/<desc>",
    "commitMessage":"conventional-commits"
  },
  "formatters":{
    "js":"prettier",
    "php":"php-cs-fixer",
    "go":"gofmt",
    "terraform":"terraform fmt"
  }
}
```

---

## 12\. Next steps I recommend

* Add a GitHub Action that lints PRs against this repo's templates and flags non-conforming repos.  
* Provide `create-repo` CLI (Node or Go) that copies the right templates and optionally prompts for language choices.

---

*End of canonical single-file manifest. Use the `templates/` and `language-guides/` files to copy content into new repos. Keep this repo small and authoritative.*
