from enum import Enum
'''
Namme = OukVicheka
Project=contact
'''

contact={
    'Sokha':'012830551',
    'Linda':'081678567',
    'Nika':'0963823824',
    'Nita':'0109878768',
    } 
def Not_found():
    while True:
        if True:
            print('Not found')
            break
def PhoneNumber_search():
    S_PN=input('Input PhoneNumber you want to search:')
    is_find=False
    for phonenumber in contact.values():
        if S_PN==phonenumber:
            is_find=True
            break
    if is_find:
        print(S_PN)
        print(contact[S_PN].keys())
    else :
        Not_found()
    return 
def edit():
    while True:
        print(contact)
        print('1.Edit_contact')
        print('0.Exit')
        Emenu=input('>>>')
        if Emenu == '1':

            print(contact)
            N=input('Input name you what to edit:')#Name
            is_find=False
            for name in contact.keys():
                if N.title()==name.title():
                    is_find=True
                    break
            if is_find:
                    while True:
                        print('1.Edit name')
                        print('2.Edit PhoneNumber')
                        print('0.Exit')
                        Menu=input('>>>')
                        if Menu=='1':
                            NewName=input('Input new name:')
                            contact[NewName]=contact[name]
                            del contact[name]
                        elif Menu=='2':
                            NewPhoneNumber=input('Input new PhhoneNumber:')
                            contact[name]=NewPhoneNumber
                            print(contact[name])
                        elif Menu =='0':
                            break
            else:
                Not_found()    
        elif Emenu == '0':
            break
    return
def add():
    while True:
        print('1.Add New')
        print('0.Exit')
        Amenu=input('>>>')
        if Amenu=='1':
            NN=input('Input new name:').title()#NewName 
            NPN=input('Input new PhoneNumber:').title()#NewPhoneNumber
            contact[NN]=NPN
            print(contact)
        elif Amenu=='0':
            break
    return


def delete():
    while True:
        print(contact)
        print('1.Delete')
        print('0.Exit')
        dmenu=input('>>>')
        if dmenu=='1':
            print(contact)
            Del=input('Input Name u want to delete:')
            print('Press 0 for exit')
            is_find=False
            for name in contact.keys():
                if Del.title() == name.title() :
                    is_find=True
                    break 
            if is_find:
                del contact[Del.title()]
                print(contact)
            else :
                Not_found()
        elif dmenu == '0':
            break
    return
def Edit():
    while True:
        print('1.Add new')
        print('2.Delete')
        print('3.Edit your contact')
        print('0.Go Back')
        Emenu=input('>>>')
        if Emenu == '1':
            add()
        elif Emenu =='2':
            delete()
        elif Emenu == '3':
            edit()
        elif Emenu == '0':
            break
    return
def Search():
    while True:
        print(contact)
        print('1.Search by Name')
        print('2.Search by PhoneNumber')
        print('0.Exit')
        Smenu=input('>>>')
        if Smenu=='1':        
            s=input('Input name you want to search:')
            is_find=False
            for name in contact.keys():
                if s.title() == name.title() :
                    is_find=True
                    break
            if is_find:
                print(f'{name.title()} and {contact[name]}')
            else :
                Not_found()
        elif Smenu=='2':
                PhoneNumber_search()
        elif Smenu=='0':
            break 
    return
print('Welcome to my contact project')   
while True:    
    print('1.Show the contact')
    print('2.Edit your contact')
    print('3.Search')
    print('0.Exit')
    menu=input('>>>') 
    if menu =='1':  
        print(contact)
    elif menu =='2':
        Edit()
    elif menu == '3':
        Search()
    elif menu =='0':
       break 