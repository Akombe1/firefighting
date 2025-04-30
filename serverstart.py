

# Step 2: Set up a basic HTTP server to serve the folder
from pyngrok import ngrok
import http.server
import socketserver
import threading

PORT = 8000
public_url = ngrok.connect(PORT)
print("🔗 Public URL:", public_url)

# Step 3: Serve the current directory (where heatmap.html is saved)
def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("🌐 Serving at port", PORT)
        httpd.serve_forever()

thread = threading.Thread(target=start_server)
thread.start()
