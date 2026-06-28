import socket
import datetime

common_ports = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP",
    25: "SMTP",
    53: "DNS",
    3306: "MySQL",
    3389: "RDP",
    135: "RPC",
    139: "NetBIOS",
    445: "SMB"
}

target = input("Enter IP to scan: ")
print("Scanning", target, "....")
print("Started at:", datetime.datetime.now())
print("-" * 40)

start = datetime.datetime.now()

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.001)
    result = sock.connect_ex((target, port))
    if result == 0:
        if port in common_ports:
            print(f"Port {port} is OPEN - {common_ports[port]}")
        else:
            print(f"Port {port} is OPEN")

end = datetime.datetime.now()
print("-" * 40)
print("Scan complete in:", end - start)