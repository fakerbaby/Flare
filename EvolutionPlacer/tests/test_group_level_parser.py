from _const import BENCHMARK, DATASET, GROUP_NUM
from  _path import ORI_CLUS_PATH, SUB_NET_PATH, PL_PATH, EXT_CLUS_PATH, MOD_CLUS_PATH, ADJ_PATH, FEAT_MAT_PATH, RES_CLUS_PATH
import bin.parser.group_level_parser as parser
import numpy as np


test = parser.GroupLevelParser()
ori_cluster_path = ORI_CLUS_PATH
sub_net_list_path = SUB_NET_PATH
pl_path = PL_PATH
ext_cluster_path = EXT_CLUS_PATH
adj_path =  ADJ_PATH
feature_path = FEAT_MAT_PATH
result_path = RES_CLUS_PATH



test.load_data(sub_net_list_path, ori_cluster_path)
test.extend_cluster(pl_path, GROUP_NUM)
test.establish_final_cluster()
test.save_data(ext_cluster_path, adj_path, feature_path, result_path)
test.add_conncetivity()


