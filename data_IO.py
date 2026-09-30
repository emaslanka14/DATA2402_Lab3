from classes import MissingValueException, TextFormatException, MeasurementUnitException


def parse_row(row: str) -> tuple:
    """
    Parses a row that fits the patient format:
    Exam ID,Date,Patient Name,Weight (kg),Height (m)

    Returns a tuple containing the Patient data.
    """

    values = row.strip().split(",")



    if "" in values:
        raise MissingValueException()

    try:
        exam_ID = int(values[0])
        Date = values[1]
        Patient_name = values[2]
        weight = float(values[3])
        height = float(values[4])
    except ValueError:
        raise TextFormatException()
    
    if height > 3:
        raise MeasurementUnitException()
    
    return (exam_ID, Date, Patient_name, weight, height)