# Wikipedia CLI Summary Tool

A simple Python command-line tool that fetches summaries of topics from the Wikipedia API and saves the results to a file.

## Features

* Fetch summaries from Wikipedia using the API
* Command-line interface for topic input
* Handles URL encoding for safe requests
* Displays results in the terminal
* Saves summaries to a local text file

## Technologies Used

* Python
* Requests Library
* Wikipedia REST API
* JSON Processing
* File Handling

## Installation

Clone the repository:

git clone (https://github.com/PUNITH-V/Wikipedia-CLI-Summary-Tool.git)

cd wiki-cli-tool

Install dependencies:

pip install requests

## Usage

Run the script with a topic:

python app.py "Machine learning"

Example Output

Title: Machine learning

Summary:
Machine learning is a field of artificial intelligence that focuses on building systems that learn from data.

The summary will also be saved in:

output.txt

## Project Structure

wiki-cli-tool
│
├── app.py
├── output.txt
├── requirements.txt
└── README.md

## What I Learned

Through this project I learned:

* How APIs work
* Making HTTP requests using Python
* Processing JSON responses
* Extracting nested data
* Command-line arguments
* File handling in Python
* Basic API error handling

## Future Improvements

* Add colored terminal output
* Handle disambiguation pages automatically
* Support multiple search results
* Convert tool into a package

## License

MIT License
