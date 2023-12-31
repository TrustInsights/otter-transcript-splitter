# Otter Transcript Splitter

For users of [Otter.ai](https://www.trustinsights.ai/otter) that want to split up transcripts by speaker, this is a handy way to take any Otter plain text transcript and split it into individual speaker files. Each speaker's text will be added to a text file of that speaker's name, in chronological order.

Now, you might be asking, what in the world good is something like this? Why would you ever use this?

Well, if you're building, say, Custom GPTs, and you want to build a corpus of one particular speaker... this is how you feed that corpus.

## Instructions for use

Launch on the command line. If you know the number of speakers, you can provide that as a flag:

python transcript-splitter.py --speakers 2 input.txt

It will use each speaker's name as provided by Otter for the individual output files, which will be written to the same directory.

Shameless plug: [need help with your AI strategy and implementation? Ask us!](https://www.trustinsights.ai/aiservices)
