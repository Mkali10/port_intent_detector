# port_intent_detector

from port_intent_detector.monitor import monitor
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Port Intent Detector")
    parser.add_argument(
        "-i", "--interval", type=float, default=2.0,
        help="Polling interval in seconds"
    )
    args = parser.parse_args()

    print(f"Starting Port-Intent Detector with poll interval = {args.interval}s")
    try:
        monitor(poll_interval=args.interval)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
