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
```

```bash
# Compress using specific method
python main.py compress document.txt -m bz2    # 📦 BZ2 compression
python main.py compress document.txt -m lzma   # 📦 LZMA compression
python main.py compress document.txt -m zlib   # 📦 ZLIB compression
```

```bash
# Specify output file
python main.py compress document.txt -o compressed.gz
```

```bash
# Set compression level (1-9)
python main.py compress document.txt -l 9  # 💪 Maximum compression
```

### 📂 Decompression

```bash
# Decompress a file (automatically detects compression type)
python main.py decompress document.txt.gz
```

```bash
# Specify output file for decompression
python main.py decompress document.txt.gz -o document_recovered.txt
```

### ℹ️ Detailed Information

```bash
# Show detailed compression statistics
python main.py compress document.txt --info
```

Example output:

✅ File compressed successfully!
📄 Input file: document.txt
💾 Output file: document.txt.gzip
🔧 Method: gzip
📊 Original size: 1024000 bytes
📉 Compressed size: 256000 bytes
🎯 Compression ratio: 75.00%


## 📋 Supported Compression Methods

| Method | Extension | Best For | Performance | Ratio |
|--------|-----------|----------|-------------|-------|
| **GZIP** 🗜️ | .gz | General purpose, web files | ⚡⚡⚡ Fast | 📊 Good |
| **BZ2** 💪 | .bz2 | Better compression ratio | ⚡⚡ Medium | 📊📊 Better |
| **LZMA** 🏆 | .xz | Best compression ratio | ⚡ Slower | 📊📊📊 Best |
| **ZLIB** ⚡ | .zlib | Quick compression | ⚡⚡⚡ Fastest | 📊 Good |

## 💡 Examples

### 📦 Compress a Large Text File

```bash
python main.py compress largefile.txt -m bz2 -l 9 --info
```

### 🚀 Compress Multiple Files

```bash
# Create a batch script
for file in *.txt; do
    python main.py compress "$file" -m gzip
done
```

### 📊 Benchmark Different Compression Methods

```bash
# Test different methods on the same file
python main.py compress test.txt -m gzip --info > results_gzip.txt
python main.py compress test.txt -m bz2 --info > results_bz2.txt
python main.py compress test.txt -m lzma --info > results_lzma.txt
python main.py compress test.txt -m zlib --info > results_zlib.txt
```

## 📝 File Naming Convention

The tool uses the following naming convention for compressed files:
- `original_name.txt` → `original_name.txt.gz` (GZIP) 🗜️
- `original_name.txt` → `original_name.txt.bz2` (BZ2) 💪  
- `original_name.txt` → `original_name.txt.xz` (LZMA) 🏆
- `original_name.txt` → `original_name.txt.zlib` (ZLIB) ⚡

## ⚠️ Error Handling

The tool handles various errors gracefully:
- ❌ File not found errors
- 🚫 Invalid compression methods
- 💥 Corrupted compressed files
- 🔒 Permission errors
- 💾 Disk space issues

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💬 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- ⚡ Built using Python's built-in compression libraries
- 💡 Inspired by the need for a simple, unified compression tool
- 🌟 Contributors and community feedback

---

<div align="center">
  <h3>🌟 If you find this project useful, please consider giving it a star! 🌟</h3>
  
  Made with ❤️ by developers for developers
</div>
