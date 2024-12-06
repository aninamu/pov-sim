build:
	docker build -t airlines .

run:
	docker run -p 8080:8080 --name airlines airlines 

stop:
	docker stop airlines
	make clean

clean:
	docker container rm airlines

.PHONY: build run stop clean
