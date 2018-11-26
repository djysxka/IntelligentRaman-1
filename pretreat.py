
import numpy as np
import pandas as pds
# �źŴ���� #
import scipy.signal as sp
import scipy.io as sio
# �Խ��� #
import preprocessing_data as pd
import rampy
import matplotlib.pyplot as plt


def Ttreat(Ramanshift1, Hem_I, n, Tri_path):
    Tri_I0 = np.mean(Hem_I, axis=0)
    # ��ȡ����350~4000cm-1, SGƽ������ #
    Tri_I_SG = sp.savgol_filter(Tri_I0[64:1014], 11, 2)
    # ȥ���ߴ��� #
    x = Ramanshift1[64:1014]
    y1 = Tri_I_SG
    roi = np.array([[350, 4000]])
    y1_arpls, base_y1 = rampy.baseline(x, y1, roi, 'arPLS', lam=10 ** 5, ratio=0.001)
    # ��һ������ #
    Tri_I_Nor = pd.Normalization(y1_arpls)
    Tri_I_Nor_n = np.around(Tri_I_Nor, decimals=3)
    x_ = x[:, np.newaxis]
    np.savez(Tri_path+'/' + 'Ramanspectra_  (' + str(n) + ').npz', x_=x_, Ramanspectra=Tri_I_Nor_n)
    # sio.savemat(Hem_path+'/' + 'Ramanspectra_  (' + str(n) + ').mat', {'ramanshift':x_, 'ramanspectra':Hem_I_Nor})
    # with open (Hem_path + '/all.mat', 'ab') as mt:
    #     sio.savemat(mt, {'ramanspectra'+str(n):Hem_I_Nor})
    # ���汻��з��
    x0 = pds.DataFrame(x, columns=['Ramanshift'])
    Tri_I_Nor = pds.DataFrame(Tri_I_Nor, columns=['Ramanspectra ' + str(n)])
    pds.merge(x0, Tri_I_Nor, how='outer', left_index=True, right_index=True). \
        to_csv(Tri_path + '/' + 'Ramanspectra_  (' + str(n) + ').csv', index=False, float_format='%.3f')
    a1 = open(Tri_path + '/all.csv')
    a = pds.read_csv(a1)
    b1 = open(Tri_path + '/' + 'Ramanspectra_  (' + str(n) + ').csv')
    b = pds.read_csv(b1)
    a.merge(b, how='outer', on='Ramanshift').to_csv(Tri_path + '/all.csv', index=False, float_format='%.3f')
    return Tri_I_Nor

def Ctreat(Ramanshift1, Cho_I, n, Cho_path):
    Cho_I0 = np.mean(Cho_I, axis=0)
    # ��ȡ����350~4000cm-1, SGƽ������ #
    Cho_I_SG = sp.savgol_filter(Cho_I0[64:1014], 5, 2)
    # ȥ���ߴ��� #
    x = Ramanshift1[64:1014]
    y2 = Cho_I_SG
    roi = np.array([[350, 4000]])
    y2_arpls, base_y2 = rampy.baseline(x, y2, roi, 'arPLS', lam=10 ** 5, ratio=0.001)
    # ��һ������ #
    Cho_I_Nor = pd.Normalization(y2_arpls)
    Cho_I_Nor_n = np.around(Cho_I_Nor, decimals=3)
    x_ = x[:, np.newaxis]
    np.savez(Cho_path + '/' + 'Ramanspectra_  (' + str(n) + ').npz', x_=x_, Ramanspectra=Cho_I_Nor_n)
    # sio.savemat(Hem_path+'/' + 'Ramanspectra_  (' + str(n) + ').mat', {'ramanshift':x_, 'ramanspectra':Hem_I_Nor})
    # with open (Hem_path + '/all.mat', 'ab') as mt:
    #     sio.savemat(mt, {'ramanspectra'+str(n):Hem_I_Nor})
    # ���汻��з��
    x0 = pds.DataFrame(x, columns=['Ramanshift'])
    Cho_I_Nor = pds.DataFrame(Cho_I_Nor, columns=['Ramanspectra ' + str(n)])
    pds.merge(x0, Cho_I_Nor, how='outer', left_index=True, right_index=True). \
        to_csv(Cho_path + '/' + 'Ramanspectra_  (' + str(n) + ').csv', index=False, float_format='%.3f')
    a1 = open(Cho_path + '/all.csv')
    a = pds.read_csv(a1)
    b1 = open(Cho_path + '/' + 'Ramanspectra_  (' + str(n) + ').csv')
    b = pds.read_csv(b1)
    a.merge(b, how='outer', on='Ramanshift').to_csv(Cho_path + '/all.csv', index=False, float_format='%.3f')
    return Cho_I_Nor

def Htreat(Ramanshift1, Hem_I, n, Hem_path):
    Hem_I0 = np.mean(Hem_I, axis=0)
    # ��ȡ����350~4000cm-1, SGƽ������ #
    Hem_I_SG = sp.savgol_filter(Hem_I0[64:1014], 5, 2)
    # ȥ���ߴ��� #
    x = Ramanshift1[64:1014]
    y3 = Hem_I_SG
    roi = np.array([[350, 4000]])
    y3_arpls, base_y3 = rampy.baseline(x, y3, roi, 'arPLS', lam=10 ** 5, ratio=0.001)
    # ��һ������ #
    Hem_I_Nor = pd.Normalization(y3_arpls)
    Hem_I_Nor_n = np.around(Hem_I_Nor, decimals=3)
    x_ = x[:, np.newaxis]
    np.savez(Hem_path + '/' + 'Ramanspectra_  (' + str(n) + ').npz', x_=x_, Ramanspectra=Hem_I_Nor_n)
    # sio.savemat(Hem_path+'/' + 'Ramanspectra_  (' + str(n) + ').mat', {'ramanshift':x_, 'ramanspectra':Hem_I_Nor})
    # with open (Hem_path + '/all.mat', 'ab') as mt:
    #     sio.savemat(mt, {'ramanspectra'+str(n):Hem_I_Nor})
    # ���汻��з��
    x0 = pds.DataFrame(x, columns=['Ramanshift'])
    Hem_I_Nor = pds.DataFrame(Hem_I_Nor, columns=['Ramanspectra ' + str(n)])
    pds.merge(x0, Hem_I_Nor, how='outer', left_index=True, right_index=True). \
        to_csv(Hem_path + '/' + 'Ramanspectra_  (' + str(n) + ').csv', index=False, float_format='%.3f')
    a1 = open(Hem_path + '/all.csv')
    a = pds.read_csv(a1)
    b1 = open(Hem_path + '/' + 'Ramanspectra_  (' + str(n) + ').csv')
    b = pds.read_csv(b1)
    a.merge(b, how='outer', on='Ramanshift').to_csv(Hem_path + '/all.csv', index=False, float_format='%.3f')
    return Hem_I_Nor

    # # ��ͼ #
    # # ����ͼ�εĳ��Ϳ�λΪӢ�磬
    # # ����figure����һ����ͼ���󣬲���ʹ����Ϊ��ǰ�Ļ�ͼ����
    # plt.figure(num=1, figsize=(8, 4))
    # # �����������ø��ÿ�
    # # �������Ƶ�����һ�����֣���������ͼʾ(legend)����ʾ��
    # # ֻҪ���ַ���ǰ�����"$"���ţ�matplotlib�ͻ�ʹ������Ƕ��latex������Ƶ���ѧ��ʽ��
    # # color : ָ�����ߵ���ɫ
    # # linewidth : ָ�����ߵĿ��
    # plt.plot(x, Tri_I_Nor, label="$Tri$", color="blue", linewidth=1)
    # plt.plot(x, Cho_I_Nor + 1, label="$Cho$", color="red", linewidth=1)
    # plt.plot(x, Hem_I_Nor + 2, label="$Hem$", color="green", linewidth=1)
    #
    # plt.figure(num=2, figsize=(8, 4))
    # # �����������ø��ÿ�
    # # �������Ƶ�����һ�����֣���������ͼʾ(legend)����ʾ��
    # # ֻҪ���ַ���ǰ�����"$"���ţ�matplotlib�ͻ�ʹ������Ƕ��latex������Ƶ���ѧ��ʽ��
    # # color : ָ�����ߵ���ɫ
    # # linewidth : ָ�����ߵĿ��
    # plt.plot(Ramanshift, Tri_I0, label="$Tri$", color="blue", linewidth=1)
    # # ����X�������
    # plt.xlabel("Raman shift/cm-1")
    # # ����Y�������
    # plt.ylabel("Intensity")
    # # ����ͼ��ı���
    # plt.title("Raman spectrum")
    # # ����Y��ķ�Χ
    # plt.ylim()
    # # ��ʾͼʾ
    # plt.legend()
    # # ��ʾ�����Ǵ��������л�ͼ����
    # plt.show()