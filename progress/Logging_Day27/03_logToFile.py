import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")

print("Check app.log file")