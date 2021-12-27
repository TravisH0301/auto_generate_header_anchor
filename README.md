# Auto Generate Header Anchor

## Purpose
This script is to parse Github README markdowns to automatically generate markdown anchors for the headers.
This is to create a table of contents to provide ease of navigation.

## Workflow
- URL link to a Github README markdown is provided to the script
- HTML content of the page is retrieved and parsed to obtain header information
- Markdown anchors are created and displayed as an output

## Demonstration
### Creation of markdown anchors for headers
![Demonstration1](https://github.com/TravisH0301/auto_generate_header_anchor/blob/main/demonstration_1.gif)

### Using created markdown anchors on markdown
![Demonstration2](https://github.com/TravisH0301/auto_generate_header_anchor/blob/main/demonstration_2.gif)

## How to Use
- Run Python script
- Copy and paste a Github README markdown into the prompted text box

## Dependencies
- Python (==3.7)
  - Request
  - BeautifulSoup
  - Pandas
