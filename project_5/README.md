# Statistical telegram bot
How it works?

Firstly, add observation with 'New video' button. Every TikTok = one observation. Add your videos' data and then use statistical tests to know what brings you more likes and views. *The more import data, the better the result statistics*📈.
Secondly, after adding data, you can get your results by pressing the 'Statistics' button. Then choose, what test's result you need to explore. A) - Correlation Analysis, which can tell you the strength of relationship between two quantitative variables(*e.g.The longer the video, the more views*) especially for your entered data. And B) - t-test, which returns boxplots for a feature with statistically significant differences(*e.g. If your TikToks with sunshine in gains more popularity then without it, it will send you a boxplot with this information*). Thirdly, use 'Clean data' button to delete either the last observation or the whole data.
To sum up, this is how you use this bot: regularly adding data about your TikToks(don't forget to wait until the view and like rates are fixed), then use statistics to mine some insights about your video-content. As an administrator, I can get all the data in the form of a .csv file of all users for further analysis.






@

To launch the bot use the bot.py file, after installing all the packages from the requirements.txt file

@

Before launching, you need to enter the token of your bot, created in @BotFather, in the misc.py file, in the line "bot = Bot (token = 'YOUR TOKEN')".
And also in the line "admin_id = 0" replace the value of the variable with your ID without quotes.
You can find out your ID using the @myidbot bot and the "/ getid" command.

###

The "/ start" command is a starting command in a dialogue with a bot, as well as a command to return to the main menu under any circumstances.

###

Before starting a dialogue with the bot, you must turn off the privacy setting in the telegram along the path "Settings -> Confidentiality -> Forwarding messages -> Who can refer to my account when forwarding messages -> All".
