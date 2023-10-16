
class ChoiceError(BaseException):pass
class CourseError(Exception):pass

def Univeristy():
    while True:
        print('-' * 40)
        print('Departments list')
        print('-' * 40)
        print('1.Arts Block')
        print('2.Science Block')
        print('3.Engineering Block')
        print('4.Education Block')
        print('-' * 40)
        try:
            ch=int(input('Enter any one option to see courses available : '))
            match(ch):
                case 1:
                    try:
                        print('='*40)
                        print('\nUG Courses for Arts Students')
                        print('='*40)
                        print('Students who think that if they choose Arts Stream, they will have less career opportunities than science and commerce, but after completing 12th from arts, there is a list of courses which will provide you good career opportunities.')
                        print('-'*40)
                        print('1) BBA- Bachelor of Business Administration')
                        print('2) BMS- Bachelor of Management Science')
                        print('3) BFA- Bachelor of Fine Arts')
                        print('4) BEM- Bachelor of Event Management')
                        print('5) Integrated Law Course- BA + LL.B')
                        print('6) BJMC- Bachelor of Journalism and Mass Communication')
                        print('7) BFD- Bachelor of Fashion Designing')
                        print('8) BSW- Bachelor of Social Work')
                        print('9) BBS- Bachelor of Business Studies')
                        print('10) BTTM- Bachelor of Travel and Tourism Management')
                        print()
                        print('AVIATION COURSES')
                        print()
                        print('11) B.Sc- Interior Design')
                        print('12) B.Sc.- Hospitality and Hotel Administration')
                        print('13) Bachelor of Design (B. Design)')
                        print('14) Bachelor of Performing Arts')
                        print('15) BA in History')
                    except ValueError as v:
                        print(v)



                    except ValueError as ve:
                        print('value error : ',ve)

        except ValueError as v:
            print('value error : ',v)

Univeristy()
'''  

UG Courses available after 12th Science:
After completing 12th with science stream, there are a variety of options available for an undergraduate course. Students who have an interest in technical learning, they can choose engineering courses and the rest can choose from the courses listed below.

BE/B.Tech- Bachelor of Technology
B.Arch- Bachelor of Architecture
BCA- Bachelor of Computer Applications
B.Sc.- Information Technology
B.Sc- Nursing
BPharma- Bachelor of Pharmacy
B.Sc- Interior Design
BDS- Bachelor of Dental Surgery
Animation, Graphics and Multimedia
B.Sc. – Nutrition & Dietetics
BPT- Bachelor of Physiotherapy
B.Sc- Applied Geology
BA/B.Sc. Liberal Arts
B.Sc.- Physics
B.Sc. Chemistry
B.Sc. Mathematics
Under B.Tech, you have an option of various courses to do after 12th which include:
Science is one of the popular streams offering a wide range of technical courses. Here is the list of UG engineering courses for students who have completed their secondary education in science stream.

Aeronautical Engineering
Automobile Engineering
Civil Engineering
Computer Science and Engineering
Biotechnology Engineering
Electrical and Electronics Engineering
Electronics and Communication Engineering
Automation and Robotics
Petroleum Engineering
Instrumentation Engineering
Ceramic Engineering
Chemical Engineering
Structural Engineering
Transportation Engineering
Construction Engineering
Power Engineering
Robotics Engineering
Textile Engineering
Smart Manufacturing & Automation
 *  You can also check the List of  B. tech. Lateral Courses for diploma holders.

UG Courses available after 12th Commerce:
Students who want to learn about financial and management, can opt commerce stream after 10th. For commerce students, mathematics is an optional subject, thus students who have an interest in mathematics but do not want to go with science stream can take commerce with maths.

B.Com- Bachelor of Commerce
BBA- Bachelor of Business Administration
B.Com (Hons.)
BA (Hons.) in Economics
Integrated Law Program- B.Com LL.B.
Integarted Law Program- BBA LL.B
Apart from courses under Science, Commerce and Arts, there is also a list of professional courses to pursue after 12th:

CA- Chartered Accountancy
CS- Company Secretary
Bachelor of Design in Accessory Design, fashion Design, Ceramic Design, Leather Design, Graphic Design, Industrial Design, Jewellery Design
Bachelor in Foreign Language
Diploma Courses
Advanced Diploma Courses
Certificate Courses
The information provided above will help students with a list of courses available in India they can choose from.

'''