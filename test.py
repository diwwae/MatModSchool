#╰( ͡☉ ͜ʖ ͡☉ )つ──☆*:・ﾟ   ฅ^•ﻌ•^ฅ   ʕ•ᴥ•ʔ
import pandas as pd

train_data = pd.read_csv("/mnt/c/Users/zer0nu11/Documents/workspace/projects/MatModSchool/train.csv")
import seaborn as sns

sns.histplot(train_data.trip_duration)