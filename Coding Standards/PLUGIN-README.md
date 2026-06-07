# Claude Code Marketplace Plugin Integration

This directory contains complete documentation for integrating the **wshobson/agents** marketplace plugins with the refine.digital Development Standards Framework.

---

## 📚 Documentation Files

| File | Size | Purpose | Read When |
|------|------|---------|-----------|
| **[PLUGIN-SUMMARY.md](PLUGIN-SUMMARY.md)** | 11KB | Executive overview, integration status | Start here - high-level overview |
| **[PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md)** | 15KB | Installation, configuration, troubleshooting | Setting up plugins for first time |
| **[PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md)** | 16KB | 21 practical workflows and examples | Daily usage, learning patterns |
| **[PLUGIN-TESTING-CHECKLIST.md](PLUGIN-TESTING-CHECKLIST.md)** | 13KB | 15 test scenarios for verification | Quality assurance, testing |

**Total Documentation**: 55KB of comprehensive guides

---

## 🚀 Quick Start (5 Minutes)

### 1. Read the Summary
Start with **[PLUGIN-SUMMARY.md](PLUGIN-SUMMARY.md)** for:
- What was done
- Key benefits
- Integration checklist
- Next steps

### 2. Install Plugins
Follow **[PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md)**:
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

### 3. Test Installation
Run first test from **[PLUGIN-TESTING-CHECKLIST.md](PLUGIN-TESTING-CHECKLIST.md)**:
```
Generate a brief overview README for development-standards/configs/
```

### 4. Try Examples
Pick a workflow from **[PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md)**:
```
Review development-standards/governance/PROJECT-NAMING-STANDARDS.md
for completeness, clarity, and consistency
```

---

## 🎯 Use Cases by Role

### Infrastructure Engineer
**Best Workflows**:
- Terraform standards validation
- Kubernetes YAML review
- Multi-cloud standards compliance
- Infrastructure diagram generation

**Start Here**: [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md#infrastructure-standards-review)

### Security Engineer
**Best Workflows**:
- Security hardening review
- SAST analysis on examples
- Compliance auditing
- Shell script safety checks

**Start Here**: [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md#security--compliance)

### Platform Engineer
**Best Workflows**:
- CI/CD pipeline creation
- Pre-commit hook setup
- Deployment strategies
- Automation workflows

**Start Here**: [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md#cicd-integration)

### Developer
**Best Workflows**:
- CLI tool development
- TDD workflows
- Unit test generation
- Code review automation

**Start Here**: [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md#cli-tool-development)

### Technical Writer
**Best Workflows**:
- Documentation generation
- README creation
- Architecture diagrams
- API documentation

**Start Here**: [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md#documentation-generation)

---

## 🔧 Most Useful Plugins for This Repository

### Tier 1: Essential (Install First)
1. **code-review-ai** - Review standards for completeness
2. **security-scanning** - Audit code examples for vulnerabilities
3. **code-documentation** - Generate missing READMEs

### Tier 2: High Value (Install Next)
4. **cloud-infrastructure** - Validate Terraform standards
5. **kubernetes-operations** - Review YAML/K8s patterns
6. **cicd-automation** - Create GitHub Actions workflows

### Tier 3: Development (Install for CLI Tool)
7. **python-development** - Scaffold refine-standards CLI
8. **tdd-workflows** - Test-driven development
9. **unit-testing** - Generate validation tests

---

## 📖 Common Commands

### Standards Validation
```bash
# Review Terraform standards
"Review terraform.md against PROJECT-NAMING-STANDARDS.md for compliance"

# Validate YAML examples
"Review yaml.md examples for .yml extension and snake_case keys"

# Check shell safety
"Audit shell.md examples for set -euo pipefail and shellcheck compliance"
```

### Documentation Generation
```bash
# Generate README
"Generate README for configs/ directory"

# Create diagrams
"Create Mermaid diagram of repository structure"

# API documentation
"Document naming-validation-rules.json schema structure"
```

### Security Auditing
```bash
# Comprehensive audit
/security-scanning:security-hardening --level comprehensive

# SAST scan
"Security scan all code examples in language-guides/"

# Compliance check
"Audit standards against SOC2 and GDPR requirements"
```

### Automation
```bash
# Create CI/CD workflow
"Generate GitHub Actions workflow for naming validation"

# Pre-commit hooks
"Create pre-commit configuration for standards enforcement"

# CLI scaffolding
"Scaffold refine-standards CLI tool with Click and pytest"
```

---

## 🧪 Testing & Validation

### Quick Test (2 Minutes)
```
Generate a one-paragraph overview of PROJECT-NAMING-STANDARDS.md
```
**Expected**: Summary of naming conventions

### Medium Test (5 Minutes)
```
Review development-standards/language-guides/yaml.md for
completeness and compliance with our .yml extension standard
```
**Expected**: Detailed review with suggestions

### Comprehensive Test (15 Minutes)
```
Perform comprehensive multi-agent review of development-standards/
covering architecture, security, documentation, and best practices
```
**Expected**: Multi-perspective analysis

**Full Testing**: See [PLUGIN-TESTING-CHECKLIST.md](PLUGIN-TESTING-CHECKLIST.md) for 15 detailed tests

---

## 🎓 Learning Path

### Day 1: Setup & Basics
1. Read [PLUGIN-SUMMARY.md](PLUGIN-SUMMARY.md)
2. Install core plugins using [PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md)
3. Run Tests 1-3 from [PLUGIN-TESTING-CHECKLIST.md](PLUGIN-TESTING-CHECKLIST.md)
4. Try 3 examples from [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md)

### Day 2: Advanced Usage
1. Complete Tests 4-10 from testing checklist
2. Try multi-agent orchestration examples
3. Generate first CI/CD workflow
4. Create documentation for configs/

### Day 3: Automation
1. Set up pre-commit hooks
2. Create GitHub Actions workflow
3. Start CLI tool development
4. Document custom workflows

### Week 2: Production
1. Integrate with team workflows
2. Create custom slash commands
3. Build automation pipelines
4. Train team members

---

## 📊 Integration Status

### ✅ Completed
- [x] Plugin marketplace added
- [x] Core plugins installed (7 plugins)
- [x] Documentation created (4 guides, 55KB)
- [x] Examples documented (21 workflows)
- [x] Testing checklist created (15 tests)
- [x] CLAUDE.md updated

### ⏳ In Progress
- [ ] Testing completion (user verification)
- [ ] CI/CD workflow implementation
- [ ] CLI tool scaffolding
- [ ] Team training

### 📅 Planned
- [ ] Custom workflow library
- [ ] Automated standards updates
- [ ] Pre-commit hook deployment
- [ ] Team adoption metrics

---

## 🆘 Troubleshooting

### Plugin Not Found
**Problem**: `/plugin install [name]` fails
**Solution**: Check spelling with `/plugin` to list available plugins

### Agent Not Responding
**Problem**: Natural language doesn't activate agent
**Solution**: Use more specific phrasing or try slash command

### Token Limit Reached
**Problem**: Context filling up too fast
**Solution**: Uninstall unused plugins, use lighter agents

**Full Troubleshooting**: See [PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md#troubleshooting)

---

## 🔗 Additional Resources

### Internal Documentation
- **Standards Framework**: [development-standards/](development-standards/)
- **Naming Standards**: [development-standards/governance/PROJECT-NAMING-STANDARDS.md](development-standards/governance/PROJECT-NAMING-STANDARDS.md)
- **AI Integration**: [AI-ASSISTED-VALIDATION.md](AI-ASSISTED-VALIDATION.md)
- **Framework Overview**: [OVERVIEW.md](OVERVIEW.md)

### External Resources
- **Plugin Repository**: https://github.com/wshobson/agents
- **Plugin Documentation**: https://github.com/wshobson/agents/tree/main/docs
- **Claude Code Docs**: https://docs.claude.com/claude-code

---

## 📝 Quick Reference

### File Structure
```
Coding Standards/
├── PLUGIN-README.md                    # ⭐ This file - start here
├── PLUGIN-SUMMARY.md                   # Executive overview
├── PLUGIN-SETUP-GUIDE.md               # Installation guide
├── PLUGIN-INTEGRATION-EXAMPLES.md      # 21 practical workflows
├── PLUGIN-TESTING-CHECKLIST.md         # 15 test scenarios
├── CLAUDE.md                           # Updated with plugin info
└── development-standards/              # Core standards framework
    ├── governance/
    │   ├── PROJECT-NAMING-STANDARDS.md
    │   └── naming-validation-rules.json
    ├── language-guides/
    ├── configs/
    └── templates/
```

### Command Patterns

**Natural Language** (exploratory):
```
"Review [file] against [standard]"
"Generate [documentation] for [component]"
"Create [workflow] that [requirement]"
```

**Slash Commands** (structured):
```
/plugin-name:command-name [arguments]
```

**Multi-Agent** (complex):
```
"Coordinate [agent1], [agent2] to [task]"
```

---

## 🎉 Success Metrics

### Installation Success
- ✅ Marketplace added
- ✅ 7 core plugins installed
- ✅ ~2,100 tokens overhead (acceptable)

### Documentation Success
- ✅ 4 comprehensive guides created
- ✅ 21 practical examples documented
- ✅ 15 test scenarios defined
- ✅ 55KB total documentation

### Integration Success
- ⏳ Testing pending (user verification)
- ⏳ CI/CD pending (automation phase)
- ⏳ Team adoption pending (training)

---

## 📞 Support

### Questions About Plugins
1. Check [PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md)
2. Review [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md)
3. GitHub Issues: https://github.com/wshobson/agents/issues

### Questions About Standards
1. Check [development-standards/](development-standards/)
2. Read [PROJECT-NAMING-STANDARDS.md](development-standards/governance/PROJECT-NAMING-STANDARDS.md)
3. Review language-specific guides

---

**Created**: 2025-11-07
**Last Updated**: 2025-11-07
**Status**: Ready for Testing
**Next Review**: After testing completion

---

## TL;DR

1. **Read**: [PLUGIN-SUMMARY.md](PLUGIN-SUMMARY.md) (high-level overview)
2. **Install**: Follow [PLUGIN-SETUP-GUIDE.md](PLUGIN-SETUP-GUIDE.md) (7 core plugins)
3. **Test**: Run [PLUGIN-TESTING-CHECKLIST.md](PLUGIN-TESTING-CHECKLIST.md) (verify functionality)
4. **Use**: Apply [PLUGIN-INTEGRATION-EXAMPLES.md](PLUGIN-INTEGRATION-EXAMPLES.md) (21 workflows)
5. **Automate**: Build CI/CD, CLI tools, and team workflows

**Result**: AI-powered standards validation and automation! 🚀
