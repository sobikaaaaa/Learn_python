def log_message(message):
    file_name="log_message.txt"
    with open(file_name,"a") as file:
        file.write(f"{message}\n")
log_message("application started")
log_message("user logged in")