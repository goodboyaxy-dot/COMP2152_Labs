# ============================================================
#  WEEK 06 LAB: NETWORK DIAGNOSTIC LOGGER
#  COMP2152
#  adeniyan ayooluwa david
# ============================================================

import subprocess
import csv
import os
import platform
from datetime import datetime

LOG_FILE = "diagnostics.csv"
TEXT_LOG = "network_log.txt"

# ============================================================
#  Cross-platform command helpers
# ============================================================

def is_windows():
    return platform.system().lower() == "windows"


# ============================================================
#  SECTION A: Running System Commands
# ============================================================

def run_ping(host):
    flag = "-n" if is_windows() else "-c"
    result = subprocess.run(
        ["ping", flag, "3", host],
        capture_output=True, text=True
    )
    return result.stdout


def safe_ping(host):
    try:
        flag = "-n" if is_windows() else "-c"
        result = subprocess.run(
            ["ping", flag, "3", host],
            capture_output=True, text=True,
            timeout=10
        )

        if result.returncode == 0:
            return result.stdout
        else:
            return "Ping failed."

    except subprocess.TimeoutExpired:
        return "Ping timed out."
    except Exception as e:
        return "Ping error: " + str(e)


def get_network_info():
    cmd = ["ipconfig", "/all"] if is_windows() else ["ifconfig"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def get_arp_table():
    try:
        result = subprocess.run(
            ["arp", "-a"],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return "ARP error: " + str(e)


def get_hostname():
    result = subprocess.run(
        ["hostname"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


# ============================================================
#  SECTION B: Parsing
# ============================================================

def parse_ping(output):
    stats = {
        "transmitted": 0,
        "received": 0,
        "loss": "100%",
        "avg_ms": "N/A",
        "status": "Failed"
    }

    lines = output.splitlines()

    for line in lines:
        if "packets transmitted" in line and "," in line:
            parts = line.split(", ")
            try:
                stats["transmitted"] = int(parts[0].split()[0])
                stats["received"] = int(parts[1].split()[0])
                stats["loss"] = parts[2].split()[0]
            except:
                pass

        if "rtt" in line or "round-trip" in line:
            try:
                times = line.split("=")[1].split("/")
                stats["avg_ms"] = times[1]
            except:
                pass

    if stats["received"] > 0:
        stats["status"] = "Success"

    return stats


def parse_mac_address(output):
    info = {"mac": "Unknown", "ip": "Unknown"}

    lines = output.splitlines()

    for line in lines:
        line = line.strip()

        if "Physical Address" in line or line.startswith("ether"):
            parts = line.split()
            info["mac"] = parts[-1]

        if "IPv4 Address" in line or "inet " in line:
            parts = line.split()
            info["ip"] = parts[-1]

    return info


def parse_arp_table(output):
    devices = []
    lines = output.splitlines()

    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            devices.append({
                "ip": parts[0],
                "mac": parts[1]
            })

    return devices


# ============================================================
#  SECTION C: Text File I/O
# ============================================================

def write_to_log(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")


def read_log(filename):
    with open(filename, "r") as file:
        return file.read()


def safe_read_log(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

            if content == "":
                print("Log file is empty.")
                return ""

            return content

    except FileNotFoundError:
        print("No log file found.")
        return ""

    finally:
        print("Log read attempt completed.")


def log_command_result(command, target, output, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {command} {target}\n{output}\n{'-'*40}"
    write_to_log(filename, entry)


# ============================================================
#  SECTION D: CSV I/O
# ============================================================

def log_to_csv(filename, command, target, result, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, command, target, result, status])


def read_csv_log(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))


def analyze_csv_log(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("Log is empty.")
        return

    print("Total entries:", len(rows))


# ============================================================
#  SECTION E: Menu Actions
# ============================================================

def do_ping():
    host = input("Enter host: ")

    output = safe_ping(host)
    data = parse_ping(output)

    print("Status:", data["status"])
    print("Avg latency:", data["avg_ms"])

    log_to_csv(LOG_FILE, "ping", host, data["avg_ms"], data["status"])
    log_command_result("PING", host, output, TEXT_LOG)


def do_network_info():
    output = get_network_info()
    info = parse_mac_address(output)

    print("MAC:", info["mac"])
    print("IP:", info["ip"])

    log_to_csv(LOG_FILE, "network", "local", info["ip"], "Captured")


def do_arp():
    output = get_arp_table()
    devices = parse_arp_table(output)

    print("Devices found:", len(devices))

    log_to_csv(LOG_FILE, "arp", "local", len(devices), "Captured")


# ============================================================
#  SECTION F: Main Program
# ============================================================

def display_menu():
    print("\nNETWORK DIAGNOSTIC LOGGER")
    print("1. Ping")
    print("2. Network Info")
    print("3. ARP Scan")
    print("4. View CSV Log")
    print("5. Quit")


def main():

    # create log files if missing
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

    if not os.path.exists(TEXT_LOG):
        open(TEXT_LOG, "w").close()

    print("Running on:", get_hostname())

    while True:
        display_menu()
        choice = input("Choice: ")

        if choice == "1":
            do_ping()
        elif choice == "2":
            do_network_info()
        elif choice == "3":
            do_arp()
        elif choice == "4":
            read_csv_log(LOG_FILE)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


# ============================================================
#  RUN PROGRAM
# ============================================================

main()
