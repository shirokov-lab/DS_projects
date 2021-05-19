import pandas as pd
from databases.db_engine import User, Interview, session

def send_csv(soft):
    user_dict = {
        'username': [],
        'user_id': [],
        'count': [],
        'views': [],
        'likes': [],
        'comments': [],
        'sound_popularity': [],
        'when_filmed': [],
        'tiktok_type': [],
        'tiktok_color': [],
        'people_number': [],
        'music_lang': [],
        'upload_time': [],
        'sunshine': [],
        'dance': [],
        'led_lights': [],
        'light': [],
        'description': [],
        'text': [],
        'tiktok_effects': [],
        'tiktok_filters': [],
        'format_outside': [],
        'camera': [],
        'hashtags': [],
        'dynamics': []
        }
    for sesh in session.query(User).order_by(User.id).all():
        for inter in session.query(Interview).filter_by(db_id=sesh.id).all():
            user_dict['username'].append(sesh.username)
            user_dict['user_id'].append(sesh.user_id)
            user_dict['count'].append(sesh.count)
            user_dict['views'].append(inter.question_1)
            user_dict['likes'].append(inter.question_2)
            user_dict['comments'].append(inter.question_3)
            user_dict['sound_popularity'].append(inter.question_4)
            user_dict['when_filmed'].append(inter.question_5)
            user_dict['tiktok_type'].append(inter.question_6)
            user_dict['tiktok_color'].append(inter.question_7)
            user_dict['people_number'].append(inter.question_8)
            user_dict['music_lang'].append(inter.question_9)
            user_dict['upload_time'].append(inter.question_10)
            user_dict['sunshine'].append(inter.question_11)
            user_dict['dance'].append(inter.question_12)
            user_dict['led_lights'].append(inter.question_13)
            user_dict['light'].append(inter.question_14)
            user_dict['description'].append(inter.question_15)
            user_dict['text'].append(inter.question_16)
            user_dict['tiktok_effects'].append(inter.question_17)
            user_dict['tiktok_filters'].append(inter.question_18)
            user_dict['format_outside'].append(inter.question_19)
            user_dict['camera'].append(inter.question_20)
            user_dict['hashtags'].append(inter.question_21)
            user_dict['dynamics'].append(inter.question_22)
    df = pd.DataFrame(user_dict)

    if soft == 'Sheets':
        sym = '\t'
    elif soft == 'Excel':
        sym = ';'
    df.to_csv('csv/users.csv', sep=sym, index=False, header=True)
    
    return open('csv/users.csv', 'rb')