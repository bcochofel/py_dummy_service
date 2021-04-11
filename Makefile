app_name = py-dummy-service

test:
	# pytest
	coverage run -m pytest

report:
	coverage report

build:
	@docker build -t $(app_name) .

run:
	docker run --detach -p 8080:8080 $(app_name)

kill:
	@echo "Killing container..."
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker stop