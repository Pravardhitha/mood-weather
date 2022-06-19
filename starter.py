import streamlit as st

st.write("# Mood-Weather")
st.write("### Experience the weather of your mood!")
with st.form(key="mood_form"):
    st.markdown(":cherry_blossom:")
    happy = st.select_slider("How happy are you today?", options=[1,2,3,4,5])
    #st.write(happy)

    st.markdown(":umbrella:")
    sad = st.select_slider("How sad are you today?", options=[1,2,3,4,5])
   
    #st.write(sad)
    st.markdown(":baby_chick:")
    calm = st.select_slider("How calm are you today? ", options=[1,2,3,4,5])
    
    #st.write(calm)
    st.markdown(":sun_with_face:")
    energetic = st.select_slider("How energetic are you today?", options=[1,2,3,4,5])
    #st.write(energetic)
    

    submit_button = st.form_submit_button(label="Submit")

if(sad==2 and happy==2 and energetic==2 and calm==2):
    st.markdown(f'<img src="https://raw.githubusercontent.com/Pravardhitha/mood-weather/main/all2.gif" width = "700" height = "500">', unsafe_allow_html=True)
    
    st.markdown("#### You are all balanced...")
    st.markdown("#### like a protogonatist from a book after all the charecter developement")
    st.markdown("#### great job, keep it up.")
    st.markdown("#### but try to be more happy.")

    st.write("## Here is a song suggestion for you")

    audio_file = open("all2.mp3", "rb")

    st.audio(audio_file.read())    

elif(happy==5):
    st.markdown(f'<img src="https://raw.githubusercontent.com/Pravardhitha/mood-weather/main/happy.gif" width = "700" height = "500">', unsafe_allow_html=True)

    st.markdown("#### You feel so happy! we are happy for you")
    st.markdown("#### Share the happiness")
    st.markdown("#### call your friend or distant relative")
    st.markdown("#### volunteer in some charity work")
    st.markdown("#### make someone's day")

    st.write("## Here is a song suggestion for you")

    audio_file = open("happy.mp3", "rb")

    st.audio(audio_file.read())  

elif(sad==5):
    st.markdown(f'<img src="https://raw.githubusercontent.com/Pravardhitha/mood-weather/main/sad.gif" width = "700" height = "500">', unsafe_allow_html=True)

    st.markdown("#### Ouch, im sorry to hear that you are sad.")
    st.markdown("#### whatever it might be that ruined your day, you can always")
    st.markdown("#### start afresh")
    st.markdown("""#### Here are some tips
    1. listen to cheerful songs

    2. Dance, move a little

    3. Dang out with your friends

    4. Go for shopping or work out
    
    If it has been same since long, get some profesional help 
    
    Don't hesitate to call helplines in extreme conditions""")


    st.write("## Here is a song suggestion to cheer you up")

    audio_file = open("sadsong.mp3", "rb")

    st.audio(audio_file.read())  

elif(energetic==5):
    st.markdown(f'<img src="https://raw.githubusercontent.com/Pravardhitha/mood-weather/main/energetic.gif" width = "700" height = "500">', unsafe_allow_html=True)

    st.markdown("#### You are so energetic right now.")
    st.markdown("#### Use your energy productively just like how solar panels work")
    st.markdown("#### Best on sunny days")
    st.markdown("#### Start doing that job you always wanted to NOW.")

    st.write("## Here is a song suggestion for you")

    audio_file = open("energetic.mp3", "rb")

    st.audio(audio_file.read()) 

elif(calm==5):
    st.markdown(f'<img src="https://raw.githubusercontent.com/Pravardhitha/mood-weather/main/calm.gif" width = "700" height = "500">', unsafe_allow_html=True)

    st.markdown("#### You feel so calm right now. that sounds perfect...who doesnt like calm people")
    
    st.markdown("""
    #### Here are some suggestions for you
    1. read a book
    2. practice meditating
    3. go for a walk
    """)

    st.write("## Here is a song suggestion for you")

    audio_file = open("calm.mp3", "rb")

    st.audio(audio_file.read())