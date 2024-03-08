import tkinter as tk
from tkinter import ttk
import webbrowser
def play_video():
    webbrowser.open("https://www.youtube.com/watch?v=v2mNt2svPlY")
def play_video1():
    webbrowser.open("https://youtu.be/59z5yb5Dr4M?si=3hQbQTtnoSN5MRTd")
def submit():
    salaryincome = int(salary.get())
    try :
        rentalincome=int(income_from_rentals.get())
    except ValueError:
        rentalincome=0
    try :
       homeinterest=int(interest_on_home_loan.get())
    except ValueError:
        homeinterest=0

    try :
      NPS=int(nps.get())
    except ValueError:
        NPS=0

    try :
      healthinsurance=int(medical_care.get())

    except ValueError:
        healthinsurance=0
    income=salaryincome+rentalincome-homeinterest-NPS-healthinsurance

    # Calculate tax
    if income <= 0:
        show_error("Error", "Income should be a positive number.")
        return
    elif income <= 300000:
        tax = 0
        category = "Below poverty line"
    elif 700001 <= income <= 900000:
        tax = 15000 + (income - 600000) * 0.1
        category = "Lower middle class"
    elif 900001 <= income <= 1200000:
        tax = 30000 + (income - 900000) * 0.15
        category = "Middle class"
    elif 1200001 <= income <= 1500000:
        tax = 45000 + (income - 1200000) * 0.2
        category = "Higher middle class"
    else:
        tax = 60000 + (income - 1500000) * 0.3
        category = "Rich and wealthy"

    total_tax = tax + tax * 0.04

    # Create new window for displaying output
    output_window = tk.Toplevel(root)
    output_window.title("Tax Calculation Result")
    output_window.geometry("1400x800")


    # Display result in the new window
    result_label = tk.Label(output_window, text=f"Category: {category}\nIncome Tax: Rs. {tax:.2f}\nTotal Income Tax (including 4% education cess): Rs. {total_tax:.2f}", font=("Arial", 12), bg="lightblue")
    result_label.pack()

def show_error(title, message):
    error_window = tk.Toplevel(root)
    error_window.title(title)
    error_window.geometry("300x100")
    tk.Label(error_window, text=message).pack()

root = tk.Tk()
root.title("income tax through new income tax slab(2023)")
root.geometry("1800x850")

# Load image and resize
image = tk.PhotoImage(file="C:\\Users\\91879\\Desktop\\Logo_of_Income_Tax_Department_India.png")  # Change path to your image "C:\Users\91879\Desktop\Logo_of_Income_Tax_Department_India.png"
image = image.subsample(2)
image1 = tk.PhotoImage(file="C:\\Users\\91879\\Desktop\\newtax.png")  # Change path to your image
image1 = image1.subsample(1) # Increase the size by a factor of 2

# Display image
image_label = tk.Label(root, image=image)
image_label.place(x=450, y=10)
image_label1 = tk.Label(root, image=image1)
image_label1.place(x=1000, y=5)

# Create and position widgets
label1 = tk.Label(root, text="Enter your income", font=("Times New Roman", 12,"bold"))
label1.place(x=50, y=160)
salary = tk.Entry(root)
salary.place(x=290, y=160)
label2=tk.Label(root, text="Income from home rentals",font=("Times New Roman",12,"bold"))
label2.place(x=50,y=190)
income_from_rentals=tk.Entry(root)
income_from_rentals.place(x=290,y=190)
label3=tk.Label(root,text="Interest on home loan",font=("Times New Roman",12,"bold")).place(x=50,y=220)
interest_on_home_loan=tk.Entry(root)
interest_on_home_loan.place(x=290,y=220)
label4=tk.Label(root,text="NPS-national pension scheme",font=("Times New Roman",12,"bold")).place(x=50,y=250)
nps=tk.Entry(root)
nps.place(x=290,y=250)
label5=tk.Label(root,text="Medical insurace cost",font=("Time new roman",12,"bold")).place(x=50,y=280)
medical_care=tk.Entry(root)
medical_care.place(x=290,y=280)




submit_button = tk.Button(root, text="Submit", command=submit,fg="black")
submit_button.place(x=290, y=330)
video=tk.Button(root,text="Video link for how to calculate the income tax through income tax slab",command=play_video,fg="black")
video.place(x=50,y=400)

video1=tk.Button(root,text="To learn how to avoid income tax through section 80c",command=play_video1,fg="black")
video1.place(x=50,y=430)

root.mainloop()
