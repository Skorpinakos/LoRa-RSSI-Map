from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

class JSONHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        try:
            json_data = json.loads(body)
            self.save_json_to_file(json_data)
            
            #print(json_data)
            # You can process the JSON data here or save it to a file, database, etc.
            print("Received JSON data")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "success"}).encode('utf-8')
            self.wfile.write(response)
        except Exception as e:
            print('failed')
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "error", "message": str(e)}).encode('utf-8')
            self.wfile.write(response)
    def save_json_to_file(self, data):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        filename = f"{timestamp}.json"

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

def run_server():
    host = '0.0.0.0'
    port = 8000
    server_address = (host, port)

    httpd = HTTPServer(server_address, JSONHandler)
    print(f"Server started on http://{host}:{port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    run_server()
