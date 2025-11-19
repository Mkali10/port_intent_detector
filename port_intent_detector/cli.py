# port_intent_detector

import argparse
from port_intent_detector.monitor import monitor

def main():
    parser = argparse.ArgumentParser(
        description="Port-Intent Detector: monitors outbound connections and explains probable intent."
    )
    parser.add_argument(
        "-i", "--interval", type=float, default=2.0,
        help="Polling interval in seconds (default 2.0)"
    )

    args = parser.parse_args()
    print(f"Starting Port-Intent Detector with poll interval = {args.interval}s")
    monitor(poll_interval=args.interval)

if __name__ == "__main__":
    main()
