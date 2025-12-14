import re
import pandas as pd

def preprocess(data):
    # Clean invisible characters
    data = data.replace("\u202f", " ").replace("\xa0", " ")

    # Pattern to match chat entries
    pattern = r"\[(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}:\d{2})\s(AM|PM)\] (.+)"
    matches = re.findall(pattern, data)

    if not matches:
        print("No matches found!")
        return pd.DataFrame()

    # Extract dates and messages
    dates = [f"{match[0]} {match[1]} {match[2]}" for match in matches]
    messages = [match[3] for match in matches]

    # Create DataFrame
    df = pd.DataFrame({'date': dates, 'user_message': messages})

    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y %I:%M:%S %p')

    # Split user and message
    users = []
    message_texts = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            message_texts.append(entry[2])
        else:
            users.append('group_notification')
            message_texts.append(entry[0])

    df['user'] = users
    df['message'] = message_texts
    df.drop(columns=['user_message'], inplace=True)

    # Additional columns for analysis
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.yearimport re
import pandas as pd

def preprocess(data):
    # Clean invisible characters
    data = data.replace("\u202f", " ").replace("\xa0", " ")

    # Pattern to match chat entries
    pattern = r"\[(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}:\d{2})\s(AM|PM)\] (.+)"
    matches = re.findall(pattern, data)

    if not matches:
        print("No matches found!")
        return pd.DataFrame()

    # Extract dates and messages
    dates = [f"{match[0]} {match[1]} {match[2]}" for match in matches]
    messages = [match[3] for match in matches]

    # Create DataFrame
    df = pd.DataFrame({'date': dates, 'user_message': messages})

    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y %I:%M:%S %p')

    # Split user and message
    users = []
    message_texts = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            message_texts.append(entry[2])
        else:
            users.append('group_notification')
            message_texts.append(entry[0])

    df['user'] = users
    df['message'] = message_texts
    df.drop(columns=['user_message'], inplace=True)

    # Additional columns for analysis
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df

    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df
