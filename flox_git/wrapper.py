class Git:
    def __init__(self, repository, tracker):
        self.tracker = tracker
        self.repository = repository

    def log(self, source, destination):
        messages = self.repository.log(f'{source}..{destination}')

        return self.tracker.parse_issues(messages)
