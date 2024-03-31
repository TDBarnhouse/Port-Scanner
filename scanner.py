# Test target: 45.33.32.156 - http://scanme.nmap.org/

import nmap
import time
import sys

nm = nmap.PortScanner()

options = "-sV -sC scan_results"

if len(sys.argv) != 2:
    print("Usage: python3 scanner.py <target>")
    sys.exit(1)

target = sys.argv[1]

start_time = time.time()

print("Scanning target %s..." % target)
nm.scan(target, arguments=options)

if not nm.all_hosts():
    print("Scan failed: No results found.")
    exit()

end_time = time.time()
elapsed_time = end_time - start_time

print("Scan completed in %.2f seconds.\n" % elapsed_time)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))
