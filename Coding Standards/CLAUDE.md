# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **refine.digital Development Standards Framework** - a comprehensive, AI-native standards repository focused on Infrastructure-as-Code (IaC) projects. It provides machine-readable, enforceable naming conventions and development standards for Terraform, YAML, Shell, Markdown, HCL, and configuration files.

**Primary Goal**: Solve project naming inconsistencies across GitHub repositories, local folders, Terraform resources, YAML configurations, and VS Code workspaces.

## Repository Structure

```
Coding Standards/
├── development-standards/          # Core standards framework (submodule/folder)
│   ├── governance/                 # Policies and naming standards
│   │   ├── PROJECT-NAMING-STANDARDS.md    # ⭐ THE BIG ONE - Canonical naming guide
│   │   └── naming-validation-rules.json   # Machine-readable validation rules
│   ├── language-guides/            # Language-specific standards
│   │   ├── terraform.md            # Terraform standards (2,420 lines)
│   │   ├── yaml.md                 # YAML formatting and linting
│   │   ├── shell.md                # Shell script best practices
│   │   ├── markdown.md             # Documentation standards
│   │   ├── hcl.md                  # Packer, Vault, Nomad configs
│   │   └── conf.md                 # Config files (.conf, .env, .ini)
│   ├── configs/                    # Drop-in configuration files
│   │   ├── editorconfig/           # .editorconfig templates
│   │   ├── terraform/              # Terraform configs
│   │   ├── yaml/                   # YAML linter configs
│   │   ├── markdown/               # Markdownlint configs
│   │   ├── shell/                  # ShellCheck configs
│   │   ├── vscode/                 # VS Code settings
│   │   └── git/                    # Git configs and hooks
│   └── templates/                  # Project templates
│       ├── github-repo/            # GitHub repository templates
│       └── terraform-module/       # Terraform module templates
├── OVERVIEW.md                     # Framework manifesto (363 lines)
├── PLAN.md                         # Implementation roadmap
├── ACCELERATED-PLAN.md             # Fast-track implementation
├── AI-ASSISTED-VALIDATION.md       # Claude Code Router integration guide
├── PLUGIN-SETUP-GUIDE.md           # wshobson/agents marketplace plugin setup
├── PLUGIN-INTEGRATION-EXAMPLES.md  # Practical plugin usage examples
├── PLUGIN-TESTING-CHECKLIST.md     # Plugin testing verification
└── CLAUDE-CODE-TEMPLATES-GUIDE.md  # claude-code-templates CLI installer guide
```

## Key Documents (Read These First!)

### 1. PROJECT-NAMING-STANDARDS.md (⭐ MOST IMPORTANT)
**Location**: `development-standards/governance/PROJECT-NAMING-STANDARDS.md`

This is the **single source of truth** for ALL naming conventions. Contains:
- GitHub repository naming (kebab-case with category prefixes)
- Terraform resource/variable naming (snake_case)
- YAML key naming (snake_case)
- Shell script/variable/function naming
- Environment naming conventions
- VS Code workspace naming
- Validation patterns and examples

**Quick Reference**:
| Item | Format | Example | Pattern |
|------|--------|---------|---------|
| GitHub Repo | kebab-case | `infrastructure-vpc` | `^[a-z0-9-]+$` |
| Local Folder | kebab-case | `infrastructure-vpc` | `^[a-z0-9-]+$` |
| Terraform Resource | snake_case | `vpc_main` | `^[a-z0-9_]+$` |
| Terraform Variable | snake_case | `vpc_cidr_block` | `^[a-z0-9_]+$` |
| YAML Key | snake_case | `environment_name` | `^[a-z0-9_]+$` |
| Shell Variable | UPPER_SNAKE | `VPC_ID` | `^[A-Z0-9_]+$` |
| Shell Function | snake_case | `deploy_infrastructure` | `^[a-z0-9_]+$` |

### 2. naming-validation-rules.json
**Location**: `development-standards/governance/naming-validation-rules.json`

Machine-readable JSON schema with:
- Regex patterns for all naming conventions
- Error messages for violations
- Valid/invalid examples
- Auto-fix transformation rules

Use this for programmatic validation.

### 3. Language-Specific Guides
**Location**: `development-standards/language-guides/`

- **terraform.md** (2,420 lines): Complete Terraform standards including file naming, folder structure, code style, formatting, documentation, AWS resource naming, multi-environment patterns, module versioning
- **yaml.md**: YAML formatting, linting with yamllint, file naming (use `.yml` not `.yaml`)
- **shell.md**: Shell script best practices, safety flags (`set -euo pipefail`), shellcheck integration
- **markdown.md**: Documentation standards, CommonMark/GFM compliance, markdownlint rules
- **hcl.md**: HCL standards for Packer, Vault, Nomad
- **conf.md**: Configuration file standards for .conf, .env, .ini files

## Architecture Principles

### 1. Naming Consistency Model
The framework enforces **naming cascades**:
```
GitHub Repo Name → Local Folder Name → VS Code Workspace → Terraform Module Name
    ↓
Category Prefix Pattern: {category}-{purpose}[-{environment}]
    ↓
Examples:
  - infrastructure-vpc
  - k8s-monitoring-stack
  - app-api-gateway
  - module-vpc
  - tool-deployment-scripts
```

### 2. File Organization Philosophy
- **Standard files are required**: Every Terraform project must have `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `providers.tf`, `backend.tf`
- **Resource-specific files are optional**: Large projects can split resources into `vpc.tf`, `subnets.tf`, `security_groups.tf`, etc.
- **Configs directory contains templates**: Never modify production configs directly; copy from `configs/` directory

### 3. Validation Layers
1. **Pre-commit hooks**: First line of defense (local)
2. **CLI tool validation**: `refine-standards check` (local/CI)
3. **GitHub Actions**: CI/CD enforcement (remote)
4. **AI-assisted validation**: Claude Code Router with OpenRouter (optional)

## Working with This Repository

### When Creating New Standards Documents

1. **Always follow existing structure**: Place language guides in `language-guides/`, governance docs in `governance/`, configs in `configs/`
2. **Include validation patterns**: Every naming rule must have a regex pattern
3. **Provide good/bad examples**: Use ✅ and ❌ to mark valid/invalid examples
4. **Update naming-validation-rules.json**: Keep machine-readable rules in sync
5. **Cross-reference related docs**: Link to PROJECT-NAMING-STANDARDS.md and language guides

### When Validating Names

**Always reference PROJECT-NAMING-STANDARDS.md first**, then check specific language guide.

Example workflow:
```bash
# Check if "infrastructure-vpc" is valid
grep -A 10 "GitHub Repository Naming" development-standards/governance/PROJECT-NAMING-STANDARDS.md

# Validate Terraform resource name "vpc_main"
grep -A 10 "Terraform Resource" development-standards/governance/PROJECT-NAMING-STANDARDS.md

# Check YAML conventions
cat development-standards/language-guides/yaml.md | grep -A 20 "Naming Conventions"
```

### When Adding New Language Standards

1. Create new file: `development-standards/language-guides/{language}.md`
2. Follow terraform.md structure:
   - File naming conventions
   - Folder structure best practices
   - Code style and formatting
   - Naming conventions
   - Documentation requirements
   - Automation tools
   - VS Code setup
   - Pre-commit hooks
   - Code examples
3. Add validation rules to `naming-validation-rules.json`
4. Update `development-standards/README.md` with new guide
5. Add config templates to `configs/{language}/`

## Common Tasks

### Validate a Repository Name
```bash
# Pattern: ^[a-z0-9-]+$
# Must be kebab-case, lowercase, hyphens only
# Should have category prefix: infrastructure-, k8s-, app-, module-, tool-, config-, docs-

VALID: infrastructure-vpc, k8s-cluster-prod, module-vpc
INVALID: Infrastructure-VPC, infrastructure_vpc, InfrastructureVPC
```

### Validate Terraform Resource Names
```bash
# Pattern: ^[a-z0-9_]+$
# Must be snake_case, lowercase, underscores only

VALID: vpc_main, subnet_public_a, nat_gateway_prod
INVALID: vpcMain, vpc-main, VpcMain, VPC_MAIN
```

### Check YAML File Extensions
```bash
# ALWAYS use .yml (not .yaml)
VALID: docker-compose.yml, config.yml, .yamllint.yml
INVALID: docker-compose.yaml, config.yaml
```

### Validate Shell Scripts
```bash
# File names: kebab-case.sh (e.g., deploy-infrastructure.sh)
# Variables: UPPER_SNAKE_CASE (e.g., VPC_ID, ENVIRONMENT_NAME)
# Functions: snake_case (e.g., deploy_infrastructure, validate_input)
# Always include: #!/usr/bin/env bash and set -euo pipefail
```

## AI-Assisted Validation

This repository supports **Claude Code Router** integration for real-time standards validation using OpenRouter (cost-effective alternative to direct Claude API).

**Setup**: See [AI-ASSISTED-VALIDATION.md](AI-ASSISTED-VALIDATION.md)

**Usage**:
```bash
# Validate naming
echo "Is 'infrastructure-vpc' a valid repository name?" | ccr code

# Query standards
echo "What are the Terraform resource naming conventions?" | ccr code

# Generate compliant code
echo "Generate Terraform module for VPC following refine.digital standards" | ccr code
```

**Cost**: ~$1-5/month (95% savings vs direct Claude API)

## Important Conventions

### Category Prefixes for Repositories
- `infrastructure-*`: Core infrastructure resources
- `k8s-*`: Kubernetes clusters and resources
- `app-*`: Application deployments
- `module-*`: Reusable Terraform modules
- `tool-*`: Automation and tooling
- `config-*`: Configuration management
- `docs-*`: Documentation repositories

### Required Terraform Files
Every Terraform project/module MUST have:
- `main.tf` - Primary resources
- `variables.tf` - Input variables
- `outputs.tf` - Output values
- `versions.tf` - Version constraints
- `providers.tf` - Provider configuration
- `backend.tf` - Backend configuration (root modules only)
- `terraform.tfvars.example` - Example variables (NEVER commit actual .tfvars)

### YAML Preferences
- **Extension**: Always `.yml` (not `.yaml`)
- **Keys**: Use `snake_case` (not camelCase or kebab-case)
- **Indentation**: 2 spaces
- **Line length**: 120 characters max
- **Linter**: yamllint with config from `configs/yaml/.yamllint.yml`

### Shell Script Standards
- **Shebang**: `#!/usr/bin/env bash` (not `#!/bin/bash`)
- **Safety flags**: ALWAYS include `set -euo pipefail` after shebang
- **Variables**: UPPER_SNAKE_CASE for constants/exports, lower_snake_case for local
- **Functions**: snake_case naming
- **Linter**: shellcheck (all scripts must pass)

## Files to Read When...

### Adding Terraform Code
1. Read: `development-standards/language-guides/terraform.md` (complete standards)
2. Check: `development-standards/governance/PROJECT-NAMING-STANDARDS.md` (resource naming)
3. Reference: `development-standards/governance/naming-validation-rules.json` (validation patterns)

### Adding YAML Configuration
1. Read: `development-standards/language-guides/yaml.md` (formatting rules)
2. Check: `configs/yaml/.yamllint.yml` (linter config)
3. Verify: File extension is `.yml` not `.yaml`

### Writing Documentation
1. Read: `development-standards/language-guides/markdown.md` (documentation standards)
2. Reference: `OVERVIEW.md` (framework overview and structure)
3. Check: `configs/markdown/.markdownlint.yml` (linter rules)

### Creating Shell Scripts
1. Read: `development-standards/language-guides/shell.md` (best practices)
2. Include: `set -euo pipefail` safety flags
3. Run: `shellcheck` before committing

## Key Constraints

1. **Never commit secrets**: No .env files, credentials, or API keys in Git
2. **Always validate names**: Check PROJECT-NAMING-STANDARDS.md before creating repos/resources
3. **Use provided configs**: Copy from `configs/` directory, don't create from scratch
4. **Follow cascade**: GitHub repo name → local folder → Terraform module naming
5. **Extension standards**: `.yml` not `.yaml`, `.sh` for shell scripts, `.tf` for Terraform
6. **Pre-commit hooks**: Always run before committing (prevents violations)

## Standards Compliance Check

Before committing ANY code, verify:
- [ ] Repository/folder name is kebab-case
- [ ] Terraform resources use snake_case
- [ ] YAML files use .yml extension
- [ ] Shell scripts have proper shebang and safety flags
- [ ] All names validated against PROJECT-NAMING-STANDARDS.md
- [ ] Machine-readable rules in naming-validation-rules.json are updated
- [ ] Documentation includes valid/invalid examples

## Testing and Validation

```bash
# Future CLI tool (under development)
refine-standards check              # Check entire project
refine-standards validate-name --repo "my-name"
refine-standards validate-name --terraform-resource "resource_name"
refine-standards fix --auto         # Auto-fix violations
```

## Version Information

- **Framework Version**: 1.0.0
- **Last Updated**: 2025-11-07
- **Status**: Phase 1 Complete (Foundation), Phase 2 In Progress (Automation)
- **Maintained By**: refine.digital Platform Team

## Claude Code Marketplace Plugins

This repository is enhanced with **wshobson/agents** marketplace plugins for multi-agent orchestration and automated standards validation.

### Installed Plugins

**Core Plugins**:
- `code-review-ai` - Architecture and security assessment
- `security-scanning` - SAST, vulnerability detection
- `code-documentation` - Automated doc generation
- `cloud-infrastructure` - AWS/Azure/GCP + Terraform validation
- `kubernetes-operations` - K8s manifests and GitOps
- `cicd-automation` - GitHub Actions workflow generation
- `python-development` - CLI tool development (for refine-standards)

**Total**: 63 plugins available, install as needed

### Plugin Usage

**Documentation**: See [PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md) for complete installation and setup instructions

**Examples**: See [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md) for 21 practical workflows

**Testing**: See [PLUGIN-TESTING-CHECKLIST.md](PLUGIN-TESTING-CHECKLIST.md) for verification steps

### Quick Plugin Commands

```bash
# Standards validation
"Review terraform.md against PROJECT-NAMING-STANDARDS.md for compliance"

# Security audit
"Security audit shell.md examples for safety issues"

# Documentation generation
"Generate README for configs/ directory"

# CI/CD setup
"Create GitHub Actions workflow for naming validation"

# Multi-agent review
"Comprehensive review of development-standards/ from multiple perspectives"
```

### Plugin Architecture

- **Progressive disclosure**: Plugins load only when needed (~300 tokens each)
- **63 specialized plugins**: Covering development, infrastructure, security, testing
- **85 agents**: Coordinated multi-agent workflows
- **47 skills**: Domain-specific expertise activated contextually

## Related Projects

- **Claude Code Plugins**: wshobson/agents marketplace (https://github.com/wshobson/agents)
- **Claude Code Router**: AI-assisted validation with OpenRouter integration (see ../Claude Code Router/)
- **refine-standards CLI**: Automated validation tool (under development)
- **MCP Server**: Model Context Protocol server for standards (planned)
