# AI Solutions Course - Document Summariser Setup Script
# Based on proven installation order that works

echo "🚀 Setting up AI Document Summariser..."
echo "=================================="
echo ""

# Function to check if command succeeded
check_status() {
    if [ $? -eq 0 ]; then
        echo "✅ $1 successful"
    else
        echo "❌ $1 failed"
        exit 1
    fi
}

# Clean any conflicting packages first
echo "🧹 Cleaning potentially conflicting packages..."
pip3 uninstall -y crewai langchain langchain-community langchain-core langchain-openai openai 2>/dev/null || true
echo ""

# Install in the exact order that works
echo "📦 Installing langchain..."
pip3 install langchain==0.0.351
check_status "LangChain installation"

echo "📦 Installing crewai..."
pip3 install crewai==0.1.7
check_status "CrewAI installation"

echo "📦 Installing openai..."
pip3 install openai==0.28.1
check_status "OpenAI installation"

echo "📦 Installing langchain-community..."
pip3 install langchain-community==0.0.38
check_status "LangChain Community installation"

echo "📦 Installing langchain-core..."
pip3 install langchain-core==0.1.52
check_status "LangChain Core installation"

echo "📦 Installing python-dotenv..."
pip3 install python-dotenv==1.0.1
check_status "Python-dotenv installation"

echo "📦 Installing streamlit..."
pip3 install streamlit==1.40.1
check_status "Streamlit installation"

echo ""
echo "📦 Installing remaining data processing libraries..."
pip3 install -r requirements.txt
check_status "Additional requirements installation"

echo ""
echo "=================================="
echo "✅ Installation complete!"
echo ""
echo "🚀 To run the application:"
echo "   streamlit run streamlit_app.py"
echo ""
echo "📚 To verify installation:"
echo "   python3 -c \"import crewai, langchain, openai, streamlit; print('✅ All imports working')\""
echo ""