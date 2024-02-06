Okay, 2 APIs.

Word Frequency Count & Search History Endpoint.

Make one module for a function which: takes text, n and returns the data they want.

flow:

- ask topic and n
- store query in cache
- check if page exists
  - page not exist:
    - return 404
  - page exist:
    - download page
- do preprocessing
- get count
- return count
