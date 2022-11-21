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

        header = {
            'authorization' : args.api_key,
            'content-type' : 'application/json'
        }

        if args.local:
            upload_url = utils.upload_file(args.audio_file,header)
        else:
            upload_url = {'upload_url' : args.audio_file}

        transcript_response = utils.request_transcript(upload_url,header)

        polling_endpoint = utils.make_polling_endpoint(transcript_response)

        utils.wait_for_completion(polling_endpoint, header)

        paragraphs = utils.get_paragraphs(polling_endpoint,header)

        with open('transcript.txt', 'w') as f:
            for para in paragraphs:
                print(para['text'] + '\n')
                f.write(para['text'] + '\n')

        return

    if __name__ == '__main__':
        main()