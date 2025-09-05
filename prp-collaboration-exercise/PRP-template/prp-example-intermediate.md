# PRP: Collaborative Todo List with Authentication

*PRP Version: 1.0*  
*Example: Intermediate Level*

## GOAL
Build a web-based collaborative todo list application with user authentication, real-time updates, and team workspaces where multiple users can manage shared task lists with role-based permissions.

## WHY
Remote teams struggle with task coordination across different time zones and tools. This application provides a centralized, real-time task management solution with clear ownership and progress tracking, reducing miscommunication and improving team productivity by 40%.

## WHAT
A full-stack web application using React frontend and Node.js backend with real-time WebSocket updates, JWT authentication, and PostgreSQL persistence.

### Functional Requirements
- User registration and authentication with email verification
- Create team workspaces with invite system
- CRUD operations for todo items with assignee tracking
- Real-time updates when team members modify todos
- Role-based access control (Admin, Member, Viewer)
- Due date tracking with notifications
- Todo categories and priority levels
- Activity log for audit trail
- Export todos to CSV/JSON

### Non-Functional Requirements
- Support 100 concurrent users per workspace
- Real-time updates within 500ms
- 99.9% uptime SLA
- GDPR compliance for user data
- Mobile-responsive design
- WCAG 2.1 AA accessibility standards

### Success Criteria
- [ ] User can register, verify email, and login with JWT tokens
- [ ] User can create workspace and invite team members via email
- [ ] Team members see todo updates in real-time without refresh
- [ ] Admins can manage user roles and permissions
- [ ] System handles 50 simultaneous todo updates without data loss
- [ ] All API endpoints respond within 200ms under normal load
- [ ] Application passes OWASP security checklist
- [ ] Mobile users can perform all desktop functions

## MUST READ - Context

### Official Documentation
- url: https://jwt.io/introduction
  why: JWT implementation for stateless authentication
  critical: Always verify token signature and expiration

- url: https://socket.io/docs/v4/
  why: WebSocket implementation for real-time updates
  critical: Handle reconnection and state synchronization

### Example Code
- file: examples/auth-middleware.js
  why: JWT verification middleware pattern
  gotchas: Check for token in both cookies and Authorization header

- file: examples/websocket-rooms.js
  why: Socket.io room management for workspaces
  gotchas: Clean up rooms when last user disconnects

### Internal Documentation
- doc: database/schema.sql
  section: User and Workspace Relations
  important: Many-to-many through workspace_members table

- doc: API_DESIGN.md
  section: RESTful Endpoints
  important: All endpoints except /auth/* require authentication

### Third-Party Resources
- resource: https://www.passportjs.org/packages/passport-jwt/
  version: 4.0.0
  why: Simplified JWT strategy for Express

- resource: https://github.com/dcodeIO/bcrypt.js
  version: 2.4.3
  why: Password hashing with salt rounds

## IMPLEMENTATION APPROACH

### Phase 1: Authentication Foundation [Estimated Time: 4 hours]

**Objective**: Implement secure user authentication system

1. **CREATE** backend/models/
   - User model with email, password_hash, verified, created_at
   - RefreshToken model for token rotation
   - EmailVerification model with token and expiry
   
2. **IMPLEMENT** backend/controllers/authController.js
   - register(): Hash password, create user, send verification email
   - login(): Validate credentials, generate JWT + refresh token
   - refresh(): Rotate refresh tokens
   - verify(): Mark email as verified
   - Error handling: Duplicate emails, invalid tokens

3. **CREATE** backend/middleware/auth.js
   - JWT verification middleware
   - Role checking middleware
   - Rate limiting for auth endpoints
   - PRESERVE: Public endpoints list

4. **SETUP** Email service
   - Configure SendGrid/SES for email delivery
   - HTML email templates for verification
   - Queue emails with retry logic

### Phase 2: Workspace & Todo Management [Estimated Time: 6 hours]

**Objective**: Build core todo functionality with team collaboration

1. **CREATE** Database schema
   ```sql
   - workspaces: id, name, owner_id, created_at
   - workspace_members: workspace_id, user_id, role, joined_at
   - todos: id, workspace_id, title, description, assignee_id, status, priority, due_date
   - todo_comments: id, todo_id, user_id, content, created_at
   - activity_logs: id, workspace_id, user_id, action, entity_type, entity_id, timestamp
   ```

2. **IMPLEMENT** backend/controllers/workspaceController.js
   - createWorkspace(): Initialize with owner as admin
   - inviteMembers(): Generate invite tokens, send emails
   - updateMemberRole(): Check admin permission
   - Follow pattern from: examples/rbac-controller.js

3. **CREATE** backend/controllers/todoController.js
   - CRUD operations with permission checks
   - Assign/reassign todos to members
   - Emit WebSocket events for real-time updates
   - Batch operations for bulk updates

4. **IMPLEMENT** WebSocket handlers
   - Connection authentication with JWT
   - Join workspace rooms on connection
   - Broadcast todo changes to room members
   - Handle disconnection gracefully

### Phase 3: Frontend Implementation [Estimated Time: 5 hours]

**Objective**: Build responsive React UI with real-time updates

1. **CREATE** React application structure
   ```
   src/
   ├── components/
   │   ├── Auth/ (Login, Register, VerifyEmail)
   │   ├── Workspace/ (WorkspaceList, WorkspaceDetail, InviteModal)
   │   ├── Todo/ (TodoList, TodoItem, TodoForm, TodoDetail)
   │   └── Common/ (Header, Sidebar, ErrorBoundary)
   ├── contexts/ (AuthContext, WorkspaceContext, SocketContext)
   ├── hooks/ (useAuth, useWebSocket, useWorkspace)
   └── services/ (api.js, websocket.js)
   ```

2. **IMPLEMENT** Authentication flow
   - Protected routes with React Router
   - Token refresh on 401 responses
   - Persistent login with secure storage
   - Email verification flow

3. **CREATE** Real-time todo interface
   - Optimistic UI updates
   - Conflict resolution for simultaneous edits
   - Offline queue for actions
   - Visual indicators for real-time changes

4. **IMPLEMENT** Responsive design
   - Mobile-first CSS Grid/Flexbox
   - Touch gestures for mobile
   - Progressive enhancement
   - Accessibility with ARIA labels

### Phase 4: Production Readiness [Estimated Time: 3 hours]

**Objective**: Security hardening and performance optimization

1. **SECURITY** improvements
   - Input sanitization for XSS prevention
   - SQL injection prevention with parameterized queries
   - Rate limiting on all endpoints
   - CORS configuration for production domain
   - Security headers (Helmet.js)

2. **OPTIMIZE** performance
   - Database indexing on foreign keys
   - Redis caching for session data
   - CDN for static assets
   - Lazy loading for React components
   - WebSocket connection pooling

3. **ADD** monitoring
   - Error tracking with Sentry
   - Performance monitoring with New Relic
   - Logging with Winston
   - Health check endpoints

## VALIDATION GATES

### Automated Testing
```bash
# Backend tests
npm run test:backend -- --coverage

# Frontend tests
npm run test:frontend -- --watchAll=false

# E2E tests
npm run test:e2e

# Load testing
npm run test:load -- --users=100 --duration=300
```

### Security Validation
```bash
# Dependency vulnerabilities
npm audit

# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py -t http://localhost:3000

# SQL injection testing
sqlmap -u "http://localhost:3000/api/todos" --headers="Authorization: Bearer TOKEN"
```

### Performance Validation
```bash
# API response times
artillery run tests/performance/api-load.yml

# WebSocket stress test
npm run test:websocket -- --connections=500

# Frontend lighthouse
lighthouse http://localhost:3000 --output=json --output-path=./lighthouse.json
```

### Manual Verification Checklist
- [ ] Create account, verify email, login successful
- [ ] Create workspace, invite user, accept invitation
- [ ] Create todo, see real-time update on another browser
- [ ] Assign todo to team member, verify notification
- [ ] Change user role, verify permission changes
- [ ] Test on mobile device (iOS and Android)
- [ ] Verify accessibility with screen reader
- [ ] Test offline mode and sync when reconnected

## DEPENDENCIES

### Backend Dependencies
```json
{
  "express": "^4.18.0",
  "socket.io": "^4.5.0",
  "jsonwebtoken": "^9.0.0",
  "bcryptjs": "^2.4.3",
  "pg": "^8.10.0",
  "sequelize": "^6.30.0",
  "nodemailer": "^6.9.0",
  "helmet": "^7.0.0",
  "express-rate-limit": "^6.7.0",
  "joi": "^17.9.0"
}
```

### Frontend Dependencies
```json
{
  "react": "^18.2.0",
  "react-router-dom": "^6.10.0",
  "socket.io-client": "^4.5.0",
  "axios": "^1.3.0",
  "react-query": "^3.39.0",
  "tailwindcss": "^3.3.0",
  "react-hot-toast": "^2.4.0"
}
```

### Environment Variables
```bash
# Backend
NODE_ENV=production
PORT=3000
DATABASE_URL=postgresql://user:pass@localhost:5432/tododb
JWT_SECRET=long-random-string-here
JWT_REFRESH_SECRET=another-long-random-string
REDIS_URL=redis://localhost:6379
EMAIL_API_KEY=sendgrid-api-key
FRONTEND_URL=https://app.example.com

# Frontend
REACT_APP_API_URL=https://api.example.com
REACT_APP_WS_URL=wss://api.example.com
```

## ROLLBACK PLAN

If deployment causes issues:

1. **Immediate Actions**
   - Revert to previous Docker image tag
   - Restore database from hourly backup
   - Clear Redis cache
   - Notify users via status page

2. **Data Recovery**
   - Database backups every hour to S3
   - Point-in-time recovery for last 7 days
   - Export critical data before major updates

3. **Communication**
   - Update status.example.com
   - Send email to affected workspace admins
   - Post in #incidents Slack channel

## NOTES FOR IMPLEMENTER

### Known Challenges
- WebSocket scaling requires sticky sessions or Redis adapter
- Email verification tokens should expire after 24 hours
- Safari may have issues with third-party cookies for JWT

### Optimization Opportunities
- Implement Redis pub/sub for horizontal WebSocket scaling
- Add GraphQL for more efficient data fetching
- Implement virtual scrolling for large todo lists
- Add push notifications for mobile apps

### Future Considerations
- OAuth integration (Google, GitHub)
- Mobile apps (React Native)
- Webhook integrations for external tools
- AI-powered task prioritization
- Time tracking and reporting features

---

*This intermediate example demonstrates multi-phase implementation with authentication, real-time features, and production considerations following Cole Medin's PRP framework.*