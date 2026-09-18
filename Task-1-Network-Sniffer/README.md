# Task 1 — Basic Network Sniffer

## Objective
Capture and analyze network packets, displaying source/destination addresses, protocols, ports, packet length, and an optional payload preview.

## Setup
```bash
python -m pip install -r requirements.txt
```

## Authorized localhost test
Terminal 1:
```bash
python -m http.server 8000 --bind 127.0.0.1
```
Terminal 2:
```bash
curl http://127.0.0.1:8000/
```
Terminal 3, using the appropriate loopback interface:
```bash
sudo python sniffer.py --count 20 --filter "host 127.0.0.1"
```

Interface names and capture privileges vary by OS. Only monitor traffic you own or are authorized to assess.
