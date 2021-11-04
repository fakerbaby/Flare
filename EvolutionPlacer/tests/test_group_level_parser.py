from _const import BENCHMARK, DATASET, GROUP_NUM 
from  _path import ORI_CLUS_PATH, SUB_NET_PATH, PL_PATH, MOD_CLUSTER_PATH, ADJ_PATH, FEAT_MAT_PAT
import bin.parser.group_level_parser as parser
import numpy as np


test = parser.GroupLevelParser()
ori_cluster_path = ORI_CLUS_PATH
sub_net_list_path = SUB_NET_PATH
pl_path = PL_PATH
modified_cluster_path = MOD_CLUSTER_PATH
adj_path =  ADJ_PATH
feature_path = FEAT_MAT_PAT

test.load_data(sub_net_list_path, ori_cluster_path)

test.modify_cluster(pl_path, GROUP_NUM)
test.save_data(modified_cluster_path, adj_path, feature_path)

