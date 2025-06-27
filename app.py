import streamlit as st
from main import chatbot_response, get_conversation_stats, get_time_greeting
import time
import random

# Configure the page
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .stats-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 Personal AI Assistant v2.0</h1>
    <p>Built by a 2nd Year BTech CS AIML Student | Showcasing AI & Web Development Skills</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with enhanced information
with st.sidebar:
    st.header("🎯 About This Project")
    
    st.markdown("""
    <div class="feature-box">
        <h4>🚀 What This Demonstrates</h4>
        <ul>
            <li>Natural Language Processing</li>
            <li>Pattern Recognition</li>
            <li>Web Application Development</li>
            <li>Data Storage & Analytics</li>
            <li>User Interface Design</li>
            <li>Error Handling</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("⚡ Features")
    features = [
        "🌤️ Weather Information",
        "😄 Programming Jokes", 
        "📚 Study Tips",
        "💪 Motivational Quotes",
        "🤓 Coding Facts",
        "🧮 Math Calculator",
        "📊 Conversation Analytics",
        "🕐 Time-Aware Responses"
    ]
    
    for feature in features:
        st.write(f"• {feature}")
    
    st.header("📊 Live Stats")
    if st.button("🔄 Refresh Stats", type="primary"):
        stats = get_conversation_stats()
        st.markdown(f"""
        <div class="stats-box">
            {stats}
        </div>
        """, unsafe_allow_html=True)
    
    st.header("💡 Try These Commands")
    sample_commands = [
        "weather in Mumbai",
        "tell me a joke",
        "give me a study tip", 
        "I need motivation",
        "calculate 15 * 8",
        "tell me something cool",
        "how many conversations?"
    ]
    
    for cmd in sample_commands:
        if st.button(f"💬 {cmd}", key=f"cmd_{cmd}"):
            # Add the command to chat
            st.session_state.messages.append({"role": "user", "content": cmd})
            response = chatbot_response(cmd)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# Main chat interface
col1, col2 = st.columns([3, 1])

with col1:
    st.header("💬 Chat Interface")
    
    # Fun loading messages
    loading_messages = [
        "🧠 Thinking...",
        "🔍 Processing...", 
        "⚡ Computing...",
        "🤖 Analyzing...",
        "💭 Contemplating..."
    ]

with col2:
    st.header("🎲 Quick Actions")
    if st.button("🎊 Random Joke"):
        joke_response = chatbot_response("tell me a joke")
        st.success(joke_response)
    
    if st.button("💡 Study Tip"):
        tip_response = chatbot_response("study tip")
        st.info(tip_response)
    
    if st.button("⚡ Motivation"):
        motivate_response = chatbot_response("motivate me")
        st.warning(motivate_response)

# Initialize chat history
if 'messages' not in st.session_state:
    greeting = get_time_greeting()
    welcome_msg = f"""{greeting} Welcome to my AI Assistant! 🎉

I'm a smart chatbot built to showcase AI and programming skills. Here's what makes me special:

🌟 **Smart Features:**
• Weather updates for any city
• Programming jokes to brighten your day  
• Study tips for CS students
• Motivational quotes when you need them
• Fun coding facts and trivia
• Math calculations
• Conversation analytics

🎯 **Try asking me:**
• "What's the weather in Delhi?"
• "Tell me a programming joke"
• "I need study motivation"
• "Calculate 25 * 4"
• "Tell me something interesting"

What would you like to explore first? 🚀"""
    
    st.session_state.messages = [
        {"role": "assistant", "content": welcome_msg}
    ]

# Display chat history with enhanced styling
chat_container = st.container()
with chat_container:
    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])

# Enhanced chat input with suggestions
st.markdown("### 💭 Ask me anything!")

# Auto-suggestions
suggestions = [
    "What's the weather in Hyderabad?",
    "Tell me a programming joke",
    "Give me a study tip",
    "I need motivation",
    "Calculate 144 / 12",
    "Tell me a coding fact"
]

# Display suggestions as buttons
st.write("**💡 Quick suggestions:**")
cols = st.columns(3)
for i, suggestion in enumerate(suggestions):
    with cols[i % 3]:
        if st.button(suggestion, key=f"suggest_{i}"):
            # Add suggestion to chat
            st.session_state.messages.append({"role": "user", "content": suggestion})
            response = chatbot_response(suggestion)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# Main chat input
if prompt := st.chat_input("Type your message here... 💬"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    
    # Get bot response with loading animation
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner(random.choice(loading_messages)):
            time.sleep(1)  # Add realistic delay
            response = chatbot_response(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer with technical information
st.markdown("---")
st.markdown("### 🛠️ Technical Architecture")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    **🐍 Backend Technologies:**
    • Python 3.8+
    • Natural Language Processing
    • JSON Data Storage
    • Regular Expressions
    • DateTime Handling
    """)

with tech_col2:
    st.markdown("""
    **🌐 Frontend Technologies:**
    • Streamlit Framework
    • HTML/CSS Styling
    • Interactive Components
    • Real-time Chat Interface
    • Responsive Design
    """)

with tech_col3:
    st.markdown("""
    **🧠 AI Features:**
    • Intent Recognition
    • Pattern Matching
    • Context Awareness
    • Response Generation
    • Data Analytics
    """)

# Project statistics
st.markdown("### 📈 Project Metrics")

metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.metric("Lines of Code", "300+", "50+")

with metrics_col2:
    st.metric("Features", "8", "3")

with metrics_col3:
    st.metric("Response Types", "15+", "10+")

with metrics_col4:
    if 'messages' in st.session_state:
        msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
        st.metric("Session Messages", msg_count, "1")
    else:
        st.metric("Session Messages", "0", "0")

# GitHub section
st.markdown("---")
st.markdown("### 🔗 Repository Information")

github_col1, github_col2 = st.columns(2)

with github_col1:
    st.info("""
    **🎯 This project demonstrates:**
    • Clean, documented code
    • Modern web development
    • AI/ML understanding
    • Problem-solving skills
    • User experience design
    """)

with github_col2:
    st.success("""
    **💼 Perfect for:**
    • GitHub portfolio
    • Job interviews
    • College projects
    • Skill demonstration
    • Learning showcase
    """)

# Instructions
with st.expander("🚀 How to Run This Project Locally"):
    st.code("""
# 1. Clone the repository
git clone https://github.com/yourusername/personal-ai-assistant.git
cd personal-ai-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py

# 4. Open browser to http://localhost:8501
    """, language="bash")

with st.expander("📁 Project Structure"):
    st.code("""
personal-ai-assistant/
├── main.py              # Core AI logic
├── app.py               # Web interface
├── requirements.txt     # Dependencies
├── README.md           # Documentation
├── data/               # Conversation storage
│   └── conversations.json
└── .gitignore          # Git ignore file
    """)

st.markdown("---")
st.markdown("**🎓 Built with ❤️ by a BTech CS AIML Student | Showcasing AI, Python & Web Development Skills**")