class PayoutDepartment:
    def __init__(self, department_name: str):
        self.department_name = department_name
        self.payouts = []

    def add_payout(self, payout: float):
        self.payouts.append(payout)

    def get_total_payout(self) -> float:
        return sum(self.payouts)

    def __str__(self):
        return f"Department: {self.department_name}, Total Payout: {self.get_total_payout()}"
    