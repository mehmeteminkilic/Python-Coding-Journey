""" Create a function that takes a valid IPv4 address 
as input and returns a defanged version of that IP address. 
In the defanged version, every period "." should be replaced with "[.]
Example:
Input: address = "1.1.1.1"
Output:          "1[.]1[.]1[.]1"
"""
def defangIPaddr(address: str):
	return address.replace('.', '[.]')

def defangIPaddr2(address: str):
    IP4 = []
    for icharacter in address:
        if icharacter.isdigit():
            IP4.append(icharacter)
        else:
            IP4.append("[.]")
    return "".join(IP4)

def defangIPaddr3(address: str):
    IP4 = ''
    for icharacter in address:
        if icharacter  == '.':
            IP4 += '[.]'
        else:
            IP4 += icharacter
    return IP4

print(defangIPaddr("1.1.1.1"))
print(defangIPaddr2("1.1.1.1"))
print(defangIPaddr3("1.1.1.1"))
    