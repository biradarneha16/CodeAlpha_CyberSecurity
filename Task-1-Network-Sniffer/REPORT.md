# Task 1 Report — Basic Network Sniffer

## Objective
Demonstrate packet capture and protocol analysis in an authorized localhost environment.

## Fields analyzed
- Source IP and destination IP
- TCP/UDP source and destination ports
- Protocol
- Packet length
- Optional raw payload length and printable preview

## Method
Install Scapy, start a local HTTP server on 127.0.0.1:8000, generate a request with curl, then capture a limited number of packets on the loopback interface.

## Expected observations
A localhost HTTP request normally produces TCP packets between an ephemeral client port and port 8000. Exact packet count and ordering depend on the operating system and TCP behavior.

## Security considerations
Packet captures can contain sensitive information. The program does not transmit captured data and uses a bounded capture count by default. Payload display is opt-in.

## Evidence checklist
Show dependency installation, local server, sniffer command, packet summaries, and an explanation of IPs, protocol, ports, length, and payload.
