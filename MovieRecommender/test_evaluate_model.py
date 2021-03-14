import unittest
import os
import pickle
import pandas as pd
#import numpy as np
from train_test_model import *
from process_data import *
from extract_data import *

#import numpy as np
from scipy.sparse import csr_matrix, save_npz, load_npz
#import random
import implicit
#from sklearn import metrics
#import os, sys, time 
import csv

#@patch('train_test_model.auc_score')
#auc_score(predictions, test) = Mock()
#auc_score.return_value = float(0.999), float(0.888)
'''
process_data.main()
test_sparse_user_item = load_npz("./output/sparse_user_item.npz")
test_train_data, test_test_data, test_users_altered = test_train_split(test_sparse_user_item)

test_als_model,test_user_vecs,test_item_vecs = train_model(test_train_data.T)

print("implicit_recomm_auc,popularity_auc",evaluate_model(test_train_data, test_users_altered,[csr_matrix(test_user_vecs), csr_matrix(test_item_vecs.T)], test_test_data))
'''

class TestEvaluateModel(unittest.TestCase):   
    
    def test_evaluate_model(self):
        pass

if __name__ == '__main__': 
        unittest.main()