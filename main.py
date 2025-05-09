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
