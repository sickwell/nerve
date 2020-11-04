# Initial project, forked from:
https://github.com/PaytmLabs/nerve

# Upgrade:
## Test1
* Scan speed increased more than x5 times by updating scan port_scanner.py in core but reduced detection 19/22 hosts identified:
      'unpriv_scan':'-PS --min-rate 5000 --max-retries 1 --open --host-timeout 1m',
      'priv_scan':'-PS --min-rate 5000 --max-retries 1 --open --host-timeout 1m -O'
## Test2
* Scan speed increased more than x2 times, 22/22 hosts:
      'unpriv_scan':'-sT --min-rate 5000 --max-retries 1 --open --host-timeout 1m',
      'priv_scan':'-sSVC --min-rate 5000 --max-retries 1 --open --host-timeout 1m -O'
## Test3
* Unpriv scan disabled, Priv_scan improved (maximum detect and fast), -O disabled since generating a falses:
      'priv_scan':'-n -PO --min-rate 5000 --max-retries 1 --open --host-timeout 1m'

could be also used: -PR -PO -PS -PA -PP -PM -PE
      
* Now working with severity issue

## To Do:
* Integration for web scans with nuclei
* Implement detection module in rules for easy-exploitable ports
* Disable non-used modules for internal scan (s3 buckets, domain takeovers & etc)
* Scalling feature for Network Topology
* Implement button to disable host in Network topology
* Scan separation / network separation to prevent trash in topology
* Setup python webhook

## Additional problems at Ubuntu server:
* sudo ufw allow 8080/tcp
* install discord_webhook https://pypi.org/project/Discord-Webhooks/#files
