""" Test student scripts for style violations & lint """
import re
from pylint import epylint as lint
import pycodestyle

MAX_LINE_LENGTH = 120
PYLINT_MINIMUM = 9
PYLINT_OPTIONS = f'--max-line-length={MAX_LINE_LENGTH} --variable-rgx=[a-z0-9_]+$'
PYCODESTYLE_MAXIMUM = 1


def evaluate_lint(script):
    """ Lint one script """
    std = lint.py_run(command_options=f'{script} {PYLINT_OPTIONS}', return_std=True)
    text = std[0].read()
    score = float(re.findall(r'rated at ([0-9.\-]*)/.*', text)[0])
    return score


def test_lint():
    """ Lint all relevant scripts """
    assert evaluate_lint('make_plots.py') > PYLINT_MINIMUM
    assert evaluate_lint('majority.py') > PYLINT_MINIMUM
    assert evaluate_lint('majority_test.py') > PYLINT_MINIMUM
    assert evaluate_lint('model.py') > PYLINT_MINIMUM
    assert evaluate_lint('util.py') > PYLINT_MINIMUM

    assert evaluate_lint('hello.py') > PYLINT_MINIMUM
    assert evaluate_lint('one_nearest_neighbor.py') > PYLINT_MINIMUM
    assert evaluate_lint('one_nearest_neighbor_test.py') > PYLINT_MINIMUM
    assert evaluate_lint('dirty_code.py') > PYLINT_MINIMUM


def evaluate_style(script):
    """ Check one script for code style """
    style = pycodestyle.StyleGuide(max_line_length=MAX_LINE_LENGTH, quiet=True)
    result = style.check_files([script])
    return result.total_errors


def test_style():
    """ Lint all relevant scripts """
    assert evaluate_style('hello.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('model.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('util.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('make_plots.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('majority.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('majority_test.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('one_nearest_neighbor.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('one_nearest_neighbor_test.py') <= PYCODESTYLE_MAXIMUM
    assert evaluate_style('dirty_code.py') <= PYCODESTYLE_MAXIMUM
