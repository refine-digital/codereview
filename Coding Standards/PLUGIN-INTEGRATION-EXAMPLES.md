# Plugin Integration Examples for Development Standards Repository

This document provides practical examples of using the wshobson/agents plugins with the refine.digital Development Standards Framework.

---

## Table of Contents

1. [Standards Validation Workflows](#standards-validation-workflows)
2. [Documentation Generation](#documentation-generation)
3. [Security & Compliance](#security--compliance)
4. [Infrastructure Standards Review](#infrastructure-standards-review)
5. [CLI Tool Development](#cli-tool-development)
6. [CI/CD Integration](#cicd-integration)
7. [Multi-Agent Orchestration](#multi-agent-orchestration)

---

## Standards Validation Workflows

### Example 1: Validate Terraform Naming Conventions

**Goal**: Ensure Terraform examples in `terraform.md` follow PROJECT-NAMING-STANDARDS.md

**Using natural language**:
```
Use the cloud-infrastructure architect to review the Terraform examples in development-standards/language-guides/terraform.md and verify they comply with our naming standards in development-standards/governance/PROJECT-NAMING-STANDARDS.md
```

**Using slash command**:
```bash
/cloud-infrastructure:terraform-review development-standards/language-guides/terraform.md
```

**Expected outcome**:
- Validates resource naming is snake_case
- Checks file naming conventions
- Verifies module structure
- Suggests improvements

### Example 2: Validate YAML Standards Compliance

**Goal**: Review YAML examples for consistency

**Using natural language**:
```
Use the kubernetes-operations specialist to validate the YAML examples in development-standards/language-guides/yaml.md against our .yml extension requirement and snake_case key naming standards
```

**Expected outcome**:
- Confirms .yml extension usage (not .yaml)
- Validates snake_case keys
- Checks indentation (2 spaces)
- Verifies yamllint compatibility

### Example 3: Shell Script Safety Audit

**Goal**: Ensure shell examples follow safety best practices

**Using natural language**:
```
Use the security-scanning agent to audit the shell script examples in development-standards/language-guides/shell.md for proper safety flags (set -euo pipefail) and shellcheck compliance
```

**Expected outcome**:
- Verifies #!/usr/bin/env bash shebang
- Checks for set -euo pipefail
- Identifies unsafe patterns
- Suggests shellcheck integration

---

## Documentation Generation

### Example 4: Generate README for configs/ Directory

**Goal**: Auto-generate README explaining configuration templates

**Using slash command**:
```bash
/code-documentation:generate-readme development-standards/configs/
```

**Using natural language**:
```
Generate a comprehensive README.md for the development-standards/configs/ directory that explains each subdirectory (editorconfig, terraform, yaml, etc.) and how to use the configuration templates
```

**Expected outcome**:
- Creates `development-standards/configs/README.md`
- Documents each config subdirectory
- Includes usage examples
- Adds quick reference table

### Example 5: Create Architecture Diagram

**Goal**: Visualize the development standards framework architecture

**Using natural language**:
```
Use the mermaid-expert skill to create a comprehensive architecture diagram showing the relationship between governance files, language guides, configs, and templates in the development standards framework
```

**Expected outcome**:
- Mermaid diagram showing repository structure
- Visual flow: PROJECT-NAMING-STANDARDS → language-guides → configs
- Integration points with CI/CD
- Save to `development-standards/docs/architecture.mmd`

### Example 6: Generate API Documentation for naming-validation-rules.json

**Goal**: Document the JSON schema structure

**Using natural language**:
```
Use the api-documenter to create comprehensive documentation for the naming-validation-rules.json schema, explaining each rule type, validation patterns, and usage examples
```

**Expected outcome**:
- Detailed schema documentation
- Field-by-field explanations
- Validation pattern examples
- Usage guide for automation tools

---

## Security & Compliance

### Example 7: Security Hardening Review

**Goal**: Comprehensive security audit of standards repository

**Using slash command**:
```bash
/security-scanning:security-hardening --level comprehensive
```

**Expected outcome**:
- Scans for secrets in example files
- Validates secure coding patterns in examples
- Checks for injection vulnerabilities
- Reviews git hook security

### Example 8: SAST Analysis on Code Examples

**Goal**: Static analysis of all code examples in language guides

**Using slash command**:
```bash
/security-scanning:sast-scan development-standards/language-guides/
```

**Expected outcome**:
- Analyzes Terraform, YAML, Shell examples
- Identifies security anti-patterns
- Suggests secure alternatives
- Creates security findings report

### Example 9: Compliance Audit

**Goal**: Ensure standards meet SOC2/compliance requirements

**Using natural language**:
```
Use the security-compliance agent to audit our development standards against SOC2 and GDPR requirements, focusing on secure coding practices, secrets management, and access control policies
```

**Expected outcome**:
- Compliance gap analysis
- Recommendations for improvements
- Documentation requirements
- Policy alignment suggestions

---

## Infrastructure Standards Review

### Example 10: Terraform Standards Completeness Check

**Goal**: Verify terraform.md covers all HashiCorp best practices

**Using natural language**:
```
Use the cloud-infrastructure architect to compare our Terraform standards in development-standards/language-guides/terraform.md against HashiCorp's latest best practices and identify any gaps
```

**Expected outcome**:
- Gap analysis report
- Missing best practices identified
- Update recommendations
- Priority ranking

### Example 11: Kubernetes Manifest Standards

**Goal**: Validate Kubernetes YAML standards are production-ready

**Using natural language**:
```
Use the kubernetes-architect to review our YAML standards and verify they align with Kubernetes best practices for production deployments, including security policies, resource limits, and health checks
```

**Expected outcome**:
- Best practices validation
- Security recommendations
- Resource management guidance
- Production readiness checklist

### Example 12: Multi-Cloud Standards Review

**Goal**: Ensure standards work across AWS/Azure/GCP

**Using natural language**:
```
Use the cloud-architect to review our infrastructure standards and ensure they are provider-agnostic where possible, while documenting provider-specific requirements for AWS, Azure, and GCP
```

**Expected outcome**:
- Multi-cloud compatibility analysis
- Provider-specific sections identified
- Abstraction recommendations
- Cost optimization suggestions

---

## CLI Tool Development

### Example 13: Scaffold refine-standards CLI Tool

**Goal**: Create the refine-standards validation CLI using TDD

**Using slash command**:
```bash
/python-development:python-scaffold cli-tool --name refine-standards --framework click
```

**Expected outcome**:
- Creates project structure
- Sets up Click CLI framework
- Includes pytest configuration
- Adds UV package manager

### Example 14: TDD Workflow for Name Validation

**Goal**: Build name validation feature using test-driven development

**Using slash command**:
```bash
/tdd-workflows:tdd-cycle "Implement repository name validation against PROJECT-NAMING-STANDARDS.md kebab-case pattern"
```

**Expected outcome**:
- Red: Write failing test for repo name validation
- Green: Implement validation function
- Refactor: Optimize and clean up
- Cycle continues for each validation rule

### Example 15: Generate Unit Tests for Validation Rules

**Goal**: Create comprehensive test suite for naming-validation-rules.json

**Using slash command**:
```bash
/unit-testing:generate-tests --framework pytest --file tests/test_naming_validation.py
```

**Expected outcome**:
- Tests for each validation pattern
- Edge case coverage
- Valid/invalid example tests
- Parametrized test cases

---

## CI/CD Integration

### Example 16: Create GitHub Actions Workflow

**Goal**: Automated standards validation on pull requests

**Using slash command**:
```bash
/cicd-automation:generate-workflow --type validation --triggers "pull_request,push"
```

**Expected outcome**:
- Creates `.github/workflows/standards-validation.yml`
- Validates naming conventions
- Checks file extensions
- Runs linters (yamllint, shellcheck, markdownlint)

### Example 17: Pre-commit Hook Configuration

**Goal**: Local validation before commits

**Using natural language**:
```
Use the deployment-engineer to create a comprehensive pre-commit hook configuration that validates all naming conventions, runs linters, and checks for secrets before allowing commits
```

**Expected outcome**:
- Creates `.pre-commit-config.yaml`
- Adds naming validation hook
- Configures yamllint, shellcheck, markdownlint
- Adds git-secrets scanning

### Example 18: Deployment Strategy for Standards Updates

**Goal**: Safe rollout of standards changes

**Using natural language**:
```
Use the deployment-engineer to design a deployment strategy for rolling out new development standards across multiple repositories, including versioning, backward compatibility, and migration guides
```

**Expected outcome**:
- Versioning strategy (SemVer)
- Rollout plan (phased approach)
- Migration documentation
- Rollback procedures

---

## Multi-Agent Orchestration

### Example 19: Comprehensive Standards Review

**Goal**: Multi-perspective analysis of entire framework

**Using slash command**:
```bash
/full-stack-orchestration:comprehensive-review development-standards/
```

**Expected outcome**:
- Code reviewer: Quality and clarity
- Architect: Structure and scalability
- Security auditor: Security implications
- Coordinated recommendations report

### Example 20: New Language Standard Development

**Goal**: Create Go language standards with multi-agent workflow

**Using natural language**:
```
Coordinate a multi-agent workflow to:
1. Research Go best practices (search-specialist)
2. Draft go.md following terraform.md structure (code-documentation)
3. Create validation rules (python-development)
4. Review for completeness (code-review-ai)
5. Add security guidelines (security-scanning)
6. Generate tests (unit-testing)
7. Document in README (code-documentation)
```

**Expected outcome**:
- Complete `development-standards/language-guides/go.md`
- Go validation rules in `naming-validation-rules.json`
- Test suite for Go naming
- Updated README and architecture docs

### Example 21: End-to-End Standards Modernization

**Goal**: Update entire framework with latest best practices

**Using natural language**:
```
Orchestrate a comprehensive modernization workflow:
1. Audit current standards (code-review-ai)
2. Research 2025 best practices (search-specialist)
3. Identify gaps and improvements (architect-review)
4. Update language guides (code-documentation)
5. Enhance validation rules (python-development)
6. Security review (security-scanning)
7. Update CI/CD (cicd-automation)
8. Generate migration guide (code-documentation)
```

**Expected outcome**:
- Updated all language guides
- Enhanced validation rules
- Modern CI/CD workflows
- Comprehensive migration documentation

---

## Quick Reference Commands

### Standards Validation
```bash
# Terraform
/cloud-infrastructure:terraform-review development-standards/language-guides/terraform.md

# YAML
/kubernetes-operations:yaml-review development-standards/language-guides/yaml.md

# Shell scripts
/security-scanning:sast-scan development-standards/language-guides/shell.md

# All standards
/full-stack-orchestration:comprehensive-review development-standards/
```

### Documentation
```bash
# Generate README
/code-documentation:generate-readme [directory]

# Create diagrams
"Use mermaid-expert to create [type] diagram for [topic]"

# API docs
/api-documenter:generate-docs naming-validation-rules.json
```

### Security
```bash
# Comprehensive audit
/security-scanning:security-hardening --level comprehensive

# SAST scan
/security-scanning:sast-scan [directory]

# Compliance check
/security-compliance:compliance-audit development-standards/
```

### Development
```bash
# Scaffold CLI
/python-development:python-scaffold cli-tool --name refine-standards

# TDD cycle
/tdd-workflows:tdd-cycle "[feature description]"

# Generate tests
/unit-testing:generate-tests --framework pytest
```

### CI/CD
```bash
# Create workflow
/cicd-automation:generate-workflow --type validation

# Deployment strategy
/deployment-strategies:deployment-plan
```

---

## Natural Language Patterns

### Pattern 1: Review & Validate
```
"Review [file/directory] against [standard/requirement]"
"Validate [code/config] for [compliance/best-practice]"
"Check [examples] follow [naming-convention]"
```

### Pattern 2: Generate & Create
```
"Generate [documentation/code] for [component]"
"Create [workflow/config] that [requirement]"
"Build [tool/script] to [purpose]"
```

### Pattern 3: Analyze & Compare
```
"Compare [our-standard] against [industry-standard]"
"Analyze [component] for [quality/security/performance]"
"Identify gaps in [documentation/implementation]"
```

### Pattern 4: Multi-Agent Coordination
```
"Coordinate [agent1], [agent2], and [agent3] to [complex-task]"
"Use full-stack workflow to [end-to-end-task]"
"Orchestrate [workflow] across [domains]"
```

---

## Best Practices for This Repository

### 1. Always Reference Standards First
Before asking agents to validate or review, point them to the canonical standards:

✅ **Good**:
```
"Review terraform.md examples against our PROJECT-NAMING-STANDARDS.md, specifically the snake_case requirement for Terraform resources"
```

❌ **Bad**:
```
"Review terraform.md for best practices"
```

### 2. Use Specific Agent Skills
Name the agent skill when you want targeted expertise:

✅ **Good**:
```
"Use the terraform-architect skill to validate our backend.tf configuration patterns"
```

❌ **Bad**:
```
"Check our Terraform backend config"
```

### 3. Provide Context from Repository Structure
Help agents understand the framework:

✅ **Good**:
```
"Our naming-validation-rules.json in governance/ provides machine-readable patterns. Use these patterns to validate the examples in language-guides/terraform.md"
```

❌ **Bad**:
```
"Validate naming in our Terraform guide"
```

### 4. Chain Related Tasks
Build workflows that make sense for standards work:

✅ **Good**:
```
1. Review standard → 2. Security scan → 3. Generate tests → 4. Update CI/CD
```

❌ **Bad**:
```
Random unrelated tasks
```

---

## Integration Checklist

Use this checklist when integrating plugins with your standards repository:

- [ ] Install core plugins (code-review-ai, security-scanning, code-documentation)
- [ ] Install infrastructure plugins (cloud-infrastructure, kubernetes-operations)
- [ ] Install development plugins (python-development for CLI tool)
- [ ] Test validation workflows on existing standards
- [ ] Create CI/CD workflows using cicd-automation
- [ ] Generate missing documentation using code-documentation
- [ ] Security audit using security-scanning
- [ ] Set up TDD workflow for CLI development
- [ ] Document custom workflows in this repository
- [ ] Train team on slash commands vs natural language

---

## Troubleshooting Integration Issues

### Issue: Agent doesn't understand repository structure

**Solution**: Provide explicit context
```
"In our repository, governance/PROJECT-NAMING-STANDARDS.md is the canonical naming guide, and language-guides/ contains language-specific standards. Review terraform.md against PROJECT-NAMING-STANDARDS.md."
```

### Issue: Validation doesn't match our patterns

**Solution**: Reference naming-validation-rules.json
```
"Use the regex patterns from governance/naming-validation-rules.json to validate these examples"
```

### Issue: Generated code doesn't follow our standards

**Solution**: Be explicit about requirements
```
"Generate a Python CLI tool that follows our shell script naming conventions from language-guides/shell.md: kebab-case filenames, UPPER_SNAKE_CASE variables"
```

---

## Next Steps

1. **Test each example** in this document with your installed plugins
2. **Document successful workflows** that work well for your standards
3. **Create custom slash commands** for frequent validation tasks
4. **Build automation pipelines** using the CI/CD examples
5. **Share findings** with the team and refine integration patterns

---

**Last Updated**: 2025-11-07
**Compatible with**: wshobson/agents marketplace plugins
**Repository**: refine.digital Development Standards Framework
