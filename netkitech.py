import os
import platform
import socket
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser

def get_current_ip_and_dns():
    """Check and display the current IP and DNS."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        dns_servers = []
        if platform.system() == "Windows":
            output = subprocess.check_output("ipconfig /all", shell=True, text=True)
            for line in output.splitlines():
                if "DNS Servers" in line:
                    dns_servers.append(line.split(":")[1].strip())
        else:
            with open("/etc/resolv.conf", "r") as f:
                for line in f:
                    if line.startswith("nameserver"):
                        dns_servers.append(line.split()[1])

        dns_info = "\n".join(dns_servers)
        messagebox.showinfo("IP and DNS Info", f"Hostname: {hostname}\nLocal IP Address: {local_ip}\n\nDNS Servers:\n{dns_info}")
    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving IP and DNS: {e}")

def ping_host(host):
    """Ping a specific host and display the result."""
    try:
        count = "-n" if platform.system() == "Windows" else "-c"
        response = subprocess.run(["ping", count, "4", host], stdout=subprocess.PIPE, text=True)
        messagebox.showinfo(f"Ping Results for {host}", response.stdout)
    except Exception as e:
        messagebox.showerror("Error", f"Error pinging {host}: {e}")

def flush_ip_and_dns():
    """Flush IP and DNS cache."""
    try:
        if platform.system() == "Windows":
            subprocess.run("ipconfig /flushdns", shell=True)
            subprocess.run("netsh int ip reset", shell=True)
        else:
            subprocess.run("sudo systemd-resolve --flush-caches", shell=True)
            subprocess.run("sudo ip route flush cache", shell=True)
        messagebox.showinfo("Success", "IP and DNS cache flushed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error flushing IP and DNS: {e}")

def open_gameserverping_website():
    """Open the gameserverping.com website in the default browser."""
    webbrowser.open("https://gameserverping.com/")

def open_router_page():
    """Open the router's configuration page in the default browser."""
    try:
        gateway = subprocess.check_output("ipconfig" if platform.system() == "Windows" else "ip route | grep default", shell=True, text=True)
        if platform.system() == "Windows":
            gateway = [line.split()[-1] for line in gateway.splitlines() if "Default Gateway" in line and line.split()[-1].strip() != "0.0.0.0"]
        else:
            gateway = [line.split()[2] for line in gateway.splitlines() if "default" in line]

        if gateway:
            webbrowser.open(f"http://{gateway[0]}")
        else:
            messagebox.showerror("Error", "Default gateway not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error opening router page: {e}")

def open_fast_com():
    """Open the Fast.com website in the default browser."""
    webbrowser.open("https://fast.com/")

def export_network_info():
    """Export network information to a file."""
    try:
        file_path = "network_info.txt"
        with open(file_path, "w") as f:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            f.write(f"Hostname: {hostname}\nLocal IP: {local_ip}\n\n")

            dns_servers = []
            if platform.system() == "Windows":
                output = subprocess.check_output("ipconfig /all", shell=True, text=True)
                f.write(output)
            else:
                with open("/etc/resolv.conf", "r") as conf:
                    f.write(conf.read())
        messagebox.showinfo("Export Complete", f"Network info saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error exporting network info: {e}")

def reset_network_adapters():
    """Reset all network adapters."""
    try:
        if platform.system() == "Windows":
            subprocess.run("netsh int ip reset", shell=True)
            subprocess.run("netsh winsock reset", shell=True)
            messagebox.showinfo("Network Reset", "Network adapters reset successfully. Please restart your computer.")
        else:
            messagebox.showwarning("Unsupported", "Network adapter reset is not supported on this OS.")
    except Exception as e:
        messagebox.showerror("Error", f"Error resetting network adapters: {e}")

def create_gui():
    """Create the GUI for the network utility."""
    root = tk.Tk()
    root.title("Netkitech - Network Utility")

    game_providers = {
        "Blizzard": "137.221.106.104",
        "Roblox": "128.116.119.4",
        "Overwatch": "185.60.112.157",
        "Marvel Rivals": "104.18.32.87",
        "Ubisoft": "216.98.48.56",
        "NARAKA": "47.246.43.208",
        "HELLDIVERS 2": "104.21.56.44",
        "Call of Duty": "99.84.56.84"
    }

    tk.Label(root, text="Netkitech - Network Utility", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Check Current IP and DNS", command=get_current_ip_and_dns, width=30).pack(pady=5)
    tk.Button(root, text="Ping Cloudflare (1.1.1.1)", command=lambda: ping_host("1.1.1.1"), width=30).pack(pady=5)

    def select_and_ping_provider():
        def on_select():
            selected_provider = provider_var.get()
            if selected_provider in game_providers:
                ping_host(game_providers[selected_provider])
            provider_window.destroy()

        provider_window = tk.Toplevel(root)
        provider_window.title("Select Game Provider")
        provider_var = tk.StringVar(value=list(game_providers.keys())[0])

        tk.Label(provider_window, text="Select a Game Provider:").pack(pady=10)
        for provider in game_providers.keys():
            tk.Radiobutton(provider_window, text=provider, variable=provider_var, value=provider).pack(anchor=tk.W)
        tk.Button(provider_window, text="Ping", command=on_select).pack(pady=10)

    tk.Button(root, text="Ping Major Game Providers", command=select_and_ping_provider, width=30).pack(pady=5)

    tk.Button(root, text="Open GameServerPing Website", command=open_gameserverping_website, width=30).pack(pady=5)
    tk.Button(root, text="Open Router Page", command=open_router_page, width=30).pack(pady=5)
    tk.Button(root, text="Run Speed Test on Fast.com", command=open_fast_com, width=30).pack(pady=5)
    tk.Button(root, text="Export Network Info", command=export_network_info, width=30).pack(pady=5)
    tk.Button(root, text="Flush IP and DNS", command=flush_ip_and_dns, width=30).pack(pady=5)
    tk.Button(root, text="Reset Network Adapters", command=reset_network_adapters, width=30).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=30).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
