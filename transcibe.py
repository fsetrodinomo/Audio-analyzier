import argparse
import os
import utils

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('audio_file', help='url to file or local audio filename')
    parser.add_argument('--local', action='store_true' , help='must be set if audio_file is a local filename')
    parser.add_argument('--api_key', action='store', help='API KEY')

    args = parser.parse_args()

    if args.api_key is None :
        args.api_key = os.getenv("AAI_API_KEY")
        if args.api_key is None:
            raise RuntimeError("AAI_API_KEY environment variable not set. Try setting it now, or passing in your "
                               "API key as a command line argument with `--api_key`.")
