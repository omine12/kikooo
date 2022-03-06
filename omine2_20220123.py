
from bs4 import BeautifulSoup #HTMLを読み取る
import urllib.request as rep #PythonでURLを扱う
import pandas as pd


parser_html = BeautifulSoup(html,"html.parser") #HTMを解析
print(parser_html.prettify())

url = "https://kino-code.work/python-scraping/"
response = rep.urlopen(url)  #指定したHTMLのurlを取得

parser_html = BeautifulSoup(response, "html.parser")
print(parser_html.title.string) #titleのみ出力
print(parser_html.find_all("a")) #指定したタグの要素を取得 （aタグ）
title_lists = parser_html.find_all("a")
title_lists[1:10]
title_lists[10].string
title_lists[10].attrs["href"]

title_list=[]
url_list=[]

for i in title_lists:
    title_list.append(i.string) #appendは、要素を追加。iを追加
    url_list.append(i.attrs["href"])

df_title_url = pd.DataFrame({"Title":title_list,"URL":url_list})
df_notnull = df_title_url.dropna(how="any") #dropnaは、欠損値を除く。行に一つでも欠損値があれば削除する。
df_notnull["Title"].str.contains("Python超入門コース") #特定の文字列で始まるか判定。正しいか正しくないかを返す
df_notnull[df_notnull["Title"].str.contains("Python超入門コース")]
df_contain_python = df_notnull[df_notnull["Title"].str.contains("Python超入門コース")]
df_contain_python
df_contain_python.to_csv("output.csv") #csvファイルに値を書き込む