# Programming-for-Penetration-Testing

# to run: python .\run_docker.py


1. run_docker.py
This Python script creates and runs Docker containers to check websites. It utilizes threading to spawn multiple containers concurrently.

![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/efa33b53-5713-4a3b-afe5-f1a742c9487b)

2. Dockerfile
The Dockerfile specifies the image for the website checker, based on python:3.8-slim. It installs the requests library and runs the http_flood.py script.

![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/f9b18e73-4e3f-4ec9-b9ba-3e1988696cb6)

3. http_flood.py
This Python script implements an HTTP flood attack by creating multiple threads to send repeated requests to a target website.

![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/15ff020f-91f6-4d87-a90a-256f75cdfd78)
# create docker immage:
![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/9aecf154-a934-4479-a2b4-87af4f90b714)
![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/1091604c-ba37-4aae-a38c-0e0369935fcb)


# create 2 docker container:
![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/12919ce5-4054-4711-9b0b-08c0f9b10c47)
![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/cb093916-df72-4757-9879-a04deb3e4ba5)

![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/31f9139c-aa9d-4abd-9f7a-97cdefd86b75)


# Spawn 5 threads for HTTP flood attack
![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/3e1b6828-50a7-402c-ac0e-d4283954a4ae)


![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/a18abd2b-5abf-423f-8669-39376ced2e12)


![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/15872850-2561-4daf-866e-307a0899184c)

# ipv4 stat:
![image](https://github.com/kevinsAngk/Programming-for-Penetration-Testing/assets/79265592/7acf61a3-82f6-4539-8791-2c93379cca05)


