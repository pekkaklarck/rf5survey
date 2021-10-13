# Robot Framework 5.0 survey results

We had a [survey](https://forms.gle/E9CKhYLxvY4uKQR46) asking what features
[Robot Framework](http://robotframework.org) community members would like to
see in the forthcoming Robot Framework 5.0 release. This repository shares
results and contains also scripts that were used for processing responses.

- [responses.csv](responses.csv) contains raw responses to the survey questions.
  All answers containing personal information like names have been removed.

- [results.md](results.md) lists voted issues by weighted priority. It is pretty
  clear that the community wants more programmatic features.

- [process.py](process.py) is a script that generates `results.md` based on
  `responses.csv`.
