
# 1.Write a Python program to sort a dictionary by value.---------------------

# mydict = {
#     'b':15,
#     'c':7,
#     'a':10,
#     'v':12
# }
# c = {}
# y = sorted(mydict, key = mydict.get)
# x = sorted(mydict.values())
# for i, j in zip(y,x):
#     c[i] = j
#     print(c)

# print({i:mydict[i]for i in sorted(mydict, key = mydict.get)})


# 2. Write a Python program to add a key to a dictionary.----------------------

# mydict = {
#     'b':15,
#     'c':7,
#     'a':10,
#     'v':12
# }
# mydict['f'] = 23
# print(mydict)

# 3. Write a Python program to check whether a
# given key already exists in a dictionary.---------------------------------

# lt = input('Enter lt: ')
# mydict = {
#     'b':15,
#     'c':7,
#     'a':10,
#     'v':12
# }
# print(lt in mydict)

# 4.Write a Python program to merge two Python dictionaries.----------------

# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)

# 5. Write a Python program to multiply all the 
# values in a dictionary.----------------------------------------------------

# mydict = {'a':1,'b':2,'c':12}
# res = 1
# for i in mydict:
#     res *= mydict[i]
# print(res)

# 6. Create a Python program to find the highest 
# 3 values in a dictionary.--------------------------------------------------

# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# newdict = {}
# keys = sorted(mydict, key = mydict.get, reverse = True)[:3]
# values = sorted(mydict.values(), reverse = True)[:3]
# for i,j in zip(keys, values):
#     newdict[i] = j
# print(newdict)
# print({i:mydict[i] for i in sorted(mydict, key = mydict.get, reverse = True)[:3]})

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

# 1. New DicTiOnAry-------------------------------------------------------

# dict_students = {
#     'st1':4,
#     'st2':7,
#     'st3':9,
#     'st4':6,
#     'st5':4,
#     'st6':10,
#     'st7':6,
#     'st8':9,
#     'st9':7,
#     'st10':5
# }

# dict_students = {}
# for i in range(1,11):
#     st = int(input(f'Enter rating(1-10) {i} student: '))
#     dict_students['st'+ str(i)] = st
# print(dict_students)

# 2. AriTHmeTic AVerAGe-----------------------------------------------------

# dict_students = {
#     'st1':4,
#     'st2':7,
#     'st3':9,
#     'st4':6,
#     'st5':4,
#     'st6':10,
#     'st7':6,
#     'st8':9,
#     'st9':7,
#     'st10':5
# }
# res = 0
# for i in dict_students:
#     res += dict_students[i]
# print('Arithmetic average of rating students =', res / len(dict_students))

# 3. GOOd And bAd sTudenT------------------------------------------------

# res = 0
# for i in dict_students:
#     res += dict_students[i]
# if res / len(dict_students) >= 5:
#     print('Good students')
# else:
#     print('Bad students')

# 4. GOOd sTudenTs------------------------------------------------------

# good_srudents = {}
# for i in dict_students:
#     if dict_students[i] >= 5:
#         good_srudents[i] = dict_students[i]
# print('Good students==>>',good_srudents)


# for i in dict_students:
#     if dict_students[i] >= 5:
#         print('Good students==>>', i)
     

# 5. bAd sTudenTs-------------------------------------------------------

# bad_srudents = {}
# for i in dict_students:
#     if dict_students[i] <= 5:    
#         bad_srudents[i] = dict_students[i]
# print('Bad students==>>', bad_srudents)


# for i in dict_students:
#     if dict_students[i] <= 5:
#         print('Bad students==>>', i)

# 6. nAme--------------------------------------------------------------

# st = input('Enter student name: ')
# for i in dict_students:
#     if st == i:
#         print({i: dict_students[i]})

# 7.New_dicT------------------------------------------------------------

ls1 = []
ls2 = []
ls3 = {} 
s = 'a,2,b,5,c,8,a,4,e,11'
s = s.split(',')
for i in s:
    if i.isalpha():
        ls1.append(i)
    elif i.isdigit():
        ls2.append(int(i))
for i, j in zip(ls1, ls2):
    if i in ls3:
        ls3[i] += j
    else:
        ls3[i] = j
print(ls3)

# 8.DicT frOm A sTrinG-----------------------------------------------------

# count = []
# mydict = {}
# word = 'exercises'
# word = list(word)
# for i in word:
#     count.append(word.count(i))
# for i, j in zip(word, count):
#     mydict[i] = j
# print(mydict)


# for i in word:
#     if i  in mydict:
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
# print(mydict)

# 9. RmOVe-----------------------------------------------------------------

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []
# for i in old_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# 10. miLLiOnAire---------------------------------------------------------

# patasxanner = {
#     'a': 4,
#     'b': 2,
#     'c': 3,
#     'd': 1
# }
# ognutyun = {
#     1 : 'zang',
#     2 : '50-50',
#     3 : 'dahlich',
#     4 : 'patasxanel aranc ognutyan'
# }

# harc1 = {
#     1 : 'ognutyan hnaravorutyun',
#     2 : 'patasxanel'
# }
# print('harc 1 in ==>> 1 + 1 = ?')
# for i in patasxanner:
#     print(i,':', patasxanner[i])
# while True:
#     print('duq karoxeq ogtvel ognutyan hnaravorutyunic kam patasxanel')
#     for j in harc1:
#         print(j,':', harc1[j])
#     pat = int(input('dzer entrutyune 1 kam 2: '))
#     if pat == 1:
#         for o in ognutyun:
#             print(o,':',ognutyun[o])
#         verj_pat = int(input('dzer verjnakan patasxane kam ognutyun: '))
#     if verj_pat in ognutyun:
#         pat = input(f'{ognutyun[4]}: ')
    
#     if  pat in 'b' and ['b'] == 2 :
#         print('chisht patasxan')
#         break
# ------------------------------------------------------------------------------
# -----------------------------------book---------------------------------------

# Упражнение 138. Текстовые сообщения----------------------------------------

# button_count = {
#     '.':'1',',':'11','?':'111','!':'1111',':':'11111',
#     'A':'2','B':'22','C':'222','D':'3','E':'33','F':'333',
#     'G':'4','H':'44','I':'444','J':'5','K':'55','L':'555',
#     'M':'6','N':'66','O':'666','P':'7','Q':'77','R':'777',
#     'S':'7777','T':'8','U':'88','V':'888','W':'9','X':'99',
#     'Y':'999','Z':'9999',' ':'0'
# }
# res = ''
# text = input('Enter text: ').upper()
# for i in text:
#     if i in button_count:
#         res += button_count[i]
# print(res)

# Упражнение 139. Азбука Морзе----------------------------------------------

# morze ={
#     'A':'.-', 'J':'.---', 'S':'...', '1':'.----',
#     'B':'-...', 'K':'-.-', 'T':'-', '2':'..---',
#     'C':'-.-.', 'L':'.-..', 'U':'..-', '3':'...--',
#     'D':'-..', 'M':'--', 'V':'...-', '4':'....-',
#     'E':'.', 'N':'-.', 'W':'.--', '5':'.....',
#     'F':'..-.', 'O':'---', 'X':'-..-', '6':'-....',
#     'G':'--.', 'P':'.--.', 'Y':'-.--', '7':'--...',
#     'H':'....', 'Q':'--.-','Z':'--..', '8':'---..',
#     'I':'..', 'R':'.-.', '0':'-----', '9':'----.', ' ':' ' 
# }
# text = input('Enter text: ').upper()
# text_list = []
# res = ''
# for i in text:
#     if i.isalpha() or i.isdigit():
#         text_list.append(i)
# new_text = ' '.join(text_list)
# for j in new_text:
#     if j in morze:
#         res += morze[j]
# print(res)

