# data_visualization_project

![commits](https://badgen.net/github/commits/davidtwynn/data_visualization_project?icon=github&color=blue)
![Python version](https://img.shields.io/badge/python%20version-3.11-good)
![Environment](https://img.shields.io/badge/Environment-Windows-blue)
![Coding style](https://img.shields.io/badge/code%20style-black-000000.svg)

Repo for following along with the Python Crash Course 2nd edition project 2 - Data Visualization

Tested only on Windows

Book - https://nostarch.com/python-crash-course-3rd-edition

# Files

src/mpl_squares.py - matplotlib plot square numbers

src/scatter_squares.py - matplotlib scatterplot square numbers

src/scatter_cubes - matplotlib scatterplot cubed numbers

src/random_walk.py - class for randomly generating a list of x and y coords to plot a path

src/rw_visual.py - matplotlib scatterplot the RandomWalk class

src/die.py - class representing a dice with a given number of sides that can be rolled

src/die_visual.py - plotly histogram from rolling dice in die.py

# First time setup

### Create virtual environment

```python
py -3.11 -m venv venv
```

Activate environment

```python
venv/Scripts/activate
```

Upgrade pip

```python
py -m pip install --upgrade pip
```

Install requirements

```python
py -m pip install -r requirements.txt
```

## Run

After installing dependencies, run one of the scripts to get one of the outputs from the example

```python
python .\src\die_visual.py
```

## Chapter 15

scatter_squares.py

Blues colormap, setting style, fonts, axis names

!["Squares plot"](images/squares_plot.png?raw=True)

scatter_cubes.py

Custom scatter plot for cubing of numbers, copper color map

!["Cubes plot"](images/cubes_plot.png?raw=True)

Random Walk scatter plot

!["RW Walk scatter plot"](images/rw_visual.png?raw=True)

rw_visual.py

Custom Random Walk change to a regular plot

!["Custom RW Walk scatter plot"](images/custom_rw_visual.png?raw=True)

die_visual.py

plotly histogram of rolling a 6 sided dice and a 10 sided dice then adding them up

![plotly histogram](images/d6_d10.JPG)
