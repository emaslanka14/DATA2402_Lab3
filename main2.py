from classes import PatientExam

exams = [] #create list for exam objects

file_name = "patient_data.csv"

#read file and append exam objects to list
with open (file_name) as f:
    
    next (f)

    for line in f:
        line = line.strip()
        parts = line.split(',')

        exams.append(PatientExam(int(parts[0]), parts[1], parts[2], int(parts[3]), float(parts[4])))

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

print(f"Busiest month: {busiest_month}") 



