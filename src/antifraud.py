from create_graph import Graph
from data_operation import load_data
from data_operation import output_stream_data


if __name__ == '__main__':
    batch_data = load_data("batch_payment.txt") #load input batch file
    batch_data_connections = Graph(batch_data)._graph #create friends undirected cyclic grapgh structure

    #in feature argument pass the feature you would require
    output_stream_data("stream_payment.txt",batch_data_connections,feature = 1) #read stream file and output respective output based on feature
