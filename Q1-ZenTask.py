
import datetime
def create_file_with_timestamp():
    get_time_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"info{get_time_now}.txt"
    file = open(file_name, 'w')
    file.write(f"The content is updated... The current time is :{get_time_now}")
    file.close()

create_file_with_timestamp()



