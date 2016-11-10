from create_graph import Graph
from read_data import load_data
from read_data import output_stream_data
import time

if __name__ == '__main__':
    batch_data = load_data("batch_payment.txt")
    batch_data_connections = Graph(batch_data)._graph
    output_stream_data("stream_payment.txt",batch_data_connections,feature = 1)
    print(time.localtime())