from tkinter import *
from tkinter import ttk
import pymysql as mdb


def put():

    e_name = i_name.get()
    e_code = i_code.get()
    e_ordinal_number = i_ordinal_number.get()
    conn = mdb.connect(user="BGPayroll", passwd="", host="localhost", database="BGPayroll", autocommit=True)
    cur = conn.cursor()
    cur.execute("""INSERT INTO danni_osiguritel(name,
                                                code,
                                                ordinal_number) 
                                         VALUES('{0}',
                                                '{1}',
                                                '{2}')"""
                .format(e_name, e_code,  e_ordinal_number))
    conn.close()

def clear_entries():
    nameEntry.delete(0, 'end')
    codeEntry.delete(0, 'end')
    ordinal_numberEntry.delete(0, 'end')
    nameEntry.focus()

root = Tk()
root.title("Данни за осигурител")

mainframe = Frame(root)
mainframe.pack(padx=20, pady=20)

i_name = StringVar()
i_code = IntVar()
i_ordinal_number = IntVar()


Label(mainframe, text="Наименование на предприятието-осигурител:").grid(row=0, column=0, sticky=W)
nameEntry = Entry(mainframe, width=50, textvariable=i_name)
nameEntry.grid(row=0, column=1)
nameEntry.focus()
Label(mainframe, text="ЕИК по БУЛСТАТ :").grid(row=1, column=0, sticky=W)
codeEntry = Entry(mainframe, width=50, textvariable=i_code)
codeEntry.grid(row=1, column=1)
Label(mainframe, text="Пореден номер на код на икономическата дейност на осигурителя:").grid(row=2, column=0, sticky=W)
ordinal_numberEntry = Entry(mainframe, width=50, textvariable=i_ordinal_number)
ordinal_numberEntry.grid(row=2, column=1)


Button(mainframe, text="Запиши", command=put).grid(row=3, column=0, padx=20, pady=20)
Button(mainframe, text="Обнови", command=clear_entries).grid(row=3, column=1, padx=20, pady=20)


root.mainloop()
