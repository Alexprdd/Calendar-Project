import tkinter as tk
import calendar

window=None
e1=None
def create_header(window, text):
    header = tk.Label(window, text=text, font=('Arial', 35, 'bold'), bg='grey', fg='black', padx=10, pady=5)
    header.pack(fill=tk.X)
    return header

def main():
    global window
    global e1

    window = tk.Tk()
    window.title("CALENDAR")

    create_header(window, "CALENDAR")

    content = tk.Label(window, text="Enter Year", font=('arial', 15),bg="lightgreen", fg="black")
    content.pack()

    e1=tk.Entry(window,text="type...",font=("Times", 20), bg="white", fg="grey",justify=tk.CENTER ,width=20, bd=4, relief=tk.SUNKEN)
    e1.pack()

    b1=tk.Button(window,text="Show Calendar",font=("arial", 15), bg="red", fg="black", command=show_calendar, width=15, height=2, bd=4, relief=tk.SUNKEN)
    b1.pack()

    b2=tk.Button(window,text="Exit",font=("arial", 15),command=window.destroy, bg="red", fg="black", width=5, height=2, bd=4, relief=tk.FLAT)
    b2.pack()
    window.mainloop()

def show_calendar():
    Wcalendar=tk.Toplevel(window)
    Wcalendar.title("Calendar")

    try:
        year=int(e1.get())
    except:
        errorLabel=tk.Label(Wcalendar,text="Error Detected-Year value not inserted", font=("Times",20))
        errorLabel.pack()
        return

    calData=calendar.calendar(year)
    
    calendarText=tk.Text(Wcalendar,font=("Times",20), wrap="none")

    calendarText.insert(tk.END, calData)
    calendarText.pack(expand=True, fill="both")

if __name__ == "__main__":
    main()

