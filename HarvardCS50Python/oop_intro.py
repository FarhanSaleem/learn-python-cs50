class Student:
    def __init__(self, name, house):
        
        self.name = name
        self.house = house


    def __str__(self):
        return "a student"
    
    # Getter
    @property
    def name(self):
        return self._name 
    
    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter 
    # Setter is automatically called when you call code like student.house = ...
    @house.setter
    def house(self, house):
        if house not in ["Smyrna", "Atlanta", "Lawrenceville", "Marietta","Alpharetta"]:
            raise ValueError("Invalid area for house")
        self._house = house

def main():
    student = get_student()
    
    print(f"{student.name} from {student.house}")
    print(student)

def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

    # use Class
    
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()