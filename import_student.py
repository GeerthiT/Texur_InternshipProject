import csv
#from Lexicon_App.models import Student
from Lexicon_App.models import Student

def import_students(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Student.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email']
            )

if __name__ == '__main__':
    csv_file_path = 'C:\\Users\\geert\\OneDrive\\Desktop\\course_list.csv'  # Replace with your actual file path
    import_students(csv_file_path)