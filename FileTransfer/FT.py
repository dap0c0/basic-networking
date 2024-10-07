#!/usr/bin/bash
import argparse
from FileTransferServer import FileTransferServer
from FileTransferClient import FileTransferClient

parser = argparse.ArgumentParser(description="Basic File Transfer in server-client model")

# Server mode and client mode are mutually exclusive
server_args = parser.add_argument_group()
server_args.add_argument("--server", "-S", action="store_true")
server_args.add_argument("--backlog", "-b", action="store", dest="backlog", type=int, default="1", required=False)
server_args.add_argument("--filepath", "-f", action="store", dest="filepath", type=str)

client_args = parser.add_argument_group()
client_args.add_argument("--client", "-C", action="store_true")
client_args.add_argument("--port", "-p", action="store", dest="port", type=int)
client_args.add_argument("--host", "-H", action="store", dest="host", type=str)
arguments = parser.parse_args()

# Server args
server = arguments.server
filepath = arguments.filepath
backlog = arguments.backlog

# Client args
client = arguments.client
port = arguments.port
host = arguments.host

# Server case
if server:
    if not filepath:
        print("Must provide filepath designation.")
    
    else:
        if backlog < 1:
            print("Backlog must be >= 1.")
        
        else:
            server = None

            if backlog == 1:
                server = FileTransferServer(filepath)

            else:
                server = FileTransferServer(filepath, backlog)
            
            server.send_file()

# Client case
elif client:
    if not port:
        parser.error("Must provide port designation.")

    if not host:
        parser.error("Must provide host designation.")

    else:
        ft_client = FileTransferClient(host, port)
        name, body = ft_client.receive_data()
        ft_client.write_data(name, body)

