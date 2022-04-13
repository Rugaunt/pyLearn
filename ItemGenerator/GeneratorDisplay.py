from tkinter import *
from tkinter import ttk
import ItemGenerator
# import dice

START_POS_ROW_MIN_TYPE_ROW = 4
BASE_POS_MIN_ITEM_COL = 1
BASE_POS_MAX_ITEM_COL = 3
BASE_POS_TYPE_ITEM_COL = 5





class DiceDisplay:
    def __init__(self, in_root):
        # STARTPOS_ROW_MIN_TYPE_ROW = 4
        # BASE_POS_MIN_ITEM_COL = 1
        # BASE_POS_MAX_ITEM_COL = 3
        # BASE_POS_TYPE_ITEM_COL = 5
        self.belt = BooleanVar()
        self.body = BooleanVar()
        self.chest = BooleanVar()
        self.eyes = BooleanVar()
        self.feet = BooleanVar()
        self.hands = BooleanVar()
        self.head = BooleanVar()
        self.headband = BooleanVar()
        self.neck = BooleanVar()
        self.shoulders = BooleanVar()
        self.wrists = BooleanVar()
        self.slot_less = BooleanVar()
        self.choose_all_types()
        self.item_min = StringVar()
        self.item_min.set("Any")
        self.item_max = StringVar()
        self.item_max.set("Any")
        self.item_name = StringVar()
        in_root.title("Magic Item Generator! (Pathfinder 1e)")

        mainframe = ttk.Frame(in_root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        in_root.columnconfigure(0, weight=1)
        in_root.rowconfigure(0, weight=1)

        self.dice_number = StringVar()
        self.die_type = StringVar()
        self.die_name = StringVar()
        # dice_entry = ttk.Entry(mainframe, width=7, textvariable=self.dice_number)
        # dice_entry.grid(column=2, row=1, sticky=(W, E))
        self.result = StringVar()
        # ttk.Label(mainframe, textvariable=self.die_name).grid(column=1, row=1, sticky=(W, E))

        # ttk.Label(mainframe, textvariable=self.result).grid(column=2, row=2, sticky=(W, E))
        # Main Display
        ttk.Label(mainframe, text="Item: ").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, textvariable=self.item_name).grid(column=2, row=1, sticky=W)
        ttk.Button(mainframe, text="CREATE!", command=lambda: self.make_an_item()).grid(column=4, row=1, sticky=W)


        # Minimum Item Level Button area
        ttk.Label(mainframe, text="Minimum Item Level").grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW - 2, sticky=W)
        ttk.Label(mainframe, textvariable=self.item_min).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW - 1, sticky=W)
        ttk.Button(mainframe, text="Any", command=lambda: self.choose_type_min("Any")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW, sticky=W)
        ttk.Button(mainframe, text="Lesser Minor", command=lambda: self.choose_type_min("Lesser Minor")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 1, sticky=W)
        ttk.Button(mainframe, text="Greater Minor", command=lambda: self.choose_type_min("Greater Minor")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 2, sticky=W)
        ttk.Button(mainframe, text="Lesser Medium", command=lambda: self.choose_type_min("Lesser Medium")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 3, sticky=W)
        ttk.Button(mainframe, text="Greater Medium", command=lambda: self.choose_type_min("Greater Medium")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 4, sticky=W)
        ttk.Button(mainframe, text="Lesser Major", command=lambda: self.choose_type_min("Lesser Major")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 5, sticky=W)
        ttk.Button(mainframe, text="Greater Major", command=lambda: self.choose_type_min("Greater Major")).grid(
            column=BASE_POS_MIN_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 6, sticky=W)

        # Maximum item level button area
        ttk.Label(mainframe, text="Maximum Item Level").grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW - 2, sticky=W)
        ttk.Label(mainframe, textvariable=self.item_max).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW - 1, sticky=W)
        ttk.Button(mainframe, text="Any", command=lambda: self.choose_type_max("Any")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW, sticky=W)
        ttk.Button(mainframe, text="Lesser Minor", command=lambda: self.choose_type_max("Lesser Minor")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 1, sticky=W)
        ttk.Button(mainframe, text="Greater Minor", command=lambda: self.choose_type_max("Greater Minor")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 2, sticky=W)
        ttk.Button(mainframe, text="Lesser Medium", command=lambda: self.choose_type_max("Lesser Medium")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 3, sticky=W)
        ttk.Button(mainframe, text="Greater Medium", command=lambda: self.choose_type_max("Greater Medium")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 4, sticky=W)
        ttk.Button(mainframe, text="Lesser Major", command=lambda: self.choose_type_max("Lesser Major")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 5, sticky=W)
        ttk.Button(mainframe, text="Greater Major", command=lambda: self.choose_type_max("Greater Major")).grid(
            column=BASE_POS_MAX_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 6, sticky=W)

        # item type checklists
        ttk.Label(mainframe, text="Item Type").grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW - 1, sticky=W)
        ttk.Button(mainframe, text="All ON", command=lambda: self.choose_all_types()).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW, sticky=W)
        ttk.Button(mainframe, text="All OFF", command=lambda: self.all_types_off()).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 1, sticky=W)
        ttk.Checkbutton(
            mainframe,
            text="Belts",
            variable=self.belt
            ).grid(
            column=BASE_POS_TYPE_ITEM_COL,
            row=START_POS_ROW_MIN_TYPE_ROW + 2,
            sticky=W)
        ttk.Checkbutton(mainframe, text="Body", variable=self.body).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 3, sticky=W)
        ttk.Checkbutton(mainframe, text="Chest", variable=self.chest).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 4, sticky=W)
        ttk.Checkbutton(mainframe, text="Eyes", variable=self.eyes).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 5, sticky=W)
        ttk.Checkbutton(mainframe, text="Feet", variable=self.feet).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 6, sticky=W)
        ttk.Checkbutton(mainframe, text="Hands", variable=self.hands).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 7, sticky=W)
        ttk.Checkbutton(mainframe, text="Head", variable=self.head).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 8, sticky=W)
        ttk.Checkbutton(mainframe, text="Headband", variable=self.headband).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 9, sticky=W)
        ttk.Checkbutton(mainframe, text="Neck", variable=self.neck).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 10, sticky=W)
        ttk.Checkbutton(mainframe, text="Shoulders", variable=self.shoulders).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 11, sticky=W)
        ttk.Checkbutton(mainframe, text="Wrists", variable=self.wrists).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 12, sticky=W)
        ttk.Checkbutton(mainframe, text="Slot-less", variable=self.slot_less).grid(
            column=BASE_POS_TYPE_ITEM_COL, row=START_POS_ROW_MIN_TYPE_ROW + 13, sticky=W)


        # ttk.Label(mainframe, text="roll: ").grid(column=1, row=2, sticky=E)
        # ttk.Label(mainframe, text="total").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # dice_entry.focus()
        # in_root.bind("<Return>", self.calculate)

    def make_an_item(self):
        type_list = self.make_type_list()
        name = ItemGenerator.generate_wondrous_item(self.item_min.get(), self.item_max.get(), type_list)
        return name

    # Wording Matches excel doc used
    def make_type_list(self):
        the_list = []
        if self.belt.get():
            the_list.append('Belt')
        if self.body.get():
            the_list.append('Body')
        if self.chest.get():
            the_list.append('Chest')
        if self.eyes.get():
            the_list.append('Eye')
        if self.feet.get():
            the_list.append('Feet')
        if self.hands.get():
            the_list.append('Hands')
        if self.head.get():
            the_list.append('Head')
        if self.headband.get():
            the_list.append('Headband')
        if self.neck.get():
            the_list.append('Neck')
        if self.shoulders.get():
            the_list.append('Shoulders')
        if self.wrists.get():
            the_list.append('Wrists')
        if self.slot_less.get():
            the_list.append('Slotless')
        return the_list
    """
    def calculate(self, *args):
        try:
            self.result.set(int(dice.dice(self.dice_number.get(), self.die_type.get())))
        except ValueError:
            pass
    """
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

    def choose_all_types(self):
        self.belt.set(True)
        self.body.set(True)
        self.chest.set(True)
        self.eyes.set(True)
        self.feet.set(True)
        self.hands.set(True)
        self.head.set(True)
        self.headband.set(True)
        self.neck.set(True)
        self.shoulders.set(True)
        self.wrists.set(True)
        self.slot_less.set(True)

    def all_types_off(self):
        self.belt.set(False)
        self.body.set(False)
        self.chest.set(False)
        self.eyes.set(False)
        self.feet.set(False)
        self.hands.set(False)
        self.head.set(False)
        self.headband.set(False)
        self.neck.set(False)
        self.shoulders.set(False)
        self.wrists.set(False)
        self.slot_less.set(False)


root = Tk()
DiceDisplay(root)
root.mainloop()
