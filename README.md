# Auto Generate Header Anchor

## Purpose
This script is to parse Github README markdowns to automatically generate markdown anchors for the headers.
This is to create a table of contents to provide ease of navigation.

## Workflow
- URL link to a Github README markdown is provided to the script
- HTML content of the page is retrieved and parsed to obtain header information
  - Only headers with sizes h2, h3 and h4 are looked for (A header with a size h1 are assumed as a README title and skipped)
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
