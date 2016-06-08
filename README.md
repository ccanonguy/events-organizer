Events Organizer
===

A python based text processor which uses NLU to keep track of the events.

To get started with contributing,

### Getting started with git

* Install git on Debian/Ubuntu by typing in the terminal,
		
		sudo apt-get install git

* Fork the [repository](https://github.com/ccanonguy/events-organizer.git).

* Clone the repository. Type in the terminal, (replace `YOUR_USERNAME` with your username on Github)
	
		git clone https://github.com/YOUR_USERNAME/events-organizer.git

* Feel free to ask anything on gitter.


### Setting up environment

* Make sure you have Python 2.7. To check, execute,
		
		python --version

* Check if you have pip installed by typing,
		
		pip --version

* If you don't have pip installed, follow the instructions [here](https://pip.pypa.io/en/latest/installing/).

* Install virtual environment by executing,

		sudo apt-get install virtualenv

* Go to the your `events-organizer` directory and execute,
		
		virtualenv env

	This will set up a virtual environment.

* Execute in the terminal,
		
		source ./env/bin/activate

* Install nltk using,

		pip install nltk
		
* Download nltk data by typing into python interpreter,

		import nltk
		nltk.download()
		
* Install dateutil for parsing datetime.

		pip install python-dateutil
