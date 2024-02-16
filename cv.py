##############################################################################
###Program Name: cv.py
###Programmer: Aaliyah Raderberg
###Project: Build a Online CV/Resume Web App with Streamlit and Python
##############################################################################

import streamlit as st
from pathlib import Path
import pandas as pd
from annotated_text import annotated_text

# Initial page config

st.set_page_config(
     page_title='📝CV-Resume-Raderberg',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cv_sidebar()
    cv_body()

    return None

col1, col2, col3 = st.columns(3)
col1.metric("Industry Experience", "15+", "+")
col2.metric("Biotech/Pharma", "10", "+")
col3.metric("Medical Device/CRO", "5", "+")

# sidebar

def cv_sidebar():
    st.image('https://aaliyahraderberg.files.wordpress.com/2024/02/araderberg_alogo.png', width=500)
    
       

    st.sidebar.header('📝Career Timeline')

    st.sidebar.markdown('''
<small>Links to Visualization [projects](https://public.tableau.com/app/profile/aaliyahraderberg/vizzes) using [Tableau](https://public.tableau.com/app/profile/aaliyahraderberg/vizzes).</small>'''
    , unsafe_allow_html=True)
    
    st.sidebar.markdown('''__Resume__''')
    st.sidebar.success('Only the right place can value you the right way!')
   

#Hire button
    st.sidebar.link_button("Hire Me!", "https://aaliyahraderberg.wordpress.com/contact-me/")
    st.toast('Welcome to my Streamlit App - Resume!', icon='🌞')
    
    st.sidebar.caption('# :red[Data | Analytics | Automation]')

#See other apps link
    with st.sidebar.expander("See My Other Streamlit Apps"):
        st.caption("Data Science NYC Collisions: [App](https://data-science-collision.streamlit.app/) 🔆,  [Blog Post](https://aaliyahraderberg.wordpress.com/read-the-blog/) 📝")
    
    st.sidebar.markdown("---")

#Education section
    st.sidebar.markdown('__🎓Education__')
    st.sidebar.code('''
>>> Google IT Automation with Python Professional Certificate
>>> Google Data Analytics Professional Certificate
>>> MS Project Management
>>> BS Information Systems
   ''')
    
#Strengths section
    st.sidebar.markdown('__💪🏼Strengths__')
    st.sidebar.code('''
# my strengths:
>>> Accountability = I take ownership of my mistakes. By
doing that I learn what I did wrong so
that it does not happen again.
>>> Problem-Solving/Troubleshooting = Adept at identifying and resolving issues.
>>> Multitasking = Comfortable juggling 2-3 projects at once
>>> Life-long Learner = Never done learning and always seeking
to improve myself. Curious about new possibilities and taking action to explore them.
>>> Results / Detail Oriented = Dedicated to completion of tasks in a timely manner and with regard to quality
    ''')

#Tech section
    st.sidebar.markdown('''__📈Tech Skills__''')
    st.sidebar.code('''
# list of tech skills:
$  JIRA
$  Tableau
$  RWD-RWE
$  EHR/EMR
$  SmartSheet
$  Conflucence
$  Spreadsheets
$  Python Coding
$  Git and GitHub
$  BigQuery/Kaggle
$  SAS / R coding
$  Automation scripting
$  Bash / SQL Scripting
$  Data Management/EDC/SDTM
$  Data Analysis/Data Visualization
$  Advanced troubleshooting and debugging
    ''')
    
 #tags   
    annotated_text(
    "coding ",
    ("python", ".py"),
    ("bash", ".sh"),
    ("C#", ".cs"),
    " statistics/analysis/SDTM ",
    ("SAS", ".sas"),
    ("R", ".rmd"),
    " data visualization ",
     ("tableau", ".twbx"),
     ("powerBI", ".pbix"),
    " troubleshooting ",
    ("debug", "breakpoint"),
    ("versionControl", "git"),
    "."
)

#Clinical section
    st.sidebar.markdown('__⚕️Clinical Knowledge__')
    st.sidebar.code('''
>>> ICH6 / HL7
>>> FDA / EMA
>>> CFR Part 11
>>> HIPPA / GDPR
>>> CDISC Standards
>>> Data Management
>>> Project Management
>>> Electronic Data Capture (EDC)
>>> Data Integrity
   ''')

#Phases section
    st.sidebar.markdown('__💊Clinical Phases__')
    st.sidebar.code('''
>>> Phase 1 - PK/PD
>>> Phase 2 – 3 - Various projects
>>> Phase 4 - GSK-post marketing
>>> Medical Device - EUA, MDR, IVD, 510K
   ''')

#Language section
    st.sidebar.markdown('''__🈳Language Skills__''')
    st.sidebar.code('''
# list of foreign languages:
🇵🇦 Spanish
🇧🇷 Portuguese
🇳🇱 Dutch
🇩🇪 German
🇮🇹 Italian
    ''')

#certificates section
    st.sidebar.markdown('__📜Certifications__')
    first = st.sidebar.checkbox("Show Google Certifications", False)
    if first:
       st.sidebar.text('Google Data Analytics')
       st.sidebar.text('Google IT Automation with Python')

    second = st.sidebar.checkbox("Show EDC Certifications", False)
    if second:
         st.sidebar.text('Rave EDC Study Builder')
         st.sidebar.text('Rave EDC Study Administrator')

#About me section  
    st.sidebar.markdown('<small>Learn more about [About Me!](https://github.com/araderberg/)</small>', unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('<small>[Resume v1.0](https://github.com/araderberg/cv-resume)  | Feb 2024 | [l Aaaliyah RaDerBerg](https://aaliyahraderberg.wordpress.com/)</small>', unsafe_allow_html=True)

    return None

##########################
# Main body of cheat sheet
##########################

def cv_body():

    col1, col2 = st.columns(2)

    #######################################
    # COLUMN 1
    #######################################

# Accomplishments / collaborations

    col1.subheader('Accomplishments')
    col1.code('''
$ SAS Data Listings
$ Auto-Labeling (data automation)
$ Checksum (data integrity tool)
$ DVS Generator– Python programming
$ EDC (ALS) Validator – Python programming
$ SDTM mapping/macros SAS programming
$ CDISC Mapping implementation tool
$ eTMF Implementation (VeeVa Vault)
$ CTMS Implementation (Medidata CTMS)
$ EDC Validation / CFR11
$ Rave EDC, Oracle RDC / Inform Global Library implementation
$ Standards Reports (BO, Crystal Reports, Cognos, SAS)
$ DNANexus Validation / CRF11
$ Oracle Inform EDC Training
$ Data Management SOP Writing

# * click the Hire Me! button on the sidebar to discuss further...

    ''')

    # Display projects
    with col1:
        col1.subheader('Hands-on Projects')
        pty = st.radio(
            "2023-Present",
            [":rainbow[Python app]", "***Mobile App with Google Sheets***", "CV19 Predictions", "Data Analysis & Visualization","Risk Predictions","Cancer Diagnostic", "Chatbot"],
            index=None,
)
        st.write("You selected:", pty)


    #######################################
    # COLUMN 2
    #######################################

    with col2:
        col2.subheader('Experience')
        st.code('''
# list of companies I have worked for:
>>>  GSK (Consultant)
>>>  RAeclinica
>>>  GenesisCare
>>>  Danaher/Beckman
>>>  Amgen (CRO FSP)
>>>  CROs
>>>  J&J / Jansen (Consultant)
>>>  Novartis Vaccines (Consultant)
>>>  Eli Lilly (CRO FSP)
>>>  Grunenthal
>>>  Consulting projects...

# * Complete cv will be provided upon request and prior to an interview...
''')   
    
# Display hobbies
    with col2:
        col2.subheader('Hobbies')
        data_df = pd.DataFrame(
        {
        "category": [
            "🥁 Drums",
            "🎸 Guitars",
            "🏀 Basketball",
            "📊 Technologies",
            "🐾 Dogs",
            ],
        }
    )

        st.data_editor(
            data_df,
            column_config={
            "category": st.column_config.SelectboxColumn(
            "Hobbies",
            help="How I spend my time outside business",
            width="medium",
            options=[
                "📊 Technologies",
                "🎸 Guitars",
                "🐾 Dogs",
                ],
            required=True,
        )
    },
    hide_index=True,
)

#Media
        
    

# Run main()

if __name__ == '__main__':
    main()
