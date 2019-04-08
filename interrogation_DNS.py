import socket
import dns.resolver

print ( socket.gethostbyname ('www.iutbeziers.fr'))

answer=dns.resolver.query("www.iutbeziers.fr", "A")
for data in answer:                      
        print ("ip = ", data) 

answer=dns.resolver.query("iutbeziers.fr", "MX")
for data in answer:
        print ("mx = ", data)

answer=dns.resolver.query("iutbeziers.fr", "NS")
for data in answer:
        print ("ns = ", data)


myResolver = dns.resolver.Resolver()
print ("resolver du container = ", myResolver.nameservers)




