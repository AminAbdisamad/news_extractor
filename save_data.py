import csv


def save_to_csv(*, file_name, data):
    with open(f"{file_name}.csv", mode="w") as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
    employee_writer.writerow(["John Smith", "Accounting", "November"])
    employee_writer.writerow(["Erica Meyers", "IT", "March"])
