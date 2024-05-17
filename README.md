<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ishaansingh99/SF6-Frame-Data-Visualizer/">
    <img src="assets/README/ryu-dance.gif" alt="Gif of Ryu dancing like Jamie" width="300" height="250">
  </a>
  <h3 align="center">Street Fighter 6 Frame Data Visualizer</h3>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#to-do">To-Do</a></li>
    <li><a href="#author">Author</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project uses the FakeNewsNet dataset to analyze fake news articles for trends and patterns, and develops machine learning models to classify them. See the [project report](Project_Report.pdf) and [code](Project_Code.ipynb) for more.

<!-- GETTING STARTED -->
## Getting Started

### Dependencies

The dataset for this project is already downloaded and available in the repository. To run the Project_Code.ipynb notebook, Python with the usual Anaconda packages are required, along with NLTK which can be installed as follows:

* Anaconda
  ```sh
  conda install anaconda
  ```
* Natural Language Toolkit
  ```sh
  conda install nltk
  ```
Also used was the python word cloud package for generating the word clouds seen in the logo above, but this is not necessary for the notebook, the cell can be skipped without any issues to the rest of the notebook:

* Natural Language Toolkit
  ```sh
  conda install wordcloud
  ```

**Alternatively**, the project repository has a requirements.yml file to clone the conda environment used to develop the code. Clone the environment as shown in the <a href="#installation">installation below</a>:

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/uf-eel6825-sp23/final-project-code-ishaansingh99.git
   ```
2. Setup (and activate) your environment (or download the packages <a href="#dependencies">above</a>)
   ```sh
   conda env create -f requirements.yml
   ```

<!-- USAGE EXAMPLES -->
## Usage

All the code for this project can be found in the commented [Project Code Jupyter Notebook](Project_Code.ipynb). Just follow the instructions above for installation.

Run every code cell in order, but you may choose to omit the word cloud and sentiment analysis cells.

A project presentation and demo can be found on [youtube here](https://youtu.be/02RJxJ7cR6c).

<!-- Author -->
## Author

Ishaan Singh - [LinkedIn](https://www.linkedin.com/in/ishaan-singh-se/) - ishaans1999@gmail.com

## Thank you

### To-do:
- Add gif opening
  -  Gif assets are added but need renaming of assets and UI elements
- Fix special input cases like neutral jump specific moves
- Styling of elements
- Add titles to tables
- Positioning
- Add icons to char select screen
- Make scraper robust
  - Get char data from pandas/csv
  - Figure out scraper API tokens