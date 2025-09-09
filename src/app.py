from bins.stream_lit import setup_page, uploadfiles, Chat
import streamlit as st
from bins.WorkFlow import WorkFlow
import os

def main():
    setup_page()
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    files = uploadfiles()

    if files:
        # Graph
        st.session_state.graph = WorkFlow(files).create_Graph()
        st.session_state.documents_processed = True
        st.success("Documents processed successfully!")
                        
        for temp_file in files:
            os.unlink(temp_file)

    if not ('documents_processed' in st.session_state and st.session_state.documents_processed):
        st.info("Please upload and process PDF documents to start chatting.")

        
    Chat()


if __name__ == "__main__":
    main()