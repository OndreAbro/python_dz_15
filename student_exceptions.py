import logging


class StudentNameError(Exception):
    def __init__(self, message='Invalid student name'):
        self.message = message
        logging.error(self.message)
        super().__init__(self.message)


class InvalidSubjectError(Exception):
    def __init__(self, subject_name):
        self.message = f'Invalid subject: {subject_name}'
        logging.error(self.message)
        super().__init__(self.message)


class InvalidScoreError(Exception):
    def __init__(self, score, score_type='score'):
        self.message = f'Invalid score: {score} for type {score_type}'
        logging.error(self.message)
        super().__init__(self.message)
