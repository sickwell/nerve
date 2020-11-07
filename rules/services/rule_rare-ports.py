from core.redis      import rds
from core.parser     import ScanParser, Helper
from db.db_ports     import known_ports

class Rule:
  def __init__(self):
    self.rule = 'SVC_0C1Z'
    self.rule_severity = 1
    self.rule_description = 'Some additional ports exposed'
    self.rule_confirm = 'Remote Server Exposes unknown for scanner ports'
    self.rule_details = ''
    self.rule_mitigation = '''Bind all possible network services to localhost, and configure only those which require remote clients on an external interface.'''
    self.intensity = 0

  def check_rule(self, ip, port, values, conf):
    h = Helper()
    p = ScanParser(port, values)
    
    domain = p.get_domain()
    
    known = False

    for ports in known_ports:
      if port in ports:
        known = True
    
    if not known:    
      self.rule_details = 'Server is listening on remote port: {} ({})'.format(port, h.portTranslate(port))
      rds.store_vuln({
        'ip':ip,
        'port':port,
        'domain':domain,
        'rule_id':self.rule,
        'rule_sev':self.rule_severity,
        'rule_desc':self.rule_description,
        'rule_confirm':self.rule_confirm,
        'rule_details':self.rule_details,
        'rule_mitigation':self.rule_mitigation
      })
    
    return
