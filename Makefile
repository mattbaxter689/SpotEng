up:
	docker compose --env-file ./.env up --build -d

down:
	docker compose --env-file .env down


run:
	docker exec spoteng python main.py

warehouse:
	docker exec -ti warehouse psql postgres://sdeuser:sdepassword1234@localhost:5432/warehouse

format:
	python -m black ./
	isort ./
