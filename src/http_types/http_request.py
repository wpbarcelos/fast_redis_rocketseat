class HttpRequest:
    def __init__(self, body: dict = None, params=dict) -> None:
        self.body = body
        self.params = params
