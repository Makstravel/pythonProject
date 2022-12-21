# This is a study Python script.

def check_email(m):
    '''This function for check valid email'''
    sm = 0
    dig = 0
    alf = 0
    simv = 0
    for i in m:
        if i.isalpha():
           sm+=1
        if i.isdigit():
            dig +=1
        if i.isupper():
           alf +=1
        if '@' in i and '.' in i and '_' in i:
            simv +=1
    if sm > 0 or dig> 0 or alf> 0 or simv > 0:
         print('ДА')
    else:
        print('НЕТ')


check_email('sc_lib@list.ru')