#!/bin/bash
nohup redis-server --port 7001 --bind 127.0.0.1 & &> /dev/null
/usr/bin/python3 main.py
