# Claude Code Marketplace Plugin Setup Guide
## wshobson/agents - Multi-Agent Orchestration System

**Repository**: https://github.com/wshobson/agents
**Type**: Claude Code Marketplace Plugin
**Components**: 63 plugins, 85 agents, 47 skills, 44 tools
**License**: MIT

---

## Overview

The wshobson/agents marketplace provides a comprehensive multi-agent orchestration system for Claude Code with specialized plugins covering:
- Development (Python, JavaScript/TypeScript, systems programming)
- Infrastructure (Kubernetes, cloud, CI/CD)
- Security (scanning, compliance, API security)
- Testing & Quality (TDD, unit testing, code review)
- AI/ML (LLM applications, agent orchestration)
- Operations (incident response, observability)

**Key Architecture**: Each plugin loads independently with minimal token overhead (~300 tokens average). Progressive disclosure ensures only relevant agents/skills activate when needed.

---

## Installation Steps

### Step 1: Add the Marketplace

```bash
/plugin marketplace add wshobson/agents
```

**What this does**:
- Makes all 63 plugins discoverable
- Does NOT load any agents into context yet
- Enables browsing and selective installation

**Expected output**:
```
✅ Marketplace added: wshobson/agents
   63 plugins available
   Use /plugin to browse
```

### Step 2: Browse Available Plugins

```bash
/plugin
```

**What this does**:
- Lists all installed and available plugins
- Shows plugin categories and descriptions
- Displays installation status

### Step 3: Install Specific Plugins

Install plugins relevant to your development standards repository:

```bash
# For Infrastructure-as-Code work
/plugin install cloud-infrastructure
/plugin install kubernetes-operations
/plugin install deployment-strategies

# For code quality and standards enforcement
/plugin install code-review-ai
/plugin install security-scanning
/plugin install code-documentation

# For CI/CD automation
/plugin install cicd-automation
/plugin install deployment-validation

# For multi-language support
/plugin install python-development
/plugin install javascript-typescript
/plugin install systems-programming
```

**Per-plugin installation confirmation**:
```
✅ Installed: cloud-infrastructure
   Loaded: 3 agents, 4 skills, 1 tool
   Token overhead: ~320 tokens
```

---

## Recommended Plugins for Development Standards Repository

Based on your **refine.digital Development Standards Framework**, here are the most relevant plugins:

### Category: Infrastructure & IaC (High Priority)

| Plugin | Purpose | Use Case |
|--------|---------|----------|
| `cloud-infrastructure` | AWS/Azure/GCP + Terraform | Validate Terraform code against standards |
| `kubernetes-operations` | K8s manifests, GitOps | Review Kubernetes YAML configurations |
| `deployment-strategies` | Deployment patterns | Document deployment best practices |
| `cicd-automation` | CI/CD pipeline config | Create GitHub Actions for standards validation |

### Category: Code Quality & Standards (High Priority)

| Plugin | Purpose | Use Case |
|--------|---------|----------|
| `code-review-ai` | Architecture & security review | Review standards compliance |
| `security-scanning` | SAST, vulnerability detection | Scan for security issues in examples |
| `code-documentation` | Doc generation | Generate documentation for standards |
| `code-refactoring` | Technical debt management | Refactor non-compliant code |

### Category: Language-Specific (Medium Priority)

| Plugin | Purpose | Use Case |
|--------|---------|----------|
| `python-development` | Python best practices | If adding Python standards |
| `javascript-typescript` | JS/TS best practices | If adding JS/TS standards |
| `systems-programming` | Rust/Go/C/C++ | Systems language standards |

### Category: Testing & Validation (Medium Priority)

| Plugin | Purpose | Use Case |
|--------|---------|----------|
| `unit-testing` | Test generation | Create validation tests for naming rules |
| `tdd-workflows` | TDD methodology | Develop CLI tool with TDD |
| `data-validation-suite` | Schema validation | Validate naming-validation-rules.json |

### Category: Documentation (Low Priority)

| Plugin | Purpose | Use Case |
|--------|---------|----------|
| `documentation-generation` | OpenAPI specs, diagrams | Generate architecture diagrams |
| `seo-content-creation` | Technical writing | Improve documentation SEO |

---

## Testing the Plugin System

### Test 1: Verify Marketplace Installation

```bash
/plugin marketplace list
```

**Expected**: Should show `wshobson/agents` in the marketplace list

### Test 2: Browse Available Plugins

```bash
/plugin
```

**Expected**: Should display categorized list of 63 plugins with descriptions

### Test 3: Install a Test Plugin

```bash
/plugin install code-documentation
```

**Expected output**:
```
✅ Installed: code-documentation
   Loaded components:
   - documentation-generator (agent)
   - api-docs-specialist (agent)
   - diagram-creator (agent)
   - doc-generation (skill)
   Token overhead: ~280 tokens
```

### Test 4: Use Slash Command

```bash
/code-documentation:generate-readme
```

**Expected**: Agent activates and generates README documentation based on current context

### Test 5: Use Natural Language Activation

Simply type in natural language:
```
"Use the documentation-generator agent to explain the PROJECT-NAMING-STANDARDS.md file"
```

**Expected**: Claude automatically activates the relevant agent from the installed plugin

### Test 6: Multi-Agent Workflow

```bash
/full-stack-orchestration:code-review "development-standards/governance/PROJECT-NAMING-STANDARDS.md"
```

**Expected**: Multiple agents coordinate to review the standards document from different perspectives (architecture, security, readability, compliance)

---

## Usage Patterns

### Pattern 1: Slash Commands (Structured)

**Format**: `/plugin-name:command-name [arguments]`

**Example**:
```bash
# Review Terraform standards
/cloud-infrastructure:terraform-review development-standards/language-guides/terraform.md

# Security scan
/security-scanning:security-hardening --level comprehensive

# Generate documentation
/code-documentation:generate-api-docs
```

**When to use**:
- Repetitive tasks
- Parameter-specific workflows
- Automation scripts

### Pattern 2: Natural Language (Exploratory)

**Example**:
```
"Use the cloud-infrastructure architect to validate our Terraform naming conventions"

"Have the security-scanning agent review our shell script standards for vulnerabilities"

"Use code-review-ai to assess the completeness of our YAML standards"
```

**When to use**:
- Exploratory work
- Contextual decisions
- Ad-hoc analysis

### Pattern 3: Multi-Agent Orchestration

**Example**:
```bash
# Full standards review workflow
/full-stack-orchestration:comprehensive-review development-standards/

# Security + compliance check
/security-scanning:security-hardening && /security-compliance:compliance-audit
```

**When to use**:
- Complex workflows requiring multiple specialties
- End-to-end validation
- Cross-domain analysis

---

## Integration with Development Standards Repository

### Use Case 1: Validate Terraform Standards

```bash
# Install required plugin
/plugin install cloud-infrastructure

# Review terraform.md for completeness
/cloud-infrastructure:terraform-review development-standards/language-guides/terraform.md

# Validate Terraform example code
"Use terraform-architect to validate the Terraform examples in terraform.md against HashiCorp best practices"
```

### Use Case 2: Security Scan Standards Documents

```bash
# Install security plugins
/plugin install security-scanning
/plugin install security-compliance

# Scan shell script examples
/security-scanning:sast-scan development-standards/language-guides/shell.md

# Check compliance
/security-compliance:compliance-audit development-standards/governance/
```

### Use Case 3: Generate Documentation

```bash
# Install documentation plugin
/plugin install code-documentation

# Generate README for configs directory
/code-documentation:generate-readme development-standards/configs/

# Create architecture diagrams
"Use diagram-creator to visualize the development standards framework architecture"
```

### Use Case 4: Code Review Standards Files

```bash
# Install code review plugin
/plugin install code-review-ai

# Comprehensive review of naming standards
/code-review-ai:comprehensive-review development-standards/governance/PROJECT-NAMING-STANDARDS.md

# Natural language review
"Use code-review-ai to assess the completeness and clarity of our naming validation rules"
```

### Use Case 5: Create CI/CD for Standards Validation

```bash
# Install CI/CD plugin
/plugin install cicd-automation

# Generate GitHub Actions workflow
/cicd-automation:generate-workflow --type validation --triggers "pull_request,push"

# Natural language request
"Create a GitHub Actions workflow that validates all naming conventions against our naming-validation-rules.json schema"
```

### Use Case 6: Build Standards CLI Tool

```bash
# Install Python development plugin
/plugin install python-development
/plugin install tdd-workflows

# Scaffold CLI tool
/python-development:python-scaffold cli-tool --name refine-standards

# Use TDD workflow
/tdd-workflows:tdd-cycle "validate repository naming against PROJECT-NAMING-STANDARDS.md"
```

---

## Advanced Testing Scenarios

### Scenario 1: Multi-Plugin Workflow

**Goal**: Complete standards validation pipeline

```bash
# Step 1: Security scan
/security-scanning:security-hardening --level comprehensive

# Step 2: Code review
/code-review-ai:comprehensive-review development-standards/

# Step 3: Documentation check
/code-documentation:validate-docs development-standards/

# Step 4: CI/CD setup
/cicd-automation:generate-workflow --type validation
```

### Scenario 2: Infrastructure Standards Review

**Goal**: Validate all IaC standards (Terraform, YAML, HCL)

```bash
# Install required plugins
/plugin install cloud-infrastructure
/plugin install kubernetes-operations

# Review Terraform standards
/cloud-infrastructure:terraform-review development-standards/language-guides/terraform.md

# Review YAML standards
/kubernetes-operations:yaml-review development-standards/language-guides/yaml.md

# Review HCL standards
"Use cloud-infrastructure architect to validate our HCL standards in language-guides/hcl.md"
```

### Scenario 3: End-to-End Standards Development

**Goal**: Create new language standard with validation

```bash
# Step 1: Research and draft (use natural language)
"Use code-documentation agent to research Go language best practices and draft a go.md standards document following our terraform.md format"

# Step 2: Code review
/code-review-ai:comprehensive-review development-standards/language-guides/go.md

# Step 3: Add validation rules
"Use python-development agent to create validation functions for Go naming conventions in naming-validation-rules.json"

# Step 4: Create tests
/unit-testing:generate-tests --framework pytest --file validation_test.py

# Step 5: Documentation
/code-documentation:generate-readme development-standards/language-guides/
```

---

## Troubleshooting

### Issue: Marketplace Not Found

**Symptom**:
```
❌ Error: Marketplace 'wshobson/agents' not found
```

**Solution**:
1. Verify Claude Code version supports plugin marketplace
2. Check network connectivity
3. Retry: `/plugin marketplace add wshobson/agents`

### Issue: Plugin Installation Fails

**Symptom**:
```
❌ Error: Failed to install plugin 'cloud-infrastructure'
```

**Solution**:
1. Check plugin name spelling: `/plugin` to list available plugins
2. Verify no conflicting plugins installed
3. Try reinstalling: `/plugin uninstall cloud-infrastructure && /plugin install cloud-infrastructure`

### Issue: Agent Not Activating

**Symptom**: Slash command or natural language doesn't activate agent

**Solution**:
1. Verify plugin is installed: `/plugin` to check status
2. Check command syntax: `/plugin-name:command-name`
3. Try natural language: "Use [agent-name] to [task]"
4. Reinstall plugin if needed

### Issue: High Token Usage

**Symptom**: Context filling up quickly

**Solution**:
1. Only install needed plugins (not all 63)
2. Use `/plugin uninstall [name]` to remove unused plugins
3. Plugins load ~300 tokens each on average
4. Skills activate progressively (only when needed)

---

## Best Practices

### 1. Install Only What You Need

✅ **Good**:
```bash
# Install specific plugins for current task
/plugin install cloud-infrastructure
/plugin install security-scanning
```

❌ **Bad**:
```bash
# Installing all 63 plugins (unnecessary token overhead)
/plugin install python-development
/plugin install javascript-typescript
/plugin install systems-programming
# ... (60 more)
```

### 2. Use Slash Commands for Repetitive Tasks

✅ **Good**:
```bash
# Create script for repeated validation
/security-scanning:sast-scan development-standards/
```

❌ **Bad**:
```
# Typing out full natural language each time
"Please use the security scanning agent to perform a static analysis security test on the development-standards directory"
```

### 3. Compose Workflows Sequentially

✅ **Good**:
```bash
# Chain related tasks
/code-review-ai:review → /security-scanning:sast → /unit-testing:generate
```

❌ **Bad**:
```bash
# Running unrelated tasks simultaneously
/seo-content-creation:seo-audit development-standards/governance/
```

### 4. Use Natural Language for Exploration

✅ **Good**:
```
"Explore our Terraform standards and suggest improvements based on HashiCorp's latest recommendations"
```

❌ **Bad**:
```bash
# Forcing slash command when context needed
/cloud-infrastructure:terraform-review --mode exploration --depth comprehensive
```

---

## Recommended Starting Configuration

For the **refine.digital Development Standards Framework**, install this minimal set:

```bash
# Core standards validation
/plugin install code-review-ai
/plugin install security-scanning
/plugin install code-documentation

# Infrastructure focus
/plugin install cloud-infrastructure
/plugin install kubernetes-operations

# Automation
/plugin install cicd-automation
/plugin install python-development
```

**Total token overhead**: ~2,100 tokens (7 plugins × ~300 tokens)

This provides:
- Standards review capabilities
- Security scanning
- Documentation generation
- IaC validation
- CI/CD automation
- CLI tool development

---

## Next Steps

1. **Install core plugins** using the recommended starting configuration
2. **Test basic functionality** with simple slash commands
3. **Create automation workflows** for standards validation
4. **Integrate with CI/CD** to enforce standards automatically
5. **Document custom workflows** specific to your standards repository

---

## Additional Resources

- **Repository**: https://github.com/wshobson/agents
- **Documentation**: https://github.com/wshobson/agents/tree/main/docs
- **Plugin Reference**: docs/plugins.md
- **Agent Reference**: docs/agents.md
- **Agent Skills Guide**: docs/agent-skills.md
- **Architecture**: docs/architecture.md

---

## Support

For issues with the plugin marketplace:
1. Check GitHub Issues: https://github.com/wshobson/agents/issues
2. Review documentation: https://github.com/wshobson/agents/tree/main/docs
3. Claude Code support: https://docs.claude.com/claude-code

---

**Last Updated**: 2025-11-07
**Plugin Version**: Latest from wshobson/agents main branch
**Compatible with**: Claude Code with marketplace plugin support
