#!/usr/bin/python
from quixote.publish import Publisher
from quixote.server.scgi_server import QuixoteHandler
from scgi.quixote_handler import main

from threadex.program_interface import RootDirectory
	
pname = 'threadex'
pnum = 4005

script_name = '/%s'%pname

def create_publisher():
	return Publisher(RootDirectory(),error_log="thrdx_err.log",access_log="thrdx_acc.log",display_exceptions="plain" )

def create_handler(parent_fd):
	return QuixoteHandler (parent_fd, create_publisher, script_name)

if __name__ == '__main__':
    main(create_handler)
