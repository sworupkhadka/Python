class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)            # sum of all marks
        avg = total / 3                    # divide by number of marks
        print(f"Hi {self.name}, your average score is: {avg}")

s1 = student("ram", [100, 90, 80])
s1.get_avg()

s2=student("thanos", [20,40,90])
s2.get_avg()