# Beginner Exercise: Recipe Storage Application

## Exercise Overview

**Difficulty**: Beginner  
**Estimated Time**: 2-3 hours  
**Prerequisites**: Basic programming knowledge, understanding of JSON

## Your Task

Create a PRP for a command-line recipe storage application that helps home cooks organize their recipe collection. This is a great first PRP because it has clear requirements, straightforward implementation, and doesn't require complex integrations.

## Background Scenario

You're working for "HomeChef Solutions," a company that creates tools for cooking enthusiasts. Market research shows that many home cooks have recipes scattered across notebooks, websites, and photos. They need a simple, offline solution to consolidate their recipes.

The product team has requested a command-line application as an MVP to validate the concept before building a full web application.

## Requirements Overview

### Core Features Required
1. **Create** new recipes with:
   - Title (required, unique)
   - Ingredients list (required)
   - Step-by-step instructions (required)
   - Prep time (optional)
   - Cook time (optional)
   - Servings (optional)
   - Tags/categories (optional)

2. **View** recipes:
   - List all recipe titles
   - View detailed recipe information
   - Search by title
   - Search by ingredient
   - Filter by tag/category

3. **Update** existing recipes:
   - Modify any field
   - Add/remove ingredients
   - Update instructions

4. **Delete** recipes:
   - Remove by title
   - Confirmation required

5. **Data Persistence**:
   - Store in JSON format
   - Human-readable file
   - Automatic save after changes

### Technical Constraints

- **Language**: Python 3.8+ or JavaScript (Node.js 16+)
- **No external databases** (use file system)
- **Command-line interface** (no GUI)
- **Cross-platform** (Windows, Mac, Linux)
- **Single user** (no multi-user support needed)

### Performance Requirements

- Application starts in under 1 second
- Search returns results in under 100ms for 1000 recipes
- No memory issues with 5000+ recipes

## Suggested PRP Structure Hints

### For the GOAL Section
Think about:
- What exactly is being built?
- What problem does it solve?
- What's the end state?

### For the WHY Section
Consider:
- Who are the users?
- What pain points exist?
- What value does this provide?
- Why command-line first?

### For the WHAT Section
Break down:
- All functional requirements
- Non-functional requirements
- Clear success criteria
- Edge cases to handle

### For Context
Research and include:
- JSON file handling best practices
- Command-line argument parsing
- Data validation approaches
- Error handling patterns

### For Implementation
Plan phases like:
1. Data model and storage
2. Core CRUD operations
3. Search functionality
4. User interface (CLI)
5. Error handling and validation

### For Validation
Include:
- Test commands
- Sample data for testing
- Performance benchmarks
- User acceptance criteria

## Deliverables

Your PRP should:

1. **Follow the Template**: Use the Cole Medin template structure
2. **Be Complete**: Address all requirements
3. **Be Specific**: No vague statements
4. **Include Context**: Help implementers succeed
5. **Define Tests**: Validation must be executable

## Evaluation Criteria

Your PRP will be evaluated on:

- **Completeness** (25%): All sections filled appropriately
- **Clarity** (25%): Requirements are unambiguous
- **Context Quality** (25%): Relevant resources and examples
- **Feasibility** (15%): Can be realistically implemented
- **Testing** (10%): Clear validation approach

## Example User Stories

To help you think about requirements:

```
As a home cook, I want to:
- Quickly add a new recipe I just tried
- Find all recipes that use chicken
- See all my dessert recipes
- Update a recipe after tweaking it
- Export my recipes to share with friends
```

## Common Pitfalls to Avoid

1. **Too Vague**: "Make it user-friendly" → Instead: "Provide clear error messages, confirm destructive actions, show progress indicators"

2. **Missing Error Cases**: What if:
   - File is corrupted?
   - Disk is full?
   - Recipe title already exists?
   - Invalid ingredients format?

3. **Assuming Knowledge**: Don't assume the implementer knows:
   - Your preferred CLI library
   - File storage location
   - JSON structure format
   - Error message style

4. **Incomplete Validation**: Include:
   - Specific test cases
   - Edge cases to test
   - Performance tests
   - Manual verification steps

## Bonus Challenges (Optional)

If you want to go beyond the basic requirements:

1. **Import/Export**: Add ability to import from common recipe formats
2. **Meal Planning**: Add weekly meal planning features
3. **Shopping List**: Generate shopping lists from selected recipes
4. **Scaling**: Adjust recipe quantities dynamically
5. **Nutrition**: Calculate nutritional information

## Resources

- [Python argparse documentation](https://docs.python.org/3/library/argparse.html)
- [Node.js Commander.js](https://github.com/tj/commander.js)
- [JSON Schema](https://json-schema.org/) for validation
- [Click (Python CLI framework)](https://click.palletsprojects.com/)

## Getting Started

1. Read through all requirements carefully
2. Review the PRP template and examples
3. Plan your approach before writing
4. Create your PRP in `student-PRPs/[username]-recipe-app.md`
5. Use the validation checklist to self-review
6. Submit via pull request

## Questions to Consider

Before starting your PRP, think about:

1. How will recipes be uniquely identified?
2. What's the JSON structure for storage?
3. How will search be implemented efficiently?
4. What commands will users type?
5. How will you handle data corruption?
6. What makes a good CLI user experience?

## Sample Interaction

Here's what the final application might look like:

```bash
$ recipe-manager add
Title: Chocolate Chip Cookies
Ingredients (comma-separated): flour, sugar, eggs, chocolate chips, butter
Instructions: Mix ingredients. Form cookies. Bake at 350F for 12 minutes.
Prep time (minutes): 15
Cook time (minutes): 12
Tags: dessert, cookies
✓ Recipe "Chocolate Chip Cookies" added successfully!

$ recipe-manager search --ingredient chocolate
Found 3 recipes with "chocolate":
1. Chocolate Chip Cookies
2. Chocolate Cake
3. Hot Chocolate

$ recipe-manager view "Chocolate Chip Cookies"
=================================
Chocolate Chip Cookies
=================================
Prep: 15 min | Cook: 12 min
Tags: dessert, cookies

Ingredients:
- flour
- sugar
- eggs
- chocolate chips
- butter

Instructions:
Mix ingredients. Form cookies. Bake at 350F for 12 minutes.
```

## Success Tips

1. **Start Simple**: Get basic CRUD working first
2. **Think Like a User**: What would frustrate you?
3. **Be Specific**: Vague requirements lead to implementation issues
4. **Test Your Logic**: Can someone follow your plan?
5. **Review Examples**: Learn from the provided example PRPs

Remember: The goal is to create a PRP so comprehensive that an implementer (human or AI) can build the application without asking you any questions!

Good luck with your first PRP! 🚀