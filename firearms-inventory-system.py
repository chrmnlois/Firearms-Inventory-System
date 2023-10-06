# San Antonio, Charmaine Lois A. (BSIT 2-5)
# GUI Application - Philippine Army Firearms Inventory System

from tkinter import *
import tkinter.messagebox
import sqlite3

# MAIN WINDOW CONFIGURATIONS
root = Tk()
root.title('Philippine Army Firearms Inventory System')
root.geometry('400x400')
root.config(bg='#41533b')

# FUNCTION BUTTONS OF MAIN MENU
def addWeapon(): # add a new record
    # Root 2 Configurations
    from tkinter import ttk
    root2 = Toplevel(root)
    root2.title('Add a Weapon')
    root2.geometry('400x400')
    root2.config(background='#41533b')
    my_tree = ttk.Treeview(root2)

    # FUNCTION BUTTONS UNDER ADD WEAPON
    def pickWeapon(e):
        if weaponCombo.get() == "Pistol":
            weaponModelCombo.config(value=pistolModel)
            weaponCountryCombo.config(value=pistolCOO)
            weaponTypeCombo.config(value=pistolType)
        elif weaponCombo.get() == "Shotgun":
            weaponModelCombo.config(value=shotgunModel)
            weaponCountryCombo.config(value=shotgunCOO)
            weaponTypeCombo.config(value=shotgunType)
        elif weaponCombo.get() == "Rifle":
            weaponModelCombo.config(value=rifleModel)
            weaponCountryCombo.config(value=rifleCOO)
            weaponTypeCombo.config(value=rifleType)
        elif weaponCombo.get() == "Sniper":
            weaponModelCombo.config(value=sniperModel)
            weaponCountryCombo.config(value=sniperCOO)
            weaponTypeCombo.config(value=sniperType)
        elif weaponCombo.get() == "Machine Gun":
            weaponModelCombo.config(value=machinegunModel)
            weaponCountryCombo.config(value=machinegunCOO)
            weaponTypeCombo.config(value=machinegunType)

    def addRecord(): # add button to add records
        # Functions for Inserting Data
        def reverse(tuples):
            new_tup = tuples[::-1]
            return new_tup

        def insert(id, weapon, model, country, type): # insert function to database
            conDB = sqlite3.connect('philippine_army_firearms_inventory.db')  # create connection to database
            c = conDB.cursor()  # cursor
            c.execute("""CREATE TABLE IF NOT EXISTS 
                weaponRecords(firearmID TEXT, weaponChoice TEXT, weaponModel TEXT, weaponCountry, weaponType TEXT)""")
            c.execute("INSERT INTO weaponRecords VALUES ('" + str(id) + "','" + str(weapon) + "','" + str(model) + "','" + str(country) + "','" + str(type) + "')")
            conDB.commit()  # commit changes

        def read(): # read function to database
            conDB = sqlite3.connect('philippine_army_firearms_inventory.db')  # create connection to database
            c = conDB.cursor()  # cursor
            c.execute("""CREATE TABLE IF NOT EXISTS 
                    weaponRecords(firearmID TEXT, weaponChoice TEXT, weaponModel TEXT, weaponCountry, weaponType TEXT)""")
            c.execute("SELECT * FROM weaponRecords")
            results = c.fetchall()
            conDB.commit()
            return results

        # Insert Data to Database
        dbFirearmID = str(fireArmID.get())
        dbWeaponChoice = str(weaponCombo.get())
        dbWeaponModel = str(weaponModelCombo.get())
        dbWeaponCountry = str(weaponCountryCombo.get())
        dbWeaponType = str(weaponTypeCombo.get())

        insert(str(dbFirearmID), str(dbWeaponChoice), str(dbWeaponModel), str(dbWeaponCountry), str(dbWeaponType))

        for data in my_tree.get_children():
            my_tree.delete(data)

        for result in reverse(read()):
            my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

        # Clear Selections after Adding a Record
        fireArmID.set("")
        weaponCombo.set("Choose Weapon")
        weaponModelCombo.set("Choose Model")
        weaponCountryCombo.set("Choose Country")
        weaponTypeCombo.set("Choose Type")

    def clearRecord(): # clear button to reset records
        fireArmID.set("")
        weaponCombo.set("Choose Weapon")
        weaponModelCombo.set("Choose Model")
        weaponCountryCombo.set("Choose Country")
        weaponTypeCombo.set("Choose Type")

    def backToMainMenu(): # back to main menu button
        ays=tkinter.messagebox.askyesno('Back to Main Menu', 'Are you sure you want to go back to the Main Menu?')
        if ays > 0:
            root2.destroy()

    # Define Firearm ID
    fireArmID = StringVar()

    # Define Type of Weapons List
    weaponChoice = ["Pistol", "Shotgun", "Rifle", "Sniper", "Machine Gun"]

    # Define Pistol Components
    pistolModel = ["M1911 pistol", "Rock Island 1911", "Glock 17", "Beretta 92"]
    pistolCOO = ["United States of America", "Philippines", "Austria", "Italy"]
    pistolType = ["Single-Shot Pistol", "Double Action Revolver", "Semi-Automatic Pistol"]

    # Define Shotgun Components
    shotgunModel = ["Browning Auto-5", "FN TPS", "Remington Model 870", "Franchi AL-48"]
    shotgunCOO = ["United States of America", "Japan", "Belgium", "Italy"]
    shotgunType = ["Double Barrel", "Semi-Automatic", "Pump Action", "Single Barrel"]

    # Define Rifle Components
    rifleModel = ["M16 Rifle", "Taurus T4", "Heckler & Koch HK416", "AKM", "CAR-15"]
    rifleCOO = ["United States of America", "Brazil", "Germany", "Russia", "Philippines"]
    rifleType = ["Automatic Rifle", "Bolt-Action Rifle", "Lever-Action Rifle", "Semi-Automatic Rifle"]

    # Define Sniper Components
    sniperModel = ["Knight's Armament SR-25", "Norinco CS/LR4", "Barrett 50 Cal/M82"]
    sniperCOO = ["United States of America", "China"]
    sniperType = ["Recoil-operated", "Bolt-Action", "Rotating Bolt"]

    # Define Machine Gun Components
    machinegunModel = ["Daewoo Precision Industries", "Ultimax 100", "M60", "M2 Browning"]
    machinegunCOO = ["South Korea", "Singapore", "United States of America"]
    machinegunType = ["Light Machine Gun", "Heavy Machine Gun", "Grenade Machine Gun"]

    # SCREEN OF ROOT 2
    txtaddWeaponTitle = Label(root2, text='           ADD A WEAPON', font=('Stencil', 23), fg='#9e9a75', bg='#41533b').grid(row=0, column=0, columnspan=2, pady=10)
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=1, column=0, columnspan=2)

    # Combobox for Weapon Choice
    txtWeaponChoice = Label(root2, text='Weapon:', font=('Rockwell', 11, 'bold'), fg='white', bg='#41533b').grid(row=2, column=0)
    weaponCombo = ttk.Combobox(root2, value=weaponChoice, width=25)
    weaponCombo.set("Choose Weapon")
    weaponCombo.grid(row=2, column=1)
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=3, column=0)

    # Entry for Firearm ID
    txtFirearmID = Label(root2, text='Firearm ID:', font=('Rockwell', 11, 'bold'), fg='white', bg='#41533b').grid(row=4, column=0)
    entryFirearmID = Entry(root2, textvariable=fireArmID, width=27, border=5).grid(row=4, column=1)
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=5, column=0)

    # Combobox for Model
    txtWeaponModel = Label(root2, text='Model:', font=('Rockwell', 11, 'bold'), fg='white', bg='#41533b').grid(row=6, column=0)
    weaponModelCombo = ttk.Combobox(root2, value=[], width=25)
    weaponModelCombo.set("Choose Model")
    weaponModelCombo.grid(row=6, column=1)
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=7, column=0)

    # Combobox for Country of Origin
    txtWeaponCountry = Label(root2, text='Country of Origin:', font=('Rockwell', 11, 'bold'), fg='white', bg='#41533b').grid(row=8, column=0)
    weaponCountryCombo = ttk.Combobox(root2, value=[], width=25)
    weaponCountryCombo.set("Choose Country")
    weaponCountryCombo.grid(row=8, column=1)
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=9, column=0)

    # Combobox for Type
    txtWeaponType = Label(root2, text='Type:', font=('Rockwell', 11, 'bold'), fg='white', bg='#41533b').grid(row=10, column=0)
    weaponTypeCombo = ttk.Combobox(root2, value=[], width=25)
    weaponTypeCombo.set("Choose Type")
    weaponTypeCombo.grid(row=10, column=1)

    # Bind All Combobox
    weaponCombo.bind("<<ComboboxSelected>>", pickWeapon)

    # Fillers for Root 2
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=11, column=0)
    root2Filler = Label(root2, text='', bg='#41533b').grid(row=12, column=0)

    # Buttons for Root 2
    btnBackMainMenu = Button(root2, text='Back to Main Menu', command=backToMainMenu, font=('Rockwell', 11), fg='White',bg='#1c222e', relief=RAISED, bd=3).grid(row=13, column=0)
    btnAddRecord = Button(root2, text='Add Record', command=addRecord, font=('Rockwell', 11), fg='black',bg='#9e9a75', relief=RAISED, bd=3).grid(row=13, column=1)
    btnclearRecord = Button(root2, text='Clear', command=clearRecord, font=('Rockwell', 11), fg='black',bg='#9e9a75', relief=RAISED, bd=3, padx=10).grid(row=13, column=2)

def viewRecords(): # view records from database
    # Root 2 Configurations
    from tkinter import ttk
    root2 = Toplevel(root)
    root2.title('View Records')
    root2.geometry('880x350')
    root2.config(bg='#41533b')
    my_tree = ttk.Treeview(root2)

    # FUNCTION BUTTONS UNDER VIEW RECORDS
    def backToMainMenu(): # back to main menu button
        ays=tkinter.messagebox.askyesno('Back to Main Menu', 'Are you sure you want to go back to the Main Menu?')
        if ays > 0:
            root2.destroy()

    def reverse(tuples): # reverse output
        new_tup = tuples[::-1]
        return new_tup

    def read(): # read data from database
        conDB = sqlite3.connect('philippine_army_firearms_inventory.db')  # create connection to database
        c = conDB.cursor()  # cursor

        c.execute("""CREATE TABLE IF NOT EXISTS 
                weaponRecords(firearmID TEXT, weaponChoice TEXT, weaponModel TEXT, weaponCountry, weaponType TEXT)""")

        c.execute("SELECT * FROM weaponRecords")
        results = c.fetchall()
        conDB.commit()
        return results

    # Screen of Root 2
    txtViewRecordsTitle = Label(root2, text='                                   VIEW RECORDS', font=('Stencil', 23), fg='#9e9a75', bg='#41533b').grid(row=0, column=0)

    # My Tree Configurations (Treeview Widget)
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview.Heading", font=('Stencil', 11))

    my_tree['columns'] = ("Firearm ID", "Weapon", "Model", "Country of Origin", "Type")
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Firearm ID", anchor=CENTER, width=120)
    my_tree.column("Weapon", anchor=CENTER, width=150)
    my_tree.column("Model", anchor=CENTER, width=200)
    my_tree.column("Country of Origin", anchor=CENTER, width=200)
    my_tree.column("Type", anchor=CENTER, width=200)
    my_tree.heading("Firearm ID", text="Firearm ID", anchor=CENTER)
    my_tree.heading("Weapon", text="Weapon", anchor=CENTER)
    my_tree.heading("Model", text="Model", anchor=CENTER)
    my_tree.heading("Country of Origin", text="Country of Origin", anchor=CENTER)
    my_tree.heading("Type", text="Type", anchor=CENTER)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#9e9a75', font=('Rockwell', 10))
    my_tree.grid(row=1, column=0, columnspan=4, rowspan=5, padx=5, pady=5)

    root2Filler = Label(root2, text='', bg='#41533b').grid(row=12, column=0)
    btnBackMainMenu = Button(root2, text='Back to Main Menu', command=backToMainMenu, font=('Rockwell', 11), fg='White',bg='#1c222e', relief=RAISED, bd=3).grid(row=13, column=0, columnspan=6)

def exit(): # exit application
    ays=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
    if ays>0:
        root.destroy()

# MAIN MENU
rootFiller = Label(root, text="", pady=20, bg='#41533b').pack()
rootTitle = Label(root, text='Philippine Army', font=('Stencil', 30), fg='#9e9a75', bg='#604439', padx=4, relief=SUNKEN, bd=3).pack()
rootTitle2 = Label(root, text='Firearms Inventory System', font=('Stencil', 18), fg='white', bg='#41533b').pack()
rootFiller = Label(root, text="", pady=15, bg='#41533b').pack()
addWeapon = Button(root, text="Add a Weapon", command=addWeapon, font=('Rockwell', 12), fg='black', bg='#9e9a75', relief=RAISED, bd=5).pack()
rootFiller = Label(root, text="", bg='#41533b').pack()
viewRecords = Button(root, text="View Records", command=viewRecords, font=('Rockwell', 12), fg='black', bg='#9e9a75', relief=RAISED, bd=5).pack()
rootFiller = Label(root, text="", bg='#41533b').pack()
exit = Button(root, text="Exit", command=exit, font=('Rockwell', 12), fg='black', bg='#9e9a75', bd=5, padx=5).pack()

# DATABASE CONFIGURATIONS
conDB = sqlite3.connect('philippine_army_firearms_inventory.db') # create connection to database
c = conDB.cursor() # cursor
c.execute("""CREATE TABLE IF NOT EXISTS 
        weaponRecords(dbfirearmID TEXT, dbweaponChoice TEXT, dbweaponModel TEXT, dbweaponCountry TEXT, dbweaponType TEXT)""")
conDB.commit() # commit changes
conDB.close()  # close connection to database

root.mainloop()