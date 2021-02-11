from Responders.DataBaseResponder import DataBaseResponder
import datetime as dt


class GameWindowResponder:
    def __init__(self, game_window):
        self.game_window = game_window
        self.data_base_responder = DataBaseResponder()

    def get_score(self):
        return self.game_window.game.points - self.game_window.game.score

    def get_minutes(self):
        return self.game_window.game.responder.get_minutes()

    def get_seconds(self):
        return self.game_window.game.responder.get_seconds()

    def get_record_minutes(self):
        return self.data_base_responder.get_time_list()[0].minute % 60

    def get_record_seconds(self):
        return self.data_base_responder.get_time_list()[0].second % 60

    def is_record(self):
        minutes = self.get_minutes()
        seconds = self.get_seconds()
        time = dt.time(minute=minutes, second=seconds)
        return time == self.data_base_responder.get_time_list()[0]

    def game_ended(self):
        minutes = self.get_minutes()
        seconds = self.get_seconds()
        time = dt.time(minute=minutes, second=seconds)
        if time not in self.data_base_responder.get_time_list():
            self.data_base_responder.add_time_to_table(dt.time(minute=minutes, second=seconds))
