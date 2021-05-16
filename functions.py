__author__ = 'Damien Jeremiah'

import filecmp, difflib

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



# This function will display the nodes that need to be added/deleted from Agama
def difference_nodes_active():
    # Path of first file1
    file1 = "Differential_Tool/agama_today.txt"

    # Path of second file2
    file2 = "Differential_Tool/active_nodes_provision.txt"

    with open(file1) as file_1:
        file_1_text = file_1.readlines()

    with open(file2) as file_2:
        file_2_text = file_2.readlines()

    # Find and print the diff:
    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile='file1.txt',
            tofile='file2.txt', lineterm=''):
        print(line)
    pass


# This function will get all the nodes from monitoring
def get_all_nodes():
    response = client.service.getAllProbeGroupNames()
    print (response)
    pass

# This function will be able to add a node to monitoring. Here we can add "Name" and "LPI Expression".
#Example
#
#    response = client.service.addLpiProbeGroup("Damien5", "*Damien5*")
#
def add_node():
    #response = client.service.addLpiProbeGroup("Damien5", "*Damien5*")
    #response = client.service.addLpiProbeGroup("byk-hartevann1ar1", "*byk-hartevann1ar1*")
    #response = client.service.addLpiProbeGroup("dabbmoi2ar1", "*dabbmoi2ar1*")
    #print (response)
    pass


# This function will delete a specific node
def delete_node():
    #response = client.service.removeProbeGroup('Damien5')
    #response = client.service.removeProbeGroup('dabbanasira1ar1')
    #response = client.service.removeProbeGroup('dabbmoi1ar1')
    #print (response)
    pass

