## Email_Spam_Classification

Email-spam-classificationとは、電子メールをスパム（迷惑メール）と正常（スパムではないメール）に分類するためのシステムやアルゴリズムを指します。このような分類システムは、主に機械学習を利用して、メールの内容や特徴に基づいてスパムかどうかを自動的に判断します。

この課題では、最初にNaive Bayesアルゴリズム（GaussianNB、MultinomialNB、BernoulliNB）の3種類を適用し、それぞれの**精度（accuracy）**と**適合率（precision）**を評価しました。その結果、**MultinomialNB**が他のモデルと比較して最も高い性能を示しました。具体的には、**精度は0.9709864603481625**で、非常に高い分類能力を持つことが確認され、さらに**適合率（precision）**では**1.0**という完璧な値を記録しました。この結果から、MultinomialNBは特に有効な手法であると判断されました。

<img src="pictures/mnb_accuracy & precision_result.png" height="400px" width ="550px">　

しかし、モデルのさらなる改善と精度の向上を目指し、Naive Bayes以外のアルゴリズムも試すことにしました。具体的には、機械学習でよく使用されるトップ11のアルゴリズム（例: SVM、決定木、ランダムフォレスト、K近傍法など）を用いて分析を行い、それぞれの性能を比較・評価しました。これにより、さらに優れたモデルを探索し、最適な分類精度を追求しました。

### LR = from sklearn.linear_model import LogisticRegression
### SVC = from sklearn.svm import SVC
### NB = from sklearn.naive_bayes import MultinomialNB
### DT = from sklearn.tree import DecisionTreeClassifier
### KN = rom sklearn.neighbors import KNeighborsClassifier
### RF = from sklearn.ensemble import RandomForestClassifier
### AdaBoost = from sklearn.ensemble import AdaBoostClassifier
### BgC = from sklearn.ensemble import BaggingClassifier
### ETC = from sklearn.ensemble import ExtraTreesClassifier
### GBDT = from sklearn.ensemble import GradientBoostingClassifier
### xgb = from xgboost import XGBClassifier

<img src="pictures/Screenshot 2024-11-18 193733.png" height="400px" width ="550px">　

上記の結果から、Naive Bayes（NB）、K近傍法（KNN）、ランダムフォレスト（RF）の適合率（precision）はいずれも1.0と非常に優れていました。一方で、モデルのさらなる改善や精度（accuracy）の向上を目指し、新たな手法として以下を試みました。

tfidf = from sklearn.feature_extraction.text import TfidfVectorizer
minmax_scaler = from sklearn.preprocessing import MinMaxScaler
ここでTfidfVectorizerでは最大特徴量（max_features）を3000に設定して分析行い、これらを適用して、それぞれのアルゴリズムで分析を行った結果は以下の通りです。


### "Please wait, the project GIF file is loading..." ###
<img src="Email_sms_spam_Classification/Email_spam_Classifier1st_part-.gif" width="700px">
<img src ="Email_sms_spam_Classification/Email_spam_Classifier2nd_part-.gif" width="700px"

### Thanks for watching.... ###
