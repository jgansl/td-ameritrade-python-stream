from tdaclient import Client

def testInitClient():
   client = Client()
   msg = client.request()
   assert msg == 'Client'
