from datetime import datetime, timedelta

class EmployeeTrainingPlatform:
    def __init__(self):
        self.employees = {}
        self.courses = {}

    def create_employee(self):
        employee_id = input("Enter Employee ID:")
        if len(employee_id) == 7 and employee_id.isalnum():
            if employee_id not in self.employees:
                name = input("Enter Employee Name: ")
                location = input("Enter Employee Location: ")
                self.employees[employee_id] = {'Name': name, 'Location': location, 'modules': []}
                print(f"Employee {name} Added Successfully.")
            else:
                print(f"Employee With ID {employee_id} Already Exists.")
        else:
            print("It Should be in the Format: EID** (Alpha-numeric)!")

    def read_employee(self):
        
        employee_id = input("Enter Employee ID To Read: ")
        if len(employee_id) == 7 and employee_id.isalnum():
            if employee_id in self.employees:
                employee_info = self.employees[employee_id]
                print(f"Employee ID: {employee_id}, Name: {employee_info['Name']}, Location: {employee_info['Location']}")
                self.display_assigned_courses(employee_info)
            else:
                print(f"Employee With ID {employee_id} Not Found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID To Update: ")
        if len(employee_id) == 7 and employee_id.isalnum():
            if employee_id in self.employees:
                name = input("Enter Updated Name (Press Enter To Skip): ")
                location = input("Enter Updated Location (Press Enter To Skip): ")

                employee_info = self.employees[employee_id]
                if name:
                    employee_info['Name'] = name
                if location:
                    employee_info['Location'] = location
                print(f"Employee {employee_id} Updated Successfully.")
            else:
                print(f"Employee With ID {employee_id} Not Found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID To Delete: ")
        if len(employee_id) == 7 and employee_id.isalnum():
            if employee_id in self.employees:
                del self.employees[employee_id]
                print(f"Employee {employee_id} Deleted Successfully.")
            else:
                print(f"Employee With ID {employee_id} Not Found.")

    def create_course(self):
        course_id = int(input("Enter Course No: "))
        title = input("Enter Course Title: ")
        description = input("Enter Course Description: ")
        instructor = input("Enter Trainer/Professor Name: ") 
        start_time_str = input("Enter Course Start Date (YYYY-MM-DD): ")
        duration_days = int(input("Enter Duration Of Course In Days: "))

        start_time = datetime.strptime(start_time_str, '%Y-%m-%d')
        end_time = start_time + timedelta(days=duration_days)

        self.courses[course_id] = {
            'Title': title,
            'Description': description,
            'Instructor': instructor,
            'Start Date': start_time,
            'End Date': end_time
        }
        print(f"Course {title} Added Successfully\nEnd Date: {end_time.strftime('%Y-%m-%d')}")

    def assign_module(self):
        employee_id = input("Enter Employee ID To Assign: ")
        if employee_id in self.employees:
            course_id = int(input("Enter Course No To Assign: "))
            if course_id in self.courses:
                if 'modules' not in self.employees[employee_id]:
                    self.employees[employee_id]['modules'] = []
                self.employees[employee_id]['modules'].append(course_id)
                print(f"Module Assigned Successfully To Employee {employee_id}.")
            else:
                print(f"Course With ID {course_id} Not Found.")
        else:
            print(f"Employee With ID {employee_id} Not Found.")

    def display_assigned_courses(self, employee_info):
        if 'modules' in employee_info:
            assigned_courses = employee_info['modules']
            if assigned_courses:
                print("Assigned Courses:")
                for course_id in assigned_courses:
                    course_info = self.courses[course_id]
                    print(f"  Course ID: {course_id}, Title: {course_info['Title']}, "
                          f"Instructor: {course_info['Instructor']}")
            else:
                print("No Courses Assigned.")
        else:
            print("No Courses Assigned.")

    def generate_training_progress(self):
        employee_id = input("Enter Employee ID To Generate Training Progress Report: ")
        if employee_id in self.employees:
            if 'modules' in self.employees[employee_id]:
                assigned_courses = self.employees[employee_id]['modules']
                total_created_courses = len(self.courses)
                total_assigned_courses = len(assigned_courses)

                if total_created_courses > 0:
                    assigned_percentage = (total_assigned_courses / total_created_courses) * 100
                    print(f"Training Progress For Employee {employee_id}: "
                          f"{total_assigned_courses} Courses Assigned Out Of {total_created_courses} Total Courses. "
                          f"Assigned Percentage: {assigned_percentage:.2f}%")
                else:
                    print("No Courses Created.")
            else:
                print(f"No Modules Assigned To Employee {employee_id}.")
        else:
            print(f"Employee With ID {employee_id} Not Found.")

    def generate_training_progress_all(self):
        if not self.employees:
            print("No Employees Found.")
            return

        for employee_id, employee_info in self.employees.items():
            if 'modules' in employee_info:
                assigned_courses = employee_info['modules']
                total_created_courses = len(self.courses)
                total_assigned_courses = len(assigned_courses)

                if total_created_courses > 0:
                    assigned_percentage = (total_assigned_courses / total_created_courses) * 100
                    print(f"Training Progress For Employee {employee_id}: "
                          f"{total_assigned_courses} Courses Assigned Out Of {total_created_courses} Total Courses. "
                          f"Assigned Percentage: {assigned_percentage:.2f}%")
                else:
                    print("No Courses Created.")
            else:
                print(f"No Modules Assigned To Employee {employee_id}.")

    def calculate_training_progress(self, start_time, end_time):
        current_time = datetime.now()
        total_duration = end_time - start_time
        elapsed_duration = current_time - start_time
        progress_percentage = (elapsed_duration / total_duration) * 100
        return min(progress_percentage, 100)

    def display_employees(self):
        if not self.employees:
            print("No Employees Found.")
        else:
            print("Employee List:")
            for employee_id, info in self.employees.items():
                print(f"ID: {employee_id}, Name: {info['Name']}, Location: {info['Location']}")
                self.display_assigned_courses(info)

    def display_courses(self):
        if not self.courses:
            print("No Courses Found.")
        else:
            print("Course List:")
            for course_id, info in self.courses.items():
                print(f"Course No: {course_id}, Title: {info['Title']}, Description: {info['Description']}, "
                      f"Instructor: {info['Instructor']}, "
                      f"Start Date: {info['Start Date'].strftime('%Y-%m-%d')}, "
                      f"End Date: {info['End Date'].strftime('%Y-%m-%d')}")

pf = EmployeeTrainingPlatform()

while True:
    print("\n1. Create Employee")
    print("2. Read Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Create Course")
    print("6. Display Employees")
    print("7. Assign Module")
    print("8. Generate Training Progress Report For Individual Employee")
    print("9. Generate Training Progress Report For All Employees")
    print("10. Display Courses")
    print("11. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        pf.create_employee()
    elif ch == 2:
        pf.read_employee()
    elif ch == 3:
        pf.update_employee()
    elif ch == 4:
        pf.delete_employee()
    elif ch == 5:
        pf.create_course()
    elif ch == 6:
        pf.display_employees()
    elif ch == 7:
        pf.assign_module()
    elif ch == 8:
        pf.generate_training_progress()
    elif ch == 9:
        pf.generate_training_progress_all()
    elif ch == 10:
        pf.display_courses()
    elif ch == 11:
        print("Exiting the Employee Training Platform.")
        break
    else:
        print("Invalid choice")
