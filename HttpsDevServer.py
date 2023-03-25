#!/usr/bin/python
import http.server
import ssl
from pathlib import Path
from sys import argv
from os import chdir, getcwd
from functools import partial
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-c", "--cert", default="./ssl/cert.pem", help="SSL Certificate path, defaults to: ./ssl/cert.pem")
parser.add_argument("-k", "--key", default="./ssl/cert.key", help="SSL certificate private key, defaults to: ./ssl/cert.key")
parser.add_argument("-d", "--dir", default=".", help="Webroot directory")
parser.add_argument("-p", "--port", default="8443", help="Port that the page is served on", type=int)
args = parser.parse_args()

hostname = "localhost"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_verify_locations(args.cert)
context.verify_mode = ssl.CERT_OPTIONAL
context.load_cert_chain(args.cert, args.key)

httpd = http.server.HTTPServer(('0.0.0.0', args.port), partial(http.server.SimpleHTTPRequestHandler, directory=args.dir))
httpd.socket = context.wrap_socket(httpd.socket, server_hostname=hostname)

print(f"Serving {args.dir} on port {args.port}")

httpd.serve_forever()