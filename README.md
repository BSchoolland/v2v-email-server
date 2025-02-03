# V2V Email Server

A self-hosted email service infrastructure designed to handle email sending across multiple websites. This system provides a centralized, reliable, and scalable solution for managing email communications.

## Project Overview

This email server implementation provides:
- REST API for sending emails
- Email templating and management
- Delivery tracking and monitoring
- Rate limiting and queuing
- Bounce handling and feedback loops
- Comprehensive logging

## Technology Stack

- **Backend**: Python/FastAPI (chosen for async capabilities and type safety)
- **Database**: PostgreSQL (for email logs, templates, and tracking)
- **Queue**: Redis (for rate limiting and job queuing)
- **Email Server**: Postfix (as MTA)
- **Monitoring**: Prometheus + Grafana
- **CI/CD**: GitHub Actions
- **Container**: Docker

## Documentation Structure

- [`/docs/architecture.md`](docs/architecture.md) - System architecture and components
- [`/docs/deployment.md`](docs/deployment.md) - Deployment guide and VPS setup
- [`/docs/email-infrastructure.md`](docs/email-infrastructure.md) - Email server configuration
- [`/docs/api-spec.md`](docs/api-spec.md) - API documentation
- [`/docs/monitoring.md`](docs/monitoring.md) - Monitoring and alerting setup
- [`/docs/timeline.md`](docs/timeline.md) - Project implementation timeline
- [`/docs/challenges.md`](docs/challenges.md) - Key challenges and mitigation strategies
- [`/docs/dns-setup.md`](docs/dns-setup.md) - DNS configuration guide

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and configure environment variables
3. Run `docker-compose up` to start the development environment
4. Access the API documentation at `http://localhost:8000/docs`

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 