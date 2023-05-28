import tkinter as tk


def main():
    root = tk.Tk()
    root.geometry("300x250+800+200")

    root.title("Выберите режим")

    def choose_cli():
        root.destroy()
        cli()

    def choose_gui():
        root.destroy()
        gui()

    button_cli = tk.Button(root, text="Режим отладки", command=choose_cli, height=6, width=20)
    button_cli.pack()

    button_gui = tk.Button(root, text="Режим игры", command=choose_gui, height=6, width=20)
    button_gui.pack()

    root.mainloop()


def gui():
    print('Doesn\'t work')
    # from interface.GUI import game
    # game()


def cli():
    from interface.CLI import all_func
    all_func()


if __name__ == "__main__":
    main()
