# 📦 File Compression Utility

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple yet powerful command-line file compression utility that supports multiple compression algorithms. This tool allows you to compress and decompress files using various methods with customizable compression levels.

## ✨ Features

- 🚀 **Multiple Compression Methods**: Support for GZIP, BZ2, LZMA, and ZLIB compression algorithms
- 🔄 **Automatic Method Detection**: Decompresses files by detecting compression type from file extension
- 📊 **Compression Statistics**: Shows original and compressed file sizes with compression ratio
- ⚙️ **Customizable Compression Levels**: Choose compression level from 1 (fastest) to 9 (best compression)
- 💡 **Simple Interface**: Easy-to-use command-line interface
- 📈 **Detailed Information**: Optional detailed output with full compression statistics
- 🛡️ **Error Handling**: Graceful handling of various error scenarios
- 💾 **Zero Dependencies**: Uses only Python's built-in libraries

## 🔧 Requirements

- 🐍 Python 3.6+
- 📚 No external dependencies required (uses built-in Python libraries)

## 📥 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/file-compression-utility.git
cd file-compression-utility
```

2. 🎉 The tool is ready to use with Python's built-in libraries!

## 🚀 Usage

### 📦 Basic Compression

```bash
# Compress a file using GZIP (default)
python main.py compress document.txt

# Compress using specific method
python main.py compress document.txt -m bz2    # 📦 BZ2 compression
python main.py compress document.txt -m lzma   # 📦 LZMA compression
python main.py compress document.txt -m zlib   # 📦 ZLIB compression

# Specify output file
python main.py compress document.txt -o compressed.gz

# Set compression level (1-9)
python main.py compress document.txt -l 9  # 💪 Maximum compression
```

