param_1 = '\'Views\''
param_2 = '\'Likes\''
param_3 = '\'Comments\''
param_4 = '\'TikToks with the same sound\''

txt_positive = 'Positive correlation📈:'
txt_negative = 'Negative correlation📉:'

def txt_correlation(side, param_1, param_2, corr):
    if side == txt_positive:
        word = 'more'
    elif side == txt_negative:
        word = 'less'
    text = f'''The greater the <b>{param_1}</b>, the {word} {param_2}(corr = {corr})'''
    return text

ttest_info_list = [
    'When the video was filmed?',
    'Set the most suitable TikTok type group:',
    'What color prevails in the video?',
    'How many people are in the video?',
    'Music in TikTok is:',
    'When did you upload the video',
    'Are there any sun rays in the video?',
    'Is there any dance in the video?',
    'Is there any LED Lighting in the video?',
    'Do you have artificial or natural light',
    'Did you write something in a description field?',
    'Is there a text write on screen?',
    'Did you use TikTok Effects',
    'Did you use TikTok Filters',
    'Did you format the video not in TikTok app?',
    'What camera did you use?',
    'Did you use any hashtags?',
    'Choose the video dynamics:'
    ]

ttest_params_list = [
    'views',
    'likes',
    'comments',
    'sound_popularity',
    'when_filmed',
    'tiktok_ type',
    'tiktok_color',
    'people_number',
    'music_lang',
    'upload_time',
    'sunshine',
    'dance',
    'led_lights',
    'light',
    'description',
    'text',
    'tiktok_effects',
    'tiktok_filters',
    'format_outside',
    'camera',
    'hashtags',
    'dynamics'
]

ttest_param_1 = 'views'
ttest_param_2 = 'likes'