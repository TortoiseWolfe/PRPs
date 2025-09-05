# Common PRP Patterns and Templates

## Introduction

This guide provides reusable patterns and templates for common scenarios in PRP creation. These patterns, derived from Cole Medin's work and successful PRPs, help maintain consistency and quality.

## Pattern Categories

### 1. API Development Patterns

#### RESTful API PRP Pattern
```markdown
## GOAL
Build RESTful API for [resource] supporting CRUD operations with [authentication type] and rate limiting of [X requests/minute].

## Context Structure
- API Design specification (OpenAPI/Swagger)
- Database schema for resource
- Authentication middleware example
- Error handling patterns
- Rate limiting implementation

## Implementation Phases
1. Database models and migrations
2. Basic CRUD endpoints
3. Authentication/authorization
4. Validation and error handling
5. Rate limiting and caching
6. Documentation and testing
```

#### GraphQL API PRP Pattern
```markdown
## GOAL
Implement GraphQL API with [queries/mutations/subscriptions] for [domain] supporting [real-time features].

## Key Context Elements
- GraphQL schema definitions
- Resolver patterns from existing code
- DataLoader for N+1 prevention
- Subscription pub/sub patterns
- Permission checking examples

## Validation Focus
- Query performance (no N+1 queries)
- Schema validation
- Subscription memory leaks
- Error handling consistency
```

### 2. Frontend Component Patterns

#### React Component PRP Pattern
```markdown
## GOAL
Create [component name] React component with [specific features] following [design system].

## Essential Context
- Design system documentation/Figma
- Similar component examples
- State management pattern (Context/Redux/Zustand)
- API integration approach
- Accessibility requirements (WCAG level)

## Success Criteria Template
- [ ] Component renders in all supported browsers
- [ ] Passes accessibility audit (aXe/WAVE)
- [ ] Responsive from 320px to 4K
- [ ] Handles loading/error/empty states
- [ ] Unit tests achieve 80%+ coverage
```

#### Form Component PRP Pattern
```markdown
## Standard Sections for Forms
1. Validation rules (client + server)
2. Error display patterns
3. Submit handling (optimistic updates?)
4. Field dependencies/conditional logic
5. Accessibility (labels, ARIA, keyboard nav)
```

### 3. Database Patterns

#### Migration PRP Pattern
```markdown
## GOAL
Migrate [data/schema] from [source] to [destination] affecting [X records] with zero downtime.

## Critical Context
- Current schema (with constraints/indexes)
- Target schema
- Data transformation rules
- Rollback procedure
- Batch processing approach

## Phases for Zero-Downtime Migration
1. Add new columns/tables (backward compatible)
2. Dual-write to old and new
3. Backfill historical data
4. Switch reads to new structure
5. Stop writes to old structure
6. Clean up old structure
```

#### Performance Optimization PRP Pattern
```markdown
## Required Metrics
- Current query execution times
- Expected performance targets
- Index analysis results
- Query execution plans
- Lock contention points

## Standard Optimizations to Consider
- [ ] Add appropriate indexes
- [ ] Denormalize hot paths
- [ ] Implement caching layer
- [ ] Partition large tables
- [ ] Archive old data
```

### 4. Integration Patterns

#### Third-Party Service Integration Pattern
```markdown
## GOAL
Integrate [service name] for [purpose] handling [volume] requests/day.

## Integration Checklist
- [ ] API documentation link
- [ ] Authentication method
- [ ] Rate limits and quotas
- [ ] Error codes and handling
- [ ] Webhook endpoints (if applicable)
- [ ] Sandbox/test environment
- [ ] SLA and uptime expectations

## Standard Implementation Flow
1. Client library setup
2. Authentication configuration
3. Basic API calls with error handling
4. Rate limiting/retry logic
5. Webhook handling (if needed)
6. Monitoring and alerting
7. Circuit breaker pattern
```

#### Message Queue Integration Pattern
```markdown
## Essential Elements
- Message format/schema
- Queue configuration (DLQ, retention)
- Consumer group setup
- Idempotency approach
- Monitoring metrics
- Poison message handling
```

### 5. Testing Patterns

#### Test Suite PRP Pattern
```markdown
## GOAL
Implement comprehensive test suite achieving [X%] coverage with [unit/integration/e2e] tests.

## Test Structure Template
tests/
├── unit/          # Fast, isolated tests
├── integration/   # Component interaction tests
├── e2e/          # User journey tests
└── fixtures/     # Test data

## Coverage Requirements by Type
- Unit: 80%+ line coverage
- Integration: Critical paths covered
- E2E: Happy path + major error cases
```

#### Performance Testing Pattern
```markdown
## Load Test Scenarios
1. Normal load: [baseline metrics]
2. Peak load: [expected spikes]
3. Stress test: [breaking point]
4. Soak test: [sustained load]

## Metrics to Measure
- Response time (p50, p95, p99)
- Throughput (requests/second)
- Error rate
- Resource utilization
```

### 6. Security Patterns

#### Authentication Implementation Pattern
```markdown
## Security Requirements Checklist
- [ ] Password requirements defined
- [ ] Session management approach
- [ ] Token expiration/refresh
- [ ] Rate limiting on auth endpoints
- [ ] Account lockout policy
- [ ] Audit logging
- [ ] CSRF protection
- [ ] XSS prevention
```

#### Data Privacy Pattern
```markdown
## GDPR/Privacy Considerations
- Data minimization approach
- Consent management
- Right to deletion implementation
- Data export format
- Encryption at rest/in transit
- PII identification and handling
```

## Context Curation Patterns

### The "Example-First" Pattern
When introducing new patterns:
```markdown
## Context
- file: existing_implementation.js
  why: This shows our current pattern
  lines: 45-67
  
- file: new_implementation.js
  why: Migrate to this new pattern
  key_differences: 
    - Async/await instead of callbacks
    - Error boundaries added
    - Typing enforced
```

### The "Anti-Pattern" Pattern
When replacing bad practices:
```markdown
## DO NOT (Current Anti-Patterns)
- ❌ Direct database queries in controllers
- ❌ Synchronous external API calls
- ❌ Storing secrets in code

## DO INSTEAD (Correct Patterns)
- ✅ Use repository pattern (see src/repositories/)
- ✅ Async with timeout (see src/utils/apiClient.js)
- ✅ Environment variables (see .env.example)
```

### The "Progressive Enhancement" Pattern
For incremental improvements:
```markdown
## Phase 1: Minimum Viable [Feature]
- Basic functionality
- Critical path only
- No optimizations

## Phase 2: Enhanced [Feature]
- Add caching
- Improve error handling
- Add telemetry

## Phase 3: Production [Feature]
- Performance optimizations
- Full monitoring
- Advanced features
```

## Implementation Instruction Patterns

### Action Verb Templates
```markdown
CREATE [file/module/component]
├── Define [structure/interface/schema]
├── Implement [core logic]
├── Add [error handling]
└── Include [tests]

MODIFY [existing file]
├── FIND: [pattern/section to locate]
├── PRESERVE: [what must not change]
├── INJECT: [new code to add]
└── VALIDATE: [ensure still works]

INTEGRATE [component A] with [component B]
├── Define interface/contract
├── Implement adapter/connector
├── Handle failures/retries
└── Test integration points

MIGRATE from [old] to [new]
├── Create parallel implementation
├── Add feature flag
├── Dual-write period
├── Switch reads
├── Remove old code
```

### Error Handling Templates
```markdown
## Standard Error Handling Pattern

### API Errors
- 400: Return validation errors with field names
- 401: Redirect to login
- 403: Show permission denied message
- 404: Show not found page
- 429: Implement exponential backoff
- 500: Show generic error, log details
- 503: Show maintenance message

### Database Errors
- Connection failed: Retry with backoff
- Timeout: Increase timeout or optimize query
- Constraint violation: Return user-friendly message
- Deadlock: Retry transaction

### External Service Errors
- Network error: Circuit breaker pattern
- Rate limited: Queue and retry
- Invalid response: Log and use fallback
```

## Validation Gate Patterns

### Standard Validation Commands
```markdown
## Automated Validation Suite

# Code Quality
npm run lint                    # ESLint
npm run format:check            # Prettier
npm run type:check              # TypeScript

# Testing  
npm test                        # Unit tests
npm run test:integration        # Integration tests
npm run test:e2e               # End-to-end tests
npm run test:coverage          # Coverage report

# Security
npm audit                       # Dependency vulnerabilities
npm run security:scan          # SAST scan
npm run secrets:scan           # Secret detection

# Performance
npm run lighthouse             # Frontend performance
npm run load:test              # Backend load test
```

### Manual Validation Checklists
```markdown
## Pre-Deployment Checklist
- [ ] All tests passing
- [ ] No console errors/warnings
- [ ] Responsive on all devices
- [ ] Accessibility audit passed
- [ ] Security scan clean
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Rollback plan tested
```

## Common Success Criteria Templates

### API Success Criteria
```markdown
- [ ] All endpoints return correct status codes
- [ ] Response times < 200ms for 95% of requests
- [ ] Handles 1000 concurrent connections
- [ ] Rate limiting prevents abuse
- [ ] API documentation auto-generated
- [ ] Backward compatibility maintained
```

### UI Component Success Criteria
```markdown
- [ ] Renders correctly in Chrome, Firefox, Safari, Edge
- [ ] Responsive from 320px to 4K resolution
- [ ] Keyboard navigable
- [ ] Screen reader compatible
- [ ] Loading states for async operations
- [ ] Error states for failures
- [ ] Empty states for no data
```

### Data Processing Success Criteria
```markdown
- [ ] Processes [X] records per second
- [ ] Memory usage stays under [X] GB
- [ ] Handles malformed data gracefully
- [ ] Maintains data integrity
- [ ] Provides progress indication
- [ ] Supports resume after failure
```

## PRP Length Guidelines

### Small Feature (500-1000 words)
- Simple CRUD operations
- UI components
- Bug fixes
- Configuration changes

### Medium Feature (1000-2000 words)
- API integrations
- Multi-step workflows
- Database migrations
- New service setup

### Large Feature (2000-4000 words)
- System architecture
- Complex integrations
- Performance optimization
- Security implementation

### Enterprise Feature (4000+ words)
- Distributed systems
- ML pipelines
- Platform migrations
- Compliance implementations

## Quick Reference Templates

### Microservice PRP Starter
```markdown
# PRP: [Service Name] Microservice

## GOAL
[One sentence description]

## Context Essentials
- Service boundaries/responsibilities
- API contracts (proto/OpenAPI)
- Database schema
- Message formats
- Deployment configuration

## Standard Microservice Phases
1. Service scaffold and configuration
2. Core business logic
3. API implementation
4. Database integration
5. Message queue integration
6. Monitoring and health checks
7. Documentation and testing
```

### Bug Fix PRP Starter
```markdown
# PRP: Fix [Bug Description]

## GOAL
Resolve [issue] affecting [users/component] causing [impact].

## Bug Analysis
- Root cause: [technical explanation]
- Affected code: [files/functions]
- Impact scope: [what breaks]
- Reproduction steps: [how to trigger]

## Fix Approach
1. Locate issue in [file:line]
2. Apply fix: [specific change]
3. Add test to prevent regression
4. Verify related code unaffected
```

## Summary

These patterns provide starting points for common PRP scenarios. Remember:

1. **Adapt patterns to your context** - Don't blindly copy
2. **Combine patterns as needed** - Real features often need multiple patterns
3. **Maintain consistency** - Use similar patterns for similar problems
4. **Evolve patterns** - Update based on what works in your environment

The goal is not rigid adherence to templates but efficient creation of high-quality PRPs that enable first-pass implementation success.

---

*"Patterns are not prescriptions but inspirations. Use them to accelerate PRP creation while maintaining the context richness that makes PRPs powerful."* - Based on Cole Medin's methodology