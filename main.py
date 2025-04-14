import os, pyfiglet

c = {
    "1": ("\033[1;31m", "Red"),
    "2": ("\033[1;32m", "Green"),
    "3": ("\033[1;33m", "Yellow"),
    "4": ("\033[1;34m", "Blue"),
    "5": ("\033[1;36m", "Cyan")
}
f = {
    "1": "standard", "2": "digital", "3": "small", "4": "starwars", "5": "doom"
}
r = "\033[0m"
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def ch(o, n):
    while True:
        print(f"\nDooro {n}:")
        for k, v in o.items():
            code, label = v if isinstance(v, tuple) else ("", v)
            print(f"{k}. {code}{label}{r}")
        x = input(f"Xulo {n} (1-{len(o)}): ").strip()
        if x in o:
            clear()
            return o[x][0] if isinstance(o[x], tuple) else o[x]

def main():
    clear()
    print("\033[1;35m© 2025 SAKI | join => https://t.me/qisooyinkahackerska\033[0m\n")
    while True:
        clr = ch(c, "midabka")
        fn = ch(f, "font-ka")
        txt = input("\n$_  ")
        print(clr + pyfiglet.Figlet(font=fn).renderText(txt) + r)
        if input("maku labaneesa? (y/n): ").lower() != 'y': break

main()
