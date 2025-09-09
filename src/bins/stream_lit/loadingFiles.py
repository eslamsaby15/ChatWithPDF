import streamlit as st
import tempfile

def uploadfiles() :

    with st.sidebar :
        st.markdown("**Upload and Read Files**")
        st.markdown("**Upload your PDFs**")

        pdfs = st.file_uploader(
                                "Drag and drop files here",
                                accept_multiple_files=True,
                                type=['pdf', 'txt'],
                                label_visibility="collapsed"
                            )
        
        if st.button("Process") and pdfs:  
            with st.spinner("Processing PDFs...") :
                temp_files = []

                for file in pdfs : 

                    temp_file = tempfile.NamedTemporaryFile(delete=False , suffix='.pdf')
                    temp_file.write(file.getvalue())
                    temp_file.close()
                    temp_files.append(temp_file.name)

                return temp_files 
