menu = [
    ("Chicken Burger","Burger με κοτόπουλο,bacon,τυρί edam,τομάτα,μαρούλι με μαγιονέζα", 4.20),
    ("Ham Burger","Burger με μπιφτέκι,τυρί,κέτσαπ,μουστράρδα", 2.85),
    ("Green Burger","Burger με ζουμερό μπιφτέκι,τυρί,φρέσκεια τομάτα,μαρούλι,κρεμμύδι,πίκλες,κέτσαπ και dressing sauce", 4.20),
    ("Club Sandwich","Club sandwich ,με 3 πλούσιες στρώσεις Philadelphia σε φρυγανισμένο ψωμί του τοστ με ζουμερό φιλέτο κοτόπουλο,bacon,τομάτα,μαρούλι και τηγανητές πατάτες", 10.90),
    ("Σαλάτα Ceasar's","Δροσερή πράσινη σαλάτα με ζουμερό κοτόπουλο σε βάση μαρουλιού,με καλαμπόκι,κρουτόν,τριμμένο τυρί και vinaigrette ελαιολάδου", 6.90),
    ("Κινόα με Λαχανικά","Δροσερή σαλάτα με κινόα,κόκκινη πιπεριά,τοματίνια,αγγούρι,δυόσμο,φρέσκο μαιντανό και sauce ελαιολάδου", 6.30)
]

order = []

def display_menu():
    print("Μενού:")
    for i, item in enumerate(menu):
      print(f"{i+1}. {item[0]} - {item[1]} - {item[2]} €")

def start_order():
    while True:
        display_menu()
        choice = input("Επιλέξτε αριθμό προιόντος που θέλετε να παραγγείλετε: ")
        quantity = int(input("Επιλέξτε αριθμό ποσότητας: "))
        order.append((menu[int(choice)-1][0], menu[int(choice)-1][2], quantity))
        print("Το προιόν προστέθηκε στην παραγγελία.")
        more_items = input("Θέλετε να παραγγείλετε κάτι άλλο απο το μενού? (ν/ο): ")
        if more_items.lower() != "ν":
            break

def display_order():
    if len(order) == 0:
        print("Δεν υπάρχουν προιόντα στην παραγγελία.")
    else:
        print("Παραγγελία:")
        total = 0
        for item in order:
            item_total = item[1] * item[2] 
            print(f"{item[0]} - Ποσότητα: {item[2]} - Τιμή: {item_total} ευρώ")
            total += item_total
        print(f"Συνολική Τιμή: {total} ευρώ")


def remove_item(order):
    if len(order) == 0:
        print("Η παραγγελία σας είναι άδεια.")
        return order

    print("Τρέχουσα Παραγγελία:")
    for i, item in enumerate(order):
        print(f"{i+1}. {item[0]} - Ποσότητα: {item[2]} - Τιμή: {item[1]:.2f}€")
    
    try:
        item_num = int(input("Επιλέξτε αριθμό προιόντος για αφαίρεση: "))
        if item_num < 1 or item_num > len(order):
            print("Λάθος Αριθμός Προιόντος.")
            return order
        else:
            item = order.pop(item_num-1)
            print(f"Το προιόν {item[0]} αφαιρέθηκε απο την παραγγελία.")
            return order
    except ValueError:
        print("Λάθος Εισαγωγή.")
        return order
    

def payment():
    if len(order) == 0:
        print("Δεν υπάρχουν προιόντα στην παραγγελία.")
    else:
        display_order()
        print("Η πληρωμή ολοκληρώθηκε.Ευχαριστούμε για την προτίμηση.")

while True:
    print("\nΕπιλογές:")
    print("==========")
    print("1. Έναρξη Παραγγελίας")
    print("2. Εμφάνιση Παραγγελίας")
    print("3. Αφαίρεση προιόντος από την παραγγελία")
    print("4. Πληρωμή")

    choice = input("Επιλέξτε αριθμό: ")

    if choice == "1":
        start_order()
    elif choice == "2":
        display_order()
    elif choice == "3":
        remove_item(order)
    elif choice == "4":
        payment()
        break
    else:
        print("Λανθασμένη Επιλογή.Παρακαλώ επιλέξτε ξανά")