from pyChatGPT import ChatGPT

session = "Session ID1"
session2 = "Session ID2"
sessions = [session, session2]

def get_api(session_idx = 0):
    return ChatGPT(sessions[session_idx]) 