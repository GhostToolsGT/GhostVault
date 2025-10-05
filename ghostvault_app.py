import subprocess
import tkinter as tk
from tkinter import messagebox
import os

def run_sync():
    base_path = os.path.dirname(os.path.abspath(__file__))
    sync_script = os.path.join(base_path, "ghostvault_sync_full.bat")
    try:
        subprocess.run(sync_script, shell=True, check=True)
        messagebox.showinfo("GhostVault", "✅ Alles succesvol gesynchroniseerd met GitHub!")
    except subprocess.CalledProcessError:
        messagebox.showerror("GhostVault", "⚠️ Er ging iets mis bij het synchroniseren.")

root = tk.Tk()
root.title("GhostVault Sync")
root.geometry("300x180")
root.config(bg="#1f1f1f")

label = tk.Label(root, text="GhostVault Sync", fg="white", bg="#1f1f1f", font=("Segoe UI", 14, "bold"))
label.pack(pady=15)

btn = tk.Button(root, text="Sync to GitHub", command=run_sync, bg="#6a5acd", fg="white",
                font=("Segoe UI", 12, "bold"), relief="flat", padx=10, pady=5)
btn.pack(pady=10)

exit_btn = tk.Button(root, text="Sluiten", command=root.quit, bg="#444", fg="white",
                     font=("Segoe UI", 10), relief="flat")
exit_btn.pack(pady=5)

root.mainloop()