
def parse_values():
	values = []
	with open('C:\\Users\\Erdos Miller\\Desktop\\February\\TRC\\Projects\\m-ary\\13.txt') as f:
		lines = f.readlines()
		for line in lines:
			parts = line.split(';')
			for part in parts:
				if part.startswith("RxWDs"):
					values.append(part.split('=')[1][1:].strip())
	return values
	
	

	
def parse_hex(value):
	results = []
	while len(value) > 0:
		hex = value[:3]
		value = value[3:]
		r = int(hex,16)
		if r >= pow(2,12-1):
			r -= (1 << 12)
		results.append(r)
	return results	
	
		
	
def flatten(xs):
	return [y for x in xs for y in x]
	
def parse_peaks(values):
	results = []
	for v in values:
		peaks = []
		for h in v:
			if h>255:
				peaks.append(1)
			else:
				peaks.append(0)
		results.append(peaks)
	return results
	

	
	
def parse_deltas(peaks):
	peaks = flatten(peaks)
	delta = 0
	last = 0
	results = []
	for i,p in enumerate(peaks):
		if p == 1:
			results.append( i - last )
			last = i
			return results		
	

values = parse_values()
with open('raw_values.txt', 'w') as f:
	for v in values:
		f.write(v)
		f.write('\n')

hex_values = map(parse_hex, values)
with open('hex_values.txt', 'w') as f:
	for v in hex_values:
		f.write("".join(map(lambda x: "%#5d" % x,v)))
		f.write('\n')

peaks = parse_peaks(hex_values)


def your_fun (values):
	results =[]
	for i in range(len(values)):
		binstring = "".join(map(str,values[i]))
		results.append(int(binstring,2))
	return results
	
decode= your_fun(peaks)
print decode

with open('bin2decfor16.txt', 'w') as f:
	for dec in decode:
		#for dec in decode_list:
		f.write(str(dec))
		f.write(' ')
		f.write('\n')




with open('binary_values.txt', 'w') as f:
	for peak_list in peaks:
		for peak in peak_list:
			f.write(str(peak))
			f.write(' ')
		f.write('\n')

deltas = parse_deltas(peaks)
with open('delta_values.txt', 'w') as f:
	for d in deltas:
		f.write(str(d))
		f.write(' ')
	f.write('\n')
