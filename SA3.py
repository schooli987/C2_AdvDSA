from collections import deque
# Queues
normal_queue = deque()
vip_queue = deque()

# Settings
order_id = 100
MAX_SIZE = 5

def place_order():
    global order_id
    
    if len(vip_queue) + len(normal_queue) >= MAX_SIZE:
        print("Queue Overflow: Cannot accept more orders\n")
        return
    
    name = input("Enter customer name: ")
    item = input("Enter food item: ")
    priority = input("Priority (VIP/Normal): ").lower()
    
    order_id += 1
    order = {"id": order_id, "name": name, "item": item}
    
    if priority == "vip":
        vip_queue.append(order)
        print(f"VIP Order Placed: {order}\n")
    else:
        normal_queue.append(order)
        print(f"Normal Order Placed: {order}\n")

# Serve order (Dequeue)
def serve_order():
    # Underflow check
    if not vip_queue and not normal_queue:
        print("Queue Underflow: No orders to serve\n")
        return
    
    if vip_queue:
        order = vip_queue.popleft()   # Dequeue
        print(f"Serving VIP Order: {order}\n")
    else:
        order = normal_queue.popleft()  # Dequeue
        print(f"Serving Normal Order: {order}\n")

# Peek (Front element)
def next_order():
    if vip_queue:
        print(f"Next Order (VIP): {vip_queue[0]}\n")
    elif normal_queue:
        print(f"Next Order (Normal): {normal_queue[0]}\n")
    else:
        print("No pending orders\n")

# Display all orders
def show_orders():
    if not vip_queue and not normal_queue:
        print("No orders in system\n")
        return
    
    print("\nVIP Orders:")
    for order in vip_queue:
        print(order)
    
    print("\nNormal Orders:")
    for order in normal_queue:
        print(order)
    
    print()

# Menu
while True:
    print("Activity 1 - Enqueue")
    print("1. Place Order")
    print("2. Serve Order")
    print("3. Show next order")
    print("4. Display all orders")
    choice = input("Enter choice: ")
    
    if choice == '1':
        place_order()
    elif choice == '2':
        serve_order()
    elif choice == '3':
        next_order()
    elif choice == '4':
        show_orders()

    else:
        print("Invalid choice\n")