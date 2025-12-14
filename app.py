import streamlit as st
import preproccesor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    df = preproccesor.preprocess(data)

    if df.empty:
        st.error("No valid chat data found!")
    else:
        st.dataframe(df)

    #fetch unique users
    user_list = df['user'].unique().tolist()

    # Safely remove 'group_notification' if it exists
    if 'group_notification' in user_list:
        user_list.remove('group_notification')

    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.selectbox("Select a user:", ['Overall'] + list(df['user'].unique()))
    if st.sidebar.button("Show Analysis"):

        num_messages, words, links  = helper.fetch_stats(selected_user,df)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Links")
            st.title(links)


    # monthly timeline
        st.title('Monthly Timeline')
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color= '#722F37')
        plt.xticks(rotation ='vertical')
        plt.show()
        st.pyplot(fig)

        # daily timeline

        st.title('Daily Timeline')
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='purple')
        plt.xticks(rotation='vertical')

        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        # finding buisiest users in group chats

        if selected_user == 'Overall':
            st.title('Most Busy User')
            x, new_df = helper.fetch_most_busy_user(df)
            fig, ax = plt.subplots()

            col1,col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values, color = '#3D5B44')
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)


        # worcloud formatio
        st.title("WORD CLOUD")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # MOST Common words
        most_common_df = helper.most_common_words(selected_user,df)
        # Fetch most common words for the selected user
        most_common_df = helper.most_common_words(selected_user, df)

        # Check if most_common_df is not None and is not empty
        if most_common_df is not None and not most_common_df.empty:
            st.title('Most Common Words')

            # Check if the expected columns 'Word' and 'Frequency' are in the DataFrame
            if 'Word' in most_common_df.columns and 'Frequency' in most_common_df.columns:
                # Proceed with plotting
                fig, ax = plt.subplots()
                ax.barh(most_common_df['Word'], most_common_df['Frequency'])
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            else:
                # If the columns are missing or have different names, try to handle it gracefully
                st.error("DataFrame does not contain 'Word' and 'Frequency' columns.")
        else:
            # Handle cases where most_common_df is None or empty
            st.error(f"No valid data found for {selected_user}.")

        # Display the dataframe for debugging or inspection
        st.dataframe(most_common_df)

        st.dataframe(most_common_df)
    # emoji analyse

        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df['Frequency'].head(), labels=emoji_df['Emoji'].head(), autopct="%0.2f%%")

            st.pyplot(fig)