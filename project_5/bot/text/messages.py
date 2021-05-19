def mes_start(username):
    text = f'''Hi {username}, it's your TikTok Booster. I can help you gain more Likes and Views using statistics!📊
Briefly explanation:
<b>Firstly</b>, add observation with 'New video' button. Every TikTok = one observation. Add your videos data and then use statistical tests to know what brings you more likes and views. <b>The more import data, the better the result statistics</b>📈.
<b>Secondly</b>, after adding data, you can get your results by pressing the 'Statistics' button. Then choose, what test's result you need to explore.A) - Correlation Analysis, which can tell you the strength of relationship between two quantitative variables(<b>e.g.The longer the video, the more views</b>)  especially for your entered data. And B) - t-test, which returns boxplots for a feature with statistically significant differences(<b>e.g. If your TikToks with sunshine in gains more popularity then without it, it will send you a boxplot with this information</b>).
<b>Thirdly</b>, use 'Clean data' button to delete either the last observation or the whole data.
<b>To sum up</b>, This is how you use this bot: regularly adding data about your TikToks(don't forget to wait until the view and like rates are fixed), then use statistics to mine some insights about your video-content. Contacts:@paleasfuck'''
    return text
mes_send_csv = 'Google Sheets or Microsoft Excel?'

mes_quest_1 = 'Enter number of views on TikTok: (<b>e.g.32790</b>)'
mes_quest_2 = 'Enter number of likes on TikTok: (<b>e.g.5650</b>)'
mes_quest_3 = 'Enter number of comments on TikTok: (<b>e.g.89</b>)'
mes_quest_4 = 'Enter number of TikToks with the same sound:  (<b>e.g.9649</b>)'
mes_quest_5 = 'When the video was filmed?'
mes_quest_6 = 'Set the most suitable TikTok type group:'
mes_quest_7 = 'What color prevails in the video?'
mes_quest_8 = 'How many people are in the video?'
mes_quest_9 = 'Music in TikTok is:'
mes_quest_10 = 'When did you upload the video'
mes_quest_11 = 'Are there any sun rays in the video?'
mes_quest_12 = 'Is there any dance in the video?'
mes_quest_13 = 'Is there any LED Lighting in the video?'
mes_quest_14 = 'Do you have artificial or natural light?'
mes_quest_15 = 'Did you write something in a description field?'
mes_quest_16 = 'Is there a text write on screen?'
mes_quest_17 = 'Did you use TikTok Effects <b>(not filters, next question is about them)</b>'
mes_quest_18 = 'Did you use TikTok Filters'
mes_quest_19 = 'Did you format the video not in TikTok app?'
mes_quest_20 = 'What camera did you use?'
mes_quest_21 = 'Did you use any hashtags?'
mes_quest_22 = 'Choose the video dynamics:'
mes_end_questions = '''Data is saved. Use 'Statistics📊' button to get insights!'''

def mes_statistics(num):
    text = f'''Total count: {num}\n<b>The more import data, the better the result statistics</b>📈.'''
    return text

mes_corr = '''<i>Degree of correlation</i>:

<b>Perfect</b>: If the value is near ± 1, then it said to be a perfect correlation: as one variable increases, the other variable tends to also increase (if positive) or decrease (if negative).
<b>High degree</b>: If the coefficient value lies between ± 0.50 and ± 1, then it is said to be a strong correlation.
<b>Moderate degree</b>: If the value lies between ± 0.30 and ± 0.49, then it is said to be a medium correlation.
<b>Low degree</b>: When the value lies below ± .29, then it is said to be a small correlation.
<b>No correlation</b>: When the value is zero.'''

mes_ttest = 'y axis stands for Likes or Views - use it to identify what is helping your videos be more popular.  Found statistically significant differences for '
mes_ttest_none = '<b>None</b>'

mes_clean = 'You can delete all data or just the last observation.'

mes_clean_all = '''Are you sure that you want to delete all your data? You won't be able to recover it.'''
mes_clean_last = 'Successful, last data was deleted'