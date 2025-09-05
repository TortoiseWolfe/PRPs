# PRP Collaboration Exercise: Learning Cole Medin's Product Requirement Prompts Framework

## Overview

Welcome to the PRP Collaboration Exercise! This repository teaches you two essential skills for modern software development:

1. **Cole Medin's PRP Framework** - A revolutionary approach to AI-assisted development that transforms vague ideas into production-ready code through comprehensive context provision
2. **GitHub Collaboration Workflows** - Professional version control patterns used in real-world software teams

## What is a PRP?

Cole Medin's formula: **PRP = PRD + Curated Codebase Intelligence + Agent Runbook**

A Product Requirement Prompt (PRP) is a comprehensive implementation blueprint that provides AI coding assistants with everything needed to generate production-ready code on the first attempt. Unlike traditional "vibe coding" where developers iterate through trial and error, PRPs enable "Context Engineering" - delivering all necessary context upfront for immediate success.

### Why PRPs Matter

- **Efficiency**: Cole built 18 MCP server tools in 25 minutes using PRPs
- **Quality**: First-pass code that's production-ready, not prototype quality
- **Clarity**: Eliminates ambiguity between requirements and implementation
- **Scalability**: Enables AI to handle complex, multi-phase implementations

## Exercise Structure

### Prerequisites

- Basic Git/GitHub knowledge
- GitHub account with repository access
- Text editor or IDE
- Understanding of markdown formatting

### Learning Objectives

By completing this exercise, you will:

1. Master the PRP template structure and components
2. Practice creating comprehensive technical documentation
3. Learn professional GitHub collaboration workflows
4. Develop peer review and feedback skills
5. Build context engineering expertise for AI-assisted development

## Getting Started

### Step 1: Fork and Clone

1. Fork this repository to your GitHub account
2. Clone your fork locally:
   ```bash
   git clone https://github.com/[your-username]/prp-collaboration-exercise.git
   cd prp-collaboration-exercise
   ```

### Step 2: Create Your Branch

Create a feature branch following our naming convention:
```bash
git checkout -b prp/[your-github-username]/[exercise-name]
# Example: git checkout -b prp/johndoe/recipe-app
```

### Step 3: Choose Your Exercise Level

Select an exercise appropriate to your skill level:

- **Beginner**: Recipe Storage App (`exercises/beginner-exercise.md`)
- **Intermediate**: Collaborative Todo List (`exercises/intermediate-exercise.md`)
- **Advanced**: E-commerce Platform Feature (`exercises/advanced-exercise.md`)

### Step 4: Create Your PRP

1. Copy the template from `PRP-template/cole-medin-prp-template.md`
2. Create your PRP in `student-PRPs/[your-username]-[exercise-name].md`
3. Follow the template structure carefully
4. Reference the example PRPs for guidance

### Step 5: Self-Validate

Before submitting, ensure your PRP:

- [ ] Includes all required template sections
- [ ] Has clear, measurable success criteria
- [ ] Provides relevant, curated context
- [ ] Defines logical implementation phases
- [ ] Specifies executable validation gates

Run the validation script:
```bash
python scripts/validate_prp.py student-PRPs/[your-file].md
```

### Step 6: Submit Pull Request

1. Commit your PRP:
   ```bash
   git add student-PRPs/[your-file].md
   git commit -m "Add PRP for [exercise-name] by [your-name]"
   git push origin prp/[your-username]/[exercise-name]
   ```

2. Open a pull request to the main branch
3. Use the PR template to describe your PRP
4. Request review from instructor or peers

### Step 7: Participate in Peer Review

Review at least two other PRPs:

1. Check for template compliance
2. Evaluate context completeness
3. Assess implementation clarity
4. Provide constructive feedback

## Assessment Rubric

### PRP Content Quality (40%)

- **Excellent (A)**: All sections complete with exceptional detail, clear goals, comprehensive context
- **Good (B)**: Most sections well-developed, minor gaps in context or clarity
- **Satisfactory (C)**: Basic requirements met, some sections need more detail
- **Needs Improvement (D-F)**: Missing sections, unclear goals, insufficient context

### Technical Documentation (25%)

- **Excellent (A)**: Precise specifications, appropriate examples, comprehensive validation
- **Good (B)**: Clear technical details, most dependencies identified
- **Satisfactory (C)**: Basic technical information provided
- **Needs Improvement (D-F)**: Vague specifications, missing technical details

### GitHub Workflow (20%)

- **Excellent (A)**: Perfect branch naming, clear commits, responsive to feedback
- **Good (B)**: Good practices followed, minor issues in workflow
- **Satisfactory (C)**: Basic workflow understood and followed
- **Needs Improvement (D-F)**: Workflow violations, merge conflicts, poor practices

### Peer Review Participation (15%)

- **Excellent (A)**: Insightful feedback on 3+ PRPs, identifies strengths and improvements
- **Good (B)**: Constructive feedback on 2 PRPs
- **Satisfactory (C)**: Basic feedback provided on minimum required PRPs
- **Needs Improvement (D-F)**: Insufficient or unconstructive feedback

## The Five Core PRP Principles

1. **Context is King**: Include all necessary documentation, examples, and caveats upfront
2. **Validation Loops**: Provide executable tests that AI can run and fix iteratively
3. **Information Dense**: Use keywords and patterns directly from the codebase
4. **Progressive Success**: Start simple, validate, then enhance systematically
5. **Global Rules**: Apply project-wide standards across all implementations

## Resources

### PRP Templates and Examples
- `PRP-template/cole-medin-prp-template.md` - The official template
- `PRP-template/prp-example-basic.md` - Simple implementation example
- `PRP-template/prp-example-intermediate.md` - Multi-phase example
- `PRP-template/prp-example-advanced.md` - Complex system example

### Learning Materials
- `resources/context-engineering-guide.md` - Deep dive into context engineering
- `resources/validation-checklist.md` - PRP quality criteria
- `resources/common-patterns.md` - Frequently used PRP patterns

### Cole Medin's Resources
- [Context Engineering Introduction](https://github.com/coleam00/context-engineering-intro)
- [Archon Framework (PRP v3)](https://github.com/coleam00/Archon)
- [Original PRP Article](https://colemedin.com/prp-framework)

## Common Pitfalls to Avoid

### In Your PRPs
- ❌ Writing vague goals without specific outcomes
- ❌ Dumping documentation without highlighting relevant sections
- ❌ Creating validation gates without executable commands
- ❌ Omitting error handling and edge cases
- ❌ Assuming "obvious" context that isn't explicitly stated

### In Your Workflow
- ❌ Committing directly to main branch
- ❌ Creating PRs without descriptions
- ❌ Providing only superficial peer feedback
- ❌ Ignoring review comments
- ❌ Submitting without self-validation

## Tips for Success

### Writing Effective PRPs
1. **Be Specific**: Replace "implement authentication" with "implement JWT-based authentication with 1-hour token expiry"
2. **Curate Context**: Don't just link docs - explain what to look for
3. **Think Like an Implementer**: What would you need to know to build this?
4. **Test Your Validation**: Can someone actually run these commands?
5. **Iterate**: Great PRPs emerge from revision and refinement

### Providing Great Reviews
1. **Start with Strengths**: Identify what works well
2. **Be Specific**: Point to exact lines or sections
3. **Suggest Solutions**: Don't just identify problems
4. **Ask Questions**: Clarify ambiguities through discussion
5. **Stay Constructive**: Focus on the work, not the person

## Instructor Contact

For questions or assistance:
- Open an issue in this repository
- Contact via course communication channels
- Office hours: [Specified by instructor]

## License

This educational material is provided under the MIT License. Students retain ownership of their individual PRP submissions.

## Acknowledgments

This exercise is based on Cole Medin's Product Requirement Prompts framework. Special thanks to Cole for pioneering the context engineering approach that makes AI-assisted development truly effective.

---

*Remember: The goal isn't just to complete the exercise, but to develop skills that will transform how you approach technical documentation and AI-assisted development in your future career.*