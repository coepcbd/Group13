#!/usr/bin/python
from neutronclient.v2_0 import client
from credentials import get_credentials

network_name = "sample_network"
local = "local"

credentials = get_credentials()
neutron = client.Client(**credentials)
try:
    body_sample = {
        
 "network":
    {
      "name": network_name,
      "admin_state_up": True,
      "provider:network_type": local,
    }	
              }
    netw = neutron.create_network(body=body_sample)
    net_dict = netw['network']
    network_id = net_dict['id']
    print "Network %s created" % network_id

finally:
    print "Execution completed"
