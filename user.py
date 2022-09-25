from course import Course
import copy

class User: 
    email = ""
    pwd = ""
    logged_in = False
    courses = []
    allUsers = []
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
        User.allUsers.append(self)
    
    def print_info(self):
        print(self.email)
        print(self.pwd)

    def chg_pwd(self, new_pwd):
        if self.logged_in == True:
            print("Password changed!")
            self.pwd = new_pwd
        else:
            print("User not logged in, please log in first!")

    def log_in(email, pwd):
        for user in User.allUsers:
            if email == user.email and pwd == user.pwd:
                user.logged_in = True
                print(user.email + " is logged in!")
                return user
        print("Username or password is incorrect!")
        return None
    def log_out(user):
        user.logged_in = False
        print(user.email + " is logged out!")

    def add_course(self, course):
        if type(course) is Course:
            self.courses.append(copy.copy(course))

user1 = User("sam", "1234")
user2 = User("kathryn", "2345")
user1.chg_pwd("dinosaur")
User.log_in("sam", "2345")
User.log_in("sam", "1234")
user1.chg_pwd("dinosaur")