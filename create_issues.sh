#!/bin/bash

# Function to create an issue with delay
create_issue() {
    gh issue create "$@"
    sleep 2  # Add 2-second delay between issue creation
}

# Create labels using the API
gh api repos/:owner/:repo/labels -f name="epic" -f color="3E4B9E" -f description="Large, high-level feature grouping"
gh api repos/:owner/:repo/labels -f name="foundation" -f color="0E8A16" -f description="Foundation setup tasks"
gh api repos/:owner/:repo/labels -f name="email-infrastructure" -f color="D93F0B" -f description="Email infrastructure tasks"
gh api repos/:owner/:repo/labels -f name="api" -f color="1D76DB" -f description="API development tasks"
gh api repos/:owner/:repo/labels -f name="monitoring" -f color="5319E7" -f description="Monitoring and logging tasks"
gh api repos/:owner/:repo/labels -f name="testing" -f color="FBCA04" -f description="Testing and QA tasks"
gh api repos/:owner/:repo/labels -f name="deployment" -f color="B60205" -f description="Deployment related tasks"
gh api repos/:owner/:repo/labels -f name="security" -f color="FF0000" -f description="Security related tasks"
gh api repos/:owner/:repo/labels -f name="performance" -f color="006B75" -f description="Performance related tasks"

# Create milestones with proper date format
gh api repos/:owner/:repo/milestones -f title="Foundation Complete" -f due_on="2024-02-17T00:00:00Z" -f description="Complete foundation setup phase"
gh api repos/:owner/:repo/milestones -f title="Email Infrastructure Ready" -f due_on="2024-03-03T00:00:00Z" -f description="Complete email infrastructure phase"
gh api repos/:owner/:repo/milestones -f title="API Feature Complete" -f due_on="2024-03-17T00:00:00Z" -f description="Complete API development phase"
gh api repos/:owner/:repo/milestones -f title="Monitoring System Ready" -f due_on="2024-03-31T00:00:00Z" -f description="Complete monitoring setup phase"
gh api repos/:owner/:repo/milestones -f title="Testing Complete" -f due_on="2024-04-14T00:00:00Z" -f description="Complete testing phase"
gh api repos/:owner/:repo/milestones -f title="Production Launch" -f due_on="2024-04-28T00:00:00Z" -f description="Complete production deployment"

# Epic 1: Foundation Setup
create_issue --title "Epic: Foundation Setup" --label "epic,foundation" --body "Initial project setup and core infrastructure implementation

Timeline: Weeks 1-2

Includes:
- Project repository setup
- CI/CD pipeline configuration
- Database schema design
- Basic API structure"

create_issue --title "Project Repository Setup" --label "foundation" --milestone "Foundation Complete" --body "Tasks:
- Initialize repository
- Configure development environment
- Set up basic project structure
- Set up dependency management"

create_issue --title "CI/CD Pipeline Configuration" --label "foundation" --milestone "Foundation Complete" --body "Tasks:
- Set up GitHub Actions
- Configure Docker builds
- Implement deployment workflow
- Set up testing pipeline"

create_issue --title "Database Schema Design" --label "foundation" --milestone "Foundation Complete" --body "Tasks:
- Design core tables
- Create migrations
- Implement models
- Set up database connections"

create_issue --title "Basic API Structure" --label "foundation,api" --milestone "Foundation Complete" --body "Tasks:
- Set up FastAPI application
- Implement basic routing
- Add authentication framework
- Set up API documentation"

# Epic 2: Email Infrastructure
create_issue --title "Epic: Email Infrastructure" --label "epic,email-infrastructure" --body "Setting up core email sending capabilities

Timeline: Weeks 3-4

Includes:
- Postfix server setup
- Email security implementation
- Queue system implementation
- Retry and error handling"

create_issue --title "Postfix Server Setup" --label "email-infrastructure" --milestone "Email Infrastructure Ready" --body "Tasks:
- Install and configure Postfix
- Set up DKIM signing
- Configure SPF
- Basic email sending tests"

create_issue --title "Email Security Implementation" --label "email-infrastructure,security" --milestone "Email Infrastructure Ready" --body "Tasks:
- Implement DMARC policies
- Set up TLS
- Configure security policies
- Security testing"

create_issue --title "Queue System Implementation" --label "email-infrastructure" --milestone "Email Infrastructure Ready" --body "Tasks:
- Set up Redis
- Implement job queuing
- Add rate limiting
- Queue monitoring"

create_issue --title "Retry and Error Handling" --label "email-infrastructure" --milestone "Email Infrastructure Ready" --body "Tasks:
- Implement retry mechanism
- Set up dead letter queue
- Add failure handling
- Error reporting"

# Epic 3: API Development
create_issue --title "Epic: API Development" --label "epic,api" --body "Implementing core and advanced API features

Timeline: Weeks 5-6

Includes:
- Core email endpoints
- Advanced email features
- Analytics implementation"

create_issue --title "Core Email Endpoints" --label "api" --milestone "API Feature Complete" --body "Tasks:
- Implement send email endpoint
- Add template management
- Handle attachments
- API documentation"

create_issue --title "Advanced Email Features" --label "api" --milestone "API Feature Complete" --body "Tasks:
- Add batch sending
- Implement scheduling
- Create webhook system
- Feature testing"

create_issue --title "Analytics Implementation" --label "api" --milestone "API Feature Complete" --body "Tasks:
- Add tracking endpoints
- Implement statistics
- Create reporting system
- Dashboard integration"

# Epic 4: Monitoring & Logging
create_issue --title "Epic: Monitoring & Logging" --label "epic,monitoring" --body "Setting up comprehensive monitoring and logging

Timeline: Weeks 7-8

Includes:
- Prometheus setup
- Grafana implementation
- Logging system"

create_issue --title "Prometheus Setup" --label "monitoring" --milestone "Monitoring System Ready" --body "Tasks:
- Install Prometheus
- Configure metrics
- Set up alerting
- Integration testing"

create_issue --title "Grafana Implementation" --label "monitoring" --milestone "Monitoring System Ready" --body "Tasks:
- Install Grafana
- Create dashboards
- Configure alerts
- Dashboard testing"

create_issue --title "Logging System" --label "monitoring" --milestone "Monitoring System Ready" --body "Tasks:
- Set up structured logging
- Implement log aggregation
- Configure retention
- Log analysis tools"

# Epic 5: Testing & Optimization
create_issue --title "Epic: Testing & Optimization" --label "epic,testing" --body "Comprehensive testing and performance optimization

Timeline: Weeks 9-10

Includes:
- Test suite implementation
- Load testing
- Performance optimization"

create_issue --title "Test Suite Implementation" --label "testing" --milestone "Testing Complete" --body "Tasks:
- Add unit tests
- Create integration tests
- Implement E2E tests
- Set up CI testing"

create_issue --title "Load Testing" --label "testing,performance" --milestone "Testing Complete" --body "Tasks:
- Set up load testing
- Perform stress tests
- Document results
- Performance analysis"

create_issue --title "Performance Optimization" --label "performance" --milestone "Testing Complete" --body "Tasks:
- Optimize database queries
- Improve caching
- Tune configurations
- Performance monitoring"

# Epic 6: Deployment & Documentation
create_issue --title "Epic: Deployment & Documentation" --label "epic,deployment" --body "Production deployment and documentation finalization

Timeline: Weeks 11-12

Includes:
- Production environment setup
- Documentation completion
- Production launch"

create_issue --title "Production Environment" --label "deployment" --milestone "Production Launch" --body "Tasks:
- Set up production VPS
- Configure SSL/TLS
- Implement backup system
- Security hardening"

create_issue --title "Documentation Completion" --label "deployment,documentation" --milestone "Production Launch" --body "Tasks:
- Finalize all documentation
- Create user guides
- Write integration guides
- API documentation"

create_issue --title "Production Launch" --label "deployment" --milestone "Production Launch" --body "Tasks:
- Final security review
- Production deployment
- System verification
- Launch checklist" 