__author__ = 'Damien Jeremiah'

from suds.client import Client as SudsClient

# VIP adresse:
#url = 'http://agama.lysetele.net:8008/ws/emp?WSDL'

# Manuell servere (Master/Slave):
url = 'http://agama-es3.lysetele.net:8008/ws/emp?WSDL'
response=''
try:
        client = SudsClient(url=url, cache=None)
except Exception as e:
        print (repr(e))


# This function will get all the nodes from monitoring
def get_all_nodes():
    response = client.service.getAllProbeGroupNames()
    print (response)


# This function will be able to add a node to monitoring. Here we can add "Name" and "LPI Expression".
#Example
#
#    response = client.service.addLpiProbeGroup("Damien5", "*Damien5*")
#
def add_node():
    #response = client.service.addLpiProbeGroup("Damien5", "*Damien5*")
    #print (response)


# This function will delete a specific node
def delete_node():
    #response = client.service.removeProbeGroup('Damien5')
    #print (response)