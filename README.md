# Online Reaching Experiments
The goal of the github repository is to host traditional in-person reaching experiments online with the help of firebase databases. This README will primarily be geared towards outlining the folders and files. For a detailed step-by-step manual documenting the entire process please visit this guide: [MANUAL FOR ONLINE HOSTING](https://docs.google.com/document/d/1E5XzQU2dJw7m880P7VhmESPpUNQlEdMcf9fweHLtG0o/edit?usp=sharing). 

## Setup
This tool in its current form requires users to create their own [Firebase](https://firebase.google.com/) accounts (which are tied to google) and [Amazon Mechanical Turk Requester](https://requester.mturk.com/) accounts. 
> **NOTE** on the firebase account, if users follow the manual they will notice that our current database rules are very lax and may be insecure. We are open to any suggestions as to how to revise the database rules but please use to your own discretion. As of now, we have not run into security issues and do not see any motive for others to breach our databases, but please be mindful when using this tool.

You will also have to download the [Firbase CLI](https://firebase.google.com/docs/cli) which can be done with npm. Open your terminal and type in:
> `$ npm install -g firebase-tools`


In addition, the experiment itself is written in Javascript and HTML/CSS, target files are JSON objects, and dataloading scripts are written in python3. All Javascript libraries for the game are stored in `public/static/lib`. Due to the amount of files you will have to manage in this tool, we highly encourage you to use this tool with an IDE.

## Firebase configurations
When initializing a Firebase project, you will be asked to create a number of configuration files for the project. These files are also pre-existing in this Github repository, the only file that we have modified from the default configurations is `firestore.rules` where we had to relax the rules. All other firebase configuration files should be identical.

## Experiment files
The the backend Javascript is located at `public/index.js`, the frontend HTML can be located at `public/index.html`, and the CSS styles are located in the folder `public/static/`. `index.html` only deals with the webpages, such as the consent page, instructions, and feedback, while `index.js` renders the experiment UI with D3.js. All areas that need to be modified should be marked by a `**TODO**` flag in the comments in each file respectively. 

## Other scripts and files
* `db_csv.py`
This file is the dataloading script. After generating a secret key from your firebase, you can access the database and download it into csv files. Note that you can access the documents in the database with any valid field, does not necessary need to be the document "id". More documentation is in the file itself.
* `csv_json.py`
This file is a prewritten script for you to convert existing csv target files into JSON target files. Please note that the script can only convert csv files following a specific format, an example can be found at `csv_tgt_files/demo_csv_file.csv`. 
* `public/tgt_files/generate_test_rot.py`
This file is the target file generator script. You can directly generate JSON target files with this script that can be read into the experiment. One such script is `public/tgt_files/demo_file` which can be fed into `index.js` to run an existing demo experiment. More documentation is in the file itself. 

## Getting help
If you are stuck, you can check out the overly detailed [Manual](https://docs.google.com/document/d/1E5XzQU2dJw7m880P7VhmESPpUNQlEdMcf9fweHLtG0o/edit?usp=sharing). For troubleshooting, check out the troubleshooting section of the manual and leave a comment if your issue has not been addressed! 

## Citation
Coming soooooooon (I hope). 

## Acknowledgements
This tool has had contributions from a number of people, but we would like to especially thank Jonathan Tsay, Guy Avraham, Darius Parvin, Riley Woo, Alan Lee, and Jeremy Ho for putting this tool together.

## References
Working on it... hehe
