import os
import re
import datetime
import threading
from tkinter import ttk, N, W, E, S, StringVar, Tk
from plyer import notification
from playsound import playsound

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def format_time(sec):
    return str(datetime.timedelta(seconds=sec))


def validate_number(newval):
    return re.match("^[0-9]*$", newval) is not None


class Clock:
    def __init__(self, timeout=10, on_update=None, on_ready=None):
        self.__timeout = timeout
        self.__interval = None
        self.on_update = on_update
        self.on_ready = on_ready

    def __set_interval(self, sec):
        def func_wrapper():
            self.__interval = self.__set_interval(sec)
            self.__timeout -= 1
            if self.on_update is not None:
                self.on_update(self.get_timeout())
            if self.__timeout <= 0:
                self.stop()
                if self.on_ready is not None:
                    self.on_ready()

        timer = threading.Timer(sec, func_wrapper)
        timer.start()
        return timer

    @property
    def running(self):
        return self.__interval is not None

    def start(self):
        self.__interval = self.__set_interval(1)

    def stop(self):
        if self.__interval is not None:
            self.__interval.cancel()
        self.__interval = None

    def set_timeout(self, timeout):
        self.__timeout = timeout

    def get_timeout(self):
        return self.__timeout


class Pomodoro(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")

        # Store time limit in minutes
        self.max_limit = StringVar(value="5")

        timeout = StringVar(value=format_time(self.get_limit()))
        validate_num_wrapper = (self.register(validate_number), "%P")

        frame = ttk.Frame(self, padding="3 3 12 12")
        clock = ttk.Label(frame, textvariable=timeout)
        restart = ttk.Button(frame, text="Start Clock", command=self.restart_clock)
        pause = ttk.Button(frame, text="Pause", command=self.toggle_clock)
        limit = ttk.Entry(
            frame,
            textvariable=self.max_limit,
            validate="key",
            validatecommand=validate_num_wrapper,
        )

        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        clock.grid(column=0, row=0, columnspan=2, sticky=(N, W, E, S))
        limit.grid(column=0, row=1, columnspan=2, sticky=(W, E))
        restart.grid(column=0, row=2, sticky=(W, S))
        pause.grid(column=1, row=2, sticky=(E, S))

        def clock_update(seconds):
            timeout.set(format_time(seconds))

        def clock_ready():
            timeout.set(format_time(0))
            playsound(os.path.join(BASE_DIR, "assets", "alarm-default.mp3"))
            notification.notify(
                title="Time's Up!",
                message="Your timer has reached 0",
                app_icon=None,
                timeout=10,
            )

        self.__clock = Clock(on_update=clock_update, on_ready=clock_ready)

    def get_limit(self):
        """Return max tim limit in seconds"""
        return int(self.max_limit.get()) * 60

    def restart_clock(self, *args):  # pylint: disable=W0613
        self.__clock.stop()
        self.__clock.set_timeout(self.get_limit())
        self.__clock.start()

    def stop_clock(self):
        self.__clock.stop()

    def toggle_clock(self):
        if self.__clock.running:
            self.__clock.stop()
        else:
            self.__clock.start()
