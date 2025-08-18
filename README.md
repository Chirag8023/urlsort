<h1 align="center"> UrlSort </h1>
<p align="center"><b> A tool to categorize URLs from tools like Katana, Waybackurls, Gau, etc. </b></p>

```
 █████  █████           ████   █████████                      █████
░░███  ░░███           ░░███  ███░░░░░███                    ░░███
 ░███   ░███  ████████  ░███ ░███    ░░░   ██████  ████████  ███████
 ░███   ░███ ░░███░░███ ░███ ░░█████████  ███░░███░░███░░███░░░███░
 ░███   ░███  ░███ ░░░  ░███  ░░░░░░░░███░███ ░███ ░███ ░░░   ░███
 ░███   ░███  ░███      ░███  ███    ░███░███ ░███ ░███       ░███ ███
 ░░████████   █████     █████░░█████████ ░░██████  █████      ░░█████
  ░░░░░░░░   ░░░░░     ░░░░░  ░░░░░░░░░   ░░░░░░  ░░░░░        ░░░░░   
```


## Current options

`UrlSort` can take input from file or directly with comma-seprated data and provide output directly in cli or in a file.

```
options:
  -h, --help           show this help message and exit
  -f, --file FILE      Input file with URLs
  -d, --data DATA      Direct comma-separated URLs/data
  -o, --output OUTPUT  Output file (also prints to terminal)

```

## Installation

To use `UrlSort` You can just go to [releases page](https://github.com/Chirag8023/urlsort/releases) and download it to use directly.

It has no runtime dependencies, Just make sure you have latest version of python installed. 


## Usage

Suppose we have this file `input.txt` :

```txt
example.com
https://www.example.com
www.example.com/file?param=1
www.example.com/file.js
www.example.com/file.css
www.example.com/file.pdf
www.example.com/file.pdf?param=1
www.example.com/file.json.xmlrpc
example@gmail.com
mailto:example@gmail.com
normal line here
# commnet line here
```

Now we pass it to urlsort :

```bash
$ python urlsort.py -f input.txt -o output.txt
```

Here is `output.txt` :

```txt
[ENDPOINT]
example.com
https://www.example.com
example@gmail.com
mailto:example@gmail.com

[ENDPOINT + PARAM]
www.example.com/file?param=1

[JS]
www.example.com/file.js

[CSS]
www.example.com/file.css

[PDF]
www.example.com/file.pdf
www.example.com/file.pdf?param=1

[XMLRPC]
www.example.com/file.json.xmlrpc

[FREE FORM TEXT]
normal line here
# commnet line here

```
`Urlsort` categorized URLs based on different Filetypes, Endpoints, Endpoints + Param and Free Form Text.

## How `UrlSort` work behind the scenes ?

Here's a simple workflow to understand how the __initial version__ works under the hood :

![urlsort workflow](/urlsort%20workflow.png)



## License

This project is open-source and available under the [MIT License](https://github.com/Chirag8023/urlsort/blob/main/LICENSE).

---
<p align=center> Made with ❤️ by <a href="https://github.com/Chirag8023">Chirag8023</a> </p>
