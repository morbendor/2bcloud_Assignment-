import http.server
import socketserver
import os
import threading

location = os.path.dirname(__file__)
print(location)
os.chdir(location)



def start_server():
    PORT = 8081
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()

t = threading.Thread(target = start_server)
t.start()
