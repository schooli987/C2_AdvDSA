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

# Menu
while True:
    print("Activity 1 - Enqueue")
    print("1. Place Order")
    print("2. Serve Order")
    choice = input("Enter choice: ")
    
    if choice == '1':
        place_order()
    elif choice == '2':
        serve_order()
    else:
        print("Invalid choice\n")