#!/usr/bin/python3

# STRING str
ip_address = "192.168.30.129"
print(ip_address)
print(type(ip_address))

# INT int
port = 80
print(type(port))

# FLOAT float 
number = 4.5
print(type(number))


# TYPE CASTING
base_number = float(4)
base_number2 = str(5)
base_number3 = int(4.0)

# LISTAS
my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(443)

print(my_ports[0])
print(my_ports[1])
print(my_ports[2])

# ITERACION POR CADA ELEMENTO
for port in my_ports:
    print("Puerto: " + str(port))

for port in my_ports:
    print(f"Puerto: {port}")


print(f"\n[+] La lista tiene un total de {len(my_ports)} elementos")

# SEGUNDA LISTA
my_ports2 = [22, 80, 443, 8080, 445, 22]

my_ports2.extend([84,85])
my_ports2 += [86, 87]
my_ports2 = sorted(my_ports2)
del my_ports2[0]

for port in my_ports2:
    print(f"Puerto: {port}")


print(f"\n[+] La lista tiene un total de {len(my_ports2)} elementos")
