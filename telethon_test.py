from telethon import TelegramClient
import sys
from telethon.tl.functions.messages import GetHistoryRequest

import json

conf = json.load(open('conf.json'))

api_id = conf["api_id"]
api_hash = conf["api_hash"]
phone = conf['phone']

client = TelegramClient('session_name', api_id, api_hash)
client.connect()


auth = client.is_user_authorized()  # Returns True if you can send requests
# If you already have a previous 'session_name.session' file, skip this.
if not auth:
    print("No Auth")
    client.sign_in(phone=phone)
    me = client.sign_in()  # Put whatever code you received here.
else:
    print("Already Auth")
    me = client.get_me()

print(me.stringify()) # Print self


def print_entity(name):
    ent = client.get_entity(name)
    print(ent.stringify())
    return ent

lonami = print_entity("lonami") # user
#movies_inc = print_entity("movies_inc") # channel
mp3downloads1 = print_entity("javascript_all") # megagroup

total, messages, senders = client.get_message_history(mp3downloads1)

offset_id=0
import time
print(total)
tot = 0
while True:
    result = client(GetHistoryRequest(
        mp3downloads1,
        limit=100,
        offset_date=None,
        offset_id=offset_id,
        max_id=0,
        min_id=0,
        add_offset=0
    ))
    tot += len(result.messages)
    print(tot)
    time.sleep(5)
    offset_id = result.messages[len(result.messages)-1].id

print(len(result.messages))
print(len(result.users))
am = len(result.messages)
print(result.messages[am-1].stringify())
# print(result.users[am-1].stringify())
sys.exit(1)

print(total)
print(len(messages))
print(len(senders))

for i,m in enumerate(messages):
    print(m.stringify())
    print(senders[i].stringify())
    print(m.id)
    break

# sys.exit(1)
from telethon.tl.functions.contacts import ResolveUsernameRequest

result = client(ResolveUsernameRequest('mp3downloads1'))
print(result.stringify())
found_chats = result.chats
found_users = result.users

#print(found_chats)
#print(found_users)

# from telethon.tl.functions.messages import GetDialogsRequest
# from telethon.tl.types import InputPeerEmpty
# from time import sleep

# dialogs = []
# users = []
# chats = []

# last_date = None
# chunk_size = 20
# while True:
#     result = client(GetDialogsRequest(
#                  offset_date=last_date,
#                  offset_id=0,
#                  offset_peer=InputPeerEmpty(),
#                  limit=chunk_size
#              ))
#     dialogs.extend(result.dialogs)
#     users.extend(result.users)
#     chats.extend(result.chats)
#     last_date = min(msg.date for msg in result.messages)
#     if not result.dialogs:
#         break
#     sleep(2)






from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import InputChannel

from telethon.tl.functions.channels import GetMessagesRequest

from telethon.tl.functions.channels import GetFullChannelRequest

offset = 0
limit = 100
all_participants = []
channel = InputChannel(mp3downloads1.id,mp3downloads1.access_hash)

full_chat = client.invoke(GetFullChannelRequest(channel))
print(full_chat)
print(full_chat.stringify())
sys.exit(1)


while True:
    participants = client.invoke(GetParticipantsRequest(
        channel, ChannelParticipantsSearch(''), offset, limit
    ))
    print(participants.stringify())
    sys.exit(1)
    if not participants.users:
        break
    all_participants.extend(participants.users)
    offset += len(participants.users)
    print(participants.users[0].stringify())
sys.exit(1)
    # sleep(1)  # This line seems to be optional, no guarantees!
# client.send_message('username', 'Hello! Talking to you from Telethon')
# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# client.download_profile_photo(me)
# total, messages, senders = client.get_message_history('username')
# client.download_media(messages[0])