# Machine Learning - Lab 1

This lab is intended to teach you the basic techniques to get started with the actual assignments later in the course. This lab is **not** graded, but it does have a hand-in flow configured so that you can familiarize yourself with how handing in will work in this course.

## What you will learn
* Using unit tests to develop according to a specification.
* Plotting your results with Matplotlib.
* Develop a simple 1-Nearest Neighbor Classifier.
* The PEP8 Python coding style standard.
* Selecting an IDE (Pycharm, MS Visual Studio Code, Google Colab, ...)

## Task 0: set up your environment
`pip install pandas matplotlib pytest`

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
TODO
- Colored according to prediction
- Styled according to true label
- Which file format scales best in a report?

## Task 3: building a 1-NN classifier
A 1-nearest neighbor classifier classifies each point in the test set according to the label of the nearest point from the training set. 

**Code:** In the file `one_nearest_neighbor.py`, change `fit` and `predict` so that the unit tests in `one_nearest_neighbor_test.py` pass.

**Report:** Generate plots of the predictions as before. Does the 1NN classifier work better or worse than the majority classifier? In general, which of these classifiers do you expect to work better? Can you think of a situation where the other one works better?

## Task 4: the PEP8 standard
TODO: make a file with some intentional errors which you can pick up with a linter, then a test that asserts that the number of transgressions is 0.

## Task 5: selecting an IDE
TODO

## Task 6: read the Zen of Python
TODO


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
