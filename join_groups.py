from telethon import TelegramClient
import json
import csv
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import functions, types
from telethon import errors
import time

api_id = 'my personal telegram api id'
api_hash = 'and its hash'

client = TelegramClient('client_name', api_id, api_hash)

async def main():

################################################################################
#CODE TO JOIN GROUPS GIVEN INVITE LINKS
################################################################################
    groups_imin_ids = []#a list of all the groups that i'm a member of
    dialogs = await client.get_dialogs()
    for i in dialogs:
        if i.is_group:
            groups_imin_ids.append(i)#filter out private chats and channels

    with open('some_file.json', 'r') as grouplinks_file:
        y = json.load(grouplinks_file)

    links = {}#dictionary with group names and invite links
    keys_infodata = y['info_data'].keys()
    for i in keys_infodata:
        if (y['info_data'][i]['id_link'] != None):
            if y['info_data'][i]['class'] > 'point from which to start':
                if y['info_data'][i]['class'] not in links.keys():
                    # print(y['info_data'][i]['class'])
                    links[y['info_data'][i]['class']] = (y['info_data'][i]['id_link'])

    for i in links.keys():
        print(i)
        print(links[i])
        if(links[i] != 'None'):
            try:
                result = await client(ImportChatInviteRequest(links[i]))
            except errors.FloodWaitError as a:
                print('you\'re going too fast bucko')
                print(a.seconds)
                time.sleep(a.seconds)
            except Exception as e:
                print(e)
            print('waiting 180 sec')#this is a limit imposed by the telegram api, if you try to send requests faster you will get a flood wait error and a time out
            time.sleep(180)

with client:
    client.loop.run_until_complete(main())
