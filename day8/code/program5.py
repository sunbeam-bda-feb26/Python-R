# flask
# - used to create backend (program running on the server) of the application
# - used to create a REST API Server or REST web services

# web architecture
# - uses client-server architecture and request and response pattern

# web application or website
# - the one which has the UI
# - python: django is used to develop the web applications

# web service
# - the one which does not have UI but returns the data (JSON format)
# - python: flask is used to develop the web services

# REST
# - representational state transfer
# - is a design pattern used to get the data in JSON format and not the UI
# - uses 
#   - JSON to communicate with client and server
#   - http methods
#   - http request and response 
# - alternatives
#   - SOAP: simple object access protocol - deprecated
#   - GraphQL: Graph Query Language
#   - socket: used to communicate with other process using port directly
#   - rpc: remote procedure call

# request
# - used to send the parameters from client to server
# - created by client and processed by the server
# - there are two parts
#   - header
#     - contains: 
#       - from url: scheme, domain name/ip address, port, file/path, query string
#       - method: used to instruct the server what operation needs to be performed
#         - GET: used to get some resource(s) from server
#         - POST: used to send some resource(s) to the server
#         - PUT: used to update existing resource on the server
#         - PATCH: used to partial update existing resource on the server
#         - DELETE: used to delete a resource from the server
#   - body: used to send extra parameters while sending the request with POST and PUT methods

# response
# - used to send the requested contents to the client
# - created by the server to carry the contents to the client
# - has two parts
#   - header
#     - status code:
#       - used to instruct the client how to intepret the response
#       - types
#         - 1xx: debugging or informational response (not used in production)
#         - 2xx: success 
#         - 3xx: redirection (from one domain to another domain)
#         - 4xx: client error
#         - 5xx: server error
#     - content type:
#     - content length:
#   - body
#     - contains the requested contents

# server
# - application or process or program or software
# - runs continuously for handling a type of requests
# - types
#   - web server
#     - used to handle the web requests
#     - e.g. apache, nginx, flask, express, IIS
#   - database server
#     - used to persist the data
#     - types
#       - RDBMS: MySQL, SQL Server, PostGre, Orable, DB2, SQLite
#       - NoSQL: MongoDB, Cassandra, Firebase, FireDB, Cockroach, Redis
#   - mail server
#     - smtp: e.g. postfix
#     - imap/pop: e.g. dovecot
#   - dns server
#     - used to map a domain name to an IP address
#     - e.g. bind
#   - file servers
#     - FTP: sftp
#     - NFS: Network File System
#     - SMB: Server Message Block

# import flask
from flask import Flask

# create a flask application
app = Flask(__name__)

# route
# - mapping between http method, path and handler (function)

# decorator
# - used to perform a task before the actual function gets executed

@app.route("/", methods=["GET"])
def root():
    return "<h1>welcome to flask server</h1>"

@app.route('/person', methods=['GET'])
def persons():
    return [{"name": "person1", "age": 30}, {"name": "person2", "age": 40}]

# start the server on a port 5600
app.run(host="0.0.0.0", port=5600, debug=True)
