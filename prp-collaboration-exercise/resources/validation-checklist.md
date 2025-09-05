# PRP Quality Validation Checklist

## Overview
This checklist helps ensure your PRP meets Cole Medin's quality standards and will effectively guide implementation.

## Section-by-Section Validation

### ✅ GOAL Section
- [ ] **Specific**: States exactly what will be built (not vague like "improve system")
- [ ] **Measurable**: Defines clear end state that can be verified
- [ ] **Achievable**: Scope is reasonable for intended timeline
- [ ] **Relevant**: Aligns with stated business needs
- [ ] **Time-bound**: Includes delivery expectations if applicable

**Red Flags:**
- ❌ "Build a better solution"
- ❌ "Improve performance"
- ❌ "Add some features"

**Good Examples:**
- ✅ "Build a REST API with 10 endpoints for user management supporting 1000 req/sec"
- ✅ "Create React dashboard displaying real-time metrics with <2 sec refresh rate"

### ✅ WHY Section
- [ ] **Business Value**: Clearly articulates ROI or cost savings
- [ ] **User Benefit**: Explains how users' lives improve
- [ ] **Problem Statement**: Identifies specific pain points addressed
- [ ] **Metrics**: Includes measurable impact (%, time, money)
- [ ] **Priority Justification**: Explains why this is needed now

**Quality Indicators:**
- Mentions specific user segments affected
- Quantifies current problems (e.g., "40% of users abandon cart")
- Projects measurable improvements
- Links to business OKRs or strategy

### ✅ WHAT Section

#### Functional Requirements
- [ ] **Complete**: All user stories/use cases covered
- [ ] **Specific**: No ambiguous terms like "user-friendly" or "fast"
- [ ] **Prioritized**: Core vs nice-to-have features distinguished
- [ ] **Testable**: Each requirement can be verified
- [ ] **Consistent**: No contradicting requirements

#### Non-Functional Requirements
- [ ] **Performance**: Specific metrics (response time, throughput)
- [ ] **Scalability**: User/data volume expectations
- [ ] **Security**: Authentication, authorization, data protection
- [ ] **Reliability**: Uptime, error rates, recovery time
- [ ] **Compatibility**: Browser, OS, device requirements

#### Success Criteria
- [ ] **Checkbox Format**: Uses markdown checkboxes
- [ ] **Specific Conditions**: Not vague ("works properly")
- [ ] **Measurable**: Can definitively say yes/no
- [ ] **Complete**: Covers all critical paths
- [ ] **Realistic**: Achievable with given resources

### ✅ MUST READ - Context Section
- [ ] **URLs Valid**: All links tested and working
- [ ] **Files Exist**: Referenced files accessible
- [ ] **Relevance Explained**: "why" field for each resource
- [ ] **Critical Insights**: Gotchas and important notes highlighted
- [ ] **Version Specific**: Libraries/APIs version noted if relevant
- [ ] **Curated**: Not just dumping links, but explaining significance

**Context Quality Scoring:**
- ⭐⭐⭐ Includes code examples with line numbers
- ⭐⭐⭐ Highlights specific patterns to follow
- ⭐⭐⭐ Warns about common mistakes
- ⭐⭐ Provides alternative approaches
- ⭐ Links to relevant documentation

### ✅ IMPLEMENTATION APPROACH
- [ ] **Phased**: Broken into logical phases
- [ ] **Objectives Clear**: Each phase has specific goal
- [ ] **Action Words**: Uses CREATE, MODIFY, DELETE, etc.
- [ ] **Dependencies**: Order of operations makes sense
- [ ] **Specific Files**: Names files/modules to create/modify
- [ ] **Error Handling**: Specifies how to handle failures
- [ ] **Patterns Referenced**: Points to examples to follow

**Implementation Clarity Test:**
Could a developer implement this without asking questions?
- If NO: Add more specific details
- If MAYBE: Clarify ambiguous points
- If YES: Good to proceed

### ✅ VALIDATION GATES
- [ ] **Automated Tests**: Specific test commands provided
- [ ] **Executable**: Commands can be copy-pasted and run
- [ ] **Comprehensive**: Covers unit, integration, e2e tests
- [ ] **Performance**: Includes load/stress testing if relevant
- [ ] **Security**: Security scanning included if applicable
- [ ] **Manual Checks**: Checklist for human verification
- [ ] **Rollback Plan**: Clear steps if validation fails

### ✅ DEPENDENCIES
- [ ] **Complete List**: All libraries/services listed
- [ ] **Versions**: Specific versions when important
- [ ] **Installation**: How to install/configure
- [ ] **Environment Vars**: All required variables documented
- [ ] **External Services**: APIs, databases, etc. specified
- [ ] **Access Requirements**: Credentials, permissions needed

## Overall Quality Metrics

### Completeness Score
Rate each section 0-10:
- [ ] GOAL clarity: ___/10
- [ ] WHY justification: ___/10
- [ ] WHAT specifications: ___/10
- [ ] Context curation: ___/10
- [ ] Implementation detail: ___/10
- [ ] Validation coverage: ___/10

**Total: ___/60** (Aim for 48+)

### Red Flag Checklist
Check for these PRP anti-patterns:
- [ ] ❌ Vague language ("probably", "maybe", "should work")
- [ ] ❌ Missing error handling
- [ ] ❌ No validation commands
- [ ] ❌ Assumed knowledge ("use standard patterns")
- [ ] ❌ Contradicting instructions
- [ ] ❌ Missing dependencies
- [ ] ❌ No success criteria
- [ ] ❌ Unstructured context dump

### Green Flag Checklist
Look for these quality indicators:
- [ ] ✅ Specific line numbers in code references
- [ ] ✅ Example requests/responses for APIs
- [ ] ✅ Rollback procedures defined
- [ ] ✅ Performance benchmarks specified
- [ ] ✅ Security considerations addressed
- [ ] ✅ Edge cases documented
- [ ] ✅ Future considerations noted
- [ ] ✅ Clear phase boundaries

## Common Issues and Fixes

### Issue: Vague Requirements
**Symptom**: "Make it user-friendly"
**Fix**: Define specific UX requirements
```
BAD:  "User-friendly interface"
GOOD: "Form validates on blur, shows inline errors, saves draft every 30 seconds"
```

### Issue: Missing Context
**Symptom**: Implementation requires guessing
**Fix**: Add specific examples and patterns
```
BAD:  "Follow our coding standards"
GOOD: "Follow pattern from src/components/Button.tsx, use CSS modules from styles/"
```

### Issue: Untestable Success Criteria
**Symptom**: "System works properly"
**Fix**: Define measurable conditions
```
BAD:  "Search works well"
GOOD: "Search returns results in <500ms for 90% of queries with relevance score >0.8"
```

### Issue: Context Without Purpose
**Symptom**: Links without explanation
**Fix**: Explain why each resource matters
```
BAD:  "See: https://docs.api.com"
GOOD: "See: https://docs.api.com/auth - Critical: Use OAuth2 flow, not API keys"
```

## Validation Process

### Self-Validation (Before Submission)
1. Read PRP from implementer perspective
2. List any questions you'd need answered
3. Address those questions in the PRP
4. Run through this checklist
5. Score each section

### Peer Validation (Review Process)
1. Can you understand the goal in 30 seconds?
2. Is the business value clear?
3. Could you implement without clarification?
4. Are test commands executable?
5. Would you feel confident deploying this?

### Instructor Validation (Final Check)
1. Meets course requirements?
2. Appropriate complexity for level?
3. Follows Cole Medin's principles?
4. Demonstrates understanding?
5. Production-ready quality?

## Quality Levels

### 🥉 Bronze (Minimum Passing)
- All sections present
- Basic requirements clear
- Some context provided
- Implementation outlined
- Basic validation included

### 🥈 Silver (Good)
- Clear, specific requirements
- Well-curated context
- Detailed implementation steps
- Comprehensive validation
- Dependencies documented

### 🥇 Gold (Excellent)
- Exceptional clarity throughout
- Context anticipates issues
- Implementation leaves no ambiguity
- Validation ensures quality
- Production-ready documentation

### 💎 Platinum (Outstanding)
- Could hand to any developer
- Context teaches best practices
- Implementation guides architecture
- Validation prevents all issues
- Sets new standard for PRPs

## Final Quality Check

Before submitting your PRP, ask yourself:

> "If I handed this PRP to a competent developer who knows nothing about our project, could they successfully implement the feature without asking me any questions?"

If the answer is not a confident "YES", continue refining your PRP.

Remember Cole Medin's standard: **First-pass success through comprehensive context.**

---

*Quality PRPs save time, reduce errors, and enable scalable development. Invest in context engineering—it pays dividends in implementation efficiency.*