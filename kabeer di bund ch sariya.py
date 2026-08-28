import sys


def new_entry():
    name= input("Enter the name of the patient :")
    age= input("Enter the age of the patient :")
    disease= input("Enter the diagnosed disease :")
    date= input("Enter the date of diagnosis (dd/mm/yyyy) :")
    file=open('data.txt','a')
    file.write(f'name : {name}\n')
    file.write(f'age : {age}\n')
    file.write(f'disease : {disease}\n')
    file.write(f'date : {date}\n')
    print('data saved successfully....')
    file.flush()
    file.close()

def view_data():
    with open('data.txt','r') as file:
        content=file.read()
        if content=='':
            print('no data available....')
        else:
            print(content)
    file.close()

def clear_data():
    with open('data.txt','w') as file:
        file.write('')
        print('data cleared....')
        file.flush()
    file.close()


print('---WELCOME TO PATIENT CASE FILING SYSTEM---')

while True:
    a=input('do you want to enter new data or view data or clear data or exit :').strip().lower()

    if a=='enter new data':
        new_entry()
    elif a=='view data':
        view_data()
    elif a=='clear data':
        clear_data()
    elif a=='exit':
        sys.exit('---GOODBYE---')
    else:
        print('invalid input....')
        sys.exit('---GOODBYE---')
