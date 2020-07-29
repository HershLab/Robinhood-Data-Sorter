# Robinhood_Data_Sorter

Script to take public Robinhood data and sort it into one excel file. Currently ongoing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Pandas

```
Windows & Mac
pip install pandas
```

openpyxl
```
Windows & Mac
pip install openpyxl
```

## Running the tests

To run

Sidenote: It is necessary to run Ticker_Adder.py to all files before running Sorter2.py. The current upload of the csv files has Ticker_Adder.py already ran on, meaning if you download the original csv files from here, you don't need to run Ticker_Adder.py. If you are using your own csv files, run Ticker_Adder, then run sorter2.py.

```
If using Ticker_Adder first run: python Ticker_Adder.py

Then run sorter2.py: python sorter2.py


```
**Running the above commands will take a long time depending on how many files there are**

## Built With

* [Pandas](https://pandas.pydata.org/)
* [OpenPyxl](https://openpyxl.readthedocs.io/en/stable/)


## Authors

* **Parsa Hassani** - *Initial work* - [parsacubesat](https://github.com/parsacubesat)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

