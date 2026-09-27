candidate={}

# main_menu 
def main_menu():
    while True:
        print("=============================")
        print("***CAMPUS 360***")
        print("***🏫SMART COLLEGE PORTAL***")
        print("=============================")
        print("1. Student Login")
        print("2. Faculty Login")
        print("3. Admin Login")
        print("4. New Student Registration")
        print("5. Explore College")
        print("6. Help")
        print("7. Exit")
        print("=============================")
        select=input("Select: ")
        if select=="1":
            student_login()
        elif select=="2":
            faculty_login()
        elif select=="3":
            admin_login()
        elif select=="4":
            new_student_registration()
        elif select=="5":
            explore_college()
        elif select=="6":
            help_menu()
        elif select=="7":
            print("Thank You for Visting") 
            break 
        else:
            print("Your Selection is Invalid") 

# student_login 
def student_login():
    print("=============================")
    print("***👨‍🎓STUDENT LOGIN***")
    print("=============================")
    student_id=input("Enter student ID: ").strip()
    password=input("Enter password: ").strip()
    if student_id in candidate:
        if candidate[student_id]["password"]==password:
            print("Verifying...")
            print("Login is successful!")
            print("Welcome",candidate[student_id]["name"])
            student_dashboard(student_id)
        else:
            print("❌wrong password")
    else:
        print("student ID is not found")

# student dashboard 
def student_dashboard(student_id):
    while True:

        print("=============================")
        print("***📚STUDENT DASHBOARD***")
        print("=============================")
        print("1. My Profile")
        print("2. Academic Performance")
        print("3. Attendance")
        print("4. Internal Assessments")
        print("5. Fee Status")
        print("6. Events and Clubs")
        print("7. Notifications")
        print("8. Placements")
        print("9.Complaints")
        print("10. My Activity")
        print("11. My Overall Summary")
        print("12. Logout")
        print("=============================")
        select=input("Select: ")
        if select=="1":
            my_profile(student_id)
        elif select=="2":
            academic_performance()
        elif select=="3":
            attendance()
        elif select=="4":
            internal_assessments()
        elif select=="5":
            fee_status()
        elif select=="6":
            events_clubs()
        elif select=="7":
            notifications()
        elif select=="8":
            placements()
        elif select=="9":
            complaints()
        elif select=="10":
            my_activity()
        elif select=="11":
            overall_summary(student_id)
        elif select=="12":
            print("Logged out")
            break
        else:
            print("Your selection is invalid")

# My profile 
def my_profile(student_id):
    while True:
        print("=============================")
        print("---------👤MY PROFILE---------")
        print("=============================")
        print("Student id: ",student_id)
        print("Name: ",candidate[student_id]["name"])
        print("department: ",candidate[student_id]["department"])
        print("Year: ",candidate[student_id]["year"])
        print("Section: ",candidate[student_id]["section"])
        print("Email: ",candidate[student_id]["email"])
        print("Mobile: ",candidate[student_id]["mobile"])
        input("Press Enter to continue...")
        print("=============================")
        print("1. Update Profile")
        print("2. Back")
        print("=============================")
        select=input("Select: ")
        if select=="1":
            update_profile(student_id)
        elif select=="2":
            break
        else:
            print("Invalid selection")
# Update profile 
def update_profile(student_id):
    while True:
        print("=============================")
        print("-------✏️UPDATE PROFILE-------")
        print("=============================")
        print("1. Update email:")
        print("2. Update mobile number:")
        print("3. Update password:")
        print("4. Back")
        print("=============================")
        select=input("Select: ")
        if select=="1":
            email=input("Enter email: ")
            if "@" in email and "." in email:
                candidate[student_id]["email"]=email
                print("✅Email is updated")
            else:
                print("❌This mail is not valid")
        elif select=="2":
            mobile=input("Enter mobile number: ")
            if len(mobile)==10 and mobile.isdigit():
                candidate[student_id]["mobile"]=mobile
                print("✅Mobile number is updated")
            else:
                print("❌The number is not valid")
        elif select=="3":
            password=input("Enter password: ")
            if password!="":
                candidate[student_id]["password"]=password
                print("✅Password is updated")
            else:
                print("❌Password is not valid")
        elif select=="4":
            break
        else:
            print("Invalid selection process")

# Academic Performance 
def academic_performance():
    while True:
        print("=============================")
        print("-----📚MY ACADEMICS-----")
        print("=============================")
        print("1. Python")
        print("2. Java")
        print("3. Data Structures")
        print("4. DBMS")
        print("5. Computer Networks")
        print("6. Back")
        print("=============================")
        select=input("Select: ")
        if select=='1':
            print("Subject: Python")
            print("=============================")
            print("Internal 1 : 18/20")
            print("Internal 2 : 16/20")
            print("assignment : 9/10")
            print("Model Exam : 72/100")
            print("Performance : Good")
            print("=============================")
        elif select=="2":
            print("Subject: Java")
            print("=============================")
            print("Internal 1 : 15/20")
            print("Internal 2 : 18/20")
            print("assignment : 9/10")
            print("Model Exam : 72/100")
            print("Performance : Good")
            print("=============================")
        elif select=="3":
            print("Subject: Data Structures")
            print("=============================")
            print("Internal 1 : 17/20")
            print("Internal 2 : 16/20")
            print("assignment : 7/10")
            print("Model Exam : 65/100")
            print("Performance : Average")
            print("=============================")
        elif select=="4":
            print("Subject: DBMS")
            print("=============================")
            print("Internal 1 : 19/20")
            print("Internal 2 : 19/20")
            print("assignment : 9/10")
            print("Model Exam : 90/100")
            print("Performance : Excellent")
            print("=============================")
        elif select=="5":
            print("Subject: Computer Networks")
            print("=============================")
            print("Internal 1 : 18/20")
            print("Internal 2 : 16/20")
            print("assignment : 9/10")
            print("Model Exam : 72/100")
            print("Performance : Good")
            print("=============================")
        elif select=="6":
            break
        else:
            print("❌Invalid selection")

# Attendance 
def attendance():
    print("=============================")
    print("---------📅ATTENDANCE---------")
    print("=============================")
    print("Subject Present Total %")
    print("=============================")
    Python=42/45*100
    Java=38/45*100
    Ds=35/45*100
    DBMS=40/45*100
    Cn=39/45*100
    overall=(Python+Java+Ds+DBMS+Cn)/5
    print("Python: ",Python,"%")
    print("Java: ",Java,"%")
    print("Ds: ",Ds,"%")
    print("DBMS",DBMS,"%")
    print("Cn",Cn,"%")
    print("=============================")
    print("Overall: ",overall,"%")
    highest=max(Python,Java,Ds,DBMS,Cn)
    lowest=min(Python,Java,Ds,DBMS,Cn)
    print("Highest attendance: ",highest,"%")
    print("Lowest attendance: ",lowest,"%")
    if overall>=75:
        print("✅Eligible")
    else:
        print("❌Shortage")
    # Attendance Shortage Calculator 
    print("=============================")
    print("----⏱️ATTENDANCE CALCULATOR----")
    print("=============================")

    present = int(input("Enter Present Classes: "))
    total = int(input("Enter Total Classes: "))
    if total==0:
        print("The total may not be zero")
    else:
        percentage = (present/total)*100
        print("Attendance Percentage:", percentage, "%")
        if percentage >= 75:
            print("✅ Eligible")
        else:
            print("❌ Shortage")

# Internal assessments    
def internal_assessments():
    while True:
        print("=============================")
        print("------📝ASSESSMENT PORTAL------")
        print("=============================")
        print("1. Internal Assessment 1")
        print("2. Internal Assessment 2")
        print("3. Assignments")
        print("4. Model Examination")
        print("5. View Overall Result")
        print("6. Back")
        print("=============================")
        select=input("Select:")
        if select=="1":
            print("Python : 18")
            print("Java : 15")
            print("DSA : 17")
            print("DBMS : 19")
            print("CN : 16")
        elif select=="2":
            print("Python : 16")
            print("Java : 18")
            print("DSA : 16")
            print("DBMS : 19")
            print("CN : 17")
        elif select=="3":
            print("Python : 9")
            print("Java : 9")
            print("DSA : 7")
            print("DBMS : 9")
            print("CN : 8")
        elif select=="4":
            print("Python : 72")
            print("Java : 75")
            print("DSA : 65")
            print("DBMS : 90")
            print("CN : 70")
        elif select=="5":
            internal1 = [18,15,17,19,16]
            internal2 = [16,18,16,19,17]
            assignments = [9,9,7,9,8]
            model = [72,75,65,90,70]
            total=sum(internal1)+sum(internal2)+sum(assignments)+sum(model)
            average=total/20
            print("=============================")
            print("-------🏆OVERALL RESULT--------")
            print("=============================")
            print("Total marks: ",total)
            print("Average marks: ",average)
            if average>=75:
                print("Performance : Excellent")
            elif average>=60:
                print("performance : Good")
            else:
                print("Performance : Average")
        elif select=="6":
            break
        else:
            print("Selection is invalid")

# Fee management 
def fee_status():
    fees = {
        "Tuition Fee": 45000,
        "Transport Fee": 10000,
        "Exam Fee": 2500,
        "Library Fine": 500
    }
    total = 58000
    paid = 50000
    pending = total - paid
    while True:
        print("=============================")
        print("--------💰FEE PORTAL--------")
        print("=============================")
        print("Total :", total)
        print("Paid :", paid)
        print("Pending :", pending)
        print("=============================")
        print("1. View Details")
        print("2. Payment")
        print("3. Back")
        print("=============================")
        select = input("Select: ")
        if select == "1":
            print("=============================")
            for fee in fees:
                print(fee, ":", fees[fee])
        elif select == "2":
            amount = int(input("Enter Amount: "))
            if amount <= pending:
                pending = pending - amount
                paid = paid + amount
                print("✅ PAYMENT SUCCESSFUL")
                print("Transaction ID : TXN10582")
                print("Amount :", amount)
                print("Status : PAID")
            else:
                print("❌ Invalid Amount")
        elif select == "3":
            break
        else:
            print("Invalid Selection")

# Events club 
def events_clubs():
    events = {
    "Hackathon": 50,
    "Technical Fest": 100,
    "Cultural Fest": 200,
    "Sports Meet": 150,
    "Workshop": 60,
    "Seminar": 80
    }
    while True:
        print("=============================")
        print("--------🎉CAMPUS EVENTS--------")
        print("=============================")
        print("1. Hackathon")
        print("2. Technical Fest")
        print("3. Cultural Fest")
        print("4. Sports Meet")
        print("5. Workshop")
        print("6. Seminar")
        print("7. Back")
        print("=============================")
        select = input("Select: ")
        if select == "1":
            print("Available Seats :", events["Hackathon"])
            choice = input("Register (yes/no): ")
            if choice == "yes":
                events["Hackathon"] = events["Hackathon"] - 1
                print("✅ Registration Successful")
                print("Remaining Seats :", events["Hackathon"])
        elif select == "2":
            print("Available Seats :", events["Technical Fest"])
            choice = input("Register (yes/no): ")
            if choice == "yes":
                events["Technical Fest"] = events["Technical Fest"] - 1
                print("✅ Registration Successful")
                print("Remaining Seats :", events["Technical Fest"])
        elif select == "3":
            print("Available Seats :", events["Cultural Fest"])
            choice = input("Register (yes/no): ")
            if choice == "yes":
                events["Cultural Fest"] = events["Cultural Fest"] - 1
                print("✅ Registration Successful")
                print("Remaining Seats :", events["Cultural Fest"])
        elif select == "4":
            print("Available Seats :", events["Sports Meet"])
            choice = input("Register (yes/no): ")
            if choice == "yes":
                events["Sports Meet"] = events["Sports Meet"] - 1
                print("✅ Registration Successful")
                print("Remaining Seats :", events["Sports Meet"])
        elif select == "5":
            print("Available Seats :", events["Workshop"])
            choice = input("Register (yes/no): ")
            if choice == "yes":
                events["Workshop"] = events["Workshop"] - 1
                print("✅ Registration Successful")
                print("Remaining Seats :", events["Workshop"])
        elif select == "6":
            print("Available Seats :", events["Seminar"])
            choice = input("Register (yes/no): ")
            if choice == "yes":
                events["Seminar"] = events["Seminar"] - 1
                print("✅ Registration Successful")
                print("Remaining Seats :", events["Seminar"])
        elif select == "7":
            break
        else:
            print("❌ Invalid Selection")

# Notifications 
def notifications():
    print("--------🔔NOTIFICATIONS--------")
    print("1. DSA attendance is below 75%")
    print("2. Internal Assessment 2 starts next week")
    print("3. Hackathon registration is open")
    print("4. Fee payment pending")
    print("5. Eligible for placement drive")

# Placements 
def placements():
    print("--------🎯PLACEMENTS--------")
    cgpa = 8.2
    attendance = 84
    backlogs = 0
    print("Company : Software Company A")
    print("Package : 8 LPA")
    if cgpa >= 7.5 and attendance >= 75 and backlogs == 0:
        print("✅ YOU ARE ELIGIBLE")
    else:
        print("❌ NOT ELIGIBLE")

# Complaints 
def complaints():
    print("--------📝COMPLAINTS--------")
    print("1. Academics")
    print("2. Library")
    print("3. Infrastructure")
    category = input("Select Category: ")
    complaint = input("Enter Complaint: ")
    print("✅ Complaint Submitted")
    print("Complaint ID : CMP1045")
    print("Status : SUBMITTED")

# My activity 
def my_activity():
    activities = [
        "Student Registered",
        "Logged into Portal",
        "Registered for Hackathon",
        "Paid Exam Fee",
        "Joined Coding Club"
    ]
    print("-------📌ACTIVITY HISTORY-------")
    for activity in activities:
        print(activity)

# Overall Summary 
def overall_summary(student_id):
    print("======================")
    print("---👨‍🎓STUDENT SUMMARY---")
    print("======================")
    print("Name :", candidate[student_id]["name"])
    print("Department :", candidate[student_id]["department"])
    print("Year :", candidate[student_id]["year"])
    print("CGPA : 8.2")
    print("Attendance : 84%")
    print("Clubs Joined : 2")
    print("Events Joined : 1")
    print("Complaints : 1")
    print("Fee Pending : 0")
    print("Placement : ELIGIBLE")

# Faculty Login 
def faculty_login():
    while True:
        print("=============================")
        print("-----👨‍🏫FACULTY DASHBOARD-----")
        print("=============================")
        print("1. View Students")
        print("2. Update Attendance")
        print("3. Enter Marks")
        print("4. View Class Performance")
        print("5. View Attendance Shortage")
        print("6. View Student Complaints")
        print("7. Notifications")
        print("8. Logout")
        print("=============================")
        select = input("Select: ")
        if select == "1":
            print("Total Students:", len(candidate))
            for student_id in candidate:
                print(student_id, "-", candidate[student_id]["name"])
        elif select == "2":
            print("Attendance Updated")
        elif select == "3":
            print("Marks Entered")
        elif select == "4":
            print("Class Performance : Good")
        elif select == "5":
            print("Students Below 75% Attendance")
            print("ST102 - Rahul")
        elif select == "6":
            print("Projector not working in Lab 3")
        elif select == "7":
            print("Internal Assessment starts next week")
        elif select == "8":
            break
        else:
            print("Invalid Selection")

# Admin Login
def admin_login():
    while True:
        print("=============================")
        print("***🔐ADMIN DASHBOARD***")
        print("=============================")
        print("1. View All Students")
        print("2. Search Student")
        print("3. Sort Students")
        print("4. Filter Students")
        print("5. College Overview")
        print("6. Logout")
        print("=============================")
        select = input("Select: ")
        if select == "1":
            print("=============================")
            print("ALL STUDENTS")
            print("=============================")
            for student_id in candidate:
                print("ID:", student_id)
                print("Name:", candidate[student_id]["name"])
                print("Department:", candidate[student_id]["department"])
                print("-------------------")
        elif select == "2":
            search_student()
        elif select == "3":
            sort_students()
        elif select == "4":
            filter_students()
        elif select == "5":
            college_overview()
        elif select == "6":
            print("Logged Out")
            break
        else:
            print("Invalid Selection")

# Search student 
def search_student():
    print("=============================")
    print("-------🔍SEARCH STUDENT--------")
    print("=============================")
    search = input("Enter Student Name: ").lower()
    found = False
    for student_id in candidate:
        if search in candidate[student_id]["name"].lower():
            print("ID:", student_id)
            print("Name:", candidate[student_id]["name"])
            print("Department:", candidate[student_id]["department"])
            found = True
    if found == False:
        print("Student Not Found")

# Sort student 
def sort_students():
    print("=============================")
    print("------🔃SORTED STUDENTS--------")
    print("=============================")
    names = []
    for student_id in candidate:
        names.append(candidate[student_id]["name"])
    names.sort()
    for name in names:
        print(name)

# Filter students 
def filter_students():
    print("=============================")
    print("-------📋FILTER STUDENTS-------")
    print("=============================")
    year = input("Enter Year: ")
    found = False
    for student_id in candidate:
        if candidate[student_id]["year"] == year:
            print(student_id,
                  candidate[student_id]["name"])
            found = True
    if found == False:
        print("No Students Found")

# College overview 
def college_overview():
    print("=============================")
    print("-------🏫COLLEGE OVERVIEW-------")
    print("=============================")
    print("Total Students :", len(candidate))
    print("Departments : 5")
    print("Faculty : 25")
    print("Active Clubs : 6")
    print("Events This Year : 5")
    print("Average Attendance : 86%")
    print("Placement Eligible : 50")
    print("Pending Complaints : 2")
    print("=============================")

# student registration 
def new_student_registration():
    print("=============================")
    print("***📝STUDENT REGISTRATION***")
    print("=============================")
    student_id=input("Enter student ID: ")
    if student_id in candidate:
        print("This Student id is already exists")
        return
    student_name=input("Enter student name: ")
    if student_name=="":
        print("This field should not be empty")
        return
    department=input("Enter department: ")
    if department=="":
        print("This field should not be empty")
        return
    year=input("Enter year: ")
    if year=="1" or year=="2" or year=="3" or year=="4":
        print("✅This is a valid year")
    else:
        print("❌This year is not valid")
        return
    section=input("Enter section: ")
    if section=="":
        print("This field should not be empty")
        return
    email=input("Enter email: ")
    if "@" in email and "." in email:
        print("✅This is a valid email address")
    else:
        print("❌This mail is not valid")
        return
    while True:
        mobile=input("Enter mobile number: ")
        if len(mobile)==10 and mobile.isdigit():
            print("✅It is valid number")
            break
        else:
            print("❌The number is not valid")
    password=input("Enter password: ")
    if password=="":
        print("The password should not be empty")
        return
    else:
        print("*"*len(password))
    candidate[student_id]={
        "name":student_name,
        "department":department,
        "year":year,
        "section":section,
        "email":email,
        "mobile":mobile,
        "password":password,
    }
    print("✅Registration successful!")
    print(candidate)

# Explore college 
def explore_college():
    print("=============================")
    print("***🏫EXPLORE COLLEGE***")
    print("=============================")
    print("College Name : ISTS Engineering College")
    print("Departments : CSE, ECE, AI, CAI, AIML")
    print("Faculty Count : 5")
    print("Student Count : 120")
    print("Library Books : 5000+")
    print("Placement Rate : 90%")
    print("Campus Area : 50 Acres")
    print("=============================")
    input("Press Enter to continue...")

# Help menu 
def help_menu():
    print("=============================")
    print("***❓HELP MENU***")
    print("=============================")
    print("1. Student Login")
    print("Login using Student ID and Password")
    print()
    print("2. Registration")
    print("Create a new student account")
    print()
    print("3. Forgot Password")
    print("Contact Admin")
    print()
    print("4. Contact")
    print("Email : support@campus360.com")
    print("Phone : 9876543210")
    print("=============================")
    input("Press Enter to continue...")
main_menu()