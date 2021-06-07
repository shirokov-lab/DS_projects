# Data science portfolio

## Table of content
  - [Projects](#projects)
    * [project_0 - IMBD movies analysis.](#project0)
    * [project_1 - Analysis of sales of an online store.](#project1)
    * [project_2 - What make chocolate bars popular among people?](#project2)
    * [project_3 - Preventing bad scores on your math exam.](#project3)
    * [project_4 - TripAdvisor fake reviews research.](#project4)
    * [project_5 - Telegram bot that collects, analyzes and saves data about TikTok videos.](#project5)
  - [Contacts](#contacts)
    * [CV](#cv)

# Projects
Evolution of my data science skills. Step by step - project by project.

## <a name="project0"></a>project_0 - IMBD movies analysis.
### Description:
This is my first pet-project where I analyze IMDB dataset. Which actor has starred in more high-budget films? For which director is winter the most productive time of the year? What actors are most often filmed together? I answer these and other 20+ interesting questions from movie industry.
### Tools:
- Python
- Pandas
- Numpy
- Collections
- Itertools
- Patplotlib.pyplot
- Seaborn
### Goal:
Main goal of this work is practicing my data-managing skills such as: data visualization, insight mining and basic EDA.


## <a name="project1"></a>project_1 - Analysis of sales of an online store.
### Description:
In this work I had datasets for an every month containing sales information so in fact it is Analysis of annual sales of an online electronics store. Also, data wasnt really clean: bunch of missing values, mistakes and wrong data types. So before main analysis I had to carry out some preprocessing. Big thanks to youtube video-maker Keith Galli for inspiring and great educational videos. 
### Tools:
- Python
- Pandas
- Numpy
- Collections
- Itertools
- Patplotlib.pyplot
- Seaborn
- Datetime
- os
### Goal:
Despite big practicing in writing code with python and working with pandas dataframes — this project made me also explore some business questions, such as: When and why we should display advertisements to maximize the likelihood of purchases? What product sold the most and why? And so on..but main one for me was how actually use data to answer questions like this?


## <a name="project2"></a>project_2 - What make chocolate bars popular among people?
### Description:
What features have the most effect on chocolate bar Rating? Data required great preprocessing: managing missing values(firstly detect them using IQR rule vs. common sense, secondly decide whether it real value or a mistake and then choosing the best way to fill them), find and solve non-Gaussian distributions and so on. After that I did a correlation analysis and analysis of nominative variables as well. In this project I used corr.matrix and student's t-test of course with extra help I gain from visualization. After every step I write analytical results, conclusions and my personal thoughts. 
### Tools:
- Python
- Pandas
- Numpy
- Collections
- Itertools
- Patplotlib.pyplot
- Seaborn
- Scipy.stats
- re
### Goal:
Learn how pipelines work — I tried to make my analysis as structured as possible. Practising my python skills with defining functions which helped me a lot during this work. I also wanted to use statistics tests here so I can get a more interpreted insights and results. Moreover, I used great opportunity to improve my English skills while reading lots of documentations and data science articles.


## <a name="project3"></a>project_3 - Preventing bad scores on your math exam.
### Description:
This work as all about Analysis of the results of the math exam for students between 15 and 22 years. What features affect the exam result? By finding this out, it is possible to identify the risk group in advance and prevent bad results. Doing this project I had great opportunity to improve my skills. Thanks to stackoverflow I got to know some new techniques and improved my English as well. Furthermore, I spend some days just to dive into the subject area so I can get a better understanding of data. I can say this analysis is very interesting.
### Tools:
- Python
- Pandas
- Numpy
- Collections
- Itertools
- Patplotlib.pyplot
- Seaborn
- Scipy.stats
- re
### Goal:
Main goal was to get a clear understanding why people fail their math exams. How we can prevent it? How we can easily find and recognize risk group and help these students? Does something else apart of real math skills affect stusents' results? How I can put together my investigation work with statistical testing to answer those questions?


## <a name="project4"></a>project_4 - TripAdvisor fake reviews research.
### Description:
There is a TripAdvisor restaurants database which contains lots of interesting for analysis features. It seems like some restaurants be 'boosting' their rating with fake reviews. I built a model which predict Restaurant Rating so we can compare my predict and real value. In case there is a large difference — we should check if this restaurant's reviews are fair. I build and test hypotheses using statistics, do Feature engineering including polynomial features. I also create and train regression model and test it with metrics. Big preprocessing(missing values, outliers, mistakes) was required as well.
### Tools:
- Python
- Pandas
- Numpy
- Collections
- Itertools
- Patplotlib.pyplot
- Seaborn
- Scipy.stats
- ast
- re
- Datetime
- Sklearn
### Goal:
Main task was building a model which can help TripAdvisor to get rid of scammers — people who boost a restaurant rating and thereby deceive visitors. As for me a great goal was also a starting to learn ML.


## <a name="project5"></a>project_5 - Telegram bot that collects, analyzes and saves data about TikTok videos.
### Description:
Best way to describe this project is just share a link [https://tg.telepult.pro/ttbooster_bot] — bot is 100% free and working 24/7. Tasks this bot performs are: regularly collecting data through surveys(20+ features), displays number of observations, performing statistical test for numerical, categorical and binary data types to gain insights, plotting categorical data in case there is statistically significant differences for the feature, cleaning your data in case you need it, collecting all data from all users and saving it to .csv for further analysis.  
### Tools:
- Python
- aiogram
- SQLAlchemy
- Scipy
- async
- Pandas
- Numpy
- Seaborn
### Goal:
My girlfriend doing tiktok and I came up with an idea to build a bot which will provide her some kind of a premium statistics — finding what are those 'parts' of video that makes it popular/unpopular. As a junior data scientist I also have a goal to collect data and do some research on people who do tiktok and their videos. To do this, I need to wait a little while people use the bot so that there will be enough collected data for interesting and quality investigation.


# Contacts
Hi, my name is Nikita! Please feel free to contact me. Also, I am currently looking for a job so I am open for any interesting work or project :)
<img src="data:image/png;base64,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" alt="alt text" width="whatever" height="whatever"> @paleasfuck
