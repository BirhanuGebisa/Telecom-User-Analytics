import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("Telecommunication User Engagement Analysis")

    df_email = pd.read_csv('data/top10_email_users.csv')
    df_game = pd.read_csv('data/top10_gameApp_users.csv')
    df_google = pd.read_csv('data/top10_google_users.csv')
    df_netflix = pd.read_csv('data/top10_netflix_users.csv')
    df_otherAct = pd.read_csv('data/top10_otherAct_users.csv')
    df_social = pd.read_csv('data/top10_socialMedia_users.csv')
    df_youtube = pd.read_csv('data/top10_youtube_users.csv')
    df_session = pd.read_csv('data/top10_user_session.csv')
    df_DLUL = pd.read_csv('data/top10_DLUL_users.csv')

    st.header("Top 3 Best Handset Manufacturers")
    st.image('data/3_best_handset_manufacturers.png')

    st.header("Top 5 Best Handsets Used for Communication")
    st.image('data/5 Best Phones used in Communication.png')

    st.header("Top 3 Most Used Applications")
    st.image('data/top10apps.png')

    st.header("Data Transfers and overall data usage correlation.")
    st.image('data/corellation.png')
    st.markdown(
        'There is a correlation between Data Transfers and total data usage in games and other apps.')

    st.header("Top 10 Users Engaged Per Application")
    st.subheader("Email App users")
    st.dataframe(df_email)
    st.bar_chart(df_email.Email_Total_Data)

    st.subheader("Game App users")
    st.dataframe(df_game)
    st.bar_chart(df_game.Gaming_Total_Data)

    st.subheader("Google App users")
    st.dataframe(df_google)
    st.bar_chart(df_google.Google_Total_Data)

    st.subheader("Netflix App users")
    st.dataframe(df_netflix)
    st.bar_chart(df_netflix.Netflix_Total_Data)

    st.subheader("Other App users")
    st.dataframe(df_otherAct)
    st.bar_chart(df_otherAct.Other_Total_Data)

    st.subheader("Social Media App users")
    st.dataframe(df_social)
    st.bar_chart(df_social.Social_Media_Total_Data)

    st.subheader("Youtube App users")
    st.dataframe(df_youtube)
    st.bar_chart(df_youtube.Youtube_Total_Data)

    st.subheader("Top 10 users based on session count")
    st.dataframe(df_session)
    st.bar_chart(df_session['Dur. (ms)'])

    st.subheader("Top 10 users based on download and upload count")
    st.dataframe(df_DLUL)
    st.bar_chart(df_DLUL['Total UL and DL'])

    st.header("3 groups k-means clustering")
    st.image('data/engclusters.png')
