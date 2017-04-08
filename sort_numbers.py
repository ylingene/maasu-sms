import string

def sort_numbers():
	num_files = 10
	with open('masterlist') as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content]
	all = string.maketrans('','')
	nodigs = all.translate(all, string.digits)
	for idx, num in enumerate(content):
		cleaned = num.translate(all, nodigs)
		if cleaned[0] != '1':
			cleaned = '+1' + cleaned
		content[idx] = cleaned
	content = list(set(content))
	counter = 0
	for number in content:
		index = counter % 10
		f = open('numbers/list'+str(index), 'a')
		f.write(number+"\n")
		f.close()
		counter += 1
		
sort_numbers()