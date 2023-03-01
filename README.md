# Subdomain Finder

[![GitHub license](https://img.shields.io/github/license/notyuu/subfinder)](https://github.com/notyuu/subfinder/blob/main/LICENSE)

## Description

Sub Finder is a Python script that uses brute-force technique to enumerate subdomains for a given domain.

## Installation

To use this script, you will need Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/

After installing Python, download or clone this repository to your local machine.

`git clone https://github.com/notyuu/subfinder.git`

`cd subfinder`

`pip install -r requirements.txt`



## Usage

`python subfinder.py -h`

![alt text](https://github.com/notyuu/subfinder/blob/main/screenshot/usage.png)

To run the subfinder, open a terminal and navigate to the directory where you saved the script. Then, run the following command:


`python subfinder.py -v <domain> -w <wordlist path> -o <output>` Replace `-v <domain>` with the domain name of the target machine, `-w <wordlist path>` with the Wordlist path.


use `-o <output>` that save the result in a output file.

you can change the threads by `-t <number>` by default set by 10.



![alt text](https://github.com/notyuu/subfinder/blob/main/screenshot/example.png)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! If you have any suggestions for improving this script, please open an issue or submit a pull request.

## Acknowledgements

This script was developed by NotYuu with the help of the following resources:

- [Python Requests Library](https://docs.python-requests.org/en/latest/) for sending HTTP requests to the target domain.

- [Sublist3r](https://github.com/aboul3la/Sublist3r) for providing inspiration on how to enumerate subdomains.

- [pyfiglet](https://github.com/pwaller/pyfiglet) for adding ASCII art headers to the script.

- [argparse](https://docs.python.org/3/library/argparse.html) for parsing command-line arguments.

## Contact Me

Discord: Yuu#8302
