# GitHub Python Repo Lead Generator

# Finds active, popular Python repositories on GitHub and outputs prioritized sales lead lists for a Python dev-tools company.

# ICP (via GitHub Search API): Python primary language, 500+ stars, not archived, pushed within 90 days.

# Segments:

# Hot leads — pushed ≤30 days
# Warm leads — pushed 31–90 days

import requests
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timezone, timedelta
import numpy as np



load_dotenv()
token=os.getenv("token")

header={
"authorization":f"Bearer {token}"
}

page=1

segment_1=[]
segment_2=[]

total_pages_required=3 # 1 page = 100 repos (can be changes but here its maximum repos/page)

cutoff_date = (datetime.now(timezone.utc) - timedelta(days=90)).strftime("%Y-%m-%d")

while page<=total_pages_required:
    try:
        response=requests.get(f"https://api.github.com/search/repositories?q=language:python+stars:>500+archived:false+pushed:>{cutoff_date}&per_page=100&page={page}",headers=header)
        #This url means:

        # "Give me up to 100 non-archived Python repositories with more than 500 stars that were pushed within the last 90 days, and give me the results for the current page.

        if response.status_code!=200:
            print(f"No response as it gave error code {response.status_code}")
            break

        data=response.json() #With gh api , we have 5000 request / hour limit and here 1 re1 = 100 repos so 300 repos = 3 requetss so adding rate limits would be a overkill here 

        for repo in data["items"]:
            
            pushed = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            days_since = (datetime.now(timezone.utc) - pushed).days

            if days_since<=30: #Segmentation of hot build - highest priority - last repo acivity in  last 30 days
                segment_1.append({

                    "Name":repo.get("full_name",np.nan),
                    "Stars":repo.get("stargazers_count",np.nan),
                    "pushed_at":repo.get("pushed_at",np.nan),
                    "Repo URL":repo.get("html_url",np.nan),
                    "Description":repo.get("description",np.nan)

                })

                print("Repo appended in high priority leads")

            else: # Segmentation 2 - repos last activity in last 30-90 days

                segment_2.append({

                    "Name":repo.get("full_name",np.nan),
                    "Stars":repo.get("stargazers_count",np.nan),
                    "pushed_at":repo.get("pushed_at",np.nan),
                    "Repo URL":repo.get("html_url",np.nan),
                    "Description":repo.get("description",np.nan)

                })


                print("Repo appended in  2nd priority leads")



    except Exception as e :
        print(f"Error : {e}")  # Bigger net to capture errors - will improve it and make specific with time
    page+=1

print(f"Summary \n Total leads - highest priority : {len(segment_1)} \n Total leads - 2nd priority : {len(segment_2)}")
df_1=pd.DataFrame(segment_1)
df_2=pd.DataFrame(segment_2)

df_1.to_csv("highest_priority_leads.csv", index=False)
df_2.to_csv("2nd_priority_leads.csv", index=False)
