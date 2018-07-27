from tkinter import *
from tkinter import ttk
import pymysql as mdb


def put():
    e_id_n = i_id_n.get()
    e_egn = i_egn.get()
    e_flag = i_flag.get()
    e_last_name = i_last_name.get()
    e_initials = i_initials.get()
    e_gross_salary = i_gross_salary.get()
    e_experience_years = i_experience_years.get()
    e_b_year = i_b_year.get()
    e_type_ens = i_type_ens.get()
    e_proff_code = i_proff_code.get()
    e_activity_code = i_activity_code.get()

    conn = mdb.connect(user="BGPayroll", passwd="", host="localhost", database="BGPayroll", autocommit=True)
    cur = conn.cursor()
    cur.execute("""INSERT INTO danni_osiguren(id_n,   
                                            egn,
                                            flag,
                                            last_name,
                                            initials,
                                            gross_salary,
                                            experience_years,
                                            b_year,
                                            type_ens,
                                            proff_code,
                                            activity_code) 
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
                                           '{10}')"""
                .format(e_id_n, e_egn, e_flag, e_last_name, e_initials, e_gross_salary, e_experience_years, e_b_year, e_type_ens, e_proff_code, e_activity_code))
    conn.close()


root = Tk()
root.title("Данни за осигурен")

mainframe = Frame(root)
mainframe.pack()


i_id_n = IntVar()
i_egn = StringVar()
i_flag = IntVar()
i_last_name = StringVar()
i_initials = StringVar()
i_gross_salary = DoubleVar()
i_experience_years = IntVar()
i_b_year = IntVar()
i_type_ens = IntVar()
i_proff_code = StringVar()
i_activity_code = IntVar()

Label(mainframe, text="Идентификационен номер на служителя").grid(row=0, column=0, sticky=W)
id_nEntry = Entry(mainframe, width=50, textvariable=i_id_n).grid(row=0, column=1)

Label(mainframe, text="ЕГН - кл. 5:").grid(row=1, column=0, sticky=W)
egnEntry = Entry(mainframe, width=50, textvariable=i_egn).grid(row=1, column=1)

Label(mainframe, text="Флаг за ЕГН/ЛНЧ - кл. 5.1:").grid(row=2, column=0, sticky=W)
flagEntry = Entry(mainframe, width=50, textvariable=i_flag).grid(row=2, column=1)

Label(mainframe, text="Фамилия - кл. 6:").grid(row=3, column=0, sticky=W)
last_nameEntry = Entry(mainframe, width=50, textvariable=i_last_name).grid(row=3, column=1)

Label(mainframe, text="Инициали - кл. 7:").grid(row=4, column=0, sticky=W)
initialsEntry = Entry(mainframe, width=50, textvariable=i_initials).grid(row=4, column=1)

Label(mainframe, text="Основна заплата:").grid(row=5, column=0, sticky=W)
gross_salaryEntry = Entry(mainframe, width=50, textvariable=i_gross_salary).grid(row=5, column=1)

Label(mainframe, text="Години професионален стаж (0,6%):").grid(row=6, column=0, sticky=W)
experience_yearsEntry = Entry(mainframe, width=50, textvariable=i_experience_years).grid(row=6, column=1)

Label(mainframe, text="Година на раждане:").grid(row=7, column=0, sticky=W)
b_yearEntry = Entry(mainframe, width=50, textvariable=i_b_year).grid(row=7, column=1)

Label(mainframe, text="Вид осигурен - кл. 12: ").grid(row=8, column=0, sticky=W)
type_ensEntry = Entry(mainframe, width=50, textvariable=i_type_ens).grid(row=8, column=1)

Label(mainframe, text="Позиция 1 от код по НКПД - кл. 12.1:").grid(row=9, column=0, sticky=W)
proff_codeEntry = Entry(mainframe, width=50, textvariable=i_proff_code).grid(row=9, column=1)

Label(mainframe, text="Код на икономическа дейност на осигурения - кл. 12.2: ").grid(row=10, column=0, sticky=W)
activity_codeEntry = Entry(mainframe, width=50, textvariable=i_activity_code).grid(row=10, column=1)

Button(mainframe, text="Запиши", command=put).grid(row=12, column=0)

root.mainloop()
