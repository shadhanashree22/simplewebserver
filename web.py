from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<title>TOP SOFTWARE INDUSTRIES</title>
<body>
<table border="2" cellspacing="10" cellpadding="6" align="center" bg colour="lavender" width="1000">
<caption>Top Revenue Generating Software companies </caption>
<tr>
<th>Rank</th>
<th>Companies Name</th>
<th>Revenue</th>
<th>Headquarters</th>
</tr>
<tr>
<th>1</th>
<th>Microsoft</th>
<th>198.3 Billion </th>
<th>Redmond, Washington, US</th>
</tr>
<th>2</th>
<th>Google</th>
<th>282.11 Billion </th>
<th>Mountain View, California, US </th>
</tr>
<tr>
<th>3</th>
<th>IBM</th>
<th>77.89  Billion</th>
<th>Armonk, New York, US</th>
</tr>
<th>4</th>
<th>Oracle</th>
<th>39.6 Billion </th>
<th>Austin, Texas, US </th>
</tr>
<tr>
<th>5</th>
<th>SAP</th>
<th>29.1 Billion</th>
<th>Walldorf, Germany</th>
</tr>
<tr>
<th>6</th>
<th>PayPal</th>
<th>21.4 BIllion</th>
<th>San Jose, California US</th>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()