from ..celery import app, logger
import time



@app.task
def test_task(text):
    logger.info(f"Starting task with text: {text}")
    time.sleep(5)  # Simulate some work
    logger.info("Task completed successfully")
    return f"Task processed text: {text}"
