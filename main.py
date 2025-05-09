class Artist:
    def __init__(self, name, art_class, skill_level, exhibitions, coaching_hours):
        self.name = name
        self.art_class = art_class
        self.skill_level = skill_level
        self.exhibitions = exhibitions
        self.coaching_hours = coaching_hours
        self.class_fees = {
            "Beginner": 15000.00,
            "Intermediate": 20000.00,
            "Advanced": 25000.00
        }

    def calculate_total_cost(self):
        coaching_fee = self.coaching_hours * 4 * 5000  # 4 weeks/month
        exhibition_fee = self.exhibitions * 10000 if self.skill_level in ["Intermediate", "Advanced"] else 0
        class_fee = self.class_fees.get(self.art_class, 0)
        total = class_fee + coaching_fee + exhibition_fee
        return class_fee, coaching_fee, exhibition_fee, total

def input_artist_data():
    name = input("Enter artist's name: ")

    while True:
        art_class = input("Enter class/workshop (Beginner, Intermediate, Advanced): ").title()
        if art_class in ["Beginner", "Intermediate", "Advanced"]:
            break
        print("Invalid class. Please enter Beginner, Intermediate, or Advanced.")

    while True:
        skill_level = input("Enter skill level (Beginner, Intermediate, Advanced): ").title()
        if skill_level in ["Beginner", "Intermediate", "Advanced"]:
            break
        print("Invalid skill level. Please enter Beginner, Intermediate, or Advanced.")

    exhibitions = 0
    if skill_level in ["Intermediate", "Advanced"]:
        try:
            exhibitions = int(input("Enter number of exhibitions participated in this month: "))
        except ValueError:
            print("Invalid input. Setting exhibitions to 0.")
            exhibitions = 0

    try:
        coaching_hours = int(input("Enter number of private coaching hours per week (Max 5): "))
        if coaching_hours > 5:
            print("Max allowed is 5 hours. Setting to 5.")
            coaching_hours = 5
    except ValueError:
        print("Invalid input. Setting coaching hours to 0.")
        coaching_hours = 0

    return Artist(name, art_class, skill_level, exhibitions, coaching_hours)
