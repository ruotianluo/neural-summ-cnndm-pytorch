# -*- coding: utf-8 -*-
#pylint: skip-file
import os 

class CommonConfigs(object):
    def __init__(self, d_type):
        self.ROOT_PATH = os.getcwd() + "/"
        self.TRAINING_DATA_PATH = self.ROOT_PATH + d_type + "/train_set/"
        self.VALIDATE_DATA_PATH = self.ROOT_PATH + d_type + "/validate_set/"
        self.TESTING_DATA_PATH = self.ROOT_PATH + d_type + "/test_set/"
        self.RESULT_PATH = self.ROOT_PATH + d_type + "/result/"
        self.MODEL_PATH = self.ROOT_PATH + d_type + "/model/"
        self.BEAM_SUMM_PATH = self.RESULT_PATH + "/beam_summary/"
        self.BEAM_GT_PATH = self.RESULT_PATH + "/beam_ground_truth/"
        self.GROUND_TRUTH_PATH = self.RESULT_PATH + "/ground_truth/"
        self.SUMM_PATH = self.RESULT_PATH + "/summary/"
        self.TMP_PATH = self.ROOT_PATH + d_type + "/tmp/"


class DeepmindTraining(object):
    IS_UNICODE = False
    REMOVES_PUNCTION = False
    HAS_Y = True
    BATCH_SIZE = 32#70

class DeepmindTesting(object):
    IS_UNICODE = False
    HAS_Y = True
    BATCH_SIZE = 100 #1951
    MIN_LEN_PREDICT = 35
    MAX_LEN_PREDICT = 120
    MAX_BYTE_PREDICT = None
    PRINT_SIZE = 500
    REMOVES_PUNCTION = False

class DeepmindConfigs():
    
    cc = CommonConfigs("deepmind")
   
    CUDA = True
    CELL = "gru"
    COPY = True
    COVERAGE = False

    DIM_X = 128
    DIM_Y = DIM_X

    MIN_LEN_X = 10
    MIN_LEN_Y = 10
    MAX_LEN_X = 400
    MAX_LEN_Y = 100
    MIN_NUM_X = 1
    MAX_NUM_X = 1
    MAX_NUM_Y = None

    NUM_Y = 1
    HIDDEN_SIZE = 256
    LATENT_SIZE = 500
    LVT_DICT_SIZE = 10000

    UNI_LOW_FREQ_THRESHOLD = 10
    NUM_FREQUENT_WORDS = 10000

    PG_DICT_SIZE = 50000 # dic for acl17 paper: pointer network
    
    W_UNK = "<unk>"
    W_BOS = "<bos>"
    W_EOS = "<eos>"
    W_PAD = "<pad>"
    W_LS = "<s>"
    W_RS = "</s>"
