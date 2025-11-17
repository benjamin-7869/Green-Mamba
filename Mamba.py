#!/usr/bin/env python3
import sys, time, random, shutil, os

# ================= SETTINGS ==================
TYPE_SPEED = 0.004
NUM_CODES = 5
VALID_CODES = ["ZX-91", "NX-2048", "ALPHA-7", "GAMMA-55", "ROOT-ACCESS"]
# ==============================================

# FIXED CLEAR FUNCTION (Windows + Termux Support)
def clear():
    if os.name == "nt":          # Windows
        os.system("cls")
    else:                        # Termux / Linux
        os.system("clear")

def cols():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def typewriter(text, speed=TYPE_SPEED, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(0, speed/3))
    sys.stdout.write(end)
    sys.stdout.flush()

def center(text):
    width = cols()
    return "\n".join(line.center(width) for line in text.split("\n"))

LOGO = r"""
       ██████╗ ██████╗ ███████╗███████╗███╗   ██╗
     ██╔════╝██╔═══██╗██╔════╝██╔════╝████╗  ██║
     ██║  ███╗██║   ██║███████╗█████╗  ██╔██╗ ██║
     ██║   ██║██║   ██║╚════██║██╔══╝  ██║╚██╗██║
     ╚██████╔╝╚██████╔╝███████║███████╗██║ ╚████║
      ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝
                     ────────────────
                   G R E E N   M A M B A
                     ────────────────

                     /\
                    /  \
                   / /\ \
                  / /  \ \
                 /_/    \_\
                 \ \    / /
                  \ \  / /
                   \ \/ /
                    \  /
                    / /
                   / /
           ________/ /
         <__________/
              \\
               \\   ~~~ venom ~~~
                \\____________________
"""

FAKE_MESSAGES = [
    "Virtual relay handshake complete.",
    "Simulated IDS bypass successful.",
    "Privilege token (mock) validated.",
    "Emulated AES container decrypted.",
    "Network ghost-tunnel active.",
    "Stealth module engaged.",
    "Sandbox kernel patched successfully.",
]

def progress():
    for i in range(31):
        percent = int((i/30)*100)
        bar = "[" + "#"*i + "-"*(30-i) + "]"
        sys.stdout.write(f"\rPROCESSING {bar} {percent}%")
        sys.stdout.flush()
        time.sleep(0.03 + random.random()*0.01)
    print()

def run_fake_output():
    for _ in range(random.randint(3, 6)):
        typewriter("[OK] " + random.choice(FAKE_MESSAGES), speed=TYPE_SPEED*1.5)
        time.sleep(0.1)
    progress()
    typewriter("ACCESS GRANTED\n", speed=TYPE_SPEED*2)

def header():
    clear()
    print(center(LOGO))
    print()
    typewriter(center("Created by Cyber Nexera / @nexera.exe"), speed=TYPE_SPEED*2)
    time.sleep(1)
    typewriter(center("Loading stealth modules..."), speed=TYPE_SPEED*1.5)
    time.sleep(0.5)
    print("\n" + "=" * cols())

def main():
    header()
    typewriter(center("ENTER 5 SECURITY CODES BELOW\n"), speed=TYPE_SPEED*1.5)

    for i in range(NUM_CODES):
        while True:
            code = input(f"[{i+1}/{NUM_CODES}] Enter access code: ").strip()

            if code in VALID_CODES:
                typewriter("Validating code...\n", speed=TYPE_SPEED*1.5)
                run_fake_output()
                break
            else:
                typewriter("ERROR: WRONG CODE — ACCESS DENIED\n", speed=TYPE_SPEED*1.3)
                time.sleep(0.3)

    # Final Disclaimer
    print("\n" + "=" * cols())
    typewriter(center("DISCLAIMER"), speed=TYPE_SPEED*1.5)
    typewriter(center("   Link Generated = https://rb.gy/e2yohx ."))
    typewriter(center("   Stolen From Red-Team Project."))
    typewriter(center("   Do not Click any link on your personal Device."))
    typewriter(center("   For educational and legal use only."))
    typewriter(center("   Enjoy and ( FUCK OFF SCRIPT KIDDIE ).\n"))
    print("=" * cols())

    input("Press Enter to exit...")
    clear()

if __name__ == "__main__":
    main()
