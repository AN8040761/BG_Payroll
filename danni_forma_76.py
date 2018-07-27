from tkinter import *
from tkinter import ttk
import pymysql as mdb


def put():
    e_year = i_year.get()    
    e_month = i_month.get()   
    e_id_n = i_id_n.get()    
    e_r = i_r.get()       
    e_o = i_o.get()       
    e_m = i_m.get()       
    e_b = i_b.get()       
    e_d = i_d.get()       
    e_a = i_a.get()       
    e_s = i_s.get()       
    e_n = i_n.get()       
    e_baza_pgo = i_baza_pgo.get()

    conn = mdb.connect(user="BGPayroll", passwd="", host="localhost", database="BGPayroll", autocommit=True)
    cur = conn.cursor()
    cur.execute("""INSERT INTO danni_forma_76(year,
                                            month,
                                            id_n,
                                            r,
                                            o,
                                            m,
                                            b,
                                            d,
                                            a,
                                            s,
                                            n,
                                            baza_pgo) 
                                     VALUES('{0}',
                                            '{1}',
                                            '{2}',
                                            '{3}',
                                            '{4}',
                                            '{5}',
                                            '{6}',
                                            '{7}',
                                            '{8}',
                                            '{9}',
                                            '{10}',
                                            '{11}')"""
    .format(e_year, e_month, e_id_n, e_r, e_o, e_m, e_b, e_d, e_a, e_s, e_n, e_baza_pgo))
    conn.close()

def clear_entries():
    yearEntry.delete(0, 'end')
    monthEntry.delete(0, 'end')
    id_nEntry.delete(0, 'end')
    rEntry.delete(0, 'end')
    oEntry.delete(0, 'end')
    mEntry.delete(0, 'end')
    bEntry.delete(0, 'end')
    dEntry.delete(0, 'end')
    aEntry.delete(0, 'end')
    sEntry.delete(0, 'end')
    nEntry.delete(0, 'end')
    baza_pgoEntry.delete(0, 'end')
    yearEntry.focus()

root = Tk()
root.title("Данни от Форма 76")

mainframe = Frame(root)
mainframe.pack(padx=20, pady=20)


i_year = IntVar()    
i_month = StringVar()   
i_id_n = IntVar()    
i_r = IntVar()       
i_o = IntVar()       
i_m = IntVar()       
i_b = IntVar()       
i_d = IntVar()       
i_a = IntVar()       
i_s = IntVar()       
i_n = IntVar()       
i_baza_pgo = DoubleVar()

Label(mainframe, text="Година, за която се въвеждат данните:").grid(row=0, column=0, sticky=W)
yearEntry = Entry(mainframe, width=50, textvariable=i_year)
yearEntry.grid(row=0, column=1)
yearEntry.focus()

Label(mainframe, text="Месец, за който се въвеждат данните:").grid(row=1, column=0, sticky=W)
monthEntry = Entry(mainframe, width=50, textvariable=i_month)
monthEntry.grid(row=1, column=1)

Label(mainframe, text="Идентификационен номер на служителя:").grid(row=2, column=0, sticky=W)
id_nEntry = Entry(mainframe, width=50, textvariable=i_id_n)
id_nEntry.grid(row=2, column=1)

Label(mainframe, text="Р - Работен ден:").grid(row=3, column=0, sticky=W)
rEntry = Entry(mainframe, width=50, textvariable=i_r)
rEntry.grid(row=3, column=1)

Label(mainframe, text="О – Редовен отпуск :").grid(row=4, column=0, sticky=W)
oEntry = Entry(mainframe, width=50, textvariable=i_o)
oEntry.grid(row=4, column=1)

Label(mainframe, text="М – Майчинство:").grid(row=5, column=0, sticky=W)
mEntry = Entry(mainframe, width=50, textvariable=i_m)
mEntry.grid(row=5, column=1)

Label(mainframe, text="Б – Болнични:").grid(row=6, column=0, sticky=W)
bEntry = Entry(mainframe, width=50, textvariable=i_b)
bEntry.grid(row=6, column=1)

Label(mainframe, text="Д – Изпълнение на държавни задължения:").grid(row=7, column=0, sticky=W)
dEntry = Entry(mainframe, width=50, textvariable=i_d)
dEntry.grid(row=7, column=1)

Label(mainframe, text="А – С разрешение на администрацията:").grid(row=8, column=0, sticky=W)
aEntry = Entry(mainframe, width=50, textvariable=i_a)
aEntry.grid(row=8, column=1)

Label(mainframe, text="С – Самоотлъчка:").grid(row=9, column=0, sticky=W)
sEntry = Entry(mainframe, width=50, textvariable=i_s)
sEntry.grid(row=9, column=1)

Label(mainframe, text="Н – Празнични и почивни дни:").grid(row=10, column=0, sticky=W)
nEntry = Entry(mainframe, width=50, textvariable=i_n)
nEntry.grid(row=10, column=1)

Label(mainframe, text="База за дневното възнаграждение за платен отпуск:").grid(row=11, column=0, sticky=W)
baza_pgoEntry = Entry(mainframe, width=50, textvariable=i_baza_pgo)
baza_pgoEntry.grid(row=11, column=1)


Button(mainframe, text="Запиши", command=put).grid(row=12, column=0, padx=20, pady=20)
Button(mainframe, text="Обнови", command=clear_entries).grid(row=12, column=1, padx=20, pady=20)

root.mainloop()

