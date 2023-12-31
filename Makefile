#!make
include .env

.PHONY: migrate migrate-down migrate-fix

up:
	docker compose up -d

down:
	docker compose down

migration:
	migrate create -seq -ext sql -dir db/migrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	migrate -path db/migrations -database "postgres://${DB_USER}:${DB_PWD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?${DB_SSL}" up $(filter-out $@,$(MAKECMDGOALS))

migrate-down:
	migrate -path db/migrations -database "postgres://${DB_USER}:${DB_PWD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?${DB_SSL}" down $(filter-out $@,$(MAKECMDGOALS))

migrate-fix:
	migrate -path db/migrations -database "postgres://${DB_USER}:${DB_PWD}@${DB_HOST}:${DB_PORT}/${DB_NAME}?${DB_SSL}" force $(filter-out $@,$(MAKECMDGOALS))
