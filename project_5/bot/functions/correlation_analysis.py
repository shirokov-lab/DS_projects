from scipy.stats.stats import pearsonr
from itertools import combinations
from databases.db_engine import Interview, session
from text import stat_params

'''ФУНКЦИЯ ПРОИЗВОДЯЩАЯ КОРРЕЛЯЦИОННЫЙ АНАЛИЗ ПИРСОНА И ВОЗВРАЩАЮЩАЯ ГОТОВОЕ СООБЩЕНИЕ С РЕЗУЛЬТАТАМИ'''
def corr(db_id):
    message = ''

    answ_dict = {
        stat_params.param_1: [], stat_params.param_2: [],
        stat_params.param_3: [], stat_params.param_4: []
        }
    try:
        for sesh in session.query(Interview).order_by(Interview.db_id).filter_by(db_id=db_id):
            answ_dict[stat_params.param_1].append(sesh.question_1)
            answ_dict[stat_params.param_2].append(sesh.question_2)
            answ_dict[stat_params.param_3].append(sesh.question_3)
            answ_dict[stat_params.param_4].append(sesh.question_4)

        combinations_all = list(combinations(answ_dict, 2))
        correlations = {stat_params.txt_positive: [], stat_params.txt_negative: []}
        for comb in combinations_all:
            corr = round(pearsonr(answ_dict[comb[0]], answ_dict[comb[1]])[0], 4)
            if corr >= 0:
                correlations[stat_params.txt_positive].append([comb[0], comb[1], corr])
            elif corr < 0:
                correlations[stat_params.txt_negative].append([comb[0], comb[1], corr])

        for side in correlations:
            message += side + '\n'
            if correlations[side] == []:
                message += 'None\n\n'
                continue
            for obj in correlations[side]:
                message += stat_params.txt_correlation(side, obj[0], obj[1], obj[2]) + '\n\n'

        message = message[:len(message)-2]
    except:
        message = stat_params.txt_positive + '\nNone\n\n' + stat_params.txt_negative + '\nNone'

    return message