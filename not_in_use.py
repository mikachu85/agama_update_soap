import suds

from suds.client import Client as SudsClient
# VIP adresse:
#url = 'http://agama.lysetele.net:8008/ws/emp?WSDL'

# Manuell servere:
url = 'http://agama-es3.lysetele.net:8008/ws/emp?WSDL'
response=''
try:
        client = SudsClient(url=url, cache=None)
except Exception as e:
        print (repr(e))
try:
        #Get all nodes
        #response = client.service.getAllProbeGroupNames()

        #Delete node:
        #response = client.service.removeProbeGroup('Damien5')

        #Add node:
        #response = client.service.addLpiProbeGroup("Damien5", "*Damien5*")

except Exception as e:
        print (repr(e))
print(response)