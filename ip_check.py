# Check the IP_addr if it is valid or not
# Works for both IPv4 and IPv6
# IPv4 (8-bit address format, range 0 to 255)
# IPv6 (16-bit address format, range 0 to 65535)
ip_format = input("IPv4 or IPv6:")
if(ip_format == 'IPv4' or ip_format == 'ipv4'): 
  _range= 255
  ip_len= 4
if(ip_format == 'IPv6' or ip_format == 'ipv6'): 
  _range=65535
  ip_len=8
Ip_addr= input("IP_address:")
Ip_addr = Ip_addr.split(":")
number = 0
flag = False
for i in range(len(Ip_addr)):
  if(Ip_addr[i]==''):
    for n, j in enumerate(Ip_addr):
      if (j ==''): Ip_addr[n]='0'
      # print(Ip_addr)
  d=Ip_addr[i]
  d_hex = '0x' + d
  if(len(str(Ip_addr[i])) <= ip_len and (int(d_hex,16) <= _range)): # and (Ip_addr[i].isdigit())
    flag = True
    number += 1
if (number == ip_len and flag == True): 
  print("\n<> VALID IP <>")
else:
  print("\n!!!! INVALID IP  !!!!")
if (number < len(Ip_addr)): 
  print ("\n!!!! INVALID IP !!!!")