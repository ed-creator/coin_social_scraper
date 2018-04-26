from coin import Coin

kwargs = {"name" : "aeternity" ,"symbol" : "AE" , "medium" : "blog.aeternity.com", "twitter" : "aeternity", 
          "facebook" : "aeternityproject", "slack" : "N/A", "github_overall" : "aeternity", "github_main_repo" : "epoch",                       "github_main_repo_desc" : "testnet_repo", "telegram" : "aeternity", "reddit" : "aeternity", "discord" : "N/A", 
          "linkedn" : "aeternity"}

AE = Coin(**kwargs)
AE.update_telegram()

print (AE.__dict__)
