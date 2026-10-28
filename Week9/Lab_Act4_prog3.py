class Professor:
    """Base class Professor with name and salary."""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Dean(Professor):
    """Derived class Dean adding department attribute."""
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def to_string(self):
        return (
            f"Status\n"
            f"Rank: Dean\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Salary: {self.salary}"
        )


class Executive(Dean):
    """Derived class Executive inheriting from Dean."""
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def to_string(self):
        # Displays "Rank: Executive" followed by superclass information
        dean_info = super().to_string()
        return dean_info.replace("Rank: Dean", "Rank: Executive")


# Test Program
if __name__ == "__main__":
    dean_obj = Dean("John Cena", 32000, "English")
    print(dean_obj.to_string())

    print()

    executive_obj = Executive("Ronald McDonald", 42000, "Computer Science")
    print(executive_obj.to_string())