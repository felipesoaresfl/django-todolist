version: "2.4"

services:
  postgres_local:
    image: "postgres:13.3-alpine"
    ports:
      - "5414:5432"
    env_file:
      - .env
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
