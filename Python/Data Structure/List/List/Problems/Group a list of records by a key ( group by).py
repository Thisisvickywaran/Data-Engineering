employees = [
    {"name": "Alice", "dept": "IT"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "IT"}
]

grouped_emp={}
for item in employees:
    dept=item["dept"]
    if dept not in grouped_emp:
        grouped_emp[dept]=[]
    grouped_emp[dept].append(item["name"])

print(grouped_emp)