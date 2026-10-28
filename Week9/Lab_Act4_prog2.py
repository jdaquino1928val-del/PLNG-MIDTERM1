class Date:
    """Structure class to represent date with year, month, and day members."""
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


class Patient:
    """Base class to store patient information."""
    def __init__(self, name, date_of_admission, disease, date_of_discharge):
        self.name = name
        self.date_of_admission = date_of_admission
        self.disease = disease
        self.date_of_discharge = date_of_discharge

    def display(self):
        print(f"1. Name of the patient: {self.name}")
        print(f"2. Date of admission: {self.date_of_admission}")
        print(f"3. Disease: {self.disease}")
        print(f"4. Date of discharge: {self.date_of_discharge}")


class PatientRecord(Patient):
    """Derived class to store the age of the patient."""
    def __init__(self, name, date_of_admission, disease, date_of_discharge, age):
        super().__init__(name, date_of_admission, disease, date_of_discharge)
        self.age = age

    def display(self):
        super().display()
        print(f"5. Age: {self.age}")


def parse_date(date_str):
    """Helper function to parse YYYY-MM-DD string into a Date object."""
    parts = list(map(int, date_str.replace('/', '-').split('-')))
    return Date(parts[0], parts[1], parts[2])


def main():
    patients = []

    while True:
        print("\nOUTPUT IN ACTIVITY 2")
        print("1. Insert New Patient")
        print("2. Display all Patient")
        print("3. Display pediatric patient")
        print("4. Exit")

        choice = input("Enter option: ")

        if choice == '1':
            name = input("1. Name of the patient: ")
            adm_str = input("2. Date of admission (YYYY-MM-DD): ")
            disease = input("3. Disease: ")
            dis_str = input("4. Date of discharge (YYYY-MM-DD): ")
            age = int(input("5. Age: "))

            patient = PatientRecord(
                name,
                parse_date(adm_str),
                disease,
                parse_date(dis_str),
                age
            )
            patients.append(patient)
            print("Patient added successfully!")

        elif choice == '2':
            if not patients:
                print("No patient records available.")
            else:
                print("\n--- List of All Patients ---")
                for idx, p in enumerate(patients, 1):
                    print(f"\nPatient {idx}:")
                    p.display()

        elif choice == '3':
            pediatric_patients = [p for p in patients if p.age < 12]
            if not pediatric_patients:
                print("No pediatric patients found (less than 12 years old).")
            else:
                print("\n--- Pediatric Patients (< 12 Years Old) ---")
                for idx, p in enumerate(pediatric_patients, 1):
                    print(f"\nPediatric Patient {idx}:")
                    p.display()

        elif choice == '4':
            print("Exiting database program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()