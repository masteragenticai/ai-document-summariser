"""
AI-Powered Document Summariser
Month 1 Mini Project - AI Solutions Course | MasterAgenticAI.Academy

OpenAI-only version for stable, reliable operation.
This application demonstrates how AI can enhance business analysis
by automatically summarising documents and extracting key insights.
"""

import streamlit as st
import os
from crew import DocumentSummariserCrew
import time

# Load environment variables if using local development
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available in production

# Page configuration
st.set_page_config(
    page_title="AI Document Summariser",
    page_icon="📄",
    layout="wide"
)

# Header
st.title("🤖 AI-Powered Document Summariser")
st.markdown("""
**Month 1 Mini Project** | AI Solutions Course - MasterAgenticAI.Academy

This tool demonstrates how AI agents can work together to analyse business documents
and create executive summaries, saving hours of manual work.
""")

# API Key Configuration
st.markdown("### 🔐 OpenAI Configuration")

# Check for API key in environment first (for deployed version)
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    st.success("✅ OPENAI_API_KEY loaded from environment")
else:
    st.info("💡 Add your OpenAI API key to environment variables or enter below")
    api_key = st.text_input(
        "Enter your OpenAI API Key",
        type="password",
        help="This will be stored only for this session"
    )

st.divider()

# Main content area
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("📥 Input Document")
    
    # Document input methods
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
            document_text = uploaded_file.read().decode("utf-8")
            st.text_area("Document Preview:", document_text, height=400, disabled=True)

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
    
    # Process button
    if st.button("🚀 Generate Summary", type="primary", use_container_width=True):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key above")
            st.info("""
            **Setup Instructions:**
            
            Add your OpenAI API key to your environment:
            ```
            # Add to your .env file (local development):
            OPENAI_API_KEY=your-actual-api-key-here
            
            # Or add as environment variable
            export OPENAI_API_KEY=your-actual-api-key-here
            ```
            """)
        elif not document_text:
            st.error("⚠️ Please provide a document to summarise")
        else:
            try:
                # Show processing message
                with st.spinner("🤖 OpenAI agents are analysing your document..."):
                    # Create progress indicator
                    progress_bar = st.progress(0)
                    status_text = st.empty()

                    # Simulate progress updates
                    status_text.text("Initialising AI agents...")
                    progress_bar.progress(20)
                    time.sleep(1)

                    # Initialise crew
                    crew = DocumentSummariserCrew(api_key)
                    status_text.text("Document Analyst reviewing content...")
                    progress_bar.progress(50)

                    # Generate summary
                    summary = crew.summarise_document(document_text)
                    status_text.text("Summary Writer creating executive summary...")
                    progress_bar.progress(80)
                    time.sleep(1)

                    progress_bar.progress(100)
                    status_text.text("✅ Summary complete!")
                    time.sleep(0.5)

                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()

                # Display the summary
                st.success("✨ Summary generated successfully!")
                
                # Show which model was used
                st.info("**AI Model Used:** GPT-4 Turbo (OpenAI)")
                
                # Display the summary
                st.markdown(summary)

                # Add download option
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="executive_summary_openai.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 Common issues: Invalid API key, rate limits, or network problems")

# Information section at the bottom
st.divider()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("### 📚 Learning Objectives")
    st.markdown("""
    - Understanding AI agents and roles
    - Prompt engineering basics
    - Secure API key management
    - Cloud deployment practices
    """)

with col2:
    st.markdown("### 💼 Business Value")
    st.markdown("""
    - Reduces document review time by 80%
    - Ensures consistent summary quality
    - Highlights key insights automatically
    - Supports better decision-making
    """)

with col3:
    st.markdown("### 🛠️ Technology Stack")
    st.markdown("""
    - **CrewAI**: Multi-agent orchestration
    - **Streamlit**: Web interface
    - **OpenAI GPT-4**: AI language model
    - **GitHub Codespaces**: Cloud development
    """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666;'>
<p>Built with CrewAI and Streamlit | AI Solutions Course - MasterAgenticAI.Academy</p>
<p>Remember: This tool enhances human analysis, it doesn't replace it!</p>
</div>
""", unsafe_allow_html=True)
