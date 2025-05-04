import gzip
import shutil
import zlib
import argparse
import os
from pathlib import Path
import bz2
import lzma
from datetime import datetime


class FileCompressor:
    def __init__(self):
        self.compression_methods = {
            'gzip': self._compress_gzip,
            'bz2': self._compress_bz2,
            'lzma': self._compress_lzma,
            'zlib': self._compress_zlib
        }
        
        self.decompression_methods = {
            'gzip': self._decompress_gzip,
            'bz2': self._decompress_bz2,
            'lzma': self._decompress_lzma,
            'zlib': self._decompress_zlib
        }

    def compress_file(self, input_file: str, output_file: str = None, method: str = 'gzip', level: int = 6) -> str:
        """Compress a file using specified compression method"""
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        if method not in self.compression_methods:
            raise ValueError(f"Unsupported compression method: {method}")
        
        if output_file is None:
            output_file = f"{input_file}.{method}"
        
        size_before = os.path.getsize(input_file)
        
        self.compression_methods[method](input_file, output_file, level)
        
        size_after = os.path.getsize(output_file)
        compression_ratio = (1 - size_after / size_before) * 100
        
        return {
            'input_file': input_file,
            'output_file': output_file,
            'method': method,
            'size_before': size_before,
            'size_after': size_after,
            'compression_ratio': f"{compression_ratio:.2f}%"
        }

    def decompress_file(self, input_file: str, output_file: str = None) -> str:
        """Decompress a file by detecting its compression method"""
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        # Detect compression method from file extension
        extension = os.path.splitext(input_file)[1].lower()
        method_map = {
            '.gz': 'gzip',
            '.bz2': 'bz2',
            '.xz': 'lzma',
            '.zlib': 'zlib'
        }
        
        method = method_map.get(extension)
        if method is None:
            raise ValueError(f"Cannot detect compression method from file: {input_file}")
        
        if output_file is None:
            output_file = os.path.splitext(input_file)[0]
        
        self.decompression_methods[method](input_file, output_file)
        
        return output_file

    def _compress_gzip(self, input_file: str, output_file: str, level: int):
        """Compress using gzip"""
        with open(input_file, 'rb') as f_in:
            with gzip.open(output_file, 'wb', compresslevel=level) as f_out:
                shutil.copyfileobj(f_in, f_out)

    def _compress_bz2(self, input_file: str, output_file: str, level: int):
        """Compress using bz2"""
        with open(input_file, 'rb') as f_in:
            with bz2.open(output_file, 'wb', compresslevel=level) as f_out:
                shutil.copyfileobj(f_in, f_out)

    def _compress_lzma(self, input_file: str, output_file: str, level: int):
        """Compress using lzma"""
        with open(input_file, 'rb') as f_in:
            with lzma.open(output_file, 'wb', compresslevel=level) as f_out:
                shutil.copyfileobj(f_in, f_out)

    def _compress_zlib(self, input_file: str, output_file: str, level: int):
        """Compress using zlib"""
        with open(input_file, 'rb') as f_in:
            compressed_data = zlib.compress(f_in.read(), level=level)
            with open(output_file, 'wb') as f_out:
                f_out.write(compressed_data)

    def _decompress_gzip(self, input_file: str, output_file: str):
        """Decompress gzip file"""
        with gzip.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def _decompress_bz2(self, input_file: str, output_file: str):
        """Decompress bz2 file"""
        with bz2.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def _decompress_lzma(self, input_file: str, output_file: str):
        """Decompress lzma file"""
        with lzma.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def _decompress_zlib(self, input_file: str, output_file: str):
        """Decompress zlib file"""
        with open(input_file, 'rb') as f_in:
            compressed_data = f_in.read()
            decompressed_data = zlib.decompress(compressed_data)
            with open(output_file, 'wb') as f_out:
                f_out.write(decompressed_data)


def main():
    parser = argparse.ArgumentParser(description='File Compression and Decompression Utility')
    parser.add_argument('command', choices=['compress', 'decompress'], help='Operation to perform')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-m', '--method', choices=['gzip', 'bz2', 'lzma', 'zlib'], 
                        default='gzip', help='Compression method (default: gzip)')
    parser.add_argument('-l', '--level', type=int, default=6, choices=range(1, 10),
                        help='Compression level (1-9, default: 6)')
    parser.add_argument('--info', action='store_true', help='Display detailed compression info')
    
    args = parser.parse_args()
    
    compressor = FileCompressor()
    
    try:
        if args.command == 'compress':
            result = compressor.compress_file(args.input_file, args.output, args.method, args.level)
            
            print(f"File compressed successfully!")
            if args.info:
                print(f"Input file: {result['input_file']}")
                print(f"Output file: {result['output_file']}")
                print(f"Method: {result['method']}")
                print(f"Original size: {result['size_before']} bytes")
                print(f"Compressed size: {result['size_after']} bytes")
                print(f"Compression ratio: {result['compression_ratio']}")
            else:
                print(f"Compressed file: {result['output_file']}")
                print(f"Compression ratio: {result['compression_ratio']}")
        
        elif args.command == 'decompress':
            output_file = compressor.decompress_file(args.input_file, args.output)
            print(f"File decompressed successfully!")
            print(f"Decompressed file: {output_file}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
