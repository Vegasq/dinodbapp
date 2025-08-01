#\!/bin/bash

# DinoDB Documentation Development Server
# Serves documentation locally for testing

set -e  # Exit on any error

# Configuration
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SOURCE_DIR/venv"

echo "🌐 Starting DinoDB Documentation Server"
echo "======================================="

# Check if virtual environment exists
if [ \! -d "$VENV_DIR" ]; then
    echo "❌ Virtual environment not found. Run ./build.sh first"
    exit 1
fi

echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Change to source directory
cd "$SOURCE_DIR"

echo "🚀 Starting development server..."
echo "   URL: http://127.0.0.1:8000"
echo "   Press Ctrl+C to stop"
echo ""

# Start the development server
mkdocs serve
EOF < /dev/null