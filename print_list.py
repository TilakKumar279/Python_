width = int(input("Enter the width:"))
rate_width =10
lan_width = width - rate_width
format_hd = "%-*s%*s"
format_bd = "%-*s%*s"
print ('-'*width)
print (format_hd % (lan_width, 'Programming Languages', rate_width, 'Rate'))
print ('-'*width)
print (format_hd % (lan_width, 'C', rate_width, 10 ))
print (format_hd % (lan_width, 'C++', rate_width, 10 ))
print (format_hd % (lan_width, 'Python', rate_width, 10 ))
print (format_hd % (lan_width, 'Ruby', rate_width, 10 ))
print (format_hd % (lan_width, 'Shell', rate_width, 10 ))
print (format_hd % (lan_width, 'Java', rate_width, 10 ))
print ('-'*width)