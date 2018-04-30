## University of Florida Audience Analytics: Data Mining and Analysis 

Welcome to the code repository for MMC6936: Data Mining and Analysis. 

For more information on the course, please see the Canvas page.

### Installation

These lessons has been tested for Python 3.6 and primarily uses the latest release of each library, except where versions are pinned. You likely can run most of the code with older releases, but if you run into an issue, try upgrading the library in question first. 

First you will need to [install Conda for your OS](https://conda.io/docs/installation.html).

Then, to install all the requirements, we will setup a conda environment. You can do so and install all the requirements like so:

```
conda create -n py3data --copy python=3.6
source activate py3data
pip install -r requirements.txt
```

Then, when you want to run code you will need to make sure you are in your environment. To do so, you will type:

```
source activate py3data
```

In addition, you will need to install [sqlite3](https://www.sqlite.org/) or make changes to our database modules with a connection string to your database of choice. [more info](https://dataset.readthedocs.io/en/latest/quickstart.html#connecting-to-a-database)

### Repository structure

Each module has it's own folder, from our precoursework (`module_00/`) to our final module (`module_12`). We also have a folder for data and an extras folder where you can see how some of the data was produced.

### Python2 v. Python3

This repository has been built with Python 3. If you are using Python 2 and need help porting some logic or finding alternatives, please let me know and I will try and help. :)

### Corrections?

If you find any issues in these code examples, feel free to submit an Issue or Pull Request. I appreciate your input!

### Questions?

Reach out to @kjam on Twitter or GitHub or via her UF email. 
