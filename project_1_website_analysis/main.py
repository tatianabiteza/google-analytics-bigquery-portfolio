# 📊 Project 1: Website Traffic Analysis using BigQuery

from google.cloud import bigquery
import pandas as pd

# Connect to BigQuery
client = bigquery.Client(project="la-vie-est-belle-project")

# Load GA4 data
query = """
SELECT *
FROM `la-vie-est-belle-project.analytics_541902922.events_20260620`
"""

df = client.query(query).to_dataframe()

# Show basic info
print("Total rows:", len(df))
print("Columns:", df.columns)

# Event breakdown
print("\nEvent counts:")
print(df["event_name"].value_counts())

# Users
print("\nUnique users:")
print(df["user_pseudo_id"].nunique())
