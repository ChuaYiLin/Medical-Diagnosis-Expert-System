from tkinter import *
from tkinter import messagebox
from experta import *

# -------------------------------
# Expert System
# -------------------------------
class Symptoms(Fact):
    fever = Field(str)
    cough = Field(str)
    breathing = Field(str)

class CovidExpert(KnowledgeEngine):

    @Rule(Symptoms(fever=MATCH.f, cough=MATCH.c, breathing=MATCH.b))
    def diagnose(self, f, c, b):
        # Count number of 'yes' symptoms
        yes_count = sum([f == 'yes', c == 'yes', b == 'yes'])
        if yes_count == 0:
            result = "Low risk of COVID-19"
        elif yes_count == 1:
            result = "Low risk of COVID-19"
        elif yes_count == 2:
            result = "Medium risk of COVID-19"
        else:  # yes_count == 3
            result = "High risk of COVID-19"
        self.declare(Fact(result=result))

    @Rule(Fact(result=MATCH.r))
    def show_result(self, r):
        self.result = r

# -------------------------------
# Tkinter GUI
# -------------------------------
def run_expert_system():
    engine = CovidExpert()
    engine.reset()
    engine.declare(Symptoms(
        fever=fever_var.get(),
        cough=cough_var.get(),
        breathing=breathing_var.get()
    ))
    engine.run()

    messagebox.showinfo("Diagnosis Result", engine.result)

# GUI setup
root = Tk()
root.title("COVID-19 Diagnosis Expert System")
root.geometry("420x320")

Label(root, text="COVID-19 Expert System",
      font=("Arial", 16, "bold")).pack(pady=15)

fever_var = StringVar(value="no")
cough_var = StringVar(value="no")
breathing_var = StringVar(value="no")

def add_selector(text, variable):
    frame = Frame(root)
    frame.pack(pady=5)
    Label(frame, text=text, width=22, anchor="w").pack(side=LEFT)
    OptionMenu(frame, variable, "yes", "no").pack(side=LEFT)

add_selector("Do you have fever?", fever_var)
add_selector("Do you have cough?", cough_var)
add_selector("Difficulty breathing?", breathing_var)

Button(root, text="Diagnose Now", font=("Arial", 12, "bold"),
       command=run_expert_system).pack(pady=20)

root.mainloop()