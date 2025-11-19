# port_intent_detector

import psutil
import socket
import time
from port_intent_detector.intent_map import get_intent

class ConnectionInfo:
    def __init__(self, pid, laddr, raddr, status, proto):
        self.pid = pid
        self.laddr = laddr
        self.raddr = raddr
        self.status = status
        self.proto = proto
        try:
            self.process = psutil.Process(pid)
            self.name = self.process.name()
            self.exe = self.process.exe()
        except Exception:
            self.process = None
            self.name = None
            self.exe = None

    def intent(self):
        if self.raddr:
            _, remote_port = self.raddr
            return get_intent(remote_port, self.proto)
        return None

    def __repr__(self):
        return (f"<Connection pid={self.pid} name={self.name} "
                f"{self.laddr} -> {self.raddr} proto={self.proto} status={self.status}>")

def scan_connections():
    conns = psutil.net_connections(kind='inet')
    results = []
    for c in conns:
        if not c.raddr:
            continue
        proto = 'tcp' if c.type == socket.SOCK_STREAM else 'udp'
        ci = ConnectionInfo(c.pid, c.laddr, c.raddr, c.status, proto)
        results.append(ci)
    return results

def monitor(poll_interval=2.0):
    seen = set()
    try:
        while True:
            conns = scan_connections()
            for c in conns:
                key = (c.pid, c.laddr, c.raddr, c.proto)
                if key not in seen:
                    seen.add(key)
                    intent = c.intent()
                    print(f"New connection: PID={c.pid}, Process={c.name}, Exe={c.exe}")
                    print(f" → Local {c.laddr} → Remote {c.raddr} ({c.proto.upper()})")
                    if intent:
                        print(f" → Likely Intent: **{intent}**")
                    else:
                        print(" → Intent: Unknown (no mapping for this port/proto)")
                    print("-" * 40)
            time.sleep(poll_interval)
    except KeyboardInterrupt:
        print("Stopping monitor.")
