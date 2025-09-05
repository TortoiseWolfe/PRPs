# Student PRP Submissions

This directory contains all student PRP submissions for the collaboration exercise.

## Submission Guidelines

### File Naming Convention
Your PRP file must follow this naming pattern:
```
[github-username]-[exercise-name].md
```

Examples:
- `johndoe-recipe-app.md`
- `janesmith-todo-list.md`
- `alexchen-recommendation-engine.md`

### Directory Structure
Place your PRP file directly in this directory. Do not create subdirectories.

### Before Submitting

1. **Validate your PRP locally**:
   ```bash
   python ../scripts/validate_prp.py your-prp-file.md
   ```

2. **Check required sections**:
   ```bash
   python ../scripts/check_sections.py your-prp-file.md
   ```

3. **Verify markdown formatting**:
   ```bash
   python ../scripts/check_markdown.py your-prp-file.md
   ```

### Submission Process

1. Create your feature branch:
   ```bash
   git checkout -b prp/[your-username]/[exercise-name]
   ```

2. Add your PRP file to this directory

3. Commit with a descriptive message:
   ```bash
   git add student-PRPs/[your-file].md
   git commit -m "Add PRP for [exercise-name] by [your-name]"
   ```

4. Push your branch:
   ```bash
   git push origin prp/[your-username]/[exercise-name]
   ```

5. Create a pull request using the template

### Review Process

After submission:
1. Automated validation will run via GitHub Actions
2. You'll receive automated feedback in your PR
3. Address any validation errors
4. Wait for instructor/peer review
5. Respond to review comments
6. Make requested changes if needed

### Common Issues

- **Validation Failures**: Run validation locally before pushing
- **Wrong Directory**: Ensure file is in `student-PRPs/` directory
- **Naming Convention**: Follow the exact pattern specified
- **Missing Sections**: Use the template and include all sections
- **No PR Description**: Fill out the PR template completely

### Need Help?

- Review the example PRPs in `../PRP-template/`
- Consult the resources in `../resources/`
- Check your exercise instructions in `../exercises/`
- Ask questions in your pull request

Good luck with your PRP! 🚀