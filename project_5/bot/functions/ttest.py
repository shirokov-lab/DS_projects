from scipy.stats.stats import ttest_ind
import pandas as pd
import math
from itertools import combinations
import matplotlib.pyplot as plt
import seaborn as sns
from databases.db_engine import Interview, session
from text.stat_params import *

def ttest_get_params(db_id):
    info_list = ttest_info_list

    pars_list = ttest_params_list

    info_dict = dict.fromkeys(info_list, None)

    n = 0
    for i in info_list:
        info_dict[i] = pars_list[n]
        n += 1

    df_dict = {ttest_param_1: [], ttest_param_2: []}

    try:
        for par in info_list:
            df_dict[par] = []

        for sesh in session.query(Interview).order_by(Interview.db_id).filter_by(db_id=db_id):
            df_dict[ttest_param_1].append(sesh.question_1)
            df_dict[ttest_param_2].append(sesh.question_2)
            df_dict[info_list[0]].append(sesh.question_5)
            df_dict[info_list[1]].append(sesh.question_6)
            df_dict[info_list[2]].append(sesh.question_7)
            df_dict[info_list[3]].append(sesh.question_8)
            df_dict[info_list[4]].append(sesh.question_9)
            df_dict[info_list[5]].append(sesh.question_10)
            df_dict[info_list[6]].append(sesh.question_11)
            df_dict[info_list[7]].append(sesh.question_12)
            df_dict[info_list[8]].append(sesh.question_13)
            df_dict[info_list[9]].append(sesh.question_14)
            df_dict[info_list[10]].append(sesh.question_15)
            df_dict[info_list[11]].append(sesh.question_16)
            df_dict[info_list[12]].append(sesh.question_17)
            df_dict[info_list[13]].append(sesh.question_18)
            df_dict[info_list[14]].append(sesh.question_19)
            df_dict[info_list[15]].append(sesh.question_20)
            df_dict[info_list[16]].append(sesh.question_21)
            df_dict[info_list[17]].append(sesh.question_22)

        df = pd.DataFrame(df_dict)
    except: pass

    txt = '<b>'
    box_list = []
    try:
        for column in info_list:
            cols = df.loc[:, column].value_counts().index
            combinations_all = list(combinations(cols, 2))
            for comb in combinations_all:
                if ttest_ind(df.loc[df.loc[:, column] == comb[0], 'views'], df.loc[df.loc[:, column] == comb[1], 'views']).pvalue <= 0.05/len(combinations_all):
                    box_list.append([df[column], df['views'], df[column]])
                    if txt == '<b>':
                        txt += info_dict[column]
                    elif txt != '':
                        txt += f', {info_dict[column]}'
                    break

        for column in info_list:
            cols = df.loc[:, column].value_counts().index
            combinations_all = list(combinations(cols, 2))
            for comb in combinations_all:
                if ttest_ind(df.loc[df.loc[:, column] == comb[0], 'likes'], df.loc[df.loc[:, column] == comb[1], 'likes']).pvalue <= 0.05/len(combinations_all):
                    box_list.append([df[column], df['likes'], df[column]])
                    if txt == '<b>':
                        txt += info_dict[column]
                    elif txt != '':
                        txt += f', {info_dict[column]}'
                    break
    except: pass

    txt += '</b>.'

    if len(box_list) == 1:
        width = len(box_list)
        fg = [10, 10]
    elif len(box_list) == 2:
        width = len(box_list)
        fg = [20, 10]
    else:
        width = 3
        if len(box_list) == 3:
            fg = [30, 10]
        else:    
            fg = [30, 10*(math.ceil(len(box_list)/3))]

    try:
        f, axes = plt.subplots(nrows=math.ceil(len(box_list)/3), ncols=width, squeeze=False, figsize=(fg))
        n = 0
        sns.set(font_scale=1.5)
        for col in box_list:
            i, j = divmod(n, 3)
            sns.boxplot(x=col[0], y=col[1], ax=axes[i, j])
            n = n+1

        plt.savefig('img/img.jpg')
    except: pass

    return txt