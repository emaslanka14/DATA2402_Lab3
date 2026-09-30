from classes import PatientExam
from data_IO import parse_row

def read_patients_into_list(fileName: str) -> list[PatientExam]:
    #read file and append exam objects to list
    exams = []
    with open (fileName) as f:
        
        for line in f: #Iterate through file until we find the header row
            if line.find(',') != -1:
                break

        for line in f:
            try:
                examID, date, name, weight, height = parse_row(line)
                exams.append(PatientExam(examID, date, name, weight, height))
            except:
                pass #Skip adding data with errors
            # exam_ID: int, date: str, name: str, weight: int, height: float
            #print(f"int{(parts[0])}, {parts[1]}, {parts[2]}, {int(parts[3])}, {float(parts[4])}")
        return exams

def print_patient_stats(exams: list[PatientExam]) -> None:
    #calculate average bmi
    bmi_total = 0
    for exam in exams:
        bmi_total += exam.get_BMI()

    #handle zero division error if list is empty and print result
    try:
        bmi_avg = bmi_total / len(exams)
        print(f'Average BMI: {bmi_avg:.2f}')
    except:
        ZeroDivisionError(print('No values to compute BMI average'))

    month_counts = {}
    for exam in exams:
        month = exam.get_exam_month()
        if month > 12:
            raise ValueError('Invalid input for month')
        if month in month_counts:
            month_counts[month] += 1
        else:
            month_counts[month] = 1
        


    #create variables to track the busiest month
    highest_count = 0
    busiest_month = None

    #loop through values and replace the count and month variables if the month count is higher, print result
    for month, count in month_counts.items():
        if count > highest_count:
            highest_count = count
            busiest_month = month


    # Dictionary to convert int to month name
    month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

    print(f"Busiest month: {month_names[busiest_month]}")

def main(): 
    file_name = "patient_data.csv"
    exams = read_patients_into_list(file_name)

    print(f'Number of Patient exams: {len(exams)}')
    print_patient_stats(exams)

if __name__ == "__main__":
    main()


