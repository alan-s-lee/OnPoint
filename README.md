# OnPoint: A package for online experiments in motor control and motor learning

The goal of the github repository is to help you host your motor learning experiment online. For a detailed step-by-step breakdown, please visit the [OnPoint Manual for Online Experiment Hosting](https://docs.google.com/document/d/1E5XzQU2dJw7m880P7VhmESPpUNQlEdMcf9fweHLtG0o/edit?usp=sharing). The experiment is in essence a website coded in Javascript/HTML/CSS and hosted on the [Firebase server](https://firebase.google.com/). Participants can be recruited using [Amazon Mechanical Turk Requester](https://requester.mturk.com/), [Prolific](https://www.prolific.co/), or any other crowdsourcing platform. 

[Try out one of our experiments here.](https://multiclamp-c2.web.app/) 

<img src="public/images/sampleOut.gif" width="720" height="404" />

## Dependencies

1. [Python3](https://www.python.org/downloads/) 
2. [NPM](https://www.npmjs.com/get-npm): requirement to download Firebase 
3. [Firebase](https://firebase.google.com/docs/cli): functions needed to host your online experiment on Google's Firebase server. 
4. [Amazon Mechanical Turk Requester](https://requester.mturk.com/) & [Prolific](https://www.prolific.co/): Crowdsourcing websites used to recruit participants. 

## Important files

1. Javascript code to make your experiment dynamic (e.g., appearance of a target): `public/index.js` 
2. HTML files to create the content (e.g., experiment instructions): `public/index.html` 
3. CSS files to style your content (e.g., color): `public/static/`.
4. JSON target files (e.g., experiment design, with one row corresponding to one trial): `public/tgt_files/`. 
5. Downloading data from the Firebase server to your local computer: `python_scripts/db_csv.py`. 
6. Generate JSON target files: `public/tgt_files/generate_test_rot.py`.
7. Convert CSV target files into JSON files: `python_scripts/csv_json.py`.
8. Example JSON target file: `public/tgt_files/demo_file`

## Need help?

If you are stuck, please make a comment on the [Manual](https://docs.google.com/document/d/1E5XzQU2dJw7m880P7VhmESPpUNQlEdMcf9fweHLtG0o/edit?usp=sharing) or use the [github's issue tab](https://github.com/alan-s-lee/Reaching_Exp_Online/issues)!

## Acknowledgements

J.S.T was funded by a 2018 Florence P. Kendall Scholarship from the Foundation for Physical Therapy Research. This work was supported by grant NS092079 from the National Institutes of Health. 

## How to cite this?

Tsay, J. S., Ivry, R. B., Lee, A., & Avraham, G. (2021). Moving outside the lab: The viability of conducting sensorimotor learning studies online. Neurons, Behavior, Data Analysis, and Theory. https://doi.org/10.51628/001c.26985

## Other Research using OnPoint

Tsay, J. S., Kim, H. E., Saxena, A., Parvin, D. E., Verstynen, T., & Ivry, R. B. (2022). Dissociable use-dependent processes for volitional goal-directed reaching. Proceedings. Biological Sciences, 289(1973), 20220415. [supplementary experiment]

Tsay, J. S., Haith, A. M., Ivry, R. B., & Kim, H. E. (2022). Interactions between sensory prediction error and task error during implicit motor learning. PLoS Computational Biology, 18(3), e1010005.

Avraham, G., Ryan Morehead, J., Kim, H. E., & Ivry, R. B. (2021). Reexposure to a sensorimotor perturbation produces opposite effects on explicit and implicit learning processes. PLoS Biology, 19(3), e3001147. (See supplemental figure, S2)

Shyr, M. C., & Joshi, S. S. (2021). Validation of the Bayesian sensory uncertainty model of motor adaptation with a remote experimental paradigm. 2021 IEEE 2nd International Conference on Human-Machine Systems (ICHMS), 



