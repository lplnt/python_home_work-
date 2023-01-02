from datetime import datetime as dt

log_file = open('Python/Python home work/h_w_7/calc/log_file.txt', 'a')
operation_time = dt.now().strftime('%H:%M')


def logwrite(note, message_text):
    log_file.write(operation_time + ' ' + note + str(message_text) + '\n')