# -*- coding: utf-8 -*-
#����ύ����Ƿ��쳣
def inspect(url):
    import pandas as pd
    import numpy as np

    data = pd.read_csv(url,header=None)
    result = data
    flag = True
    if data.shape != (2000,15):
        print '����ȱʧ����࣡�����¼�顣'
        flag = False
    if data.abs().sum().sum() != data.sum().sum():
        print '����г��ָ���������0���档'
        result = data - data[data < 0].fillna(0)
        flag = False
    for tp in data.dtypes.values:
        if tp.type is not np.int64:
            print '���ݲ������������滻Ϊ������'
            flag = False
            break
    if True in (data.isnull().values):
        print '�����а�����ֵ�����滻Ϊ�㡣'
    result = result.fillna(0).astype(int)
    if flag == True:
        print 'Great�����������������ڿ�ֵ���������㡣'

    return result

inspect("../../data/dataset/out/�ں�_50x15.csv")
