# Memento Client Validator
A tool for testing your client applications for compliance to the [Memento Framework (RFC7089)](https://tools.ietf.org/html/rfc7089).

Requires the [tornado](http://www.tornadoweb.org/en/stable/index.html) web framework and python3
Which can be downloaded using pip
## Installation
This tool requires Python 3 and other packages that can be installed via:

```sh
$ virtualenv mcv
$ source mcv/bin/activate
$ pip3 install -r requirements.txt
```

## Directory Structure
- static: holds static resources served to the rendered templates
- templates: holds html template files. These are [tornado templates](http://www.tornadoweb.org/en/stable/template.html) 
- timemaps: holds all timemaps. these timemaps are configured to link directly to this tool per each Pattern as described in [section 4](https://tools.ietf.org/html/rfc7089#section-4) of the rfc

## Files
- Patterns.py contains the headers sent. The link portion of the headers as defined in that file are the paths that the tool is recognizing
- RequestHandlers.py contains the HTTP request handler subclasses
