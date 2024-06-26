import readline
import re

class Completer():
    def __init__(self, options):
        self.options = options
        self.current_candidates = []
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # Создание списка соответствий.
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # Первое слово
                        candidates = self.options.keys()
                    else:
                        # Последующие слова
                        first = words[0]
                        candidates = self.options[first]

                    if being_completed:
                        # параметры сопоставления с частью ввода
                        self.current_candidates = [ w  + ' ' for w in candidates if w and w.startswith(being_completed) ]
                        #  self.current_candidates = [ w  + ' ' for w in candidates if re.match(being_completed, w) ]
                    else:
                        # соответствие пустой строке, используются все кандидаты
                        self.current_candidates = candidates
                except IndexError as err:
                    self.current_candidates = []
                except KeyError as err:
                    self.current_candidates = []
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        return response




