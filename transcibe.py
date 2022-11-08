import argparse
import os
import utils

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('audio_file', help='url to file or local audio filename')
    parser.add_argument('--local', action='store_true' , help='must be set if audio_file is a local filename')
    parser.add_argument('--api_key', action='store', help='API KEY')