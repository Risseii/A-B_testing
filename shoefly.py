#A/B Testing for ShoeFly.com
#Our favorite online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.

import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

print(ad_clicks.groupby(['utm_source']).user_id.count().reset_index())

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp .isnull()

#We want to know the percent of people who clicked on ads from each utm_source.Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups.
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

#Pivot table
clicks_pivot = clicks_by_source.pivot(columns = 'is_click',index = 'utm_source',values = 'user_id')

print(clicks_pivot)

#Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

#Count of user_id group by experimental_group
ad_clicks.groupby(['experimental_group']).user_id.count().reset_index()

#Pivot table of user_id group by experimental_group and is_click and divided by True and False
print(ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='experimental_group',values='user_id').reset_index())

#Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
print(a_clicks)

b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']
print(b_clicks)

#For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
a_clicks_group = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(columns='is_click',index='day',values='user_id')

print(a_clicks_group)

a_clicks_group['percentage_A'] = a_clicks_group[True] / (a_clicks_group[True] + a_clicks_group[False])

print(a_clicks_group)

b_clicks_group = b_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(columns='is_click',index='day',values='user_id')

b_clicks_group['percentage_B'] = b_clicks_group[True] / (b_clicks_group[True] + b_clicks_group[False])

print(b_clicks_group)

#Result: We can see that overall Ad A is better than Ad b except for tuesday. 









