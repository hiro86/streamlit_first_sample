# いまにゅ先生のSteamlit入門
# Streamlitの公開方法
# Streamlit shareling & git hub
# gitにadd, requirementに外部ライブラリを記載

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit 超入門")
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(11):
    latest_iteration.text(f'Iteration {i*10}')
    bar.progress(i*10)
    time.sleep(0.1)

'Done!!!'

st.write('インタラクティブ')
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムだよ')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容はこちらへ')

condition = st.slider('あなたの今の調子は?', 0, 100, 50)
hobby = st.text_input('あなたの趣味を教えて下さい。')

# st.write('インタラクティブ')
# condition = st.sidebar. slider('あなたの今の調子は?', 0, 100, 50)
# hobby = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# 'コンディション:', condition
# 'あなたの趣味は', hobby, 'ですね'

option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です'

st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('test.jpg')
    st.image(img, caption='test', use_column_width=True)

st.write('DataFrame')
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],

})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

"""
# マークダウンで記載できる。
## H2タグ
バッククオテーションで囲むと、パイソン系形式で記載できる。

```
import streamlit as st
import numpy as np
import pandas as pd
```

"""