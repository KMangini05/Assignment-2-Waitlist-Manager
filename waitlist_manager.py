# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def _init_(self, name):
        self.name = name #Stores names of each customer in waiting list
        self.next = None #Reference to next node in the list
    



# Create a LinkedList class to manage the waitlist
class Waitlist:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def _init_(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name) #Create new node
        new_node.next = self.head #Next for new node becomes current head
        self.head = new_node #Head now points to new node

    def add_end(self, name):
        new_node = Node(name) #Create new node
        if not self.head:
            self.head = new_node #If list is empty, make new node the head
            return
        last = self.head
        while last.next : #Otherwise, traverse list to find last node
            last = last.next
        last.next = new_node #Makes new node the next node of last node

    def remove(self, name):
        current = self.head #Start at the head
        previous = None #Previous node (starts as None)

        while current:
            if current.name == name: #Customer to remove
                if previous is None: #Custome is at the front
                    self.head = current.next
                else:
                    previous.next = current.next #Customer is in middle or end
                return #Exit aafter removing name
            #Moving to next node
            previous = current
            current = current.next
            
    def print_list(self):
        current = self.head #Starts from the head of list
        if not current:
            print("Waitlist is empty.")
        else:
            while current:
                print(current.name)
                current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = Waitlist()
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
My list works by implemeting the use of custom linked lists.Each customer will be stores in a node that will hold their name with reference to the next node.
In order to keep these nodes organized, I used the Waitlist class. This class supports the usage of adding, removing, and printing customers into the current waitlist.

- What role does the head play?
The head references the first node in the list. It has a direct access point the the entire list, allowing for operations/codes such as adding, removing, or printing customers to be accessed.
If the head responds as "None," the list is empty. When the head is changed (like when adding and removing customers), the entire stucture will be affected.

- When might a real engineer need a custom list like this?
A real engineer might use a custom list like this in a system for managing the waitlist at a busy restaurant. Customers will arrive at different times, but often times, customers aren't put in order from arrival but rather due to availability.
Availability meaning that some parties are large which means they may not get in as fast as a smaller party due to the occupancy of the restaurant at that time. Some restaurants even consider specific people such as celebrities or people coming for a special event over other none famous people.
Someone who has made a reservation for a specific time days in advance will also get priority over someone who walks in at that time because they called ahead, this will call for them to have an assigned spot in the chart while other names/parties are added around them.
By using a linked list, it would make it easier for them to add/remove customers without shifting the entire list all day.
'''
