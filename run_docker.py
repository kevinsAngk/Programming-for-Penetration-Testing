import subprocess
import threading

def run_container(container_name, image_name):
    subprocess.run(["docker", "run", "--name", container_name, image_name])

if __name__ == "__main__":
    num_containers = 5
    image_name = "website-checker"
    subprocess.run(["docker", "build", "-t", image_name, "."])

    # Create and start threads for running containers
    threads = []
    for i in range(1, num_containers + 1):
        container_name = f"websitechecker{i}"
        thread = threading.Thread(target=run_container, args=(container_name, image_name))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
