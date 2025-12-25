from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static

class TimeDisplay(Static):
    pass

class StopWatch(Static):
    def compose(self):
        yield Button("Start", variant="success", id= "start")
        yield Button("Stop", variant="error", id= "stop")
        yield Button("Reset", variant="warning", id= "reset")
        yield TimeDisplay("00:00:00", id= "time")

class StopWatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark/Light Mode"),
        ("s", "start", "Start"),
        ("e", "stop", "Stop"),
    ]

    CSS_PATH = "StopWatch.css"

    def compose(self):
        yield Header(show_clock=True)
        with ScrollableContainer(id = "stopwatches"):
            yield StopWatch()
            yield StopWatch()
            yield StopWatch()
            
        yield Footer()

    def action_start(self):
        pass
    
    def action_stop(self):
        pass

if __name__ == "__main__":
    StopWatchApp().run()
