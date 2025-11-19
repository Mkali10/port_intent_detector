# port_intent_detector

# A mapping of (port, protocol) → intent description.
# You can extend this as needed.
INTENT_MAP = {
    (443, 'tcp'): "HTTPS / TLS",
    (80, 'tcp'): "HTTP",
    (53, 'udp'): "DNS query",
    (25, 'tcp'): "SMTP (email sending)",
    (587, 'tcp'): "SMTP (submission)",
    (993, 'tcp'): "IMAP over TLS",
    (3306, 'tcp'): "MySQL database",
    (5432, 'tcp'): "PostgreSQL database",
    (5000, 'tcp'): "Common dev server or REST API",
    # QUIC / HTTP3 typically uses UDP 443
    (443, 'udp'): "QUIC / HTTP/3",
    (1194, 'udp'): "OpenVPN",
    # … add more as you identify
}

def get_intent(port: int, proto: str):
    """
    Return a human-readable intent for a given port and protocol.
    If unknown, returns None.
    """
    return INTENT_MAP.get((port, proto.lower()))
