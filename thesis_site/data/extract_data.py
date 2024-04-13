import pandas as pd

# Load the data
excel_sheet = pd.read_excel('thesis_site/data/Sample data for Objective 1.xlsx', sheet_name=['Topics', 'Descriptions'])

# Extract the data

# Sheet 1
topic_list = excel_sheet['Topics']
topic_list.drop(topic_list.columns[1:-3], axis=1, inplace=True)

# Sheet 2
desc_list = excel_sheet['Descriptions']

# Print the columns
print(topic_list.columns)
print(desc_list.columns)

topic_list.to_json('./topic_obj_1.json', orient='records')
desc_list.to_json('./desc_obj_1.json', orient='records')
