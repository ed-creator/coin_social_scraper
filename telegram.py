from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep

api_id = 218536
api_hash = '52bd2ab98459476186498548209fbe7b'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

def member_count(channel):
    coin_tel = client.get_entity(channel)

    member_list = client.get_participants(coin_tel,aggressive=True)
    
    return len(member_list)
