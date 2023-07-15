
import re
class ValidationError(ValueError):
    pass


class User:
    
    def __init__(self, username, password) -> None:
        self.username= username
        self.password= password


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not re.match('[a-zA-Z]{3,}', value):
            raise ValidationError("Invalid username!")
        self.__username= value


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not re.match('[a-zA-Z0-9]{8,}', value):
            raise ValidationError("Invalid password!")
        self.__password= value



    def check_user(self, user: str, password: str, users: dict):
        try:
            if users[user] and users[user]['password']== password:
                return True
        except:
            return False



    def signin(self, user: str, password: str, users: dict) -> bool:
        return self.check_user(user, password, users)


    def signup(self, fullname: str, username: str, password: str, email: str, users: dict) -> str:
        self.email = email
        self.fullname = fullname
        users[username]= {'fullname': fullname, 'password': password, 'email': email}
        return users
    

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError('Email must be a string')
        if not value.endswith('@gmail.com'):
            raise ValidationError('Invalid email format')
        self.__email= value
    
    @property
    def fullname(self):
        return self.__fullname
    
    @fullname.setter
    def fullname(self, value):
        if not isinstance(value, str):
            raise TypeError('Fullname must be a string')
        self.__fullname= value
        
