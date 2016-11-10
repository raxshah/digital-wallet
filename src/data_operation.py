import csv
import os


def load_data(input_file):
    '''
    Load batch data
    :param input_file: name of the input batch file
    :return: list of tuples that have sender and receiver of money
    '''
    os.chdir("..")
    rows = []
    with open(os.path.join(os.getcwd(), "paymo_input", input_file), 'r', encoding="utf8") as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        header_flag = False
        for row in read_csv:
            if header_flag:
                if len(row) >= 3:
                    rows.append((row[1].strip(), row[2].strip()))
            header_flag = True
    os.chdir("src")
    return rows


def output_stream_data(input_file, friends_connections, feature):
    '''
    Load and output stream payment data
    :param input_file: name of stream file
    :param friends_connections: friends graph created from batch file
    :param feature: either 1, 2 or 3 based on the required feature
    :return: it will write a output file
    '''
    os.chdir("..")
    rows = []
    with open(os.path.join(os.getcwd(), "paymo_input", input_file), 'r', encoding="utf8") as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        header_flag = False
        for row in read_csv:
            if header_flag:

                if len(row) >= 3:
                    if feature == 1:
                        host_direct_friends = friends_connections.get(row[1].strip())
                        if (feature1_check(host_direct_friends, row[2].strip())):
                            rows.append("trusted")
                        else:
                            rows.append("unverified")

                    elif feature == 2:
                        if(feature_check(friends_connections,row[1].strip(), row[2].strip(), 2)):
                        #if (feature_check(row[1].strip(), row[2].strip(), friends_connections, 2)):
                            rows.append("trusted")
                        else:
                            rows.append("unverified")

                    elif feature == 3:
                        if (feature_check(friends_connections, row[1].strip(), row[2].strip(), 4)):
                            rows.append("trusted")
                        else:
                            rows.append("unverified")
            header_flag = True

    with open(os.path.join(os.getcwd(), "paymo_output", str("output" + str(feature) + ".txt")), mode='w',
              encoding='utf-8') as outfile:
        outfile.write('\n'.join(rows))

    os.chdir("src")


def feature1_check(host_direct_friends,receiver):
    '''
    check if transactions is authorised or not
    :param host_direct_friends: sendre's 1st degree friend
    :param receiver: recipient of money
    :return: True or False based on the type of transactions
    '''
    authorized = False
    if (host_direct_friends is not None):
        if receiver.strip() in host_direct_friends:
            authorized = True
    return authorized


def feature_check(friends_connections,sender,receiver,maxDepth):
    '''
    bfs search of a graph till given depth
    :param friends_connections: graph structure from batch file
    :param sender: sender of money
    :param receiver: recipient of money
    :param maxDepth: degree of friendship
    :return:
    '''

    node_visited = []
    node_queue = []
    node_visited.append(sender)
    node_queue.append(sender)
    depth = 0

    while node_queue:

        if depth == maxDepth:
            return False

        host = node_queue.pop()
        host_friends = friends_connections.get(host, [])
        for friend in host_friends:
            if(friend not in node_visited):
                if(friend == receiver):
                    return True
                node_visited.append(friend)
                node_queue.append(friend)
        depth= depth +1

    return False
