<div align="center">
  <h3>🌳 Unilint 🌳</h3>
</div>

Unilint is a command-line interface tool that combines style, formatting, and type checks into one place. It functions as a CLI utility that enables users to manage, share, and update their specific style settings from a single repository.

Cli functional
* Style checking 
* Type checking

### Client usage
* Installing the library as a third-party library (latest version)
```shell
pip install --index-url https:// unilint
```
* Installing a library as a third-party library (specific version)
```shell
pip install --index-url https:// unilint==0.0.2
```
* Help
```shell
$ unilint --help
...
$ unilint linting --help
...
$ unilint typing --help
...
```
* Style Check
```shell
$ unilint linting
...
$ unilint linting -e scripts
...
$ unilint linting -e scripts -e wrappers/script.py
...
```
* Checking types
```shell
$ unilint typing -d scripts
...
$ unilint typing -d scripts -d wrappers
...
$ unilint typing -d scripts -e scripts/module.py
...  
```

### Developing
* Installing the library for local development and debugging
```shell
pip install -e .
```
* Installing the dependencies to build the package and send it to your storage
```shell
pip install -r requirements/dev.txt
```
* Build package and upload to your repo
```shell
python3 -m build
python3 -m twine upload dist/*
```
* Tests
```shell
$ python3 -m unittest
```
### Appeals 
[Pull Request](https://github.com/vitomed/unilint/pulls)

[Issues](https://github.com/vitomed/unilint/issues)