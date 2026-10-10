import requests
import pandas as pd

final_data=[]

try:
    response_1=requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    data_response_1=response_1.json()


    if response_1.status_code==200:

        for id in data_response_1[0:20]:

            response_2=requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")

            if response_2.status_code==200:
                
                data_response_2=response_2.json()

                final_data.append({
                    "Title": data_response_2.get("title", "Not available"),
                    "Score": data_response_2.get("score", "Not available"),
                    "Url": data_response_2.get("url","Not available")                
                    })

                print(f"Request succeed at id : {id}")


            else:
                print(f"Request failded at id : {id}")


    else:
        print(f"Request didn't proceeded as we got status code :{response_1.status_code} ")

except Exception as e:
    print(f"Error:{e}")

df=pd.DataFrame(final_data)
df.to_csv("Top 20 users from topstories.csv")
