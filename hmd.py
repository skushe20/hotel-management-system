import tkinter as tk

def open_main_app():
    welcome.destroy()

welcome = tk.Tk()
welcome.title("Welcome - Hotel Gupta Palace")
welcome.geometry("1000x600")
welcome.resizable(False, False)
welcome.configure(bg="#081226")

canvas = tk.Canvas(welcome, width=1000, height=600, highlightthickness=0, bg="#081226")
canvas.pack(fill="both", expand=True)

for i, color in enumerate(["#07263f", "#0a2f4f", "#0f3f63"]):
    canvas.create_rectangle(0, i*200, 1000, (i+1)*200, fill=color, outline="")

shadow = canvas.create_rectangle(200+8, 150+8, 800+8, 450+8, fill="#071826", outline="", stipple="gray50")
panel = tk.Frame(welcome, bg="#162a41")
panel.place(x=200, y=150, width=600, height=300)

title = tk.Label(panel, text=" WELCOME TO HOTEL GUPTA PALACE", font=("Georgia", 22, "bold"), bg="#162a41", fg="#F8FBFF")
title.pack(pady=(28, 6))

sub = tk.Label(panel, text="Luxury • Comfort • Hospitality", font=("Helvetica", 14, "italic"), bg="#162a41", fg="#DCC08A")
sub.pack(pady=4)

sep = tk.Frame(panel, bg="#D4A45A", height=4, width=460)
sep.pack(pady=16)

btn_frame = tk.Frame(panel, bg="#162a41")
btn_frame.pack(pady=8)

def on_enter(e):
    continue_btn.config(bg="#e0b85f")
    continue_btn.config(width=18)

def on_leave(e):
    continue_btn.config(bg="#c9a36a")
    continue_btn.config(width=16)

continue_btn = tk.Button(btn_frame, text="ENTER →", font=("Verdana", 16, "bold"), bg="#c9a36a", fg="#081226",
                         activebackground="#e0b85f", activeforeground="#081226", relief="flat", width=16, height=1,
                         command=open_main_app)
continue_btn.pack(pady=4)
continue_btn.bind("<Enter>", on_enter)
continue_btn.bind("<Leave>", on_leave)


def fade_in(a=0.0):
    if a <= 1.0:
        welcome.attributes("-alpha", a)
        welcome.after(18, lambda: fade_in(a+0.04))

welcome.attributes("-alpha", 0.0)
fade_in()

welcome.mainloop()
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="kushe2008",database="hotel_db")
cur=db.cursor()
def add():
    print("ADD NEW CUSTOMER")
    name=input("ENTER CUSTOMER NAME")
    phone=int(input("ENTER THE CUSTOMER NUMBER"))
    roomno=int(input("ENTER ROOM NUMBER"))
    checkin=input("ENTER CHECK IN DATE (YYYY-MM-DD)")
    checkout=input("ENTER CHECK OUT DATE (YYYY-MM-DD)")
    totpay=input("ENTER THE AMOUNT")
    print("\nROOM TYPES: 1. DELUXE  2. SEMIDELUXE  3. STANDARD")
    room_choice = input("ENTER ROOM TYPE (1/2/3): ")
    
    if room_choice=='1':
        roomtype='DELUXE'
    elif room_choice=='2':
        roomtype='SEMIDELUXE'
    else:
        roomtype='STANDARD'
    cur.execute("""
        INSERT INTO customers(name, mobile, room_no, check_in, check_out, room_type,totalamount)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, phone, roomno, checkin, checkout, roomtype, totpay))
    db.commit()
    print("RECORD INSERTED")

def search():
    print("SEARCH  CUSTOMER")
    ph=int(input("ENTER THE PHONE NUMBER"))
    cur.execute("SELECT *  FROM customers WHERE mobile=%s", (ph,))
    data=cur.fetchone()
    if data:
        print("\nCustomer Details:")
        print(f"Name: {data[0]}")
        print(f"Mobile: {data[1]}")
        print(f"Room No: {data[2]}")
        print(f"Check-in:{data[3]}")
        print(f"Check-out: {data[4]}")
        print(f"Room Type: {data[5]}")
        print(f"total: {data[6]}")
    
    else:
        print("No record found.")
def viewall():
    cur.execute("SELECT * FROM customers")
    data=cur.fetchall()
    if not data:
        print("NO CUSTOMERS FOUND")
    else:
        for d in data:
            print(f'''
Name: {d[0]}\t\tMobile: {d[1]}\t\tRoom No: {d[2]}
Check-in: {d[3]}\tCheck-out: {d[4]}\tRoom Type: {d[5]}
Total: {d[6]}''')
def delete():
    print("DELETE CUSTOMER RECORD")
    room=int(input("ENTER ROOM NO TO DELETE"))
    cur.execute("SELECT * FROM customers WHERE room_no=%s",(room,))
    data=cur.fetchone()
    if data:
        cur.execute("DELETE FROM customers WHERE room_no=%s",(room,))
        db.commit()
        print("CUSTOMER RECORD DELETED SUCESSFULLY")
    else:
        print("NO RECORD FOUND")

def update():
    print("\n--- Update Customer Details ---")
    mob = input("ENTER MOBILE NO OF CUSTOMER: ")
    cur.execute("SELECT * FROM customers WHERE mobile=%s", (mob,))
    data = cur.fetchone()

    if data:
        print("What do you want to update?")
        print("1. Check-out date")
        print("2. Room type")
        print("3. Payment details")
        choice = input("Enter your choice: ")

        if choice == '1':
            newda= input("Enter new check-out date (YYYY-MM-DD): ")
            cur.execute("UPDATE customers SET check_out=%s WHERE mobile=%s", (newda, mob))
        elif choice == '2':
            newty = input("Enter new room type: ")
            cur.execute("UPDATE customers SET room_type=%s WHERE mobile=%s", (newty, mob))
        elif choice == '3':
            newamt = float(input("Enter new  amount: "))
            cur.execute("UPDATE customers SET  totalamount=%s  WHERE mobile=%s",
                        ( newamt, mob))
        else:
            print("Invalid choice.")
            return

        db.commit()
        print("Customer details updated successfully.")
    else:
        print("No customer found with that mobile number.")


while True:
    print("\n========== HOTEL GUPTA PALACE  ==========")
    print("1. ADD CUSTOMER")
    print("2. SEARCH CUSTOMER")
    print("3. UPDATE CUSTOMER")
    print("4. DELETE CUSTOMER")
    print("5. VIEW ALL CUSTOMER")
    print("6. EXIT")
    choice = input("Enter your choice: ")

    if choice == '1':
        add()
    elif choice == '2':
        search()
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        viewall()
    elif choice == '6':
        print("Thank you for visiting Hotel Gupta Palace!")
        break
    else:
        print("Invalid choice,Please try again.")
