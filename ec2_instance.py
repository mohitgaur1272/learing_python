print("this programme is available for you ....)\n      that will help you get pricing detail about ec2 instances.")
print()

ec2_detail  = [ 

{"S.n": 1, "type": "t2.nano",     "vCPUs": 1, "Architecture": "i386, x86_64", "Cores": 1, "Memory (GiB)": 0.5,   "Storage (GB)": "-",      "On-Demand Linux pricing": "0.0058 USD per Hour", "On-Demand Windows pricing": "0.0081 USD per Hour"},
{"S.n": 2, "type": "t2.micro",    "vCPUs": 1, "Architecture": "i386, x86_64", "Cores": 1, "Memory (GiB)": 1,     "Storage (GB)": "-",      "On-Demand Linux pricing": "0.0116 USD per Hour", "On-Demand Windows pricing": "0.0162 USD per Hour"},
{"S.n": 3, "type": "t2.small",    "vCPUs": 1, "Architecture": "i386, x86_64", "Cores": 1, "Memory (GiB)": 2,     "Storage (GB)": "-",      "On-Demand Linux pricing": "0.023 USD per Hour",  "On-Demand Windows pricing": "0.032 USD per Hour"},
{"S.n": 4, "type": "t2.medium",   "vCPUs": 2, "Architecture": "i386, x86_64", "Cores": 2, "Memory (GiB)": 4,     "Storage (GB)": "-",      "On-Demand Linux pricing": "0.0464 USD per Hour", "On-Demand Windows pricing": "0.0644 USD per Hour"},
{"S.n": 5, "type": "t2.large",    "vCPUs": 2, "Architecture": "x86_64",       "Cores": 2, "Memory (GiB)": 8,     "Storage (GB)": "-",      "On-Demand Linux pricing": "0.0928 USD per Hour", "On-Demand Windows pricing": "0.1208 USD per Hour"},
{"S.n": 6, "type": "t2.xlarge",   "vCPUs": 4, "Architecture": "x86_64",       "Cores": 4, "Memory (GiB)": 16,    "Storage (GB)": "-",      "On-Demand Linux pricing": "0.1856 USD per Hour", "On-Demand Windows pricing": "0.2266 USD per Hour"},
{"S.n": 7, "type": "t2.2xlarge",  "vCPUs": 8, "Architecture": "x86_64",       "Cores": 8, "Memory (GiB)": 32,    "Storage (GB)": "-",      "On-Demand Linux pricing": "0.3712 USD per Hour", "On-Demand Windows pricing": "0.4332 USD per Hour"},
{"S.n": 8, "type": "c5a.large",   "vCPUs": 2, "Architecture": "x86_64",       "Cores": 1, "Memory (GiB)": 4,     "Storage (GB)": "-",      "On-Demand Linux pricing": "0.077 USD per Hour",  "On-Demand Windows pricing": "0.169 USD per Hour"},

]

for instance in ec2_detail:
    print("Instance:", instance["type"])
    print("vCPUs:", instance["vCPUs"])
    print("Architecture:", instance["Architecture"])
    print("Cores:", instance["Cores"])
    print("Memory (GiB):", instance["Memory (GiB)"])
    print("Storage (GB):", instance["Storage (GB)"])
    print("On-Demand Linux pricing:", instance["On-Demand Linux pricing"])
   #print("On-Demand Windows pricing:", instance["On-Demand Windows pricing"])
    print()

print("                             All instance name so please choose and type.")
print()
print("t2.nano")
print("t2.micro")
print("t2.small")
print("t2.medium")
print("t2.large")
print("t2.xlarge")
print("t2.2xlarge")
print("c5a.large")

# instance_name = input("Enter name of the Ec2 instance that you want know about pricing :-")

#def pricing(instance_name) :
instance_name = input("Enter name of the Ec2 instance that you want know about pricing :-")
if instance_name == "t2.nano" :
        print()
        print("0.0058 * 24 * 30 = ", 0.0058 * 24 * 30 ,"$") 
elif instance_name == "t2.micro" :
        print()
        print("0.0116 * 24 * 30 = ", 0.0116 * 24 * 30 ,"$") 
elif instance_name == "t2.small" :
        print()
        print("0.023 * 24 * 30 = ", 0.023 * 24 * 30 ,"$") 
elif instance_name == "t2.medium" :
        print()
        print("0.0464 * 24 * 30 = ", 0.0464 * 24 * 30 ,"$")
elif instance_name == "t2.large" :
        print()
        print("0.0928 * 24 * 30 = ", 0.0928 * 24 * 30 ,"$") 
elif instance_name == "t2.xlarge" :
        print()
        print("0.1856 * 24 * 30 = ", 0.1856  * 24 * 30 ,"$") 
elif instance_name == "t2.2xlarge" :
        print()
        print("0.3712 * 24 * 30 = ", 0.3712 * 24 * 30 ,"$") 
elif instance_name == "c5a.large" :
        print()
        print(" 0.077  * 24 * 30 = ", 0.077 * 24 * 30 ,"$") 
else :
        print()
        print("please try again lator for get pricinf of servers.")





