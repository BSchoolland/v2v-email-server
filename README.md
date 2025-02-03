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

## Development Setup

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- Git

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/v2v-email-server.git
cd v2v-email-server
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Start development services:
```bash
docker-compose up -d
```

6. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation will be at `http://localhost:8000/docs`

### Running Tests

```bash
# Run unit tests
pytest tests/unit

# Run integration tests
pytest tests/integration

# Run with coverage
pytest --cov=app tests/
```

### Code Quality

```bash
# Format code
black app tests

# Sort imports
isort app tests

# Lint code
flake8 app tests

# Type checking
mypy app
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 