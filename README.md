# Machine Learning - Lab 1

This lab is intended to teach you the basic techniques to get started with the actual assignments later in the course. This lab is **not** graded, but it does have a hand-in flow configured so that you can familiarize yourself with how handing in will work in this course.

## What you will learn
* Using unit tests to develop according to a specification.
* Plotting your results with Matplotlib.
* Develop a simple 1-Nearest Neighbor Classifier.
* The PEP8 Python coding style standard.
* Selecting an IDE (Pycharm, MS Visual Studio Code, Google Colab, ...)

## Task 0: set up your environment

This code requires Python 3.6 or higher.

If you're using a `virtualenv`/`venv`, install the following with pip:

`pip install matplotlib pytest sklearn`

If you're using a `conda` environment or Google Colab these should already be pre-installed.

## Task 1: using unit tests
Unit tests allow us to test bit by bit whether all the individual components of a program behave as we desire. For each unit, we specify one or more tests where we run that piece of code, and see whether it satisfies expectations that we `assert`.

Let's do a really simple example. Look in the files `hello.py` and `hello_test.py`. Run the tests in the second file with:

`pytest hello_test.py`

You should see that the test fails with something like this: 
```
    def test_hello():
>       assert hello.hello_world() == "Hello World!"
E       AssertionError: assert 'Hello!' == 'Hello World!'
E         - Hello World!
E         + Hello!
```

The test tries to assert that the outcome of calling `hello.hello_world()` is equal to the expected value "Hello World!". Our code doesn't produce the expected output, so the test fails.

Alter `hello.py` so that the test will pass.

Unit testing can be used to find bugs in programs, but it can also be used pro-actively, by describing how we expect a program to behave, and only then starting to program it. The typical workflow here is that you write tests and confirm that they fail. If the tests pass before you've even written the program, then they're clearly not useful tests!

We'll use this workflow in the rest of this lab and in the future assignments. Each assignment will have some starter code, and a set of tests. Your job will be to change the starter code so that the tests pass. You can see what you still need to do by just running `pytest .`, which will run all the tests in the directory. As long as it's still throwing errors, you still have work to do.


## Task 2: plotting the results of a classifier

Run the script `make_plots.py`, which shows you a collection of randomly generated data points labeled 1 and -1. It shows you the training and test set together, and then just the test set (what a perfect prediction would look like) and a prediction according to the majority classifier.

### What you should do:
- Modifiy the `show_performance` function to save each plot to a file automatically before displaying it on the screen.
- Try out different file formats (PNG, JPG, PDF, SVG, EPS). Find out which is the default if you don't specify a file format. Which one results in the largest files? Which one scales best if you zoom in and out? Which one contains selectable text when you include it in a LaTeX report?

## Task 3: building a 1-NN classifier
A 1-nearest neighbor classifier classifies each point in the test set according to the label of the nearest point from the training set. 

**Code:** In the file `one_nearest_neighbor.py`, change `fit` and `predict` so that the unit tests in `one_nearest_neighbor_test.py` pass.

**Report:** Generate plots of the predictions as before. Does the 1NN classifier work better or worse than the majority classifier? In general, which of these classifiers do you expect to work better? Can you think of a situation where the other one works better?

## Task 4: read the Zen of Python
Every programming language has some philosophy behind it. One of Python's principles is `explicit is better than implicit` so there is a clear statement of Python's philosophy: PEP20, `The Zen of Python`. Read a good explanation of it [here](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/). It's worth re-reading the Zen of Python every year.

## Task 5: the PEP8 standard
Unlike for example C++ where there are lots of discussions about which line to put your curly braces on, there is just one standardized proper code style for Python, known as [PEP8](https://www.python.org/dev/peps/pep-0008/).

Adhering to the standard makes your code easier to read ("readability counts") and often makes it easier to spot things that may be a bug. Also, checking most of this standard can be automated, which most IDEs can help do for you.

In future assignments, a small part of your grade will be based on adhering to the standard. We'll use automated "linters" to check your code for violations of these style rules. Install these two to get started: `pylint` and `pycodestyle`. 

You can now run `pytest clean_code_test.py` to go through all the files looking for code violations. Try to make the tests pass.

It's sometimes necessary to break the style guidelines. For example, an assignment might specify that a function name needs to contain your surname, including starting with capitals. Or a comment contains a long URL. Therefore, you get a budget of a certain amount of acceptable violations before we deduct points. Use it wisely!



## Task 6: selecting an IDE
A good Integrated Development Environment does a lot of the grunt work for you. Popular IDEs for Python include Pycharm and MS Visual Studio Code. They can do a lot of code inspection for you, making it easy to spot and fix bad code rightaway. They also have advanced syntax highlighting, code completion and they can often show you when you're making a mistake. It takes some initial time to get used to them, but using a good IDE makes your life much easier afterwards and saves a lot of time.

The choice of IDE is up to you, but the two we mentioned above are certainly suitable, and are available for free to students on all operating systems.

An alternative is use of Google Colab. It doesn't have quite as powerful code inspection and syntax highlighting, but on the plus side it runs in the cloud somewhere, which can help if your own computer isn't so powerful. It's also useful for teamwork. The format is similar to Jupyter Notebooks, and you can easily import and export from Colab to Notebook format.


## How to submit

### Your code
1. Once your code passes all the unit tests, you should feel confident that you can submit it.
2. Commit your local code to your local repository.
3. Push the commit to the remote repository.
4. Wait for the auto-grading workflow to run. If it passes then you're done with submitting code.

### Your report
* Your report should be **at most** 1 page.
* It should be a PDF.
* It should contain all the graphs you plotted. Graphs should have axis labels, units on the axis labels where appropriate, a legend and a title. They should also have a caption describing in 1-3 sentences what the plot shows.

Submit the report through Brightspace. We recommend using LaTeX and Overleaf. You can use the `report-template.tex` example file as a starting point.

## Autograding
### Setup command

`sudo -H pip3 install pytest`

### Run command

`pytest`

### Notes

*    pip's install path is not included in the PATH var by default, so without installing via sudo -H, pytest would be unaccessible.
