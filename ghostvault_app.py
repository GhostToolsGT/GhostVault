import subprocess
import tkinter as tk
from tkinter import messagebox
import os
import webbrowser

def run_sync():
    base_path = os.path.dirname(os.path.abspath(__file__))
    sync_script = os.path.join(base_path, "ghostvault_sync_full.bat")

    # Run via cmd.exe en capture output
    proc = subprocess.run(
        ["cmd", "/c", sync_script],
        capture_output=True, text=True
    )

    # Toon log (ook bij succes – lekker transparant)
    log = proc.stdout + "\n" + proc.stderr
    show_log(log.strip())

    if proc.returncode == 0:
        messagebox.showinfo("GhostVault", "✅ Alles succesvol gesynchroniseerd met GitHub!")
    else:
        messagebox.showerror("GhostVault", "⚠️ Er ging iets mis bij het synchroniseren.\nCheck het logvenster.")

def show_log(text):
    log_win = tk.Toplevel(root)
    log_win.title("GhostVault – Sync log")
    log_win.geometry("720x420")
    text_box = tk.Text(log_win, wrap="word")
    text_box.insert("1.0", text if text else "(geen output)")
    text_box.config(state="disabled")
    text_box.pack(fill="both", expand=True)

def open_projects():
    base_path = os.path.dirname(os.path.abspath(__file__))
    projects = os.path.join(base_path, "Projects")
    if os.path.isdir(projects):
        os.startfile(projects)  # Windows
    else:
        messagebox.showwarning("GhostVault", "Map 'Projects' niet gevonden.")

def open_repo():
    webbrowser.open("https://github.com/GhostToolsGT/GhostVault")

root = tk.Tk()
root.title("GhostVault Sync")
root.geometry("360x240")
root.config(bg="#1f1f1f")

title = tk.Label(root, text="GhostVault Sync", fg="white", bg="#1f1f1f", font=("Segoe UI", 16, "bold"))
title.pack(pady=14)

btn_sync = tk.Button(root, text="Sync to GitHub", command=run_sync, bg="#6a5acd", fg="white",
                     font=("Segoe UI", 12, "bold"), relief="flat", padx=12, pady=8)
btn_sync.pack(pady=8)

row = tk.Frame(root, bg="#1f1f1f")
row.pack(pady=4)
btn_proj = tk.Button(row, text="Open Projects-map", command=open_projects, bg="#444", fg="white",
                     font=("Segoe UI", 10), relief="flat", padx=8, pady=6)
btn_proj.pack(side="left", padx=6)
btn_repo = tk.Button(row, text="Open GitHub-repo", command=open_repo, bg="#444", fg="white",
                     font=("Segoe UI", 10), relief="flat", padx=8, pady=6)
btn_repo.pack(side="left", padx=6)

btn_close = tk.Button(root, text="Sluiten", command=root.quit, bg="#333", fg="white",
                      font=("Segoe UI", 10), relief="flat", padx=8, pady=6)
btn_close.pack(pady=8)

root.mainloop()