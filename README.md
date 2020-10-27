# Initial project, forked from:
https://github.com/PaytmLabs/nerve

## Upgrade:
# Test1
* Scan speed increased more than x5 times by updating scan port_scanner.py in core but reduced detection 19/22 hosts identified:
      'unpriv_scan':'-PS --min-rate 5000 --max-retries 1 --open --host-timeout 1m',
      'priv_scan':'-PS --min-rate 5000 --max-retries 1 --open --host-timeout 1m -O'
# Test2
* Scan speed increased more than x2 times, 22/22 hosts:
      'unpriv_scan':'-sT --min-rate 5000 --max-retries 1 --open --host-timeout 1m',
      'priv_scan':'-sSVC --min-rate 5000 --max-retries 1 --open --host-timeout 1m -O'
      
* Now working with severity issue

# To Do:
* Integration for web scans with nuclei
* Disable non-used modules for internal scan (s3 buckets, domain takeovers & etc)
* Scalling feature for Network Topology
* Scan separation / network separation to prevent trash in topology

# Additional problems at Ubuntu server:
* sudo ufw allow 8080/tcp
