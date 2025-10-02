.PHONY: start stop restart logs build ps lint format

# Start the containers in detached mode
start:
	docker-compose up -d

# Stop the containers and remove network
stop:
	docker-compose down

# Restart containers
restart: stop start

# Build or rebuild services
build:
	docker-compose build

# Show container status
ps:
	docker-compose ps

# View logs (follow)
logs:
	docker-compose logs -f

# Check if code is properly formatted (fails if not)
lint:
	poetry run black --check .

# Auto-format code
format:
	poetry run black .
