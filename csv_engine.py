class CSVEngine:
    def __init__(self, header: str):
        self.id: str
        self.name:str
        self.email: str
        self.department: str
        self.hours_worked: int
        self.hourly_rate: float
        self.id_index: int
        self.name_index: int
        self.email_index: int
        self.department_index: int
        self.hours_worked_index: int
        self.hourly_rate_index: int

        header_parts = header.strip().split(',')
        self.id_index = header_parts.index('id')
        self.name_index = header_parts.index('name')
        self.email_index = header_parts.index('email')
        self.department_index = header_parts.index('department')
        self.hours_worked_index = header_parts.index('hours_worked')

        indexes = list(range(len(header_parts)))
        indexes.remove(self.id_index)
        indexes.remove(self.name_index)
        indexes.remove(self.email_index)
        indexes.remove(self.department_index)
        indexes.remove(self.hours_worked_index)
        self.hourly_rate_index = indexes[0]

    def csv_data(self, in_str: str) -> tuple:
        """Parse a CSV line and set values."""
        parts = in_str.strip().split(',')
        self.id = parts[self.id_index]
        self.name = parts[self.name_index]
        self.email = parts[self.email_index]
        self.department = parts[self.department_index]
        self.hours_worked = int(parts[self.hours_worked_index])
        self.hourly_rate = float(parts[self.hourly_rate_index])
