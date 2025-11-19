# port_intent_detector/intent_map.py

PORT_INTENT_MAP = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP Mail",
    53: "DNS Query",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP Web Traffic",
    110: "POP3 Mail",
    111: "RPCbind",
    123: "NTP Time",
    135: "MS RPC",
    139: "NetBIOS Session",
    143: "IMAP Mail",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS Web Traffic",
    445: "SMB/CIFS",
    465: "SMTP over SSL",
    993: "IMAP over SSL",
    995: "POP3 over SSL",
    1433: "MS SQL Server",
    1521: "Oracle DB",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate",
    27017: "MongoDB",
    # Add more as needed
    "*": "Other/Unknown port"
}

def get_intent(port, proto):
    """
    Returns intent string for a given port.
    Falls back to '*' if port not found.
    """
    return PORT_INTENT_MAP.get(port, PORT_INTENT_MAP.get("*"))
