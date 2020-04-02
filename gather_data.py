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
#GATHER DATA ABOUT GROUPS AND CREATE NODE AND EDGE FILES
################################################################################
#get all the groups i'm in
    group_list = []
    dialog_list = await client.get_dialogs()
    for dialog in dialog_list:
        if dialog.is_group:
            #print(a.name, a.id)
            group_list.append(dialog.name)

#get the participants of each group
    print(len(group_list))
    short_group_list = group_list[0:3]#used for testing

    group_member_dictionary = {}#for each group there is a list of its members
    for group in group_list:
        print(group)
        count = 0
        group_member_dictionary[group] = []
        async for member in client.iter_participants(group):
            group_member_dictionary[group].append(member.id)

#calculate how many members in common there are between any two groups
    print('starting quadratic complexity loop')
    edge_weight_dictionary = {}#each connection between two groups has a weight (the number of members they have in common)
    weight = 0
    for i in range(len(group_list)):
        for k in range(i):#connections are symmetrical / the graph is undirected
            print(group_list[i], group_list[k])
            weight = 0
            for user in group_member_dictionary[group_list[i]]:
                if user in group_member_dictionary[group_list[k]]:
                    weight += 1
            print(weight)
            edge_weight_dictionary[tuple((group_list[i], group_list[k]))] = weight
    print('quadratic complexity loop completed')

    keys=[]
    for i in edge_weight_dictionary.keys():
        keys.append(i)
    # keys = edge_weight_dictionary.keys()

    groups = []
    for i in group_member_dictionary.keys():
        groups.append(i)
    # groups = group_member_dictionary.keys()

#create the file with the nodes of the graph (each node is a group)
    group_id_dictionary = {}#assign a unique id to each group(maybe not necessary since there are no two groups with the same name)
    groups_file = open('nodes.csv', 'w')
    with groups_file:
        fields = ['id', 'group_name', 'count']#these will be the columns in the file(unique groups id, group name and number of members of the group)
        writer = csv.DictWriter(groups_file, fieldnames = fields)
        writer.writeheader()
        for i in range(len(groups)):
            writer.writerow({'id' : i, 'group_name' : groups[i], 'count' : len(group_member_dictionary[groups[i]])})
            group_id_dictionary[groups[i]] = i

#create the file with all the edges of the graph(edge weight is the number of common members between groups)
    output_file = open('edges.csv', 'w')
    with output_file:
        field_names = ['group_1', 'group_2', 'connection_weight']
        writer = csv.DictWriter(output_file, fieldnames = field_names)
        writer.writeheader()
        for i in range(len(keys)):
            writer.writerow({'group_1' : group_id_dictionary[(keys[i])[0]], 'group_2' : group_id_dictionary[(keys[i])[1]], 'connection_weight' : edge_weight_dictionary[(keys[i])]})


with client:
    client.loop.run_until_complete(main())
