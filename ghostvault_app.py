import os
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
from datetime import datetime

# ---------- helpers ----------
def app_base_dir():
    # In .exe: map van de executable; in .py: map van dit bestand
    return os.path.dirname(sys.executable) if getattr(sys, "frozen", False) \
           else os.path.dirname(os.path.abspath(__file__))

def show_log(text):
    win = tk.Toplevel(root)
    win.title("GhostVault – Sync log")
    win.geometry("760x420")
    box = tk.Text(win, wrap="word")
    box.insert("1.0", text or "(geen output)")
    box.config(state="disabled")
    box.pack(fill="both", expand=True)

def set_status(msg=None, pct=None, busy=None):
    def _apply():
        if msg is not None:
            status_var.set(msg)
        if pct is not None:
            progress_var.set(int(pct))
        if busy is not None:
            state = "disabled" if busy else "normal"
            btn_sync.config(state=state)
            btn_clip.config(state=state)
            btn_proj.config(state=state)
            btn_repo.config(state=state)
    root.after(0, _apply)

# ---------- actions ----------
def run_sync_async():
    t = threading.Thread(target=_run_sync_thread, daemon=True)
    t.start()

def _run_sync_thread():
    base_path = app_base_dir()
    sync_script = os.path.join(base_path, "ghostvault_sync_full.bat")
    if not os.path.exists(sync_script):
        messagebox.showerror("GhostVault", f"Script niet gevonden:\n{sync_script}")
        return

    set_status("Start sync…", 0, True)

    # Start batch en lees live mee; forceer UTF-8 en verberg console
    proc = subprocess.Popen(
        ["cmd", "/c", sync_script],
        cwd=base_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)
    )

    log_lines = []
    steps = {
        "GV_STEP:BACKUP_START": (5,  "Backup starten…"),
        "GV_STEP:BACKUP_DONE":  (25, "Backup klaar"),
        "GV_STEP:ADD_START":    (30, "Wijzigingen verzamelen…"),
        "GV_STEP:COMMIT_DONE":  (50, "Commit klaar"),
        "GV_STEP:PULL_START":   (55, "Updates ophalen (pull)…"),
        "GV_STEP:PULL_DONE":    (75, "Pull klaar"),
        "GV_STEP:PUSH_START":   (80, "Wijzigingen uploaden (push)…"),
        "GV_STEP:PUSH_DONE":    (100,"Push succesvol"),
        "GV_STEP:PUSH_FAIL":    (95, "Push mislukt"),
    }

    while True:
        line = proc.stdout.readline()
        if not line and proc.poll() is not None:
            break
        if not line:
            continue
        line = line.rstrip("\r\n")
        log_lines.append(line)
        for key, (pct, msg) in steps.items():
            if key in line:
                set_status(msg, pct, True)

    proc.wait()
    if proc.returncode == 0:
        set_status("Klaar ✅", 100, False)
    else:
        set_status("Fout bij sync ⚠️", progress_var.get(), False)

    show_log("\n".join(log_lines))

    if proc.returncode == 0:
        messagebox.showinfo("GhostVault", "✅ Alles succesvol gesynchroniseerd met GitHub!")
    else:
        messagebox.showerror("GhostVault", "⚠️ Er ging iets mis bij het synchroniseren.\nZie logvenster voor details.")

def new_from_clipboard():
    try:
        text = root.clipboard_get()
    except Exception:
        text = ""
    if not text:
        messagebox.showwarning("GhostVault", "Je klembord is leeg of bevat geen tekst.")
        return
    base = app_base_dir()
    drafts_dir = os.path.join(base, "Projects", "GhostCoach", "drafts")
    os.makedirs(drafts_dir, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(drafts_dir, f"clip_{stamp}.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        os.startfile(path)  # open in Notepad
        messagebox.showinfo("GhostVault", f"📄 Nieuw bestand gemaakt:\n{path}")
    except Exception as e:
        messagebox.showerror("GhostVault", f"Kon bestand niet opslaan:\n{e}")

def open_projects():
    path = os.path.join(app_base_dir(), "Projects")
    if os.path.isdir(path):
        os.startfile(path)
    else:
        messagebox.showwarning("GhostVault", "Map 'Projects' niet gevonden.")

def open_repo():
    webbrowser.open("https://github.com/GhostToolsGT/GhostVault")

# ---------- UI ----------
root = tk.Tk()
root.title("GhostVault Sync")
root.geometry("420x340")
root.config(bg="#1f1f1f")

title = tk.Label(root, text="GhostVault Sync", fg="white", bg="#1f1f1f", font=("Segoe UI", 16, "bold"))
title.pack(pady=10)

btn_sync = tk.Button(root, text="Sync to GitHub", command=run_sync_async, bg="#6a5acd", fg="white",
                     font=("Segoe UI", 12, "bold"), relief="flat", padx=12, pady=8)
btn_sync.pack(pady=6)

btn_clip = tk.Button(root, text="Nieuw uit klembord", command=new_from_clipboard, bg="#2e8b57", fg="white",
                     font=("Segoe UI", 11, "bold"), relief="flat", padx=10, pady=7)
btn_clip.pack(pady=4)

progress_var = tk.IntVar(value=0)
progress = ttk.Progressbar(root, maximum=100, variable=progress_var, mode="determinate")
progress.pack(fill="x", padx=14, pady=(8, 2))

status_var = tk.StringVar(value="Wachten op actie…")
status_lbl = tk.Label(root, textvariable=status_var, fg="#ddd", bg="#1f1f1f", font=("Segoe UI", 9))
status_lbl.pack(pady=(0, 8))

row = tk.Frame(root, bg="#1f1f1f")
row.pack(pady=6)

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