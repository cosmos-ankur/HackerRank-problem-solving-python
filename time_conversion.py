s="04:15:45PM"
def time_conv(s):
	if(s[-2]=='A'):
		print (s[0:8])
	if(s[-2]=='P'):
		print(str(int(s[0:2])+12)+s[2:8])
time_conv(s)

