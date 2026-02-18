# Attendance Calculator Program

try:
    total_classes = int(input("Enter total conducted classes: "))
    attended_classes = int(input("Enter total attended classes: "))
    required_percentage = 75

    if total_classes <= 0:
        print("Total classes must be greater than 0.")
    elif attended_classes > total_classes:
        print("Attended classes cannot be more than total classes.")
    else:
        attendance_percentage = (attended_classes / total_classes) * 100
        print("\nAttendance Percentage:", round(attendance_percentage, 2), "%")

        if attendance_percentage >= required_percentage:
            print("Status: Eligible for exams ✅")
        else:
            shortage = required_percentage - attendance_percentage
            print("Status: Not Eligible ❌")
            print("You need", round(shortage, 2), "% more attendance.")

except ValueError:
    print("Please enter valid numbers only.")
