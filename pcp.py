from collections import deque

queue = deque()

def add_customer():
    name = input("Enter customer name: ")
    place = input("Enter destination: ")
    amount = int(input("Enter ticket amount: "))
    
    customer = {
        "name": name,
        "place": place,
        "amount": amount
    }
    
    queue.append(customer)
    print(f"Customer added: {customer}\n")

def serve_customer():
    if not queue:
        print("No customers to serve\n")
    else:
        customer = queue.popleft()
        print(f"Serving: {customer}\n")

def next_customer():
    if not queue:
        print("No customers in queue\n")
    else:
        print(f"Next customer: {queue[0]}\n")

def show_queue():
    if not queue:
        print("Queue is empty\n")
    else:
        print("Current Queue:")
        for c in queue:
            print(c)
        print()

# Menu
while True:
    print("Ticket Counter System")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. View Next Customer")
    print("4. Show Queue")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_customer()
    elif choice == '2':
        serve_customer()
    elif choice == '3':
        next_customer()
    elif choice == '4':
        show_queue()
    elif choice == '5':
        break
    else:
        print("Invalid choice\n")