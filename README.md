Saya
=========

Plex media server anime list updater.

=========
Requires:
- Plex (d'oh)
- Python 3
- [hummingbird.me API wrapper](https://pypi.python.org/pypi/Hummingbird/)
- Only tested on linux (ubuntu), but should work on anything else.

=========
Currently supported file naming coventions (where XX is the episode count and [\*] can be (\*)):
- Title - XX.ext
- [Group] Title - XX.ext
- Title - XX [Media data].ext
- [Group] Title - XX [Media data].ext
- [text][Group][text] Title - XX [text][Media data][text].ext

=========
TODO:
- ~~myanimelist.net support~~
- ~~Dual list support (update both HB and MAL lists at the same time)~~
- ~~Support for most of the file naming conventions~~
- Movies support
- A GUI? (QT or wxWidgets probably)
- An indicator?
