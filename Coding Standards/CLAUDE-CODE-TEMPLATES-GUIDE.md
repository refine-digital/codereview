# Claude Code Templates Installation & Usage Guide

**Repository**: https://github.com/davila7/claude-code-templates
**Website**: https://aitmpl.com
**Documentation**: https://docs.aitmpl.com
**Type**: CLI Tool for Installing Pre-built Templates
**License**: MIT

---

## Overview

Claude Code Templates is a **CLI-based installer** for ready-to-use Claude Code configurations. It provides 100+ pre-built components that you can install with a single command.

### Key Difference from wshobson/agents

| Feature | wshobson/agents | claude-code-templates |
|---------|-----------------|----------------------|
| **Type** | Marketplace plugin system | CLI installer tool |
| **Installation** | `/plugin marketplace add` | `npx claude-code-templates` |
| **Activation** | Plugins load into context | Installs files to `.claude/` directory |
| **Content** | 63 plugins, 85 agents, 47 skills | 100+ templates (agents, commands, MCPs) |
| **Source** | Single comprehensive framework | Curated from multiple sources |
| **Token Usage** | Plugins load into context (~300 tokens each) | Files written to disk (no persistent token cost) |
| **Updates** | Plugin marketplace updates | CLI re-runs to update templates |
| **Custom** | Via slash commands/skills | Direct file editing in `.claude/` |
| **Analytics** | Not included | Built-in analytics dashboard |
| **MCPs** | Not directly included | PostgreSQL, GitHub, Stripe, AWS, etc. |

**In summary**:
- **wshobson/agents**: Marketplace plugin system (loads into Claude's context)
- **claude-code-templates**: File installer (writes to `.claude/` directory)

---

## Installation

### Method 1: Interactive Installation (Recommended)

Run the CLI tool interactively to browse and select templates:

```bash
npx claude-code-templates@latest
```

**What happens**:
1. Interactive menu appears
2. Browse available agents, commands, MCPs
3. Select what you want to install
4. Confirms installation locations
5. Writes files to your `.claude/` directory

### Method 2: Direct Installation (Fast)

Install specific components directly with `--yes` flag:

```bash
# Install a specific agent
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes

# Install a command
npx claude-code-templates@latest --command testing/generate-tests --yes

# Install an MCP
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

### Method 3: Global Installation (For Frequent Use)

Install the CLI globally for easier access:

```bash
# Install globally
npm install -g claude-code-templates

# Then use directly
claude-code-templates
claude-code-templates --agent development-tools/code-reviewer --yes
```

---

## What Gets Installed

### Installation Location

All templates install to your project's `.claude/` directory:

```
your-project/
├── .claude/
│   ├── agents/           # AI specialist definitions
│   ├── commands/         # Custom slash commands
│   ├── mcps/             # External integrations
│   ├── settings/         # Configuration files
│   ├── hooks/            # Automation triggers
│   └── skills/           # Reusable capabilities
├── [your project files]
└── CLAUDE.md             # May be created/updated
```

### Available Template Categories

#### 1. **Agents** (Domain Specialists)

Located in: `.claude/agents/`

**Development Team**:
- `frontend-developer` - React, Vue, Angular expert
- `backend-developer` - Node.js, Python, Go specialist
- `fullstack-developer` - Complete stack coverage
- `mobile-developer` - React Native, Flutter, native iOS/Android

**Infrastructure**:
- `devops-engineer` - CI/CD, deployment, infrastructure
- `cloud-architect` - AWS, Azure, GCP design
- `kubernetes-specialist` - Container orchestration
- `terraform-expert` - Infrastructure as Code

**Quality & Security**:
- `security-auditor` - Vulnerability assessment
- `performance-optimizer` - Speed and efficiency
- `code-reviewer` - Quality assurance
- `test-engineer` - Comprehensive testing

**Data & Analytics**:
- `database-architect` - Schema design, optimization
- `data-engineer` - Pipelines, ETL, warehousing
- `ml-engineer` - Machine learning workflows

#### 2. **Commands** (Slash Commands)

Located in: `.claude/commands/`

**Testing**:
- `/generate-tests` - Create comprehensive test suites
- `/run-tests` - Execute test runners
- `/coverage-report` - Generate coverage analysis

**Code Quality**:
- `/optimize-bundle` - Reduce bundle size
- `/check-security` - Security vulnerability scan
- `/refactor-code` - Improve code structure
- `/fix-lint` - Auto-fix linting issues

**Documentation**:
- `/generate-docs` - Create documentation
- `/update-readme` - Update README files
- `/api-docs` - Generate API documentation

**Infrastructure**:
- `/deploy-staging` - Deploy to staging environment
- `/rollback` - Rollback deployment
- `/check-health` - System health check

#### 3. **MCPs** (External Integrations)

Located in: `.claude/mcps/`

**Development Tools**:
- `github-integration` - GitHub API access
- `gitlab-integration` - GitLab operations
- `jira-integration` - Issue tracking

**Databases**:
- `postgresql-integration` - PostgreSQL access
- `mongodb-integration` - MongoDB operations
- `redis-integration` - Redis cache management

**Cloud Services**:
- `aws-integration` - AWS SDK access
- `stripe-integration` - Payment processing
- `openai-integration` - OpenAI API access

**Monitoring**:
- `datadog-integration` - Metrics and logs
- `sentry-integration` - Error tracking

#### 4. **Settings**

Located in: `.claude/settings/`

- Timeout configurations
- Memory limits
- Output formatting
- Model preferences

#### 5. **Hooks**

Located in: `.claude/hooks/`

- Pre-commit validation
- Post-completion actions
- Error handlers
- Custom automation

#### 6. **Skills**

Located in: `.claude/skills/`

- PDF processing
- Excel automation
- Image manipulation
- Custom workflows

---

## Usage Examples

### Example 1: Install Code Reviewer Agent

```bash
# Interactive
npx claude-code-templates@latest
# Select: Agents → Development Tools → Code Reviewer

# Direct
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
```

**What gets installed**: `.claude/agents/code-reviewer.md`

**How to use**:
```
Use the code-reviewer agent to analyze my Python code for quality issues
```

The agent definition is now in your project, so Claude reads it automatically!

### Example 2: Install Test Generation Command

```bash
npx claude-code-templates@latest --command testing/generate-tests --yes
```

**What gets installed**: `.claude/commands/generate-tests.md`

**How to use**:
```bash
/generate-tests
```

### Example 3: Install PostgreSQL MCP

```bash
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

**What gets installed**: `.claude/mcps/postgresql.json` (configuration)

**How to use**:
```
Query the users table in my PostgreSQL database and show me all active users
```

Claude can now directly access your PostgreSQL database!

### Example 4: Install Multiple Templates

```bash
# Install frontend developer agent
npx claude-code-templates@latest --agent development-team/frontend-developer --yes

# Install testing command
npx claude-code-templates@latest --command testing/generate-tests --yes

# Install GitHub integration
npx claude-code-templates@latest --mcp development/github-integration --yes
```

---

## Additional Features

### Analytics Dashboard

Monitor your Claude Code usage:

```bash
npx claude-code-templates --analytics
```

**Provides**:
- Session statistics
- Token consumption tracking
- Performance metrics
- Usage patterns

### Conversation Monitor

Real-time monitoring of Claude responses:

```bash
npx claude-code-templates --chats
```

**Features**:
- Live session viewing
- Mobile-optimized interface
- Secure remote access via Cloudflare Tunnel
- Response history

### Health Check

Diagnose your Claude Code installation:

```bash
npx claude-code-templates --health-check
```

**Checks**:
- Installation status
- Configuration validity
- MCP connectivity
- File permissions
- System requirements

### Plugin Dashboard

Unified plugin management interface:

```bash
npx claude-code-templates --plugins
```

**Features**:
- View installed plugins
- Manage permissions
- Enable/disable components
- Update templates

---

## Integration with Your Development Standards Repository

### Recommended Setup for refine.digital Standards

**Step 1: Install Standards-Related Templates**

```bash
# Code reviewer for standards validation
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes

# Security auditor for example code
npx claude-code-templates@latest --agent quality-assurance/security-auditor --yes

# Documentation generator
npx claude-code-templates@latest --agent development-tools/documentation-specialist --yes
```

**Step 2: Create Custom Commands**

The templates install to `.claude/commands/`, which you can then customize:

Edit `.claude/commands/validate-terraform.md`:
```markdown
---
name: validate-terraform
description: Validate Terraform against refine.digital standards
---

Review Terraform files against our standards:
1. Check development-standards/governance/PROJECT-NAMING-STANDARDS.md
2. Validate snake_case resource naming
3. Verify file structure (main.tf, variables.tf, outputs.tf)
4. Check security best practices
5. Ensure documentation completeness

Reference: development-standards/language-guides/terraform.md
```

**Step 3: Use Installed Templates**

```bash
# Use code reviewer agent
"Use the code-reviewer to validate our Terraform standards in language-guides/terraform.md"

# Use slash command
/validate-terraform

# Use security auditor
"Security audit all shell script examples in language-guides/shell.md"
```

---

## Comparison: wshobson/agents vs claude-code-templates

### When to Use wshobson/agents (Marketplace Plugins)

✅ **Use when**:
- You want comprehensive, integrated framework
- Prefer marketplace plugin system
- Need progressive disclosure (token efficiency)
- Want 63+ specialized plugins
- Coordinated multi-agent workflows are important

### When to Use claude-code-templates (CLI Installer)

✅ **Use when**:
- You want to browse and pick specific templates
- Prefer file-based customization
- Need MCP integrations (PostgreSQL, GitHub, Stripe, etc.)
- Want analytics and monitoring dashboards
- Prefer direct file editing over plugin system
- Need pre-built project scaffolding

### Can You Use Both? **YES!**

They work together perfectly:

```
Your Project/
├── .claude/
│   ├── agents/           # From claude-code-templates
│   ├── commands/         # From claude-code-templates
│   ├── mcps/             # From claude-code-templates
│   └── skills/           # From claude-code-templates
├── CLAUDE.md             # References both systems
└── [wshobson/agents installed via /plugin marketplace add]
```

**Best of both worlds**:
- wshobson/agents: Core plugin framework (marketplace)
- claude-code-templates: Additional templates + MCPs + Analytics

---

## Recommended Setup for Development Standards Repository

### Hybrid Approach (Best Option)

**1. Keep wshobson/agents for core functionality**:
```bash
# Already installed
/plugin install code-review-ai
/plugin install security-scanning
/plugin install cloud-infrastructure
/plugin install python-development
```

**2. Add claude-code-templates for specific enhancements**:
```bash
# Add PostgreSQL MCP (for future CLI tool database)
npx claude-code-templates@latest --mcp database/postgresql-integration --yes

# Add analytics
npx claude-code-templates --analytics

# Add specific commands you want to customize
npx claude-code-templates@latest --command testing/generate-tests --yes
```

**3. Result**:
- ✅ wshobson/agents: 7 plugins (~2,100 tokens) for general development
- ✅ claude-code-templates: MCPs + Analytics + Custom commands (file-based)
- ✅ Both systems working together seamlessly

---

## Quick Reference

### Installation Commands

```bash
# Interactive mode
npx claude-code-templates@latest

# Install specific agent
npx claude-code-templates@latest --agent [category]/[name] --yes

# Install command
npx claude-code-templates@latest --command [category]/[name] --yes

# Install MCP
npx claude-code-templates@latest --mcp [category]/[name] --yes

# Global installation
npm install -g claude-code-templates
```

### Utility Commands

```bash
# Analytics dashboard
npx claude-code-templates --analytics

# Conversation monitor
npx claude-code-templates --chats

# Health check
npx claude-code-templates --health-check

# Plugin dashboard
npx claude-code-templates --plugins
```

### Browse Templates

- **Website**: https://aitmpl.com
- **Docs**: https://docs.aitmpl.com
- **GitHub**: https://github.com/davila7/claude-code-templates

---

## File Locations After Installation

```
your-project/
├── .claude/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── security-auditor.md
│   │   └── frontend-developer.md
│   ├── commands/
│   │   ├── generate-tests.md
│   │   ├── optimize-bundle.md
│   │   └── validate-terraform.md
│   ├── mcps/
│   │   ├── postgresql.json
│   │   ├── github.json
│   │   └── stripe.json
│   ├── settings/
│   │   └── config.json
│   ├── hooks/
│   │   └── pre-commit.md
│   └── skills/
│       └── pdf-processor.md
└── CLAUDE.md
```

---

## Best Practices

### ✅ DO:

1. **Start with interactive mode** to browse available templates
2. **Install selectively** - only what you need
3. **Customize installed files** in `.claude/` directory
4. **Version control** your `.claude/` directory
5. **Use analytics** to track usage patterns
6. **Combine with wshobson/agents** for maximum power
7. **Check health** regularly with `--health-check`

### ❌ DON'T:

1. **Install everything** - clutters your `.claude/` directory
2. **Ignore installed files** - customize them for your needs
3. **Skip analytics** - valuable insights available
4. **Forget to commit** `.claude/` to git
5. **Treat as exclusive** - works great with other tools

---

## Troubleshooting

### Issue: Templates Not Activating

**Problem**: Installed templates but Claude doesn't use them

**Solution**:
1. Check files exist in `.claude/` directory
2. Restart Claude Code session
3. Reference agent/command explicitly
4. Run health check: `npx claude-code-templates --health-check`

### Issue: MCP Not Connecting

**Problem**: MCP integration not working

**Solution**:
1. Check `.claude/mcps/` configuration
2. Verify credentials/API keys
3. Review MCP logs
4. Run health check
5. Consult docs: https://docs.aitmpl.com

### Issue: Conflicts with Marketplace Plugins

**Problem**: claude-code-templates conflicts with wshobson/agents

**Solution**:
- Rename files to avoid duplicates
- Use different namespaces
- Generally they coexist fine - no real conflicts

---

## Migration Strategy

### If Currently Using Only wshobson/agents

**Keep it!** Add claude-code-templates for:
- MCPs (database, API integrations)
- Analytics dashboard
- Pre-built commands to customize
- Monitoring tools

### If Currently Using Only claude-code-templates

**Add wshobson/agents** for:
- Comprehensive plugin framework
- 85 coordinated agents
- Multi-agent orchestration
- Progressive disclosure

### Recommended: Use Both

**Optimal setup**:
```bash
# Core framework (marketplace)
/plugin marketplace add wshobson/agents
/plugin install [core plugins]

# Enhancements (CLI templates)
npx claude-code-templates --mcp database/postgresql-integration --yes
npx claude-code-templates --analytics
```

---

## Summary

**claude-code-templates** is a **CLI installer tool** that writes pre-built templates to your `.claude/` directory. It's different from wshobson/agents (marketplace plugins) but **works perfectly alongside it**.

**Key Benefits**:
- ✅ 100+ ready-to-use templates
- ✅ MCP integrations (PostgreSQL, GitHub, Stripe, AWS)
- ✅ Analytics and monitoring dashboards
- ✅ File-based (easy customization)
- ✅ No persistent token cost
- ✅ Health check and diagnostics

**Best Use Case**:
Add claude-code-templates to your existing wshobson/agents setup for MCPs, analytics, and file-based customization.

---

**Installation**: `npx claude-code-templates@latest`
**Browse Templates**: https://aitmpl.com
**Documentation**: https://docs.aitmpl.com
**Repository**: https://github.com/davila7/claude-code-templates

**Last Updated**: 2025-11-07
**Compatible with**: wshobson/agents marketplace plugins ✅
