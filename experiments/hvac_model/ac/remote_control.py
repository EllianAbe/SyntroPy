import requests


commands = {
    '1': 'turn_on',
    '2': 'turn_off',
    '3': 'temperature_rise',
    '4': 'temperature_fall'
}

prompt = """Enter command:
1. turn_on
2. turn_off
3. temperature_rise
4. temperature_fall
"""


class RemoteControl:
    def __init__(self, url, port):
        self.url = url
        self.port = port
        self.session = requests.Session()

    def run(self):
        while True:
            event = input(prompt).strip()

            event = commands.get(event)

            if not event:
                continue

            self.session.post(
                f'http://{self.url}:{self.port}/event', json={'event': event})


def main():
    remote_control = RemoteControl(url='127.0.0.1', port=1234)

    remote_control.run()


if __name__ == "__main__":
    main()
