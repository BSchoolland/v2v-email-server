# Deployment Guide

## VPS Requirements

### Minimum System Requirements
- CPU: 2 cores
- RAM: 4GB
- Storage: 40GB SSD
- OS: Ubuntu 22.04 LTS

### Recommended System Requirements
- CPU: 4 cores
- RAM: 8GB
- Storage: 80GB SSD
- OS: Ubuntu 22.04 LTS

## Initial Server Setup

### System Updates
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y software-properties-common curl git
```

### Security Configuration
```bash
# Configure UFW
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 25/tcp
sudo ufw allow 587/tcp
sudo ufw enable

# Setup fail2ban
sudo apt install -y fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

## Docker Setup

### Install Docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

### Install Docker Compose
```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## GitHub Actions Configuration

### Repository Secrets
Set up the following secrets in your GitHub repository:
- `VPS_HOST`: Your VPS IP address
- `VPS_USERNAME`: SSH username
- `VPS_SSH_KEY`: SSH private key
- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub password

### Workflow Configuration
```yaml
name: Deploy to VPS

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push Docker images
        run: |
          docker-compose build
          docker-compose push

      - name: Deploy to VPS
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USERNAME }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /opt/v2v-email-server
            git pull
            docker-compose pull
            docker-compose up -d
```

## SSL/TLS Configuration

### Install Certbot
```bash
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

### Obtain SSL Certificate
```bash
sudo certbot certonly --standalone -d mail.yourdomain.com
```

## DNS Configuration

### Required Records
```
# A Record
mail.yourdomain.com. IN A <VPS-IP>

# MX Record
yourdomain.com. IN MX 10 mail.yourdomain.com.

# SPF Record
yourdomain.com. IN TXT "v=spf1 ip4:<VPS-IP> -all"

# DKIM Record
mail._domainkey.yourdomain.com. IN TXT "v=DKIM1; k=rsa; p=<DKIM-PUBLIC-KEY>"

# DMARC Record
_dmarc.yourdomain.com. IN TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com"
```

## Monitoring Setup

### Prometheus Installation
```bash
docker-compose -f docker-compose.monitoring.yml up -d
```

### Grafana Configuration
1. Access Grafana at `https://mail.yourdomain.com:3000`
2. Import dashboard templates
3. Configure alert notifications

## Backup Configuration

### Automated Backups
```bash
# Create backup script
cat > /opt/backup-script.sh << 'EOF'
#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/opt/backups"

# Backup databases
docker-compose exec -T postgres pg_dump -U postgres v2v_email > "$BACKUP_DIR/db_$TIMESTAMP.sql"

# Backup configurations
tar -czf "$BACKUP_DIR/configs_$TIMESTAMP.tar.gz" /opt/v2v-email-server/config

# Cleanup old backups (keep last 7 days)
find "$BACKUP_DIR" -type f -mtime +7 -delete
EOF

# Make script executable
chmod +x /opt/backup-script.sh

# Add to crontab
echo "0 2 * * * /opt/backup-script.sh" | sudo tee -a /var/spool/cron/crontabs/root
```

## Post-Deployment Verification

### Health Checks
1. Verify all services are running:
```bash
docker-compose ps
```

2. Check logs for errors:
```bash
docker-compose logs
```

3. Test email sending:
```bash
curl -X POST https://mail.yourdomain.com/api/v1/email/test \
  -H "Authorization: Bearer YOUR-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{"to": "test@example.com", "subject": "Test Email", "body": "Test content"}'
```

### Monitoring Checks
1. Verify Prometheus metrics
2. Check Grafana dashboards
3. Test alert notifications

## Troubleshooting

### Common Issues
1. Email Delivery Issues
   - Check Postfix logs
   - Verify DNS records
   - Check spam scores

2. Performance Issues
   - Monitor resource usage
   - Check database queries
   - Verify cache hit rates

3. Security Issues
   - Review fail2ban logs
   - Check SSL certificate status
   - Monitor authentication logs 