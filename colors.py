class TerminalColor:
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def red_text_color(cls, text: str) -> str:
        return f'{cls.RED}{text}{cls.ENDC}'

    @classmethod
    def green_text_color(cls, text: str) -> str:
        return f'{cls.GREEN}{text}{cls.ENDC}'

    @classmethod
    def orange_text_color(cls, text: str) -> str:
        return f'{cls.ORANGE}{text}{cls.ENDC}'


