import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


df=pd.read_csv("social_media_engagement_data.csv")
print(df.head());

Linkedindata=df[df["Platform"]=="LinkedIn"]
print(Linkedindata.head());



import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    database='Social_media_projects',
    user='root',
    password='6844'
)

cursor = conn.cursor()

# Create Matrics Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Matrics (
    MatricsID INT PRIMARY KEY,
    `Like` INT,
    Comment INT,
    Share INT,
    Reach INT,
    Engagement_Rate INT,
    Audience_Age INT,
    Post_Type VARCHAR(255),
    Platform_Name VARCHAR(255)
);
''')

# Create Audience Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Audience (
    AudienceID INT PRIMARY KEY,
    Audience_Age INT,
    Audience_Gender VARCHAR(255),
    Audience_Location VARCHAR(255),
    Audience_Interests VARCHAR(255)
);
''')

# Create Platform Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Platform (
    PlatformID INT PRIMARY KEY,
    Campaign_Name VARCHAR(255),
    PlatformName VARCHAR(255)
);
''')

# Create Post Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Post (
    PostID INT PRIMARY KEY,
    Post_Type VARCHAR(255),
    Post_Content TEXT,
    Post_Timestamp TIMESTAMP
);
''')

# Close connection
conn.commit()
cursor.close()
conn.close()
print("Table Created")

Linkedindata['MatricsID'] = range(1, len(Linkedindata) + 1)

# Verify 'MatricsID' column now exists
print(Linkedindata.head())

print(Linkedindata.columns)

import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host='localhost',
    database='Social_media_projects',
    user='root',
    password='6844'
)

cursor = conn.cursor()

# Prepare the SQL query for insertion
insert_query = """
    INSERT INTO Matrics (MatricsID, Like, Comment, Share, Reach, Engagement_Rate, Audience_Age, Post_Type, Platform_Name)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Iterate through each row in the DataFrame
for _, row in Linkedindata.iterrows():
    try:
        cursor.execute(insert_query, (
            row['MatricsID'],
            row['Likes'],
            row['Comments'],
            row['Shares'],
            row['Reach'],
            row['Engagement_Rate'],
            row['Audience_Age'],
            row['Post_Type'],
            row['Platform']
        ))
    except Exception as e:
        print(f"Error inserting row: {e}")

# Commit the transaction
conn.commit()

print("Data inserted successfully!")

# Close the connection
cursor.close()
conn.close()

Linkedindata=Linkedindata.rename(columns={"Post ID":"Post_id","Post Type":"Post_Type","Post Content":"Post_Content", "Post Timestamp":"Post_Timestamp", 
                             "Engagement Rate":"Engagement_Rate", "Audience Age": "Audience_Age", "Audience Gender": "Audience_Gender",
                            "Audience Location": "Audience_Location", "Audience Interests": "Audience_Interests", "Campaign ID":"Campaign_ID",
                            "Influencer ID": "Influencer_ID", "MatricsID": "Matrics_ID" })
print(Linkedindata.head())


Linkedindata['AudienceID'] = range(1, len(Linkedindata) + 1)

# Verify 'MatricsID' column now exists
print(Linkedindata.head())

import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    database='Social_media_projects',
    user='root',
    password='6844'
)
cursor = conn.cursor()

# Iterate through Linkedindata rows
for _, row in Linkedindata.iterrows():
    try:
        # SQL query with corrected column names
        insert_query = """
        INSERT INTO audience (AudienceID, Audience_Age, Audience_Gender, Audience_Location, Audience_Interests)
        VALUES (%s, %s, %s, %s, %s)
        """
        # Execute the query with the current row's values
        cursor.execute(insert_query, (
            row['AudienceID'],
            row['Audience_Age'], 
            row['Audience_Gender'], 
            row['Audience_Location'], 
            row['Audience_Interests']
           
        ))
    except mysql.connector.Error as err:
        print(f"Error inserting row: {err}")
        continue

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

Linkedindata['PlatformID'] = range(1, len(Linkedindata) + 1)

# Verify 'MatricsID' column now exists
print(Linkedindata.head())

import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    database='Social_media_projects',
    user='root',
    password='6844'
)
cursor = conn.cursor()

# Iterate through Linkedindata rows
for _, row in Linkedindata.iterrows():
    try:
        # SQL query with corrected column names
        insert_query = """
        INSERT INTO platform (PlatformID,Campaign_ID,PlatformName )
        VALUES (%s, %s, %s)
        """
        # Execute the query with the current row's values
        cursor.execute(insert_query, (
            row['PlatformID'],
            row['Campaign_ID'], 
            row['Platform']
           
        ))
    except mysql.connector.Error as err:
        print(f"Error inserting row: {err}")
        continue

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    database='Social_projects',
    user='root',
    password='6844'
)
cursor = conn.cursor()

# Iterate through Linkedindata rows
for _, row in Linkedindata.iterrows():
    try:
        # SQL query with corrected column names
        insert_query = """
        INSERT INTO post (PostID, Post_type, Post_Content, Post_Timestamp )
        VALUES (%s, %s, %s, %s)
        """
        # Execute the query with the current row's values
        cursor.execute(insert_query, (
            row['Post_id'],
            row['Post_Type'], 
            row['Post_Content'],
            row['Post_Timestamp']
           
        ))
    except mysql.connector.Error as err:
        print(f"Error inserting row: {err}")
        continue

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

