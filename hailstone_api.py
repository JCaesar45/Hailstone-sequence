import http.server
import json
import urllib.parse
from functools import lru_cache

class HailstoneHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/hailstone':
            params = urllib.parse.parse_qs(parsed_path.query)
            limit_param = params.get('limit', [None])[0]
            
            if limit_param is None:
                self.send_error(400, "Missing 'limit' parameter")
                return

            try:
                limit = int(limit_param)
            except ValueError:
                self.send_error(400, "'limit' must be an integer")
                return

            if limit < 1:
                self.send_error(400, "'limit' must be a positive integer")
                return

            result = self.calculate_longest_sequence(limit)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    @staticmethod
    @lru_cache(maxsize=None)
    def sequence_length(n):
        if n == 1:
            return 1
        if n % 2 == 0:
            return 1 + HailstoneHandler.sequence_length(n // 2)
        else:
            return 1 + HailstoneHandler.sequence_length(3 * n + 1)

    def calculate_longest_sequence(self, limit):
        max_length = 0
        max_number = 0
        
        for i in range(1, limit):
            length = self.sequence_length(i)
            if length > max_length:
                max_length = length
                max_number = i
                
        return [max_number, max_length]

if __name__ == '__main__':
    server_address = ('', 8001)
    httpd = http.server.HTTPServer(server_address, HailstoneHandler)
    print('Hailstone API running on port 8001...')
    httpd.serve_forever()
