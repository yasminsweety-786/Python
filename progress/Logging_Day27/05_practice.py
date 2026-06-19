import logging

logging.basicConfig(
    filename="student.log",
    level=logging.INFO
)

name = "Yasmin"

logging.info(f"Student Logged In: {name}")

print("Data Saved")