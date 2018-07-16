## REGULAR EXPRESSIONS HERE..

# extract email
# re.findall("[a-z]+@[a-z]+\.[a-z]{2,3}", s)#
# "created new email dmdm@dmdmspace.com bsor3a peter@codescalers.com samir@codescalers.com"



# extract IP

# 192.168.12.39

# num . num . num . num
# [0-9]+ . [0-9]+ . [0-9]+ . [0-9]+ 

# pat = "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"


s = """
hello
laptop1 500$
laptop2 502$
radio 200$
contact us
about 
"""

# pat = "\w+\s\d+\$"
# # naive way
# orders_prices = {}
# for line in s.splitlines():
#     if not line.strip():
#         continue 
    
#     item, price = line.split()
#     orders_prices[item] = price


# In [46]: pat = "(\w+)\s(\d+\$)"

# In [44]: re.findall(pat, s)
# Out[44]: [('laptop1', '500$'), ('laptop2', '502$'), ('radio', '200$')]

# In [45]: dict(re.findall(pat, s))
# Out[45]: {'laptop1': '500$', 'laptop2': '502$', 'radio': '200$'}


# In [46]: pat = "(?P<item>\w+)\s(?P<price>\d+\$)"

# In [47]: re.findall(pat, s)
# Out[47]: [('laptop1', '500$'), ('laptop2', '502$'), ('radio', '200$')]

# In [48]: m = re.search(pat, s)

# In [49]: m
# Out[49]: <_sre.SRE_Match object; span=(7, 19), match='laptop1 500$'>

# In [50]: m.groupdict()
# Out[50]: {'item': 'laptop1', 'price': '500$'}
