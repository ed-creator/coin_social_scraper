import telegram as tl

class Coin:
    allowed_keys = ["name","symbol", "medium", "twitter", "facebook", "slack", "github_overall", "github_main_repo",                                       "github_main_repo_desc", "telegram", "reddit", "discord", "linkedin"]
    def __init__(self,**kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in Coin.allowed_keys)
        
    def update_telegram(self):
        self.telegram_member_count = tl.member_count(self.telegram)
        