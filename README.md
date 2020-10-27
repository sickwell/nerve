# Initial project, forked from:
https://github.com/PaytmLabs/nerve

# Upgrade:
* Scan speed increased more than x5 times by updating scan port_scanner.py in core:
      'unpriv_scan':'-PS --min-rate 5000 --max-retries 1 --open --host-timeout 1m',
      'priv_scan':'-PS --min-rate 5000 --max-retries 1 --open --host-timeout 1m -O'
* Now working with severity issue

# To Do:
* Integration for web scans with nuclei
* Disable non-used modules for internal scan (s3 buckets, domain takeovers & etc)
* Scalling feature for Network Topology
* Scan separation / network separation to prevent trash in topology

# Additional problems at Ubuntu server:
* sudo ufw allow 8080/tcp
