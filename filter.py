import csv

with open('edges.csv', 'r') as edges_file:
    r = csv.DictReader(edges_file)
    # print(r.fieldnames)
    
    edge_dic = {}
    # for i in range(10):
    #     row = r.reader.__next__()
    #     edge_dic[tuple((row[0], row[1]))] = row[2]

    important_edges = []
    node_counters = {}
    for i in range(int(256)):
        node_counters[i] = 0

    for i in r:
        if ((node_counters[int(i['Source'])] < 5) & (node_counters[int(i['Target'])] < 5)) | ((node_counters[int(i['Source'])] == 0) | (node_counters[int(i['Target'])] == 0)):
            node_counters[int(i['Source'])] +=1
            node_counters[int(i['Target'])] +=1
            important_edges.append(i)

    # print(important_edges)

with open('important_edges.csv', 'w') as output:
    fieldnames = ['Source', 'Target', 'Weight', 'Type']
    writer = csv.DictWriter(output, fieldnames = fieldnames)
    writer.writeheader()
    index = 0
    for i in important_edges:
        writer.writerow(important_edges[index])
        index += 1