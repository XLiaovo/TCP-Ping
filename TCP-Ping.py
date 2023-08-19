import socket
import sys
import time

def tcp_ping(target_host, target_port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set connection timeout to 5 seconds

        # Record start time
        start_time = time.time()

        # Attempt to connect to the target address and port
        sock.connect((target_host, target_port))

        # Record end time
        end_time = time.time()

        # Calculate delay time (in milliseconds)
        delay_ms = (end_time - start_time) * 1000
        print(f"Success: Connected to {target_host}:{target_port} (delay {delay_ms:.2f} ms)")

        sock.close()

    except socket.timeout:
        print(f"Error: Connection to {target_host}:{target_port} timed out")
    except socket.error as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    try:
        target = input("Please enter the target domain or IP address: ")
        target_port = int(input("Please enter the target port number: "))
        delay_ms = 1000

        # If the input is a domain name, convert it to an IP address
        try:
            target_host = socket.gethostbyname(target)
        except socket.gaierror:
            print(f"Error: Invalid domain name or unable to resolve {target}")
            sys.exit(1)

        while True:
            tcp_ping(target_host, target_port)
            time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds and delay
    except KeyboardInterrupt:
        print("\nDetection has been stopped.")
        sys.exit(0)
