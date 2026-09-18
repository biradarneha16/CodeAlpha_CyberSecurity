#!/usr/bin/env python3
"""CodeAlpha Task 1: authorized network packet sniffer."""
import argparse
from datetime import datetime
from scapy.all import IP, IPv6, Raw, TCP, UDP, ICMP, sniff

def protocol_name(packet):
    if packet.haslayer(TCP): return "TCP"
    if packet.haslayer(UDP): return "UDP"
    if packet.haslayer(ICMP): return "ICMP"
    if packet.haslayer(IP): return "IP"
    if packet.haslayer(IPv6): return "IPv6"
    return packet.lastlayer().__class__.__name__

def summarize(packet, show_payload):
    layer = IP if packet.haslayer(IP) else IPv6 if packet.haslayer(IPv6) else None
    src = layer and packet[layer].src or "-"
    dst = layer and packet[layer].dst or "-"
    src_port = dst_port = ""
    for transport in (TCP, UDP):
        if packet.haslayer(transport):
            src_port, dst_port = f":{packet[transport].sport}", f":{packet[transport].dport}"
            break
    stamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    line = f"[{stamp}] {src}{src_port} -> {dst}{dst_port} | {protocol_name(packet)} | len={len(packet)}"
    if packet.haslayer(Raw):
        raw = bytes(packet[Raw].load)
        line += f" | payload={len(raw)} bytes"
        if show_payload:
            preview = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in raw[:64])
            line += f" | preview={preview!r}"
    print(line)

def main():
    p = argparse.ArgumentParser(description="Authorized packet capture and summary tool")
    p.add_argument("-i", "--interface")
    p.add_argument("-c", "--count", type=int, default=20, help="packets; 0 means unlimited")
    p.add_argument("-f", "--filter", default="", help="optional BPF filter")
    p.add_argument("--show-payload", action="store_true")
    args = p.parse_args()
    if args.count < 0: raise SystemExit("--count must be zero or positive")
    print("CodeAlpha Task 1 — Basic Network Sniffer")
    print("Authorized-use reminder: capture only traffic you are permitted to monitor.")
    sniff(iface=args.interface, filter=args.filter or None, prn=lambda x: summarize(x, args.show_payload), count=args.count, store=False)

if __name__ == "__main__": main()
