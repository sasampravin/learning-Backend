import sqlite3, sys, getpass, os
from datetime import datetime

print('='*70)
print('Welcome to Python Full Stack Developer Course details')
print('='*70)
option=input('What Do you want to know more about Python FullStackDeveloper(courses(c)/fees(f)/proceed_to_pay(pp)/none(n)) : ')
if option.lower() == 'none' or option.lower() == 'n':
    print('Thank you for your responce, if you want to know more you can check at any time')
    sys.exit
elif option.lower() == 'courses' or option.lower() == 'c':
    print('1. Front End Developer')
    print('2. Back End Developer')
    try:
        choice2=int(input('Enter your choice to Know more about it : '))
        match choice2:
            case 1:
                print('='*50)
                print('Client Side')
                print('='*50)
                print('a) HTML\nb) CSS\nc) JavaScript\nd) Bootstrap\ne) Jquerry')
                choice3=input('Enter any Course to see the tutorial : ')
                match choice3:
                    case 'a':
                        print('https://www.w3schools.com/html/html_intro.asp')
                    case 'b':
                        print('https://www.w3schools.com/css/')
                    case 'c':
                        print('https://javascript.info/')
                    case 'd':
                        print('https://www.javatpoint.com/bootstrap-tutorial')
                    case 'e':
                        print('https://www.javatpoint.com/jquery-tutorial')
                    case _:
                        print('your choice is wronge try again')
                        print("problem in input ---> Don't enter numeric & alphanumeric values and sysbles for choice")
            case 2:
                print('='*50)
                print('Server Side')
                print('='*50)
                print('a) Python\nb) Django\nc) SQL\nd) MYSQL\ne) MongoDB')
                choice4=input('Enter any Course to see the tutorial : ')
                match choice4:
                    case 'a':
                        print('https://www.javatpoint.com/python-tutorial')
                    case 'b':
                        print('https://www.javatpoint.com/django-tutorial')
                    case 'c':
                        print('https://www.w3schools.com/sql/default.asp')
                    case 'd':
                        print('https://www.w3schools.com/mysql/')
                    case 'e':
                        print('https://www.w3schools.com/mongoDB/')
                    case _:
                        print('your choice is wronge try again')
                        print("problem in input ---> Don't enter numeric & alphanumeric values and sysbles for choice")
            case _:
                print('your choice of operation is wronge try again')
    except ValueError:
        print("Problem in input ---> Don't enter str, alphanumerics and symbles for choice")
elif option.lower()=='fees' or option.lower() == 'f':
    print('1) Python FullStackDeveloper')
    print('2) FrontEndDeveloper')
    print('3) BackEndDeveloper')
    try:
        choice5=int(input('Enter your choice to get Course duration and Payment details : '))
        match choice5:
            case 1:
                print('='*60)
                print('Course duration and Payment details of Python-FullStackDeveloper')
                print('='*60)
                print('Course duration is 6-8 months\nPayment details is Rs.40,000/-(3 installments)')
                print("\nRs.20,000/- 1st installment at joining time\nRs.10,000/- 2'nd installment at 45-days\nRs.10,000/- 3'rd installment at 3'rd month")
                print('\nClasses available both Online/Offline\nTimings Morning 7:00AM-9:00AM &\t 10:00AM-12:00PM \n\tAfternoon 4:00PM-6:00PM \n\tEvening 7:00PM-9:00PM')  
                print('-'*60)
            case 2:
                print('='*60)
                print('Course duration and Payment details of FrontEndDeveloper')
                print('='*60)
                print('Course duration is 4-5 months\nPayment details is Rs.25,000/-(3 installments)')
                print("\nRs.10,000/- 1st installment at joining time\nRs.10,000/- 2'nd installment at 45-days\nRs.5,000/- 3'rd installment at 3'rd month")
                print('\nClasses available both Online/Offline\nTimings Morning 7:00AM-9:00AM &\t 10:00AM-12:00PM \n\tAfternoon 4:00PM-6:00PM \n\tEvening 7:00PM-9:00PM')        
                print('-'*60)
            case 3:
                print('='*60)
                print('Course duration and Payment details of BackEndDeveloper')
                print('='*60)
                print('Course duration is 4-5 months\nPayment details is Rs.25,000/-(3 installments)')
                print("\nRs.10,000/- 1st installment at joining time\nRs.10,000/- 2'nd installment at 45-days\nRs.5,000/- 3'rd installment at 3'rd month")
                print('\nClasses available both Online/Offline\nTimings Morning 7:00AM-9:00AM &\t 10:00AM-12:00PM \n\tAfternoon 4:00PM-6:00PM \n\tEvening 7:00PM-9:00PM')  
                print('-'*60)
            case _:
                print('your choice of operation is wrong try again')
                print("Problem in input ---> Don't enter str, alphanumerics, symbles and beyond choice for choice")
    except ValueError:
        print("Problem in input ---> Don't enter str, alphanumerics and symbles for choice")
        
elif option.lower() == 'proceed_to_pay' or option.lower() == 'pp':
    print()
    print('Thank you for your step into the Courses, All the best for your bright future')
    
    def create_db():
        conn = sqlite3.connect('dummypayone.db')
        print('Database created')
        return conn
    
    def create_table(conn):
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS dummypayone (
                        pid INTEGER PRIMARY KEY,
                        person VARCHAR(250),
                        place VARCHAR(250),
                        phone INTEGER,
                        amount REAL,
                        timestamp TEXT
                        )''')
        conn.commit()
        print('Table created')
    conn = create_db()

    def insert_data(conn):
        try:
            cur = conn.cursor()
            pid = int(input('Enter payment id: '))
            person = input('Enter person name: ')
            place = input('Enter person place: ')
            phone = int(input('Enter phone number: '))
            amount = float(input('Enter amount: '))
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cur.execute('INSERT INTO dummypayone (pid, person, place, phone, amount, timestamp) VALUES (?, ?, ?, ?, ?, ?)',
                        (pid, person, place, phone, amount, timestamp))
            conn.commit()
            print('Record inserted')
        except Exception:
            print('Something went wrong in your input Try to enter valid inputs')            

    def retrieve_data(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM dummypayone')
        records = cur.fetchall()
        for rec in records:
            print(rec)
        print()

    def update_data(conn):
        try:
            cur = conn.cursor()
            pid = int(input('Enter payment id to check your record: '))
            payment = float(input('Enter amount to update your payment details: '))
            cur.execute('SELECT * FROM dummypayone WHERE pid = ?', (pid,))
            record = cur.fetchone()
            if record is not None:
                bal = record[4]
                cur.execute('UPDATE dummypayone SET amount = ? WHERE pid = ?', (bal + payment, pid))
                conn.commit()
                print('Record updated')
            else:
                print('No record found with the specified payment id')
        except Exception:
            print('Something went wrong in your input Try to enter valid inputs')

    def delete_data(conn):
        try:
            cur=conn.cursor()
            pid=int(input('Enter pid to delete the record from the table permanantly : '))
            cur.execute('SELECT * FROM dummypayone WHERE pid=?',(pid,))
            result = cur.fetchone()
            if result is not None:
                cur.execute('DELETE FROM dummypayone WHERE pid=?',(pid,))
                conn.commit()
                print('Record is Deleted on %d'%pid)
            else:
                print('Record not found on %d '%pid)
        except Exception:
            print('Something went wrong in your input Try to enter valid inputs')      

    def alter_data(conn):
        cur = conn.cursor()
        cur.execute('ALTER TABLE dummypayone ADD COLUMN email TEXT')
        conn.commit()
        print('table altered successfully')

    def info_data(conn):
        cur = conn.cursor()
        me = cur.execute('PRAGMA TABLE_INFO(dummypayone)')
        print('TABLE STRUCTURE ')
        for m in me:
            print(m)
        print()
        print('DATA IN THE TABLE')
        retrieve_data(conn)
        conn.commit()
        
    def get_data(conn):
        choice = input("Enter your choice of operation: ").lower()
        print()
        match choice:        
            case 'insert':
                insert_data(conn)            
            case 'retrieve':
                retrieve_data(conn)            
            case 'update':
                update_data(conn)            
            case 'delete':
                delete_data(conn)            
            case 'alter':
                alter_data(conn)            
            case "info":
                info_data(conn)            
            case _:
                print('your choice of operation is wrong')


    print('='*50)
    print('Welcome to Python FullStackDeveloper Course AAP')
    print('='*50)
    print()
    choice1=input('Tell me your Profession (manager/staff/student) : ')
    print()
    if choice1.lower()=='manager':
        PASSWORD_FILE = "password.txt"  # File to store the password
        attempts = 1

        def save_password(password):
            with open(PASSWORD_FILE, "w") as file:
                file.write(password)

        def read_password():
            with open(PASSWORD_FILE, "r") as file:
                return file.read().strip()

        # Check if the password file exists, if not, create it with the default password
        if not os.path.exists(PASSWORD_FILE):
            save_password("MANAGER_HERE")

        while True:
            password = getpass.getpass("Enter the current password to proceed: ")
            # If we want to know the entered pass word check it once ----> print('entered pass word : ',password)

            if password == read_password():
                choice = input("Enter 'C' to change the password or any other key to proceed: ")

                if choice.lower() == 'c':
                    new_password = getpass.getpass("Enter the new password: ")
                    save_password(new_password)  # Update and save the new password
                    print("Password changed successfully.")
                    break
                else:
                    print("=" * 60)
                    print("Manager can do your work here.")
                    print("=" * 60)
                    print()
                    print("=" * 70)
                    print("Choose the option to proceed (retrieve/delete/info): ")
                    print("=" * 70)
                    
                    get_data(conn)
                    
                    print('='*70)
                    ch = input('Do you want to go back to the operations(yes/no) : ')
                    if ch.lower() == 'yes':
                        continue
                    elif ch.lower() == 'no':
                        print('thank you for using program')
                        break
                    else:
                        print('your choice of operation is wrong, thank you for using program')
                    print('='*70)

            else:
                if attempts == 3:
                    print("You have exceeded the maximum number of attempts. Access denied.")
                    break
                print("Incorrect password. Please try again.")
                attempts += 1


    elif choice1.lower()=='staff':
        staff_password_file = 'staff_password.txt'
        attempts = 1

        def save_staff_password(password):
            with open(staff_password_file, 'w') as file:
                return file.write(password)

        def read_staff_password():
            with open(staff_password_file,'r') as file:
                return file.read().strip()

        if not os.path.exists(staff_password_file):
            save_staff_password('STAFF_HERE')

        while True:
            password = getpass.getpass("Enter the current password to proceed : ")
            # If we want to know the entered password just check it ----> print('entered pass word : ',password)

            if password == read_staff_password():
                pw_choice = input("Enter 'C' to make changes in your pass word or any charecter in the pass word : ")

                if pw_choice.lower() == 'c':
                    new_password = getpass.getpass("Enter new password to replay old password : ")
                    save_staff_password(new_possword)  # Update and save the new password
                    print("password changed successfully")
                else:          
                    print("="*60)
                    print('staff can do there work here ')
                    print('='*60)
                    print()   
                    print('='*70)
                    print('Chose one option to proceed (insert/retrieve/update/delete/alter/info) : ')
                    print('='*70)
                    
                    get_data(conn)
                    
                    print('='*70)
                    ch = input('Do you want to go back to the operations(yes/no) : ')
                    if ch.lower() == 'yes':
    #                     manager_work()
                        continue
                    elif ch.lower() == 'no':
                        print('thank you for using program')
                        break
                    else:
                        print('your choice of operation is wrong, thank you for using program')
                    print('='*70)
                    
            else:
                if attempts == 3:
                    print("I think Your are Unauthorized person not Office Staff")
                    break
                print("Incorrect password. Please try again.")
                attempts += 1


    elif choice1.lower()=='student':
        print("="*60)
        print('students can do there work here ')
        print('='*60)
        choice = input('Do you want to check your record(yes/no) : ')
        if choice.lower()=='yes':
            pid = int(input("Enter your payment id to check your record : "))
            cur = conn.cursor()
            records = cur.execute('SELECT * FROM dummypayone WHERE pid = ?',(pid,))
            for rec in records:
                print(rec)
            print()
        elif choice.lower() == 'no':
            print("You can check your record at any time, Have a Nice Day")
        else:
            print('Your choice of operation is wrong, better luck for next time')

    else:
        print('I think You are unauthorized person for this AAP')

    conn.close()   
    
    
elif option not in (['courses'] and ['fees'] and ['proceed_to_pay']):
    print('Your Choice of operation is wrong, please learn typing')
    sys.exit
else:
    print('Your selection is wrong try it properly, thank you')
