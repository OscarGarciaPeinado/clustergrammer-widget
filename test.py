from clustergrammer_widget import *

net = Network()
net.load_file('/home/oscar/wopr_example.txt')
net.make_clust()
net.write_json_to_file('viz', './mult_view2.json')

print('finish')
