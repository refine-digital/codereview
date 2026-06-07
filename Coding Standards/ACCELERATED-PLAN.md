# Accelerated IaC Development Standards - ASAP Implementation

## 🎯 Focus: Infrastructure-as-Code Project Consistency

**Timeline**: 2 weeks to MVP, 4 weeks to production-ready
**Lead**: You (full-time)
**Stack**: Markdown, YAML, Terraform, HCL, Shell, Config files
**Primary Goal**: Eliminate project naming inconsistencies

---

## Week 1: Foundation + Core Standards

### Day 1-2: Repository Setup + Project Naming Standards

#### Immediate Actions

**1. Create Repository Structure** (2 hours)
```bash
mkdir -p development-standards/{templates,configs,language-guides,governance,mcp,automation,examples}
cd development-standards
git init
```

**2. Create Core Naming Standards** (4 hours)

Create comprehensive project naming guide that covers EVERYTHING:

**File**: `governance/PROJECT-NAMING-STANDARDS.md`

Includes:
- GitHub repository naming conventions
- Local folder structure standards
- File naming patterns per type (.tf, .yml, .sh, .md, etc.)
- VS Code workspace naming
- Terraform resource naming
- YAML key naming
- Environment naming (dev, staging, prod)
- Branch naming
- Tag naming
- Variable naming across all languages

**3. Create Validation Rules** (2 hours)

**File**: `governance/naming-validation-rules.json`

Machine-readable rules for automated checking:
```json
{
  "github_repo": {
    "pattern": "^[a-z0-9-]+$",
    "max_length": 50,
    "format": "kebab-case",
    "examples": ["infrastructure-vpc", "k8s-cluster-prod"]
  },
  "terraform_resource": {
    "pattern": "^[a-z0-9_]+$",
    "format": "snake_case",
    "examples": ["vpc_main", "eks_cluster_prod"]
  }
}
```

#### Deliverables Day 1-2
- [ ] Repository created
- [ ] Folder structure complete
- [ ] PROJECT-NAMING-STANDARDS.md (comprehensive)
- [ ] naming-validation-rules.json
- [ ] Initial README.md

---

### Day 3-4: IaC Language Guides

**Priority Order**: Terraform → YAML → Markdown → Shell → HCL → Conf

#### Create 6 Language Guides

**Template for each** (`language-guides/{language}.md`):
```markdown
# {Language} Standards for IaC Projects

## 1. File Naming
- Pattern: [specific pattern]
- Examples: [good examples]
- Anti-patterns: [bad examples]

## 2. Folder Structure
- Standard layout
- Required files
- Optional files

## 3. Code Style
- Formatting rules
- Linting tools
- Best practices

## 4. Naming Conventions
- Variables
- Resources
- Modules/Functions

## 5. Documentation Requirements
- Required comments
- README sections
- Inline documentation

## 6. Automation
- Formatter: [tool]
- Linter: [tool]
- Validator: [tool]

## 7. Examples
- Minimal example
- Full example
- Common patterns

## 8. VS Code Settings
- Recommended extensions
- Workspace settings
```

#### Specific Guides to Create

1. **terraform.md** (6 hours)
   - Terraform fmt standards
   - Module structure
   - Resource naming
   - Variable/output naming
   - terraform.tfvars structure
   - Backend config naming

2. **yaml.md** (3 hours)
   - YAML linting rules
   - GitHub Actions naming
   - Kubernetes manifests
   - Docker Compose
   - Key naming conventions

3. **markdown.md** (2 hours)
   - README.md structure
   - Documentation patterns
   - Linting rules (markdownlint)
   - Heading conventions

4. **shell.md** (3 hours)
   - Script naming
   - Shebang standards
   - Error handling
   - Variable naming
   - Function naming

5. **hcl.md** (2 hours)
   - Packer templates
   - Terraform configs
   - Vault policies

6. **conf.md** (2 hours)
   - Nginx configs
   - Apache configs
   - Application configs
   - INI files

#### Deliverables Day 3-4
- [ ] 6 comprehensive language guides
- [ ] Code examples for each
- [ ] Linting configurations

---

### Day 5: Configuration Templates

#### Create Drop-in Config Files

**1. EditorConfig** (`configs/editorconfig/.editorconfig`)
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.tf]
indent_size = 2

[*.{yml,yaml}]
indent_size = 2

[*.sh]
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

**2. Terraform** (`configs/terraform/.terraform-version`, `.tflint.hcl`)

**3. YAML Lint** (`configs/yaml/.yamllint.yml`)

**4. Markdown Lint** (`configs/markdown/.markdownlint.yml`)

**5. ShellCheck** (`configs/shell/.shellcheckrc`)

**6. Prettier** (`configs/prettier/.prettierrc.yml`) - for YAML/Markdown

**7. VS Code** (`configs/vscode/.vscode-settings.json`)
```json
{
  "editor.formatOnSave": true,
  "editor.rulers": [80, 120],
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "terraform.format.enable": true,
  "terraform.languageServer.enable": true,
  "[terraform]": {
    "editor.defaultFormatter": "hashicorp.terraform",
    "editor.formatOnSave": true
  },
  "[yaml]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[shellscript]": {
    "editor.defaultFormatter": "foxundermoon.shell-format"
  }
}
```

**8. Git** (`configs/git/.gitattributes`, `.gitignore-terraform`)

#### Deliverables Day 5
- [ ] 8+ config files ready to drop into projects
- [ ] Installation instructions
- [ ] VS Code recommended extensions list

---

## Week 2: Automation + MCP Integration

### Day 6-7: CLI Tool (Standards Checker)

#### Build `refine-standards` CLI Tool

**Tech**: Node.js/TypeScript (fast to build, npm distribution)

**Structure**:
```
automation/refine-standards/
├── package.json
├── tsconfig.json
├── src/
│   ├── index.ts                 # CLI entry
│   ├── commands/
│   │   ├── init.ts              # Initialize project
│   │   ├── check.ts             # Check standards
│   │   ├── fix.ts               # Auto-fix violations
│   │   └── validate-name.ts     # Validate naming
│   ├── validators/
│   │   ├── terraform.ts         # Terraform validator
│   │   ├── yaml.ts              # YAML validator
│   │   ├── markdown.ts          # Markdown validator
│   │   └── naming.ts            # Naming validator
│   └── utils/
│       ├── rules-loader.ts      # Load validation rules
│       └── reporter.ts          # Format results
└── tests/
```

**Core Commands**:
```bash
# Initialize new IaC project
refine-standards init --type terraform

# Check current project
refine-standards check

# Auto-fix issues
refine-standards fix

# Validate specific item
refine-standards validate-name --repo "my-vpc-config"
refine-standards validate-name --terraform-resource "vpc_main"

# Generate configs
refine-standards config --terraform --yaml --vscode
```

**Implementation**:
1. Use Commander.js for CLI
2. Use Chalk for colored output
3. Load rules from `naming-validation-rules.json`
4. Validate against language-specific rules
5. Report violations with fix suggestions

#### Deliverables Day 6-7
- [ ] Working CLI tool
- [ ] Published to npm (or local install)
- [ ] Documentation
- [ ] Test suite

---

### Day 8-9: MCP Server with OpenRouter

#### Setup MCP Server for Standards

**Purpose**: Allow Claude Code (and other AI tools) to query standards in real-time.

**Tech Stack**:
- MCP SDK (TypeScript)
- OpenRouter API integration
- Docker container for easy deployment

**Structure**:
```
mcp/standards-server/
├── Dockerfile
├── docker-compose.yml
├── package.json
├── .env.example
├── src/
│   ├── index.ts              # MCP server
│   ├── tools/
│   │   ├── query-standard.ts    # Query standards
│   │   ├── validate-code.ts     # Validate code snippet
│   │   ├── suggest-name.ts      # Suggest proper naming
│   │   └── get-template.ts      # Get project template
│   ├── openrouter/
│   │   └── client.ts         # OpenRouter API client
│   └── standards/
│       └── loader.ts         # Load standards docs
└── tests/
```

#### MCP Tools to Implement

**1. `query_standard`**
```typescript
// Ask questions about standards
// Input: { language: "terraform", question: "How should I name modules?" }
// Output: Specific guidance from terraform.md
```

**2. `validate_naming`**
```typescript
// Validate if a name follows standards
// Input: { type: "github_repo", name: "My-VPC-Config" }
// Output: { valid: false, issues: [...], suggestion: "my-vpc-config" }
```

**3. `validate_code`**
```typescript
// Validate code snippet against standards
// Input: { language: "terraform", code: "..." }
// Output: { valid: true/false, violations: [...], fixes: [...] }
```

**4. `suggest_structure`**
```typescript
// Suggest project structure
// Input: { type: "terraform-module" }
// Output: Folder structure + required files
```

**5. `get_template`**
```typescript
// Get template for specific file type
// Input: { type: "terraform-module-readme" }
// Output: README.md template
```

#### OpenRouter Integration

**Setup** (`mcp/standards-server/.env.example`):
```bash
OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet  # or your preferred model
MCP_SERVER_PORT=3000
STANDARDS_PATH=/path/to/development-standards
```

**Docker Setup** (`docker-compose.yml`):
```yaml
version: '3.8'
services:
  standards-mcp:
    build: .
    ports:
      - "3000:3000"
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - OPENROUTER_MODEL=${OPENROUTER_MODEL}
    volumes:
      - ../../:/standards:ro  # Mount standards repo
    restart: unless-stopped
```

**Dockerfile**:
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

#### Claude Code Integration

**Setup File** (`.claude/mcp-config.json` in projects):
```json
{
  "mcpServers": {
    "standards": {
      "url": "http://localhost:3000",
      "description": "refine.digital development standards"
    }
  }
}
```

**Usage in Claude Code**:
```
User: "Create a new Terraform module for VPC"
Claude: [Queries MCP server for Terraform standards]
Claude: [Generates code following exact standards]
```

#### Deliverables Day 8-9
- [ ] Working MCP server
- [ ] OpenRouter integration
- [ ] Docker setup
- [ ] 5 working MCP tools
- [ ] Claude Code integration guide
- [ ] Testing documentation

---

### Day 10: GitHub Actions + Templates

#### Create GitHub Actions Workflows

**1. Standards Check Action** (`.github/workflows/standards-check.yml`)
```yaml
name: Standards Check

on:
  pull_request:
    branches: [main, master]
  push:
    branches: [main, master]

jobs:
  check-standards:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install refine-standards
        run: npm install -g refine-standards

      - name: Check Terraform formatting
        if: contains(github.event.pull_request.files, '.tf')
        run: terraform fmt -check -recursive

      - name: Run tflint
        if: contains(github.event.pull_request.files, '.tf')
        uses: terraform-linters/setup-tflint@v4
        run: tflint --recursive

      - name: Validate YAML
        if: contains(github.event.pull_request.files, '.yml') || contains(github.event.pull_request.files, '.yaml')
        run: |
          npm install -g yaml-lint
          yamllint **/*.{yml,yaml}

      - name: Check Markdown
        if: contains(github.event.pull_request.files, '.md')
        run: |
          npm install -g markdownlint-cli
          markdownlint '**/*.md'

      - name: Run ShellCheck
        if: contains(github.event.pull_request.files, '.sh')
        uses: ludeeus/action-shellcheck@master

      - name: Check naming conventions
        run: refine-standards check

      - name: Post results
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '❌ Standards check failed. Please run `refine-standards check` locally and fix violations.'
            })
```

**2. Auto-fix Action** (`.github/workflows/auto-fix.yml`)
```yaml
name: Auto-fix Standards

on:
  issue_comment:
    types: [created]

jobs:
  auto-fix:
    if: contains(github.event.comment.body, '/fix-standards')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup tools
        run: |
          npm install -g refine-standards
          curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
          sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
          sudo apt-get update && sudo apt-get install terraform

      - name: Run auto-fix
        run: |
          terraform fmt -recursive
          refine-standards fix

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          commit-message: 'fix: auto-fix standards violations'
          branch: auto-fix-standards
          title: 'Auto-fix standards violations'
          body: 'This PR was automatically created to fix standards violations.'
```

#### Create Project Templates

**1. Terraform Module Template** (`templates/terraform-module/`)
```
terraform-module/
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
├── examples/
│   └── basic/
│       ├── main.tf
│       └── README.md
├── .terraform-docs.yml
├── .tflint.hcl
└── .github/
    └── workflows/
        └── terraform.yml
```

**2. GitHub Repository Template** (`templates/github-repo/`)
```
github-repo/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── .gitattributes
├── .editorconfig
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── .github/
│   ├── workflows/
│   │   └── standards.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
└── docs/
    └── .gitkeep
```

**3. README Template** (`templates/README-iac-template.md`)
```markdown
# {Project Name}

> {One-line description}

[![Standards Check](https://github.com/{org}/{repo}/workflows/standards-check/badge.svg)](https://github.com/{org}/{repo}/actions)

## Overview

{Detailed description}

## Prerequisites

- Terraform >= 1.0
- AWS CLI configured
- [Other tools]

## Project Structure

\`\`\`
{tree output}
\`\`\`

## Usage

### Quick Start

\`\`\`bash
{commands}
\`\`\`

### Configuration

{Configuration details}

## Development

### Local Setup

\`\`\`bash
{setup commands}
\`\`\`

### Running Tests

\`\`\`bash
{test commands}
\`\`\`

## Standards Compliance

This project follows [refine.digital Development Standards](https://github.com/{org}/development-standards).

To check compliance:
\`\`\`bash
refine-standards check
\`\`\`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

{License}
```

#### Deliverables Day 10
- [ ] 2 GitHub Actions workflows
- [ ] 3 project templates
- [ ] README template
- [ ] Template usage documentation

---

## Week 3-4: Polish + Rollout

### Week 3: Documentation + Examples

**Day 11-12: Main Documentation**
- [ ] Comprehensive README.md
- [ ] QUICKSTART.md (15-minute guide)
- [ ] FAQ.md
- [ ] TROUBLESHOOTING.md

**Day 13-14: Example Projects**
- [ ] Example Terraform module (fully compliant)
- [ ] Example GitHub Actions workflow
- [ ] Example multi-environment setup
- [ ] Migration guide for existing projects

**Day 15: Testing**
- [ ] Test CLI tool on real projects
- [ ] Test MCP server with Claude Code
- [ ] Test GitHub Actions on test repo
- [ ] Gather feedback, iterate

### Week 4: Rollout + Automation

**Day 16-17: Team Onboarding**
- [ ] Create onboarding video/guide
- [ ] Set up support channel
- [ ] Prepare demo/presentation
- [ ] Document common issues

**Day 18-19: Apply to Existing Projects**
- [ ] Identify 3-5 pilot projects
- [ ] Run `refine-standards check` on each
- [ ] Create PRs with fixes
- [ ] Document learnings

**Day 20: Launch + Monitoring**
- [ ] Announce to team
- [ ] Enforce on new projects
- [ ] Set up metrics dashboard
- [ ] Schedule review meeting

---

## Quick Start: Day 1 Actions

### Immediate Setup (Do This First)

**1. Create Repository** (15 min)
```bash
cd /Users/mattias/ProjectFiles/
mkdir development-standards
cd development-standards
git init

# Create structure
mkdir -p templates configs language-guides governance mcp automation examples
mkdir -p configs/{editorconfig,terraform,yaml,markdown,shell,prettier,vscode,git}
mkdir -p templates/{terraform-module,github-repo}
mkdir -p mcp/standards-server
mkdir -p automation/refine-standards

# Create initial files
touch README.md CONTRIBUTING.md
touch governance/PROJECT-NAMING-STANDARDS.md
touch governance/naming-validation-rules.json
```

**2. Set Up MCP Server Environment** (30 min)
```bash
# Create MCP server
cd mcp/standards-server
npm init -y
npm install @modelcontextprotocol/sdk express dotenv

# Create .env file
cat > .env << EOF
OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
MCP_SERVER_PORT=3000
STANDARDS_PATH=../../
EOF

# Create Dockerfile
cat > Dockerfile << EOF
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["node", "dist/index.js"]
EOF
```

**3. Start with PROJECT-NAMING-STANDARDS.md** (2-3 hours)

This is your HIGHEST PRIORITY - create comprehensive naming guide.

**4. Create First Language Guide** (2-3 hours)

Start with `language-guides/terraform.md` since Terraform is critical for IaC.

---

## Success Metrics

### Week 2 MVP Metrics
- [ ] 100% of naming standards documented
- [ ] CLI tool working for validation
- [ ] MCP server responding to queries
- [ ] 1 project template ready
- [ ] GitHub Action working

### Week 4 Production Metrics
- [ ] All 6 language guides complete
- [ ] All config templates available
- [ ] 3 example projects compliant
- [ ] Team onboarded
- [ ] Standards enforced in CI/CD

---

## Tools & Resources Needed

### Development Tools
- Node.js 20+
- Docker Desktop (you have this)
- VS Code with extensions:
  - HashiCorp Terraform
  - YAML
  - Markdown All in One
  - ShellCheck

### Services
- OpenRouter API key (you have this)
- GitHub account/org
- npm account (for publishing CLI)

### Time Estimate
- **Week 1**: 40 hours (core standards)
- **Week 2**: 40 hours (automation)
- **Week 3**: 30 hours (documentation)
- **Week 4**: 30 hours (rollout)
- **Total**: ~140 hours (3.5 weeks full-time)

---

## Next Actions (Right Now!)

1. **Create repository structure** (run commands above)
2. **Start PROJECT-NAMING-STANDARDS.md** (this is your pain point)
3. **Create terraform.md** (most critical language guide)
4. **Set up MCP server skeleton** (for AI integration)

Would you like me to help you with any of these immediate actions?
