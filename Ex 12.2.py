logging_profile = ("192.168.1.100", 514)

ip_address, server_port = logging_profile

print("IP Address:", ip_address)
print("Server Port:", server_port)

try:
    logging_profile[1] = 8080
except TypeError as error:
    print("Modification failed:", error)

print("Logging profile remains:", logging_profile)