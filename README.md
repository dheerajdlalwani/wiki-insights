# wiki-insights

Wiki Insights: Specific Text Analysis APIs

This is a simple web app written in Flask to perform Word Frequency Analysis of Wikipedia articles.

## Basic Setup

- This setup assumes you are running it in a linux based environment
- Create a `.env` file (use [sample.env](sample.env) as a reference) and fill in the values
- Make sure you have the `make` utility installed.
- If you do not have `make` installed, run the following commands:
  - `sudo apt-get update`
  - `sudo apt-get -y install make`
  - Now to test, check the installed version: `make -v`
- After `make` is installed, run the following commands:

  - `make install` -> this will create the virtual evnironment and install all the necessary requirements.

    > This may take a while to install. So be patient.

  - `make run` -> this will start the server on port `5000`. Make sure it is free.

- To cleanup the server and start fresh, run `make clean` then run `make install` and `make run`

## Endpoints

### Word Frequency Analysis Endpoint

- `GET: /wiki-word-frequency`
- Required query params:
  - `topic` (string) = Name of the wikipedia article
  - `n` (int) = Number of top words required
- Optional query params:
  - `disable_preprocess` (bool) = Can see the results by disabling preprocessing applied to the text.
  - Default value: `False`
- Sample usage:
  - Run the server and then visit the following URL
  - [http://127.0.0.1:5000/wiki-word-frequency?n=10&topic=Boston%20Tea%20Party](http://127.0.0.1:5000/wiki-word-frequency?n=10&topic=Boston%20Tea%20Party)

### Search History Endpoint

- `GET: /search-history`
- Query params:
  - `q` (string) = Query String - can search through the previous search history topics
  - If `q` is an empty string, it returns all searches.
- Sample Usage:
  - Run the server and then visit the following URL
  - [http://127.0.0.1:5000/search-history?q=Bos](http://127.0.0.1:5000/search-history?q=Bos)

## Tests

- There are some basic API tests written in [test.py](src/test.py)
- To run these tests, first start the API server using `make run` and in another terminal run `make test`
