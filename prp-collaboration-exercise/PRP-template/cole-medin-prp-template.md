# PRP: [Feature/Project Name]

*PRP Version: 1.0*  
*Based on Cole Medin's Product Requirement Prompts Framework*

## GOAL
[Clearly state what needs to be built. Be specific about the end state and desired outcomes. This should be 2-3 sentences that leave no ambiguity about what success looks like.]

## WHY
[Explain the business justification and user value. Why does this need to be built? What problem does it solve? Who benefits and how? This context helps the implementer make better decisions during development.]

## WHAT
[Provide detailed feature specifications. Break down the requirements into specific, actionable components. Include:]

### Functional Requirements
- [List specific features and capabilities]
- [Include user interactions and workflows]
- [Define data requirements and structures]

### Non-Functional Requirements
- [Performance requirements]
- [Security requirements]
- [Scalability considerations]
- [Compatibility requirements]

### Success Criteria
- [ ] [Specific, measurable outcome 1]
- [ ] [Specific, measurable outcome 2]
- [ ] [User can perform specific action]
- [ ] [Performance requirement met]
- [ ] [Security standard followed]
- [ ] [All tests pass]

## MUST READ - Context

Include these resources in your implementation context:

### Official Documentation
- url: [Official API documentation URL]
  why: [Specific sections/methods you'll need]
  critical: [Key insight that prevents common errors]

### Example Code
- file: [path/to/example/file.ext]
  why: [Pattern to follow, specific implementation to mirror]
  gotchas: [Common mistakes to avoid]

### Internal Documentation
- doc: [Internal documentation or design doc]
  section: [Specific section about architecture/patterns]
  important: [Critical design decision or constraint]

### Third-Party Resources
- resource: [Library or framework documentation]
  version: [Specific version if important]
  why: [Integration patterns or compatibility notes]

## IMPLEMENTATION APPROACH

### Phase 1: Foundation [Estimated Time: X hours]

**Objective**: [What this phase accomplishes]

1. **CREATE** [file/module/component]
   - [Specific instruction 1]
   - [Specific instruction 2]
   
2. **MODIFY** [existing file/module]
   - FIND: [pattern/section to locate]
   - INJECT: [what to add]
   - PRESERVE: [what must not change]

3. **IMPLEMENT** [core functionality]
   - [Implementation detail 1]
   - [Implementation detail 2]
   - Error handling: [specific error cases to handle]

### Phase 2: Core Features [Estimated Time: X hours]

**Objective**: [What this phase accomplishes]

1. **EXTEND** [component from Phase 1]
   - [Specific feature to add]
   - [Integration requirement]

2. **CREATE** [new component]
   - Follow pattern from: [reference file]
   - Key differences: [what's different]

3. **INTEGRATE** [components]
   - [Connection points]
   - [Data flow requirements]

### Phase 3: Polish and Validation [Estimated Time: X hours]

**Objective**: [Final touches and quality assurance]

1. **OPTIMIZE** [performance bottlenecks]
   - [Specific optimization 1]
   - [Specific optimization 2]

2. **ENHANCE** [user experience]
   - [UI/UX improvement]
   - [Error message clarity]

3. **DOCUMENT** [critical components]
   - [What needs documentation]
   - [Documentation format/location]

## VALIDATION GATES

Execute these validation steps before considering implementation complete:

### Automated Testing
```bash
# Unit tests
pytest tests/unit/ -v

# Integration tests  
pytest tests/integration/ -v

# End-to-end tests
pytest tests/e2e/ -v
```

### Code Quality
```bash
# Linting
flake8 src/ --max-line-length=100

# Type checking
mypy src/ --strict

# Security scan
bandit -r src/
```

### Performance Validation
```bash
# Load testing
python scripts/load_test.py --users=100 --duration=60

# Performance benchmarks
python scripts/benchmark.py --iterations=1000
```

### Manual Verification Checklist
- [ ] Feature works as specified in success criteria
- [ ] Edge cases handled gracefully
- [ ] Error messages are clear and actionable
- [ ] Documentation is complete and accurate
- [ ] Code follows project conventions
- [ ] No security vulnerabilities introduced
- [ ] Performance meets requirements

## DEPENDENCIES

### Required Libraries/Packages
```
library==version  # Purpose/usage
package>=min_version  # Critical for [feature]
```

### External Services
- [Service name]: [Purpose and configuration requirements]
- [API name]: [Endpoint and authentication details]

### Environment Variables
```bash
VARIABLE_NAME  # Description and example value
API_KEY  # Required for [service], obtain from [location]
```

## ROLLBACK PLAN

If implementation fails or causes issues:

1. **Immediate Actions**
   - [Step to disable feature]
   - [Step to restore previous state]

2. **Data Recovery**
   - [Backup location]
   - [Recovery procedure]

3. **Communication**
   - [Who to notify]
   - [Status page update]

## NOTES FOR IMPLEMENTER

### Known Challenges
- [Potential issue 1 and suggested approach]
- [Potential issue 2 and mitigation strategy]

### Optimization Opportunities
- [Area that could be improved if time permits]
- [Nice-to-have feature that's not critical]

### Future Considerations
- [How this implementation might need to scale]
- [Potential future integrations to keep in mind]

## APPROVAL

- [ ] Product Owner reviewed and approved
- [ ] Technical Lead reviewed and approved
- [ ] Security review completed (if applicable)
- [ ] Performance impact assessed

---

*This PRP follows Cole Medin's framework: PRP = PRD + Curated Codebase Intelligence + Agent Runbook*

*Remember: Context is King. The more relevant context you provide, the better the implementation outcome.*