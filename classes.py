
class PatientExam:
    def __init__(self, exam_ID: int, date: str, name: str, weight: int, height: float):
        self.exam_ID = exam_ID
        self.date = date
        self.name = name
        self.weight = weight
        self.height = height

    def get_BMI(self):
        return round(self.weight / (self.height ** 2), 2)

    def get_exam_month(self):
        return int(self.date.split("/")[0])

# patient_1 = PatientExam(1, "4/20/2007", "Jon Favreau", 50, 1.70)

# print(patient_1.get_BMI())

# print(patient_1.get_exam_month())
