# Memento Client Validator
A tool for those who are wanting to test their client applications in how 
they interact with the memento framework.

Replicates the behavior as described in [rfc7089](https://tools.ietf.org/html/rfc7089)


## Directory Structure
- static: holds static resources served to the rendered templates
- templates: holds html template files. These are [tornado templates](http://www.tornadoweb.org/en/stable/template.html) 
- timemaps: holds all timemaps. these timemaps are configured to link directly to this tool per each Pattern as described in [section 4](https://tools.ietf.org/html/rfc7089#section-4) of the rfc

## Files
- Patterns.py contains the headers sent. The link portion of the headers as defined in that file are the paths that the tool is recognizing
- RequestHandlers.py contains the HTTP request handler subclasses