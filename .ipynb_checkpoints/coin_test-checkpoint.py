from coin import Coin
import pytest

kwargs = {"name" : "aeternity" ,"symbol" : "AE" , "medium" : "blog.aeternity.com", "twitter" : "aeternity", 
          "facebook" : "aeternityproject", "slack" : "N/A", "github_overall" : "aeternity", "github_main_repo" : "epoch",                       "github_main_repo_desc" : "testnet_repo", "telegram" : "aeternity", "reddit" : "aeternity", "discord" : "N/A", 
          "linkedn" : "aeternity"}

@pytest.fixture
def new_coin():
    '''Returns a newly initialized coin with data'''
    coin = Coin(**kwargs)
    return coin

def test_new_coin_init(new_coin):
    assert new_coin.name == 'aeternity'
    
