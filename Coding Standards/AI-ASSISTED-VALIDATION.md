# AI-Assisted Standards Validation

Using Claude Code Router for automated standards validation and code generation.

## Overview

The [Claude Code Router](../Claude%20Code%20Router) project provides AI-powered assistance for working with these development standards. It enables real-time validation, code generation, and interactive documentation queries at minimal cost.

## Quick Start

### Prerequisites

The Claude Code Router must be installed and configured. See:
- [../Claude Code Router/README.md](../Claude%20Code%20Router/README.md) - Main setup guide
- [../Claude Code Router/SETUP-COMPLETE.md](../Claude%20Code%20Router/SETUP-COMPLETE.md) - Detailed installation

### Basic Usage

```bash
# Start the router
ccr start

# Validate a repository name
echo "Is 'infrastructure-vpc' a valid repository name?" | ccr code

# Check Terraform resource naming
echo "Validate: aws_vpc.main_vpc" | ccr code

# Query standards
echo "What are the YAML file naming conventions?" | ccr code
```

## Use Cases

### 1. Validate Project Names

Before creating a new project:

```bash
PROJECT_NAME="my-new-project"
echo "Is '$PROJECT_NAME' compliant with refine.digital naming standards?" | ccr code
```

**Standards Reference**: [development-standards/governance/PROJECT-NAMING-STANDARDS.md](development-standards/governance/PROJECT-NAMING-STANDARDS.md)

### 2. Validate Terraform Code

Check resource names and module structure:

```bash
# Validate resource naming
cat main.tf | ccr code --prompt "Check all Terraform resource names for standards compliance"

# Validate module structure
echo "Review this Terraform module structure: $(ls -R modules/)" | ccr code
```

**Standards Reference**: [development-standards/language-guides/terraform.md](development-standards/language-guides/terraform.md)

### 3. Validate YAML Files

Check file names and formatting:

```bash
# Validate file name
echo "Is 'docker-compose.yml' a valid YAML file name?" | ccr code

# Validate content
cat .github/workflows/ci.yml | ccr code --prompt "Review against YAML standards"
```

**Standards Reference**: [development-standards/language-guides/yaml.md](development-standards/language-guides/yaml.md)

### 4. Generate Compliant Code

Create new code following standards:

```bash
# Generate Terraform module
echo "Generate a Terraform module for AWS VPC following refine.digital standards" | ccr code

# Generate documentation
echo "Create a README.md template for a Terraform project" | ccr code
```

## Integration Methods

### VS Code Integration

Add to your project's `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Validate Naming Standards",
      "type": "shell",
      "command": "echo 'Validate all files in ${workspaceFolder}' | ccr code"
    }
  ]
}
```

### Pre-commit Hooks

Automate validation before commits. See:
- [../Claude Code Router/INTEGRATION-WITH-CODING-STANDARDS.md](../Claude%20Code%20Router/INTEGRATION-WITH-CODING-STANDARDS.md#method-3-pre-commit-hooks)

### CI/CD Integration

Add GitHub Actions workflow. See:
- [../Claude Code Router/INTEGRATION-WITH-CODING-STANDARDS.md](../Claude%20Code%20Router/INTEGRATION-WITH-CODING-STANDARDS.md#method-4-github-actions-integration)

## Common Validation Queries

### Repository Names
```bash
echo "Validate repository name: infrastructure-vpc" | ccr code
# Expected format: kebab-case (lowercase with hyphens)
```

### Terraform Resources
```bash
echo "Validate Terraform resource: aws_vpc.main_vpc" | ccr code
# Expected format: snake_case (lowercase with underscores)
```

### YAML Files
```bash
echo "Validate YAML file name: docker-compose.yml" | ccr code
# Expected format: kebab-case.yml
```

### Shell Scripts
```bash
echo "Validate shell script name: deploy-infrastructure.sh" | ccr code
# Expected format: kebab-case.sh
```

### Environment Variables
```bash
echo "Validate environment variable: DATABASE_URL" | ccr code
# Expected format: UPPER_SNAKE_CASE
```

## Documentation Queries

Get instant answers from standards documentation:

```bash
# Naming conventions
echo "What is the naming convention for Terraform modules?" | ccr code

# Code examples
echo "Show me examples of valid Terraform resource names" | ccr code

# Best practices
echo "What are the best practices for YAML formatting?" | ccr code

# Specific guidance
echo "How should I structure a Terraform project?" | ccr code
```

## Cost Information

Using the Claude Code Router is very cost-effective:

**Current Setup (GPT-4o Mini)**:
- Input: $0.15 per 1M tokens
- Output: $0.60 per 1M tokens
- Typical query: $0.0005 - $0.001 (less than 1¢)
- Monthly estimate: $1-5 for moderate usage

**Comparison**:
- Claude API direct: $50-100/month
- With Router: $1-5/month (95% savings)

See [../Claude Code Router/OPENROUTER-MODELS.md](../Claude%20Code%20Router/OPENROUTER-MODELS.md) for detailed pricing.

## Advanced Features

### Batch Validation

Validate multiple items at once:

```bash
# Create validation script
cat > validate-project.sh << 'EOF'
#!/bin/bash
echo "Validating project structure..."

# Check all Terraform files
find . -name "*.tf" -exec echo "Validate: {}" \; | ccr code

# Check all YAML files
find . -name "*.yml" -o -name "*.yaml" | while read f; do
    echo "Validate: $(basename $f)" | ccr code
done

# Check all shell scripts
find . -name "*.sh" | while read f; do
    echo "Validate: $(basename $f)" | ccr code
done
EOF

chmod +x validate-project.sh
./validate-project.sh
```

### Interactive Standards Assistant

Create an interactive helper:

```bash
#!/bin/bash
# standards-assistant.sh

echo "refine.digital Standards Assistant"
echo "=================================="
echo ""

while true; do
    echo -n "Ask a standards question (or 'exit'): "
    read question

    if [ "$question" = "exit" ]; then
        break
    fi

    echo "$question" | ccr code
    echo ""
done
```

## Troubleshooting

### Router Not Running
```bash
# Check status
ccr status

# Start if needed
ccr start
```

### Slow Responses
```bash
# Check model in use
cat ~/.claude-code-router/config.json

# Verify using fast model (GPT-4o Mini)
# If using Claude, switch to GPT-4o Mini for simple queries
```

### Unexpected Results
```bash
# Be specific in queries
# Bad:  "Check this"
# Good: "Is 'Infrastructure-VPC' valid per refine.digital repository naming standards?"

# Reference specific standards
echo "According to development-standards/governance/PROJECT-NAMING-STANDARDS.md, is 'my_project' valid?" | ccr code
```

## Standards References

All standards documents are available in:
- [development-standards/governance/](development-standards/governance/) - Project governance and naming
- [development-standards/language-guides/](development-standards/language-guides/) - Language-specific guides

### Quick Links

- **Naming Standards**: [PROJECT-NAMING-STANDARDS.md](development-standards/governance/PROJECT-NAMING-STANDARDS.md)
- **Terraform**: [terraform.md](development-standards/language-guides/terraform.md)
- **YAML**: [yaml.md](development-standards/language-guides/yaml.md)
- **Shell**: [shell.md](development-standards/language-guides/shell.md)
- **Markdown**: [markdown.md](development-standards/language-guides/markdown.md)
- **HCL**: [hcl.md](development-standards/language-guides/hcl.md)
- **Config Files**: [conf.md](development-standards/language-guides/conf.md)

## Router Documentation

Complete documentation is available in the Claude Code Router project:

- [README.md](../Claude%20Code%20Router/README.md) - Overview and quick start
- [SETUP-COMPLETE.md](../Claude%20Code%20Router/SETUP-COMPLETE.md) - Detailed setup guide
- [INTEGRATION-WITH-CODING-STANDARDS.md](../Claude%20Code%20Router/INTEGRATION-WITH-CODING-STANDARDS.md) - Integration examples
- [OPENROUTER-MODELS.md](../Claude%20Code%20Router/OPENROUTER-MODELS.md) - Model recommendations
- [TESTING-GUIDE.md](../Claude%20Code%20Router/TESTING-GUIDE.md) - Testing and troubleshooting

## Benefits

### For Developers

- **Real-time validation**: Check naming instantly
- **Guided compliance**: Get immediate feedback
- **Reduced errors**: Catch issues before commit
- **Faster onboarding**: Query standards interactively

### For Teams

- **Consistency**: Automated enforcement
- **Efficiency**: Reduce review time
- **Quality**: Maintain standards compliance
- **Cost-effective**: ~$1-5/month per developer

## Getting Started

1. **Install Claude Code Router**: See [../Claude Code Router/README.md](../Claude%20Code%20Router/README.md)

2. **Start using validation**:
   ```bash
   ccr start
   echo "Is 'my-project-name' valid?" | ccr code
   ```

3. **Integrate with workflow**: Add pre-commit hooks or VS Code tasks

4. **Monitor costs**: Check OpenRouter dashboard at https://openrouter.ai/dashboard

## Support

- **Router issues**: See [../Claude Code Router/TESTING-GUIDE.md](../Claude%20Code%20Router/TESTING-GUIDE.md)
- **Standards questions**: Query via `ccr code` or review documentation
- **Integration help**: See [../Claude Code Router/INTEGRATION-WITH-CODING-STANDARDS.md](../Claude%20Code%20Router/INTEGRATION-WITH-CODING-STANDARDS.md)

---

**Status**: Production Ready
**Last Updated**: 2025-11-07
**Related Project**: [../Claude Code Router](../Claude%20Code%20Router)
