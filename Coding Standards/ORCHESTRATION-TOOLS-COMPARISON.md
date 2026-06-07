# Claude Code Orchestration Tools Comparison

**Purpose**: Help you choose the right orchestration tools for your development workflow

**Last Updated**: 2025-11-07

---

## Available Tools

### 1. wshobson/agents (Marketplace Plugins)
**Type**: Plugin marketplace system
**Repository**: https://github.com/wshobson/agents
**Installation**: `/plugin marketplace add wshobson/agents`

### 2. claude-code-templates (CLI Installer)
**Type**: Template installer tool
**Repository**: https://github.com/davila7/claude-code-templates
**Installation**: `npx claude-code-templates@latest`

---

## Side-by-Side Comparison

| Feature | wshobson/agents | claude-code-templates |
|---------|-----------------|----------------------|
| **Installation Method** | Marketplace plugin (`/plugin`) | CLI installer (`npx`) |
| **Components** | 63 plugins, 85 agents, 47 skills | 100+ templates (agents, commands, MCPs) |
| **Storage** | Loads into Claude's context | Writes to `.claude/` directory |
| **Token Impact** | ~300 tokens per plugin (persistent) | Files on disk (no token cost) |
| **Activation** | Progressive disclosure | File-based (always loaded) |
| **Customization** | Via slash commands/skills | Direct file editing |
| **MCPs** | Not included | PostgreSQL, GitHub, Stripe, AWS, etc. |
| **Analytics** | Not included | Built-in dashboard |
| **Health Check** | Not included | Built-in diagnostic |
| **Updates** | Marketplace auto-updates | Re-run CLI to update |
| **Multi-Agent** | Native orchestration (85 agents) | Template-based coordination |
| **Documentation** | GitHub docs | Website + docs portal |
| **Best For** | Comprehensive framework | Specific templates + MCPs |

---

## Detailed Comparison

### Architecture

#### wshobson/agents
```
Marketplace Plugin System
    ↓
Plugins load into Claude's context
    ↓
Progressive disclosure (activate when needed)
    ↓
~300 tokens per plugin overhead
    ↓
85 agents coordinate automatically
```

**Pros**:
- ✅ Token-efficient (progressive loading)
- ✅ Comprehensive framework (63 plugins)
- ✅ Multi-agent orchestration built-in
- ✅ Regular marketplace updates
- ✅ No file clutter

**Cons**:
- ❌ Persistent token overhead (small)
- ❌ No MCP integrations
- ❌ No built-in analytics
- ❌ Less customizable (need wrappers)

#### claude-code-templates
```
CLI Installer Tool
    ↓
Writes files to .claude/ directory
    ↓
Files loaded when Claude Code starts
    ↓
No persistent token cost (files on disk)
    ↓
Templates activate based on file content
```

**Pros**:
- ✅ No token overhead (file-based)
- ✅ Easy customization (edit files)
- ✅ MCP integrations included
- ✅ Analytics dashboard
- ✅ Health check tool
- ✅ Browse templates on website

**Cons**:
- ❌ File clutter in `.claude/`
- ❌ Manual updates (re-run CLI)
- ❌ Less integrated framework
- ❌ No automatic orchestration

---

## Use Case Recommendations

### Use wshobson/agents WHEN:

1. **You want a comprehensive, integrated framework**
   - 63 plugins cover most development scenarios
   - 85 agents coordinate automatically
   - Multi-agent workflows built-in

2. **Token efficiency matters**
   - Progressive disclosure loads only what's needed
   - ~300 tokens per plugin (acceptable overhead)
   - Clean context management

3. **You prefer marketplace-style plugin system**
   - Easy installation: `/plugin install [name]`
   - Automatic updates from marketplace
   - No file management

4. **Multi-agent orchestration is important**
   - Agents coordinate automatically
   - Complex workflows (full-stack, security, etc.)
   - 47 skills activate contextually

**Recommended for**:
- General software development
- Multi-agent workflows
- Large-scale projects
- Teams wanting standardization

### Use claude-code-templates WHEN:

1. **You need specific MCP integrations**
   - PostgreSQL database access
   - GitHub API integration
   - Stripe payment processing
   - AWS SDK access

2. **You want analytics and monitoring**
   - Session tracking
   - Token consumption metrics
   - Real-time conversation monitoring

3. **You prefer file-based customization**
   - Edit `.claude/` files directly
   - Full control over templates
   - Version control templates easily

4. **You want pre-built project scaffolding**
   - React, Vue, Angular templates
   - Django, FastAPI templates
   - Framework-specific CLAUDE.md files

**Recommended for**:
- Projects needing database/API access
- Analytics-driven development
- Highly customized workflows
- Quick project scaffolding

### Use BOTH WHEN:

1. **You want the best of both worlds**
   - wshobson/agents: Core framework + multi-agent
   - claude-code-templates: MCPs + analytics + custom templates

2. **You have diverse needs**
   - Development work: wshobson/agents plugins
   - Database access: claude-code-templates MCPs
   - Monitoring: claude-code-templates analytics

3. **Maximum flexibility required**
   - Plugin framework for standard workflows
   - File-based templates for customization
   - MCPs for external integrations

**Recommended for**:
- Professional development teams
- Complex full-stack projects
- Projects requiring external integrations
- Maximum productivity

---

## Recommended Setup for Development Standards Repository

### Option 1: wshobson/agents Only (Current Setup)

**What you have**:
```bash
/plugin marketplace add wshobson/agents
/plugin install code-review-ai
/plugin install security-scanning
/plugin install code-documentation
/plugin install cloud-infrastructure
/plugin install kubernetes-operations
/plugin install cicd-automation
/plugin install python-development
```

**Token overhead**: ~2,100 tokens (7 plugins)

**Pros**:
- ✅ Clean, integrated system
- ✅ Multi-agent coordination
- ✅ Covers 90% of standards validation needs
- ✅ No file clutter

**Cons**:
- ❌ No database MCPs (for future CLI tool)
- ❌ No analytics dashboard
- ❌ No health monitoring

**Rating**: ⭐⭐⭐⭐ (Excellent for most use cases)

### Option 2: Hybrid Approach (Recommended)

**Combine both tools**:

```bash
# Keep wshobson/agents for core framework
/plugin marketplace add wshobson/agents
/plugin install code-review-ai
/plugin install security-scanning
/plugin install cloud-infrastructure
/plugin install python-development

# Add claude-code-templates for specific enhancements
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates --analytics
```

**Token overhead**: ~1,200 tokens (4 plugins) + file-based templates

**Pros**:
- ✅ Core framework from wshobson/agents
- ✅ MCPs for database access (future CLI tool)
- ✅ Analytics dashboard for monitoring
- ✅ Best of both worlds

**Cons**:
- ❌ Two systems to manage
- ❌ Slight added complexity

**Rating**: ⭐⭐⭐⭐⭐ (Best for professional use)

### Option 3: claude-code-templates Only

**Switch to templates**:

```bash
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --agent quality-assurance/security-auditor --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates --analytics
```

**Token overhead**: 0 tokens (all file-based)

**Pros**:
- ✅ No token overhead
- ✅ Easy customization (edit files)
- ✅ MCPs included
- ✅ Analytics dashboard

**Cons**:
- ❌ Less integrated framework
- ❌ No automatic multi-agent orchestration
- ❌ File management required
- ❌ Manual template updates

**Rating**: ⭐⭐⭐ (Good for specific use cases)

---

## Decision Matrix

### Choose wshobson/agents if:

- ✅ You want integrated multi-agent framework
- ✅ Token overhead is acceptable (~2,100 for 7 plugins)
- ✅ You prefer marketplace plugins
- ✅ You need automatic agent coordination
- ✅ You want minimal file management

### Choose claude-code-templates if:

- ✅ You need MCP integrations (databases, APIs)
- ✅ You want analytics and monitoring
- ✅ You prefer file-based customization
- ✅ You need project scaffolding
- ✅ Token overhead is a concern

### Choose BOTH if:

- ✅ You want maximum capabilities
- ✅ You need MCPs AND multi-agent framework
- ✅ Analytics are important
- ✅ You're willing to manage two systems
- ✅ Professional/production use case

---

## Quick Start Guide

### Scenario 1: Just Starting (Beginner)

**Recommendation**: Start with **wshobson/agents** only

```bash
/plugin marketplace add wshobson/agents
/plugin install code-review-ai
/plugin install python-development
```

**Why**: Simpler, integrated, covers most needs

### Scenario 2: Need Database Access

**Recommendation**: Add **claude-code-templates** MCPs

```bash
# Keep existing wshobson/agents plugins
# Add PostgreSQL MCP
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

**Why**: wshobson/agents doesn't provide MCPs

### Scenario 3: Want Analytics

**Recommendation**: Add **claude-code-templates** analytics

```bash
# Keep existing wshobson/agents plugins
# Add analytics
npx claude-code-templates --analytics
```

**Why**: Real-time monitoring and insights

### Scenario 4: Maximum Power (Advanced)

**Recommendation**: Use **BOTH**

```bash
# Core framework
/plugin marketplace add wshobson/agents
/plugin install code-review-ai
/plugin install security-scanning
/plugin install cloud-infrastructure
/plugin install python-development

# Enhancements
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates@latest --mcp development/github-integration --yes
npx claude-code-templates --analytics
```

**Why**: Best of both worlds, maximum capabilities

---

## Cost Analysis

### Token Budget Comparison

**wshobson/agents** (7 plugins):
```
code-review-ai:        ~300 tokens
security-scanning:     ~300 tokens
code-documentation:    ~300 tokens
cloud-infrastructure:  ~300 tokens
kubernetes-operations: ~300 tokens
cicd-automation:       ~300 tokens
python-development:    ~300 tokens
────────────────────────────────
Total:                 ~2,100 tokens
Percentage of 200K:    1.05%
```

**claude-code-templates** (file-based):
```
Agents (5 files):      0 tokens (on disk)
Commands (3 files):    0 tokens (on disk)
MCPs (2 configs):      0 tokens (on disk)
────────────────────────────────
Total:                 0 tokens
Percentage of 200K:    0%
```

**Hybrid Approach** (recommended):
```
wshobson/agents:       ~1,200 tokens (4 plugins)
claude-code-templates: 0 tokens (file-based)
────────────────────────────────
Total:                 ~1,200 tokens
Percentage of 200K:    0.6%
```

**Verdict**: All options have negligible token impact! Choose based on features, not tokens.

---

## Real-World Recommendations

### For Your Development Standards Repository

**Current Status**: wshobson/agents with 7 plugins ✅

**Recommendation**: **Add claude-code-templates MCPs + Analytics**

```bash
# Keep existing plugins (don't uninstall)
# Add these enhancements:
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates --analytics
npx claude-code-templates --health-check
```

**Why**:
1. **PostgreSQL MCP**: For future `refine-standards` CLI tool database
2. **Analytics**: Track standards validation usage
3. **Health Check**: Ensure optimal setup
4. **Keep plugins**: They're working great, no need to change

**Result**: Best of both worlds! 🎉

---

## Migration Paths

### From wshobson/agents → Hybrid

```bash
# KEEP existing plugins (don't uninstall)
# ADD enhancements
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates --analytics
```

**Effort**: 5 minutes
**Risk**: Very low (additive, not replacement)

### From Nothing → Hybrid

```bash
# Install both systems
/plugin marketplace add wshobson/agents
/plugin install code-review-ai
/plugin install python-development

npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates --analytics
```

**Effort**: 10 minutes
**Risk**: Very low (clean install)

### From Hybrid → wshobson/agents only

```bash
# Remove claude-code-templates files
rm -rf .claude/agents/
rm -rf .claude/commands/
rm -rf .claude/mcps/

# Keep wshobson/agents plugins (already installed)
```

**Effort**: 2 minutes
**Risk**: Low (just file deletion)

---

## Summary

### Quick Decision Guide

**Question**: Do you need database/API integrations (MCPs)?
- **Yes** → Use claude-code-templates (or hybrid)
- **No** → wshobson/agents is sufficient

**Question**: Do you want analytics and monitoring?
- **Yes** → Add claude-code-templates analytics
- **No** → wshobson/agents is sufficient

**Question**: Are you willing to manage two systems?
- **Yes** → Hybrid approach (recommended)
- **No** → Choose primary based on needs

### Final Recommendation for Development Standards Repository

**Use Hybrid Approach**:
- ✅ wshobson/agents: 4-5 core plugins (~1,500 tokens)
- ✅ claude-code-templates: PostgreSQL MCP + Analytics (0 tokens)

**Total overhead**: ~1,500 tokens (0.75% of context)
**Total capability**: Maximum! 🚀

---

## Quick Reference

### wshobson/agents
- **Installation**: `/plugin marketplace add wshobson/agents`
- **Usage**: Natural language or `/plugin-name:command`
- **Docs**: [PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md)

### claude-code-templates
- **Installation**: `npx claude-code-templates@latest`
- **Usage**: Files in `.claude/` directory
- **Docs**: [CLAUDE-CODE-TEMPLATES-GUIDE.md](CLAUDE-CODE-TEMPLATES-GUIDE.md)

### Both Together
- **Installation**: Follow both guides
- **Usage**: Seamless integration
- **Docs**: Both guides + this comparison

---

**Last Updated**: 2025-11-07
**Recommendation**: Hybrid approach for maximum capability
**Status**: Both tools production-ready ✅
