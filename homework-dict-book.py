# Упражнение 138. Текстовые сообщения----------------------------------------

# tabl= {
#     '1':['.',',','?','!',':'],
#     '2':{'2':'A','2':'B','2':'C'},
#     '3':['D','E','F'],
#     '4':['G','H','I'],
#     '5':['J','K','L'],
#     '6':['M','N','O'],
#     '7':['P','Q','R','S'],
#     '8':['T','U','V'],
#     '9':['W','X','Y','Z'],
#     '0':[' ']
# }
# x = ''
# text = input('Enter text: ')
# for i in text:
#     if i in tabl.values():
#         # for j in tabl[i]:
#             # x += [j]
#         print(i)
ta = {
    '.':'1',',':'11','?':'111','!':'1111',':':'11111',
    'A':'2','B':'22','C':'222','D':'3','E':'33','F':'333',
    'G':'4','H':'44','I':'444','J':'5','K':'55','L':'555',
    'M':'6','N':'66','O':'666','P':'7','Q':'77','R':'777',
    'S':'7777','T':'8','U':'88','V':'888','W':'9','X':'99',
    'Y':'999','Z':'9999',' ':'0'
}
res = ''
text = input('Enter text: ').upper()
for i in text:
    if i in ta:
        res += ta[i]
print(res)









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