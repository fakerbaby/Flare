import os

benchmark = ["ispd2005"]
dataset = ["adaptec1", "adaptec2","adaptec3", "adaptec4", "bigblue1", "bigblue2", "bigblue3", "bigblue4"]


BENCHMARK = benchmark[0] # choose the benchmark

DATASET = dataset[0] # choose the dataset

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #the absolute path to base directory
