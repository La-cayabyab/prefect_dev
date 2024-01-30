from prefect import flow, task

@task
def print_message():
    message = 'YOLO'
    return(message)

@flow
def yolo_message():
    task_message = print_message()
    print(task_message)

if __name__ == "__main__":
    yolo_message()