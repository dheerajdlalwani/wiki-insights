Okay, 2 APIs.

## Word Frequency Count

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

## Search History

- store in an array temp
- later move to relational DB (sqlite) or redis
- empty query => return all search history
- use starts with (later add fuzziness)

## Server:

- Makefile
- docs


## Future:
- add functional caching
- move search history to redis/relational DB
- check last modified and fetch only if its new?