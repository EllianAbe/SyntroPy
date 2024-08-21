from fastapi import FastAPI
from pydantic import BaseModel
from air_conditionair import AirConditioner
import logging
import threading

app = FastAPI()
ac = AirConditioner()

# Configure logging to suppress API logs in the terminal
logging.basicConfig(level=logging.ERROR)


class Event(BaseModel):
    event: str


@app.post("/event")
async def handle_event(event: Event):
    ac.on_event(event.event)

    return {"message": "Event processed"}


def run_ac():
    while True:
        ac.run()


if __name__ == "__main__":
    threading.Thread(target=run_ac, daemon=True).start()

    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=1234)
