import argparse
import re
import os

def split_transcript(input_file, num_speakers, output_dir):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # Regular expression to match the pattern "Name Timestamp"
        pattern = re.compile(r'^([\w\s]+)\s+(\d+:\d+)')

        # Dictionary to store each speaker's dialogue
        speakers = {}
        current_speaker = None

        # Iterate over the lines to process the text
        for line in content:
            match = pattern.match(line)
            if match:
                current_speaker = match.group(1)
                if current_speaker not in speakers:
                    speakers[current_speaker] = []
            if current_speaker:
                speakers[current_speaker].append(line)

        # Check if the number of speakers matches the expected count
        if len(speakers) != num_speakers:
            print(f"Warning: Expected {num_speakers} speakers, but found {len(speakers)}. Please check the transcript.")

        # Write each speaker's dialogue to a separate file
        for speaker, dialogues in speakers.items():
            file_name = os.path.join(output_dir, f"{speaker.replace(' ', '_').replace('.', '')}.txt")
            with open(file_name, 'w', encoding='utf-8') as speaker_file:
                speaker_file.write(''.join(dialogues))

        return "Splitting complete."

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split a transcript into separate files based on speakers.')
    parser.add_argument('input_file', type=str, help='The path to the transcript file.')
    parser.add_argument('--speakers', type=int, help='Number of expected speakers in the transcript.', required=True)
    args = parser.parse_args()

    # Setting output directory to the same as input file
    output_dir = os.path.dirname(args.input_file)

    # Call the function with command line arguments
    result = split_transcript(args.input_file, args.speakers, output_dir)
    print(result)

### Copyright and Disclaimer
'''
This script is copyright 2023 by TrustInsights.ai. It is provided under the GPL 3.0 license as is, with absolutely no warranty, promise of support, or statement of fitness. Use at your own risk.
'''
