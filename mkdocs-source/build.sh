#!/bin/bash

# DinoDB Documentation Build Script
# Generates static website directly to ../docs/

set -e  # Exit on any error

# Configuration
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_OUTPUT_DIR="$SOURCE_DIR/../docs"
VENV_DIR="$SOURCE_DIR/venv"

echo "🚀 Building DinoDB Documentation"
echo "================================="
echo "Source: $SOURCE_DIR"
echo "Output: $DOCS_OUTPUT_DIR"

# Create and activate virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install/upgrade dependencies
echo "📥 Installing dependencies..."
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r requirements.txt

# Change to source directory
cd "$SOURCE_DIR"

# Clean previous build
if [ -d "$DOCS_OUTPUT_DIR" ]; then
    echo "🧹 Cleaning previous build..."
    rm -rf "$DOCS_OUTPUT_DIR"/*
fi

# Build the documentation
echo "🔨 Building documentation..."
"$VENV_DIR/bin/mkdocs" build --clean

# Check if build was successful
if [ -f "$DOCS_OUTPUT_DIR/index.html" ]; then
    echo "✅ Documentation built successfully!"
    echo "📂 Output directory: $DOCS_OUTPUT_DIR"
    echo "🌐 Main file: $DOCS_OUTPUT_DIR/index.html"
    
    # Create a .nojekyll file for GitHub Pages
    touch "$DOCS_OUTPUT_DIR/.nojekyll"
    
    echo "🚀 Ready for deployment!"
else
    echo "❌ Build failed!"
    exit 1
fi

echo ""
echo "Next steps:"
echo "- Open $DOCS_OUTPUT_DIR/index.html in your browser"
echo "- Or run './serve.sh' for development server"
echo "- Deploy the $DOCS_OUTPUT_DIR directory to your web server"
