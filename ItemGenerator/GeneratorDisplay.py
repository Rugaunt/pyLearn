from tkinter import *
from tkinter import ttk
# import dice


class DiceDisplay:
    def __init__(self, in_root):
        STARTPOS_ROW_MIN_TYPE_ROW = 4
        BASE_POS_MIN_ITEM_COL = 1
        BASE_POS_MAX_ITEM_COL = 3
        in_root.title("Magic Item Generator! (Pathfinder 1e)")

        mainframe = ttk.Frame(in_root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        in_root.columnconfigure(0, weight=1)
        in_root.rowconfigure(0, weight=1)

        self.dice_number = StringVar()
        self.die_type = StringVar()
        self.die_name = StringVar()
        dice_entry = ttk.Entry(mainframe, width=7, textvariable=self.dice_number)
        dice_entry.grid(column=2, row=1, sticky=(W, E))
        self.result = StringVar()
        ttk.Label(mainframe, textvariable=self.die_name).grid(column=1, row=1, sticky=(W, E))

        ttk.Label(mainframe, textvariable=self.result).grid(column=2, row=2, sticky=(W, E))

        ttk.Label(mainframe, text="Minimum Item Level").grid(column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW - 1, sticky=W)
        ttk.Button(mainframe, text="Any", command=lambda: self.choose_type_min("Any")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW, sticky=W)
        ttk.Button(mainframe, text="Lesser Minor", command=lambda: self.choose_type_min("Lesser Minor")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 1, sticky=W)
        ttk.Button(mainframe, text="Greater Minor", command=lambda: self.choose_type_min("Greater Minor")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 2, sticky=W)
        ttk.Button(mainframe, text="Lesser Medium", command=lambda: self.choose_type_min("Lesser Medium")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 3, sticky=W)
        ttk.Button(mainframe, text="Greater Medium", command=lambda: self.choose_type_min("Greater Medium")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 4, sticky=W)
        ttk.Button(mainframe, text="Lesser Major", command=lambda: self.choose_type_min("Lesser Major")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 5, sticky=W)
        ttk.Button(mainframe, text="Greater Major", command=lambda: self.choose_type_min("Greater Major")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 6, sticky=W)

        ttk.Label(mainframe, text="Maximum Item Level").grid(column=3, row=STARTPOS_ROW_MIN_TYPE_ROW - 1, sticky=W)
        ttk.Button(mainframe, text="Any", command=lambda: self.choose_type_max("Any")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW, sticky=W)
        ttk.Button(mainframe, text="Lesser Minor", command=lambda: self.choose_type_max("Lesser Minor")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 1, sticky=W)
        ttk.Button(mainframe, text="Greater Minor", command=lambda: self.choose_type_max("Greater Minor")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 2, sticky=W)
        ttk.Button(mainframe, text="Lesser Medium", command=lambda: self.choose_type_max("Lesser Medium")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 3, sticky=W)
        ttk.Button(mainframe, text="Greater Medium", command=lambda: self.choose_type_max("Greater Medium")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 4, sticky=W)
        ttk.Button(mainframe, text="Lesser Major", command=lambda: self.choose_type_max("Lesser Major")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 5, sticky=W)
        ttk.Button(mainframe, text="Greater Major", command=lambda: self.choose_type_max("Greater Major")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=STARTPOS_ROW_MIN_TYPE_ROW + 6, sticky=W)
        
        ttk.Label(mainframe, text="number of dice").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="roll: ").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="total").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        dice_entry.focus()
        in_root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            self.result.set(int(dice.dice(self.dice_number.get(), self.die_type.get())))
        except ValueError:
            pass

    def update_dice_name(self, *args):
        self.die_name.set("D" + self.die_type.get())

    def choose_die(self, die_size, *args):
        self.die_type.set(die_size)
        self.update_dice_name()
        print("die set to " + str(die_size))

    def roll_dice(self, die_size, *args):
        try:
            d_number = self.dice_number.get()
            self.result.set(dice.dice(d_number, die_size))
        except ValueError:
            self.result.set("Error!")

    def choose_type_min(self, item_minimum):
        self.item_min.set(item_minimum)

    def choose_type_max(self, item_maximum):
        self.item_max.set(item_maximum)


root = Tk()
DiceDisplay(root)
root.mainloop()
