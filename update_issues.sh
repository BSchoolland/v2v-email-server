#!/bin/bash

# Function to update an issue
update_issue() {
    local issue_number=$1
    local body=$2
    gh issue edit $issue_number --body "$body"
    sleep 2  # Add delay between updates
}

# Update Epic 1 issues
update_issue 1 "Initial project setup and core infrastructure implementation

Timeline: Weeks 1-2

Includes:
- Project repository setup
- CI/CD pipeline configuration
- Database schema design
- Basic API structure"

update_issue 2 "Tasks:
- Initialize repository
- Configure development environment
- Set up basic project structure
- Set up dependency management"

update_issue 3 "Tasks:
- Set up GitHub Actions
- Configure Docker builds
- Implement deployment workflow
- Set up testing pipeline"

update_issue 4 "Tasks:
- Design core tables
- Create migrations
- Implement models
- Set up database connections"

update_issue 5 "Tasks:
- Set up FastAPI application
- Implement basic routing
- Add authentication framework
- Set up API documentation"

# Update Epic 2 issues
update_issue 6 "Setting up core email sending capabilities

Timeline: Weeks 3-4

Includes:
- Postfix server setup
- Email security implementation
- Queue system implementation
- Retry and error handling"

update_issue 7 "Tasks:
- Install and configure Postfix
- Set up DKIM signing
- Configure SPF
- Basic email sending tests"

update_issue 8 "Tasks:
- Implement DMARC policies
- Set up TLS
- Configure security policies
- Security testing"

update_issue 9 "Tasks:
- Set up Redis
- Implement job queuing
- Add rate limiting
- Queue monitoring"

update_issue 10 "Tasks:
- Implement retry mechanism
- Set up dead letter queue
- Add failure handling
- Error reporting"

# Update Epic 3 issues
update_issue 11 "Implementing core and advanced API features

Timeline: Weeks 5-6

Includes:
- Core email endpoints
- Advanced email features
- Analytics implementation"

update_issue 12 "Tasks:
- Implement send email endpoint
- Add template management
- Handle attachments
- API documentation"

update_issue 13 "Tasks:
- Add batch sending
- Implement scheduling
- Create webhook system
- Feature testing"

update_issue 14 "Tasks:
- Add tracking endpoints
- Implement statistics
- Create reporting system
- Dashboard integration"

# Update Epic 4 issues
update_issue 15 "Setting up comprehensive monitoring and logging

Timeline: Weeks 7-8

Includes:
- Prometheus setup
- Grafana implementation
- Logging system"

update_issue 16 "Tasks:
- Install Prometheus
- Configure metrics
- Set up alerting
- Integration testing"

update_issue 17 "Tasks:
- Install Grafana
- Create dashboards
- Configure alerts
- Dashboard testing"

update_issue 18 "Tasks:
- Set up structured logging
- Implement log aggregation
- Configure retention
- Log analysis tools"

# Update Epic 5 issues
update_issue 19 "Comprehensive testing and performance optimization

Timeline: Weeks 9-10

Includes:
- Test suite implementation
- Load testing
- Performance optimization"

update_issue 20 "Tasks:
- Add unit tests
- Create integration tests
- Implement E2E tests
- Set up CI testing" 