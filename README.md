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
* ~~Integration for web scans with nuclei
* Implement detection module in rules for easy-exploitable ports
* ~~Disable non-used modules for internal scan (s3 buckets, domain takeovers & etc)
* Scalling feature for Network Topology
* Implement button to disable host in Network topology
* Scan separation / network separation to prevent trash in topology
* ~~Setup webhook with discord

## Additional problems at Ubuntu server:
* sudo ufw allow 8080/tcp
* install discord_webhook https://pypi.org/project/Discord-Webhooks/#files

## String to choose only findings with high severity to report it using webhook
```node6@ubserver:/tmp$ cat myfile.txt | tr ',' '\n' | tr '{' '\n' | grep -e "'ip':" -e "'port':" -e "'rule_sev':" -e "'rule_desc':" | awk 'NR%4{printf "%s ",$0;next;}1' | grep -vi "'rule_sev': 0" | grep -vi "'rule_sev': 1" | grep -vi "'rule_sev': 2"```

Result:
'ip': '10.10.10.152'  'port': 21  'rule_sev': 3  'rule_desc': 'This rule checks if FTP Server allows Anonymous Access'

```
created binary and upgraded utils.py code
node6@ubserver:/opt/nerve$ cat /tmp/hooker 
cat /tmp/myfile.txt | tr ',' '\n' | tr '{' '\n' | grep -e "'ip':" -e "'port':" -e "'rule_sev':" -e "'rule_details':" | awk 'NR%4{printf "%s ",$0;next;}1' | grep -vi "'rule_sev': 0" | grep -vi "'rule_sev': 1" | grep -vi "'rule_sev': 1"
node6@ubserver:/opt/nerve$ 
```

```
def submit_webhook(self, webhook, cfg, data={}):
    logger.info('Sending the webhook and writing to tmp file...')
    try:
      #obj = json.load(data) # load json data
      #obj = obj['ip', 'port', 'rule_sev', 'rule_details'] # choose only required paths to webhook
      #write file to OS
      f = open("/tmp/myfile.txt", "w") #create file      
      f.write(str(data)) # write to file
      f.close() #close
      #below block with code to execute binary hooker with cmd cat myfile.txt | tr ',' '\n' | tr '{' '\n' | grep -e "'ip':" -e "'port':" -e "'rule_sev':" -e "'rule_desc':" | awk 'NR%4{printf "%s ",$0;next;}1' | grep -vi "'rule_sev': 0" | grep -vi "'rule_sev': 1" | grep -vi "'rule_sev': 2"
      stream = os.popen('bash /tmp/hooker')
      output = stream.read()
      #done
      #sample_string = json.dumps(data) #discord limit to put only 2000 symbols
      webhook2 = DiscordWebhook(url=webhook, content=output[0:1998])
      response = webhook2.execute()
      return True
#      data = {'status':'done', 'vulnerabilities':data, 'scan_config':cfg}
#      requests.post(webhook, 
#                    json=data, 
#                    headers={'User-Agent':USER_AGENT, 
#                            'Content-Type':'application/json'},
#                    verify=False)
#      return True
    except Exception as e:
      logger.error('Could not submit webhook: {}'.format(e))
```

```
node6@ubserver:/opt$ cat /tmp/hooker
cat /tmp/myfile.txt | tr ',' '\n' | tr '{' '\n' | grep -e "'ip':" -e "'port':" -e "'rule_sev':" -e "'rule_details':" | awk 'NR%4{printf "%s ",$0;next;}1' | grep -vi "'rule_sev': 0" | grep -vi "'rule_sev': 1" | grep -vi "'rule_sev': 2"
node6@ubserver:/opt$ 
```
## hooker & ipmaker & nucleizer
```
node6@ubserver:~/scanner$ ls
fornuclei.txt  hooker  ipmaker  myfile.txt  nuclei-output.txt  nucleizer
node6@ubserver:~/scanner$ cat hooker 
cat /home/node6/scanner/myfile.txt | tr ',' '\n' | tr '{' '\n' | grep -e "'ip':" -e "'rule_sev':" -e "'rule_details':" | awk 'NR%3{printf "%s ",$0;next;}1' | grep -vi "'rule_sev': 0" | grep -vi "'rule_sev': 1" | grep -vi "'rule_sev': 2" | tr -d "'" | tr -s " " | sed 's/rule_sev: //g' | sed 's/rule_details/details/g' | sort -u
node6@ubserver:~/scanner$ cat ipmaker 
#!/bin/bash
cat /home/node6/scanner/myfile.txt | grepip | /home/node6/go/bin/httprobe -c 50 -p http:88 -p http:8080 -p http:8443 -p http:8888 -p http:8181 -p http:8282 -p http:8089 -p http:4443 -p http:4343 -p -p https:8080 -p https:8443 -p https:8888 -p https:8181 -p https:8282 -p https:8383 -p https:8989 -p https:4443 -p http:4343 > /home/node6/scanner/fornuclei.txt
node6@ubserver:~/scanner$ cat nucleizer 
#!/bin/bash
/home/node6/go/bin/nuclei -c 25 -l /home/node6/scanner/fornuclei.txt -t /home/node6/nuclei-templates/ -retries 0 -timeout 4 -o /home/node6/scanner/nuclei-output.txt -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko)" -silent
node6@ubserver:~/scanner$ 
```

## redis on non-standard port
```redis-server --port 6380```
