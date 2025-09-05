# PRP: Recipe Storage Application

*PRP Version: 1.0*  
*Example: Basic Level*

## GOAL
Build a command-line recipe storage application that allows users to create, read, update, and delete recipes with ingredients and instructions, storing data persistently in JSON format.

## WHY
Home cooks need a simple, offline solution to organize their recipe collection without relying on complex web applications or subscription services. This tool provides instant access to personal recipes from the terminal.

## WHAT
A Python CLI application that manages recipe data with full CRUD operations, search functionality, and data persistence.

### Functional Requirements
- Create new recipes with title, ingredients, and instructions
- View all recipes or individual recipe details
- Update existing recipes
- Delete recipes
- Search recipes by title or ingredient
- Export recipes to markdown format

### Non-Functional Requirements
- Start-up time under 100ms
- Support for 1000+ recipes without performance degradation
- Human-readable JSON storage format
- Cross-platform compatibility (Windows/Mac/Linux)

### Success Criteria
- [ ] User can create a recipe with title, ingredients list, and step-by-step instructions
- [ ] User can view a list of all recipe titles
- [ ] User can search recipes by ingredient
- [ ] Recipes persist between application sessions
- [ ] Application handles invalid input gracefully
- [ ] All CRUD operations complete successfully

## MUST READ - Context

### Official Documentation
- url: https://docs.python.org/3/library/json.html
  why: JSON serialization for recipe storage
  critical: Use indent parameter for human-readable output

### Example Code
- file: examples/cli_app.py
  why: Command-line argument parsing pattern using argparse
  gotchas: Remember to handle missing arguments gracefully

### Internal Documentation
- doc: https://click.palletsprojects.com/en/8.1.x/
  section: Building Command Line Applications
  important: Click provides better UX than argparse for interactive CLIs

## IMPLEMENTATION APPROACH

### Phase 1: Foundation [Estimated Time: 2 hours]

**Objective**: Set up project structure and data models

1. **CREATE** src/models.py
   - Define Recipe dataclass with id, title, ingredients, instructions, created_at
   - Implement to_dict() and from_dict() methods for serialization
   
2. **CREATE** src/storage.py
   - Implement JSONStorage class with load() and save() methods
   - Handle file not found gracefully with empty recipe list
   - Use pathlib for cross-platform file paths

3. **IMPLEMENT** data validation
   - Ensure recipe titles are unique
   - Validate required fields are present
   - Error handling: FileNotFoundError, JSONDecodeError

### Phase 2: Core Features [Estimated Time: 3 hours]

**Objective**: Implement CRUD operations and search

1. **CREATE** src/recipe_manager.py
   - Implement RecipeManager class with storage instance
   - Methods: add_recipe(), get_recipe(), update_recipe(), delete_recipe()
   - Method: search_recipes(query, search_in=['title', 'ingredients'])

2. **CREATE** src/cli.py
   - Use Click for command-line interface
   - Commands: add, list, view, update, delete, search
   - Interactive prompts for multi-line input (instructions)

3. **INTEGRATE** components
   - Wire CLI commands to RecipeManager methods
   - Format output with rich or tabulate for better display
   - Add confirmation prompts for destructive operations

### Phase 3: Polish and Validation [Estimated Time: 1 hour]

**Objective**: Add export functionality and improve UX

1. **EXTEND** recipe export feature
   - Add export_to_markdown() method
   - Include recipe metadata in export
   - Support bulk export of all recipes

2. **ENHANCE** user experience
   - Add colored output for success/error messages
   - Implement recipe duplicate detection
   - Add "recent recipes" quick access feature

## VALIDATION GATES

### Automated Testing
```bash
# Run all tests
pytest tests/ -v

# Test coverage
pytest --cov=src tests/
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint
pylint src/

# Type hints
mypy src/ --ignore-missing-imports
```

### Manual Verification Checklist
- [ ] Create a recipe and verify it persists after restart
- [ ] Search finds recipes by partial ingredient match
- [ ] Update preserves other recipe fields
- [ ] Delete removes recipe from storage
- [ ] Invalid JSON in storage file handled gracefully
- [ ] Export creates valid markdown file

## DEPENDENCIES

### Required Libraries/Packages
```
click==8.1.0  # CLI framework
pytest==7.4.0  # Testing
black==23.0.0  # Code formatting
rich==13.0.0  # Terminal formatting
```

### Environment Variables
```bash
RECIPE_STORAGE_PATH  # Optional: Override default ~/.recipes/data.json
```

## ROLLBACK PLAN

If implementation fails:

1. **Immediate Actions**
   - Restore backup of recipes.json from ~/.recipes/backup/

2. **Data Recovery**
   - JSON files are human-readable, can be manually edited
   - Provide migration script for data format changes

## NOTES FOR IMPLEMENTER

### Known Challenges
- Multi-line input for instructions requires special handling in CLI
- Windows may require different path handling for home directory

### Optimization Opportunities
- Could add caching layer for frequent searches
- Recipe tags/categories would enhance organization

### Future Considerations
- Web API for remote access
- Import from common recipe website formats
- Nutritional information integration

---

*This basic example demonstrates PRP structure for a simple CLI application with clear requirements and straightforward implementation path.*