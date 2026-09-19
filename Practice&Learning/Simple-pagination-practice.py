import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
token=os.getenv("token")

header={
    "authorization":f"Bearer {token}"
}

page=0
since=0
final_result=[]
total_pages_required=3 # 1 page = 30 users

while page<total_pages_required:

    try:
        response=requests.get(f"https://api.github.com/users?since={since}",headers=header)

    
        if response.status_code!=200:
            print(f"No response as it gave error code {response.status_code}")
            break


        data=response.json()
        if len(data)==0:
                     print(f"Lenght of response is 0")
                     break
        
        for user in data:
                print(f"User:{user["login"]} has id {user["id"]}")
                final_result.append({
                    "Username":user["login"],
                    "ID":user["id"]
            })
            

        since=data[-1]["id"]
        page+=1

    except Exception as e:
        print(f"Error : {e}")

df=pd.DataFrame(final_result)
df.set_index("ID",inplace=True)
df.to_csv("pagination(3 pages).csv")

    
    
