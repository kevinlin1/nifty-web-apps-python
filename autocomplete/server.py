from json import dumps
from random import seed

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs

from autocomplete import all_matches, city_weights

if __name__ == "__main__":
    class Handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path.startswith("/query"):
                query_string = self.path[len("/query?"):]
                s = parse_qs(query_string, keep_blank_values=True)["s"][0]
                if not s:
                    self.send("application/json", {"items": []})
                else:
                    # Step 1: Return the top 5 matches as a JSON object (dict)
                    result = all_matches(s)[:5]
                    self.send("application/json", {"items": result})
            elif self.path.startswith("/random"):
                # Step 2: Remove this API endpoint
                self.send("application/json", {"items": result})
            else:
                # Serve local files such as index.html
                super().do_GET()

        def send(self, content_type, data):
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(dumps(data).encode("utf-8"))

        def log_message(self, format, *args):
            # Silence log messages
            return

    seed(1 + 0x43)
    # Create an HTTPServer listening on port 8000
    with HTTPServer(("", 8000), Handler) as httpd:
        httpd.serve_forever()
