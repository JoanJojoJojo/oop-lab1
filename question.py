# Question One solution
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __repr__(self):
        return f"{self.course_code} - {self.course_name}"

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.enrolled_courses = []  

    def enroll(self, course_name):
        if course_name in self.enrolled_courses:
            print(f"{self.name} is already enrolled in {course_name}.")
        else:
            self.enrolled_courses.append(course_name)
            print(f"{self.name} enrolled in {course_name}.")

    def drop(self, course_name):
        if course_name in self.enrolled_courses:
            self.enrolled_courses.remove(course_name)
            print(f"{self.name} dropped {course_name}.")
        else:
            print(f"Cannot drop {course_name} — {self.name} is not enrolled in it.")

    def display_student_info(self):
        print(f"Student name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled courses:")
        if not self.enrolled_courses:
            print("  None")
        else:
            for c in self.enrolled_courses:
                print(" ", c)



s1 = Student("Alice", 20, "S001")
s2 = Student("Bob", 21, "S002")

s1.enroll("Mathematics")
s1.enroll("Physics")
s2.enroll("Biology")
s2.enroll("Chemistry")


s1.drop("Physics")
s1.drop("History")  


print()
s1.display_student_info()
print()
s2.display_student_info()


# Question Two solution

class Book:
    def __init__(self, title, author, copies_available=1):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def __repr__(self):
        return f"'{self.title}' by {self.author} (copies: {self.copies_available})"


class Library:
    total_books = 0  

    def __init__(self):
        self.books = {}  

    def add_book(self, title, author, copies=1):
        if title in self.books:
            self.books[title].copies_available += copies
        else:
            self.books[title] = Book(title, author, copies)
        Library.total_books += copies
        print(f"Added {copies} copies of '{title}'. Total books now: {Library.total_books}")

    def borrow_book(self, title):
        if title not in self.books:
            print(f"'{title}' not found in the library.")
            return
        book = self.books[title]
        if book.copies_available <= 0:
            print(f"'{title}' is currently not available for borrowing.")
        else:
            book.copies_available -= 1
            Library.total_books -= 1
            print(f"You borrowed '{title}'. Copies left: {book.copies_available}")

    def return_book(self, title):
        if title not in self.books:
            
            self.books[title] = Book(title, "Unknown", 1)
            print(f"Returned '{title}'. Book added to library.")
        else:
            self.books[title].copies_available += 1
            print(f"Returned '{title}'. Copies available: {self.books[title].copies_available}")
        Library.total_books += 1

    def display_library_info(self):
        print("Library contents:")
        if not self.books:
            print("  No books.")
        else:
            for book in self.books.values():
                print(" ", book)
        print("Total copies in library (class var):", Library.total_books)



lib = Library()
lib.add_book("1984", "George Orwell", 3)
lib.add_book("To Kill a Mockingbird", "Harper Lee", 2)
lib.add_book("Python Programming", "A. Author", 1)

lib.borrow_book("1984")
lib.borrow_book("Python Programming")
lib.borrow_book("Python Programming")  

lib.return_book("Python Programming")
lib.return_book("A Book Not Present")  

print()
lib.display_library_info()


# Question Three solution

class MenuItem:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def order(self):
        return f"{self.name} - {self.price:.2f}"

    def __repr__(self):
        return f"{self.name} ({'Available' if self.available else 'Unavailable'}) - {self.price:.2f}"


class Drink(MenuItem):
    def __init__(self, name, price, size="Medium", available=True):
        super().__init__(name, price, available)
        self.size = size

    def order(self):
        return f"Drink: {self.name} ({self.size}) - UGX {self.price:.2f}"


class Food(MenuItem):
    def __init__(self, name, price, is_vegetarian=False, available=True):
        super().__init__(name, price, available)
        self.is_vegetarian = is_vegetarian

    def order(self):
        veg = "Vegetarian" if self.is_vegetarian else "Non-vegetarian"
        return f"Food: {self.name} - {veg} - UGX {self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []  

    def add_item(self, item):
        if not item.available:
            print(f"Sorry, {item.name} is not available.")
            return
        self.items.append(item)
        print(f"Added to order: {item.order()}")

    def remove_item(self, item_name):
        for i, it in enumerate(self.items):
            if it.name == item_name:
                removed = self.items.pop(i)
                print(f"Removed from order: {removed.name}")
                return
        print(f"Item {item_name} not found in order.")

    def display_order(self):
        print("Order details:")
        total = 0.0
        if not self.items:
            print("  (order is empty)")
        else:
            for it in self.items:
                print(" ", it.order())
                total += it.price
        print(f"Total price: UGX {total:.2f}")



d1 = Drink("Coke", 2000, size="Large")
d2 = Drink("Mineral Water", 1000, size="Small", available=False)
f1 = Food("Burger", 5000, is_vegetarian=False)
f2 = Food("Salad", 4000, is_vegetarian=True)

order = Order()
order.add_item(d1)
order.add_item(d2)
order.add_item(f1)
order.add_item(f2)

order.remove_item("Pizza")  
order.remove_item("Burger")

print()
order.display_order()


# Question Four solution

class Device:
    def __init__(self, device_name, location, status=False):
        self.device_name = device_name
        self.location = location
        self.status = status  

    def __repr__(self):
        state = "On" if self.status else "Off"
        return f"{self.device_name} ({self.location}) - {state}"


class SmartHomeController:
    total_devices = 0

    def __init__(self):
        self.devices = {}  

    def add_device(self, device_name, location):
        if device_name in self.devices:
            print(f"Device '{device_name}' already exists.")
            return
        dev = Device(device_name, location, status=False)
        self.devices[device_name] = dev
        SmartHomeController.total_devices += 1
        print(f"Added device: {device_name} at {location}. Total devices: {SmartHomeController.total_devices}")

    def turn_on_device(self, device_name):
        dev = self.devices.get(device_name)
        if not dev:
            print(f"Device '{device_name}' not found. Cannot turn on.")
            return
        if dev.status:
            print(f"Device '{device_name}' is already ON.")
        else:
            dev.status = True
            print(f"Device '{device_name}' turned ON.")

    def turn_off_device(self, device_name):
        dev = self.devices.get(device_name)
        if not dev:
            print(f"Device '{device_name}' not found. Cannot turn off.")
            return
        if not dev.status:
            print(f"Device '{device_name}' is already OFF.")
        else:
            dev.status = False
            print(f"Device '{device_name}' turned OFF.")

    def display_all_devices(self):
        print("Smart Home devices:")
        if not self.devices:
            print("  No devices in system.")
            return
        for d in self.devices.values():
            print(" ", d)
        print("Total devices (class var):", SmartHomeController.total_devices)


controller = SmartHomeController()
controller.add_device("LivingRoomLight", "Living Room")
controller.add_device("KitchenFan", "Kitchen")
controller.add_device("BedroomAC", "Bedroom")


controller.turn_on_device("LivingRoomLight")
controller.turn_on_device("KitchenFan")
controller.turn_off_device("BedroomAC")  
controller.turn_on_device("NonExisting") 

print()
controller.display_all_devices()
