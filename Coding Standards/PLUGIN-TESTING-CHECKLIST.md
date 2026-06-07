# Plugin Testing Checklist for Development Standards Repository

Use this checklist to verify all installed plugins work correctly with the refine.digital Development Standards Framework.

---

## Pre-Testing Setup

### ✅ Verify Plugin Installation

Check which plugins are currently installed:
```
/plugin
```

**Expected**: List of installed plugins with status indicators

### ✅ Confirm Marketplace Access

Verify marketplace is accessible:
```
/plugin marketplace list
```

**Expected**: Shows `wshobson/agents` in marketplace list

---

## Basic Functionality Tests

### Test 1: Documentation Generation ⚙️

**Plugin**: `code-documentation`

**Test command**:
```
Generate a brief overview README for the development-standards/configs/ directory explaining what configuration templates are available
```

**Expected outcome**:
- Agent activates and generates README content
- Includes list of subdirectories (editorconfig, terraform, yaml, etc.)
- Provides usage instructions
- Formatted as proper markdown

**Verification**:
- [ ] Agent activated successfully
- [ ] Generated appropriate content
- [ ] Content is relevant and accurate
- [ ] Markdown formatting is correct

---

### Test 2: Code Review ⚙️

**Plugin**: `code-review-ai`

**Test command**:
```
Review the development-standards/governance/PROJECT-NAMING-STANDARDS.md file for completeness, clarity, and consistency. Identify any missing naming scenarios or unclear examples.
```

**Expected outcome**:
- Comprehensive review of the standards document
- Identifies strengths and weaknesses
- Suggests improvements
- Provides actionable feedback

**Verification**:
- [ ] Thorough analysis completed
- [ ] Suggestions are relevant
- [ ] Feedback aligns with standards goals
- [ ] Identifies genuine improvements

---

### Test 3: Security Scanning ⚙️

**Plugin**: `security-scanning`

**Test command**:
```
Perform a security audit on the shell script examples in development-standards/language-guides/shell.md. Check for unsafe patterns, missing safety flags, and potential vulnerabilities.
```

**Expected outcome**:
- Identifies security issues in examples
- Checks for `set -euo pipefail` usage
- Validates safe scripting practices
- Provides remediation suggestions

**Verification**:
- [ ] Security analysis performed
- [ ] Identifies shell script safety issues
- [ ] Recommendations are practical
- [ ] No false positives

---

### Test 4: Infrastructure Review ⚙️

**Plugin**: `cloud-infrastructure`

**Test command**:
```
Review the Terraform naming conventions in development-standards/governance/PROJECT-NAMING-STANDARDS.md and verify they align with HashiCorp best practices. Identify any conflicts or missing patterns.
```

**Expected outcome**:
- Validates Terraform naming patterns
- Compares against HashiCorp standards
- Identifies gaps or conflicts
- Suggests improvements

**Verification**:
- [ ] Terraform expertise demonstrated
- [ ] Accurate comparison to HashiCorp standards
- [ ] Relevant suggestions provided
- [ ] No major misunderstandings

---

### Test 5: Multi-Agent Orchestration ⚙️

**Plugin**: `full-stack-orchestration`

**Test command**:
```
Coordinate a comprehensive review of development-standards/language-guides/yaml.md using multiple perspectives: code quality, security, documentation clarity, and infrastructure best practices.
```

**Expected outcome**:
- Multiple agents activate
- Each provides specialized perspective
- Coordinated final recommendations
- Comprehensive coverage

**Verification**:
- [ ] Multiple agents coordinated
- [ ] Different perspectives provided
- [ ] Recommendations complement each other
- [ ] No duplicate feedback

---

## Advanced Functionality Tests

### Test 6: Validation Rule Generation ⚙️

**Plugin**: `python-development`

**Test command**:
```
Analyze the structure of development-standards/governance/naming-validation-rules.json and suggest Python code for validating repository names against the github_repo pattern using regex.
```

**Expected outcome**:
- Python code snippet provided
- Uses regex from JSON schema
- Includes error handling
- Ready to integrate into CLI tool

**Verification**:
- [ ] Valid Python code generated
- [ ] Correctly uses regex pattern
- [ ] Includes proper error handling
- [ ] Follows Python best practices

---

### Test 7: Architecture Diagram Creation ⚙️

**Plugin**: `code-documentation` (mermaid-expert skill)

**Test command**:
```
Create a Mermaid diagram showing the structure of the development standards repository, including the relationships between governance files, language guides, configs, and templates directories.
```

**Expected outcome**:
- Valid Mermaid syntax
- Clear hierarchical structure
- Shows directory relationships
- Includes key files

**Verification**:
- [ ] Mermaid syntax is valid
- [ ] Diagram accurately represents structure
- [ ] Relationships are correct
- [ ] Rendering would be clear

---

### Test 8: CI/CD Workflow Generation ⚙️

**Plugin**: `cicd-automation`

**Test command**:
```
Generate a GitHub Actions workflow that validates all files in the repository against naming-validation-rules.json patterns. The workflow should run on pull requests and push to main branch.
```

**Expected outcome**:
- Valid GitHub Actions YAML
- Includes validation steps
- Proper trigger configuration
- Uses naming-validation-rules.json

**Verification**:
- [ ] Valid YAML syntax
- [ ] Correct GitHub Actions structure
- [ ] Appropriate triggers configured
- [ ] Would work in real repository

---

### Test 9: TDD Workflow ⚙️

**Plugin**: `tdd-workflows`

**Test command**:
```
Start a TDD cycle for implementing a function that validates YAML file extensions against our standard (.yml not .yaml). Write the test first, then implement the function.
```

**Expected outcome**:
- Red phase: Failing test written
- Green phase: Minimal implementation
- Refactor phase: Improved code
- Complete test coverage

**Verification**:
- [ ] Test written before implementation
- [ ] Test properly validates .yml requirement
- [ ] Implementation makes test pass
- [ ] Refactoring improves code quality

---

### Test 10: Kubernetes Standards Review ⚙️

**Plugin**: `kubernetes-operations`

**Test command**:
```
Review our YAML standards in development-standards/language-guides/yaml.md from a Kubernetes perspective. Ensure they align with Kubernetes manifest best practices for production deployments.
```

**Expected outcome**:
- K8s-specific validation
- Production readiness checks
- Best practices confirmation
- Suggestions for K8s scenarios

**Verification**:
- [ ] Kubernetes expertise demonstrated
- [ ] Relevant to manifest creation
- [ ] Production-ready recommendations
- [ ] Aligns with K8s conventions

---

## Integration Tests

### Test 11: Cross-Plugin Workflow ⚙️

**Plugins**: Multiple (code-review-ai → security-scanning → code-documentation)

**Test sequence**:
1. **Review**: `Review development-standards/language-guides/shell.md for completeness`
2. **Security**: `Security audit the shell script examples for vulnerabilities`
3. **Documentation**: `Generate a security best practices addendum for shell.md based on the findings`

**Expected outcome**:
- Each plugin activates in sequence
- Findings from earlier steps inform later steps
- Coherent workflow execution
- Final output incorporates all perspectives

**Verification**:
- [ ] All three plugins activated
- [ ] Context maintained between steps
- [ ] Final output comprehensive
- [ ] Workflow felt natural

---

### Test 12: Standards Update Workflow ⚙️

**Plugins**: Multiple (search-specialist → code-documentation → code-review-ai → unit-testing)

**Test sequence**:
```
Create a comprehensive workflow to add Go language standards:
1. Research current Go best practices (2024-2025)
2. Draft go.md following terraform.md structure
3. Review draft for completeness and accuracy
4. Create validation patterns for Go naming conventions
5. Generate tests for Go name validation
```

**Expected outcome**:
- Multi-agent orchestration
- Complete go.md draft created
- Validation patterns added
- Tests generated

**Verification**:
- [ ] Research was thorough and current
- [ ] go.md follows terraform.md structure
- [ ] Validation patterns are correct
- [ ] Tests are comprehensive

---

## Performance Tests

### Test 13: Token Efficiency ⚙️

**Goal**: Verify plugins load with minimal token overhead

**Test method**:
1. Check starting context usage
2. Activate a plugin
3. Check context usage after activation
4. Calculate token overhead

**Expected**: ~300 tokens per plugin on average

**Verification**:
- [ ] Token usage is reasonable
- [ ] No unexpected context bloat
- [ ] Progressive disclosure working
- [ ] Can install multiple plugins

---

### Test 14: Response Time ⚙️

**Goal**: Verify agents respond in reasonable time

**Test commands**:
```
# Simple task
Generate a one-paragraph overview of PROJECT-NAMING-STANDARDS.md

# Complex task
Perform comprehensive multi-agent review of entire development-standards directory
```

**Expected**:
- Simple tasks: < 10 seconds
- Complex tasks: < 60 seconds

**Verification**:
- [ ] Response times acceptable
- [ ] No hanging or timeout
- [ ] Progress indication clear
- [ ] Quality not sacrificed for speed

---

## Error Handling Tests

### Test 15: Invalid Input Handling ⚙️

**Test commands**:
```
# Non-existent file
Review the file development-standards/nonexistent.md

# Invalid syntax
/invalid-plugin:invalid-command

# Ambiguous request
Do something with the standards
```

**Expected outcome**:
- Clear error messages
- Graceful degradation
- Helpful suggestions
- No crashes

**Verification**:
- [ ] Errors handled gracefully
- [ ] Error messages are helpful
- [ ] System remains stable
- [ ] Recovery is possible

---

## Results Summary

Use this table to track your testing results:

| Test # | Test Name | Plugin(s) | Status | Notes |
|--------|-----------|-----------|--------|-------|
| 1 | Documentation Generation | code-documentation | ⬜ Pass / ❌ Fail | |
| 2 | Code Review | code-review-ai | ⬜ Pass / ❌ Fail | |
| 3 | Security Scanning | security-scanning | ⬜ Pass / ❌ Fail | |
| 4 | Infrastructure Review | cloud-infrastructure | ⬜ Pass / ❌ Fail | |
| 5 | Multi-Agent Orchestration | full-stack-orchestration | ⬜ Pass / ❌ Fail | |
| 6 | Validation Rule Generation | python-development | ⬜ Pass / ❌ Fail | |
| 7 | Architecture Diagram | code-documentation | ⬜ Pass / ❌ Fail | |
| 8 | CI/CD Workflow | cicd-automation | ⬜ Pass / ❌ Fail | |
| 9 | TDD Workflow | tdd-workflows | ⬜ Pass / ❌ Fail | |
| 10 | Kubernetes Review | kubernetes-operations | ⬜ Pass / ❌ Fail | |
| 11 | Cross-Plugin Workflow | Multiple | ⬜ Pass / ❌ Fail | |
| 12 | Standards Update | Multiple | ⬜ Pass / ❌ Fail | |
| 13 | Token Efficiency | All | ⬜ Pass / ❌ Fail | |
| 14 | Response Time | All | ⬜ Pass / ❌ Fail | |
| 15 | Error Handling | All | ⬜ Pass / ❌ Fail | |

---

## Post-Testing Actions

After completing tests:

1. **Document Issues** 📝
   - Create GitHub issues for any failures
   - Note unexpected behaviors
   - Record workarounds

2. **Update Documentation** 📚
   - Add successful workflows to PLUGIN-INTEGRATION-EXAMPLES.md
   - Document any limitations discovered
   - Update best practices based on findings

3. **Create Automation** 🤖
   - Convert successful workflows to scripts
   - Add to CI/CD pipeline
   - Create slash command shortcuts

4. **Share Results** 📢
   - Brief team on capabilities
   - Demonstrate successful workflows
   - Gather feedback for improvements

---

## Quick Test Commands

Copy and paste these for rapid testing:

```bash
# Documentation test
Generate a README overview for development-standards/configs/

# Review test
Review PROJECT-NAMING-STANDARDS.md for completeness and clarity

# Security test
Security audit shell.md examples for safety issues

# Infrastructure test
Review Terraform naming patterns against HashiCorp standards

# Multi-agent test
Comprehensive review of yaml.md from multiple perspectives

# Python code test
Generate Python regex validation for github_repo naming pattern

# Diagram test
Create Mermaid diagram of repository structure

# CI/CD test
Generate GitHub Actions workflow for naming validation

# TDD test
TDD cycle for YAML extension validation (.yml vs .yaml)

# Kubernetes test
Review YAML standards for K8s manifest compatibility
```

---

## Troubleshooting

### Agent Not Responding

**Try**:
1. Rephrase request more specifically
2. Reference exact file paths
3. Use slash command instead of natural language
4. Restart Claude Code if needed

### Incorrect Output

**Try**:
1. Provide more context about repository structure
2. Reference specific standards documents
3. Give examples of expected output
4. Use more targeted agent selection

### Token Limit Reached

**Try**:
1. Uninstall unused plugins
2. Break task into smaller steps
3. Clear conversation and start fresh
4. Use lighter-weight agents (Haiku where possible)

---

**Testing Date**: _________________
**Tester**: _________________
**Plugin Versions**: Latest from wshobson/agents
**Overall Result**: ⬜ Pass / ❌ Fail / ⚠️ Partial

**Notes**:
