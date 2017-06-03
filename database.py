people = {
  'Alice':
    {'phone': '2341', 'addr': 'bangalore'},
  'Beth' :
    {'phone': '9102', 'addr': 'New Zealand'},
  'Cecil':
    {'phone': '3258', 'addr': 'Australia'}
}

key_n = input("Enter Name:")
key_v = input("phone or addr:")

print (("%s 's %s is %s") % (key_n, key_v, people[key_n][key_v]))