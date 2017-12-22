import csv

'''The function read_arr takes as argument the name of a csv file without the extension 
and returns a list of lists created by each row in the csv file'''
def read_arr( arr_name ):
  datafile = open(arr_name + '.csv', 'r')
  datareader = csv.reader(datafile,delimiter=',')
  arr_name = []
  for row in datareader:
    arr_name.append(row)
  '''del arr_name [0]'''
  print(arr_name)
  return arr_name

danni_osiguritel = read_arr("danni_osiguritel")
danni_osiguren   = read_arr("danni_osiguren")
danni_forma_76   = read_arr("danni_forma_76")
col1 = [i[0] for i in danni_osiguren]
print (col1)
'''The folowing code performs an inner join of the two lists of lists danni_osiguren and danni_forma_76.
The id_n column from danni_forma_76 is excluded from the join because it is available in danni_osiguren.
Everithing is saved in the list of lists onsoven_masiv
'''
osnoven_masiv = []

osnoven_masiv = [(i[:] + j[:2] + j[3:]) for i in danni_osiguren for j in danni_forma_76 if i[0] == j[2]]
print(osnoven_masiv)
'''The following code converts osnoven_masiv into the dictionary omd'''
keys = osnoven_masiv[0]
omd = [dict(zip(keys, values)) for values in osnoven_masiv[1:]]


print(omd)


'''The codes f1, f2 etc. represent the fields in the file EMPL2000.txt - a csv with structure and contents
  predefined by the National Revenue Agency of Bulgaria'''
for row in omd:

    result = int(row['month'])
    row.update( {'f1': result})

    result = int(row['year'])
    row.update( {'f2': result})
    result = int(danni_osiguritel[1][1])
    row.update( {'f3': result})
    result = int(row['egn'])
    row.update( {'f4': result})
    result = int(row['flag'])
    row.update( {'f5': result})
    result = (row['last_name'])
    row.update( {'f6': result})
    result = (row['initials'])
    row.update( {'f7': result})
    result = int(row['type_ens'])
    row.update( {'f12': result})
    result = int(row['r']) + int(row['o']) + int(row['m']) + int(row['b']) + int(row['a'])
    row.update( {'f24': result})
    result = int(row['r'])
    row.update( {'f25': result})

    if (int(row['b']) <= 3):
      result = 0
      result1 = int(row['b'])
    else:
        result = int(row['b']) - 3
        result1 = 3
    row.update( {'f26': result})
    result = int(row['m'])
    row.update( {'f27': result})
    result = int(row['a'])
    row.update( {'f28': result})
    result = danni_osiguritel [1][2]
    row.update( {'f71': result})
    result = (row['activity_code'])
    row.update( {'f72': result})
    result = int(row['proff_code'][0])
    row.update( {'f73': result})
    row.update( {'f94': result1})
    '''etc.'''

    '''This code converts the list of dictinaries omd into the list of lists osnoven_masiv, removes the first 22 columns
    and then inserts 4 empty strings in the slice between elements 6 and 7 (starting from 0) i.e. f7 and f12.
    Then writes the list of lists into a csv file called EMPL2000.txt'''
    osnoven_masiv = [list(d.values()) for d in omd]

    for row in osnoven_masiv:
        del row [:22]
        row[7:7] = ["","","",""]

    with open("EMPL2000.txt", "w") as f:
      writer = csv.writer(f)
      writer.writerows(osnoven_masiv)




print(omd)
print(osnoven_masiv)


'''https://stackoverflow.com/questions/25417184/multiply-2-elements-in-each-row-create-new-column-list-of-lists-python
https://stackoverflow.com/questions/1859864/how-to-create-an-integer-array-in-python
https://stackoverflow.com/questions/4575973/python-conditional-list-creation-from-2d-lists
https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
https://stackoverflow.com/questions/2646157/what-is-the-fastest-to-access-struct-like-object-in-python
https://stackoverflow.com/questions/3086973/how-do-i-convert-this-list-of-dictionaries-to-a-csv-file-python
'''
