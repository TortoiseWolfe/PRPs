# Meta-PRP: Collaborative App Ideation Through GitHub Workflow

## PROJECT GOAL
Create a teaching exercise where students submit Product Requirement Prompts (PRPs) proposing what application the class should build together, while simultaneously learning GitHub branching, pull requests, and merging workflows. The instructor practices merge conflict resolution while students learn collaborative development through proposing, reviewing, and refining ideas.

## WHY
- **Dual Learning Objectives**: Students learn both PRP documentation AND GitHub collaboration in a meaningful context
- **Democratic Project Selection**: The class collectively decides what to build based on student interests and learning goals
- **Real-World Simulation**: Mimics actual product development where multiple stakeholders propose features and requirements
- **Instructor Skill Building**: Provides hands-on practice with merge conflicts and branch management

## WHAT
Students will each create a PRP on their own branch proposing either:
1. A completely unique application idea they want the class to build
2. Their vision for a commonly suggested app (likely with unique features)
3. Specific features or modifications to emerging consensus ideas

Through pull request reviews and discussions, the best ideas will "bubble up" and merge into a consensus PRP that defines what the class will actually build.

### Success Criteria
- [ ] Each student successfully creates and maintains their own branch
- [ ] All students submit a PRP following Cole Medin's template
- [ ] Instructor successfully merges all branches, resolving conflicts
- [ ] Class reaches consensus on application to build
- [ ] Final merged PRP represents best ideas from all submissions
- [ ] Students understand how their ideas influenced the final decision

## REPOSITORY STRUCTURE

```
class-app-prp/
├── README.md                          # Exercise instructions & current consensus
├── .github/
│   ├── pull_request_template.md      # PRP proposal template
│   └── DISCUSSIONS.md                 # Voting and consensus tracking
├── templates/
│   ├── cole-medin-prp-template.md    # Base PRP template
│   ├── example-todo-app-prp.md       # Example: Todo app proposal
│   ├── example-game-prp.md           # Example: Game proposal
│   └── example-data-viz-prp.md      # Example: Data viz proposal
├── proposals/                         # Where PRPs get merged
│   ├── README.md                     # Proposal guidelines
│   └── [student-name]-proposal.md    # Individual proposals after merge
├── consensus/
│   ├── current-consensus.md          # Living document of agreed features
│   ├── feature-votes.md              # Tracking popular features
│   └── rejected-ideas.md             # Ideas that didn't make it (with reasons)
└── resources/
    ├── prp-writing-guide.md          # How to write compelling PRPs
    ├── app-idea-prompts.md           # Inspiration for students
    └── learning-objectives.md        # What skills each app type teaches
```

## STUDENT WORKFLOW

### Phase 1: Initial Brainstorming (Week 1)
1. **Fork and Clone Repository**
   ```bash
   git clone https://github.com/[student]/class-app-prp.git
   cd class-app-prp
   ```

2. **Create Personal Proposal Branch**
   ```bash
   git checkout -b proposal/[github-username]/[app-name]
   # Example: proposal/johndoe/recipe-tracker
   ```

3. **Write Initial PRP Proposal**
   - Create `proposals/[username]-[appname]-proposal.md`
   - Follow Cole Medin's PRP template
   - Focus on:
     - What they want to learn by building this
     - Why this would benefit the whole class
     - Core features that teach important concepts
     - Technology stack preferences

### Phase 2: Submit and Discuss (Week 1-2)
1. **Push Branch and Create Pull Request**
   ```bash
   git add proposals/[username]-[appname]-proposal.md
   git commit -m "feat: propose [app name] for class project"
   git push origin proposal/[username]/[app-name]
   ```

2. **Pull Request Description Must Include:**
   - Brief elevator pitch (2-3 sentences)
   - Top 3 learning objectives addressed
   - Estimated complexity (beginner/intermediate/advanced)
   - Similar proposals they've reviewed

3. **Participate in Discussions**
   - Comment on at least 3 other proposals
   - Identify common themes
   - Suggest feature combinations
   - Vote using reactions (👍 for support)

### Phase 3: Consensus Building (Week 2)
1. **Update Proposals Based on Feedback**
   - Incorporate popular features from other PRPs
   - Modify scope based on class skill level
   - Align with emerging consensus

2. **Merge Strategies for Instructor**
   - Start with non-conflicting proposals
   - Group similar proposals together
   - Create merge commits showing evolution:
   ```bash
   git checkout main
   git merge --no-ff proposal/student1/todo-app -m "merge: student1's todo app proposal"
   git merge --no-ff proposal/student2/task-tracker -m "merge: student2's task tracker (similar to todo)"
   ```

3. **Handling Conflicts**
   - When proposals conflict, create a `consensus/conflicts/` directory
   - Document both versions
   - Hold class vote or discussion
   - Merge resolution into `consensus/current-consensus.md`

## INSTRUCTOR'S MERGING PLAYBOOK

### Strategy 1: Categorical Merging
Group proposals by app type and merge in waves:
```bash
# Wave 1: All todo/task/productivity apps
git checkout main
git merge proposal/alice/todo-app
git merge proposal/bob/task-tracker
git merge proposal/charlie/productivity-suite
# Resolve conflicts by combining features

# Wave 2: All game proposals
git merge proposal/diana/puzzle-game
git merge proposal/eric/trivia-app
# Create games-category.md with all game ideas

# Wave 3: Unique proposals
git merge proposal/frank/weather-viz
git merge proposal/grace/recipe-share
```

### Strategy 2: Feature Extraction
Instead of merging complete PRPs, extract features:
1. Create `consensus/features/` directory
2. Cherry-pick specific features from each proposal
3. Build consensus PRP from extracted features
4. Show students how their ideas contributed

### Strategy 3: Progressive Consensus
1. Merge most popular proposal first (most 👍 reactions)
2. Each subsequent merge adds features to consensus
3. Document evolution in git history
4. Final result shows contribution from everyone

## COLE MEDIN'S PRP TEMPLATE (Student Reference)

```markdown
# PRP: [Your App Name] - Class Project Proposal

## GOAL
[Describe what app you want the class to build and why it would be a good learning project]

## WHY
### Learning Objectives
- [ ] What will building this teach the class?
- [ ] What technologies will we learn?
- [ ] What real-world skills does this develop?

### Personal Interest
- Why are YOU excited about this project?
- What specific skills do you want to gain?

## WHAT
### Core Features (MVP)
1. [Feature 1 - essential for learning objective]
2. [Feature 2 - demonstrates key concept]
3. [Feature 3 - provides hands-on practice with X]

### Stretch Features (if time permits)
- [Advanced feature that could be added]
- [Integration with external service]
- [Performance optimization opportunity]

### Technology Stack Suggestion
- Frontend: [Your recommendation and why]
- Backend: [Your recommendation and why]
- Database: [Your recommendation and why]
- Testing: [Frameworks to learn]
- Deployment: [Platform to practice with]

## Success Criteria
- [ ] All students can contribute regardless of skill level
- [ ] Project can be completed in [timeline]
- [ ] Each student owns at least one feature
- [ ] App is actually useful/fun when complete
- [ ] We can demo this in our portfolios

## Similar Proposals
[After reviewing others, list proposals that align with yours]
- @username1's proposal: [How it relates]
- @username2's proposal: [Common features]
- Could be combined with: [Other proposals]
```

## CONSENSUS BUILDING MECHANICS

### Voting System
Use GitHub's built-in reactions for democratic selection:
- 👍 Support this proposal
- ❤️ Love this idea (counts as 2 votes)
- 🚀 This would challenge us (good complexity)
- 👀 Interesting but needs work
- 😕 Too complex/simple for our class
- 💭 Good features but different app preferred

### Conflict Resolution Process
When proposals conflict or diverge:

1. **Identify Conflict Type**
   - Different apps entirely → Vote for top 3, then final
   - Same app, different features → Combine feature sets
   - Different tech stacks → Instructor decides based on curriculum

2. **Document Decision Rationale**
   ```markdown
   ## Decision: [Feature/App/Stack chosen]
   ### Options Considered
   - Option A: [Description] (proposed by @user1, @user2)
   - Option B: [Description] (proposed by @user3)
   
   ### Decision Factors
   - Learning value: [Which teaches more]
   - Feasibility: [Which fits timeline]
   - Interest: [Vote counts]
   
   ### Final Decision
   We chose [X] because [reasoning]
   Ideas from [Y] will be incorporated as [stretch goals/future features]
   ```

3. **Preserve Rejected Ideas**
   - Move to `consensus/parking-lot.md`
   - Could become future projects
   - Students can pursue independently

## ASSESSMENT RUBRIC

### PRP Quality (40%)
- **Clarity of Vision** (10%): Is the app idea well-defined?
- **Learning Objectives** (10%): Are educational goals clear?
- **Feasibility** (10%): Is scope appropriate for class?
- **Template Compliance** (10%): Follows Cole Medin's structure?

### GitHub Workflow (30%)
- **Branch Management** (10%): Correct naming, clean commits
- **Pull Request Quality** (10%): Good description, links to issues
- **Merge Readiness** (10%): No conflicts, responds to feedback

### Collaboration (30%)
- **Peer Reviews** (10%): Constructive feedback on 3+ proposals
- **Consensus Building** (10%): Works toward common ground
- **Flexibility** (10%): Adapts proposal based on class needs

## TIMELINE

### Week 1: Ideation
- Day 1: Introduction to PRP format, review examples
- Day 2-3: Students write initial proposals
- Day 4-5: Submit PRs, begin peer reviews

### Week 2: Consensus
- Day 1-2: Review and discussion period
- Day 3: Instructor begins merging proposals
- Day 4: Resolve conflicts, vote on contentious items
- Day 5: Final consensus PRP published

### Week 3+: Build
- Class begins building the agreed-upon application
- Each student claims features from consensus PRP
- Continue using PR workflow for actual development

## EXAMPLE SCENARIOS

### Scenario 1: Convergent Ideas
Five students propose todo apps, three propose task trackers:
- Instructor merges all into `proposals/productivity-apps/`
- Creates unified `consensus/productivity-suite-prp.md`
- Combines best features from each proposal
- Credits all contributors in commit messages

### Scenario 2: Divergent Ideas
Students propose completely different apps:
- Hold "PRP Pitch Day" where students present
- Anonymous vote for top 3
- Finalists revise PRPs with features from others
- Final vote determines winner
- Runner-up ideas become "stretch features" or "v2 possibilities"

### Scenario 3: The Wild Card
One student proposes something unique and ambitious:
- Class discusses feasibility
- If too complex: extract innovative features for chosen app
- If brilliant: pivot entire class to support it
- Document why class chose to take the risk

## INSTRUCTOR TIPS

### Managing Merge Conflicts
1. **Intentionally Create Conflicts**: Have students edit same sections to practice resolution
2. **Merge Party**: Live-code conflict resolution in class
3. **Three-Way Merges**: Show how Git tracks changes from common ancestor
4. **Conflict Journal**: Document each conflict and resolution method

### Facilitating Consensus
- **Set Expectations**: "Not everyone's exact idea will win, but everyone's input matters"
- **Highlight Contributions**: Show how each PRP influenced final decision
- **Create Hybrids**: Combine complementary proposals into something better
- **Future Promises**: Parking lot ideas could become next semester's project

### Common Pitfalls to Avoid
- Don't let one strong personality dominate discussions
- Avoid "design by committee" → Designate final decision maker (you)
- Prevent scope creep → Lock consensus after Week 2
- Don't ignore quiet students → Actively solicit their input

## FINAL DELIVERABLE

By end of Week 2, the repository should contain:
1. **All Individual Proposals**: Merged into `proposals/` directory
2. **Consensus PRP**: Final agreed-upon project specification
3. **Decision Documentation**: How/why choices were made
4. **Contribution Map**: Which student contributed which ideas
5. **Implementation Plan**: Who builds what in coming weeks

The git history itself becomes a teaching artifact, showing how collaborative software development really works - messy, iterative, but ultimately convergent through good process and communication.