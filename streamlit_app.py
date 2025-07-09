"""
AI-Powered Document Summariser
Month 1 Mini Project - AI Solutions Course | MasterAgenticAI.Academy

This application demonstrates how AI can enhance business analysis
by automatically summarising documents and extracting key insights.
"""

import streamlit as st
from crew import DocumentSummariserCrew
import time

# Page configuration
st.set_page_config(
    page_title="AI Document Summariser",
    page_icon="📄",
    layout="wide"
)

# Header
st.title("🤖 AI-Powered Document Summariser")
st.markdown("""
<div style='text-align: center; font-size: 16px;'>
<b>Month 1 Mini Project</b><br>AI Solutions Course - <i>MasterAgenticAI.Academy</i>
</div>
""", unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    # Model provider selection
    model_provider = st.selectbox(
        "Select AI Provider",
        ["anthropic", "openai"],
        help="Choose your AI model provider (Gemini support coming soon!)"
    )

    # Initialize session state for api_key
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

    # API Key section
    st.markdown("### 🔐 API Key")
    st.markdown("""
    Your API key is stored securely in your session and never saved.

    **For deployment**, add your key to Streamlit Secrets instead.
    """)

    # Load from secrets if available
    try:
        if model_provider == "anthropic":
            st.session_state.api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
        else:
            st.session_state.api_key = st.secrets.get("OPENAI_API_KEY", None)
    except:
        pass

    # Prompt user for API key if not set
    if not st.session_state.api_key:
        provider_name = "Anthropic" if model_provider == "anthropic" else "OpenAI"
        st.session_state.api_key = st.text_input(
            f"Enter your {provider_name} API Key",
            type="password",
            help="This will be stored only for this session"
        )
    else:
        st.success("✅ API Key loaded from secrets")

    st.divider()

    # Info section
    st.markdown("### 📚 About This Project")
    st.info("""
    **Learning Objectives:**
    - Understanding AI agents and roles
    - Prompt engineering basics
    - Secure API key management
    - Cloud deployment practices

    **Business Value:**
    - Reduces document review time by 80%
    - Ensures consistent summary quality
    - Highlights key insights automatically
    """)

# Main content area
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("📥 Input Document")

    input_method = st.radio(
        "Choose input method:",
        ["Paste Text", "Upload File", "Use Sample"],
        horizontal=True
    )

    document_text = ""

    if input_method == "Paste Text":
        document_text = st.text_area(
            "Paste your document text here:",
            height=400,
            placeholder="Enter any business document, report, meeting notes, or requirements..."
        )

    elif input_method == "Upload File":
        uploaded_file = st.file_uploader(
            "Choose a text file",
            type=['txt', 'md'],
            help="Support for more formats coming in future modules!"
        )
        if uploaded_file is not None:
            content = uploaded_file.read()
            if content:
                document_text = content.decode("utf-8")
                st.text_area("Document Preview:", document_text, height=400, disabled=True)
            else:
                st.warning("⚠️ Uploaded file is empty")

    else:  # Use Sample
        sample_text = """
        BUSINESS REQUIREMENTS DOCUMENT
        Project: Customer Portal Modernisation
        Date: January 2024

        EXECUTIVE OVERVIEW
        The current customer portal, implemented in 2018, no longer meets our business needs. 
        Customer complaints have increased by 45% over the past year, primarily related to 
        performance issues and lack of mobile responsiveness. This project aims to modernise 
        the portal using cloud-native technologies.

        KEY STAKEHOLDERS
        - Sarah Johnson (Head of Digital)
        - Mike Chen (IT Director)
        - Customer Service Team
        - External customers (50,000+ active users)

        REQUIREMENTS
        1. Performance: Page load time must be under 2 seconds
        2. Mobile-first design with responsive layouts
        3. Integration with new CRM system (Salesforce)
        4. Enhanced security with MFA support
        5. Real-time chat functionality

        BUDGET AND TIMELINE
        - Approved budget: £450,000
        - Target completion: Q3 2024
        - Development team: 8 resources

        RISKS
        - Legacy system integration complexity
        - Data migration challenges
        - Change management for 50,000 users
        - Potential security vulnerabilities during transition

        SUCCESS METRICS
        - Reduce customer complaints by 60%
        - Increase mobile usage from 30% to 70%
        - Improve customer satisfaction score from 3.2 to 4.5
        - Achieve 99.9% uptime
        """
        document_text = sample_text
        st.text_area("Sample Document:", document_text, height=400, disabled=True)

with col2:
    st.header("📊 AI-Generated Summary")

    if st.button("🚀 Generate Summary", type="primary", use_container_width=True):
        if not st.session_state.api_key:
            st.error("⚠️ Please enter your API key in the sidebar")
        elif not document_text:
            st.error("⚠️ Please provide a document to summarise")
        else:
            try:
                with st.spinner("🤖 AI agents are analysing your document..."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()

                    status_text.text("Initialising AI agents...")
                    progress_bar.progress(20)
                    time.sleep(1)

                    crew = DocumentSummariserCrew(st.session_state.api_key, model_provider)

                    # Optional validation of crew
