# my-first-app-fall-2026

## Prerequisites

Install python version 3.x (for example using Anaconda).

## Setup

1. Clone [the repo](https://github.com/s2t2/my-first-app-fall-2026) from GitHub, and put it somewhere (like your Desktop).
2. Navigate to the local repo from the command line (for example if on your desktop):

```sh
cd ~/Desktop/my-first-app-fall-2026
```

3. Create a new Anaconda virtual environment called "rps-env" (first time only):

```sh
conda create -n rps-env python=3.11
```

4. Activate the virtual environment as necessary (every time you come back to the project):

```sh
conda activate rps-env
```

5. Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

some commands here to run our file(s)

Run the example script:

```sh
python app/my_script.py

# alternatively:
python -m app.my_script
```


Run the example script:

```sh
python app/rps.py

# alternatively:
python -m app.rps
```




## Usage

some commands here to run our file(s)

Run the example script:

```sh
python app/my_script.py

# alternatively:
python -m app.my_script
```


Run the example script:

```sh
python app/rps.py

# alternatively:
python -m app.rps
```

## testing

to run tests 

```sh
pytest
```

## Configuration

The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```

Stocks dashboard:

```sh
python -m app.stocks
```