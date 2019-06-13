#!/usr/bin/env python
"""Remove all artifacts of running"""
import subprocess
import glob


def strip_notebook_output_cells(notebook):
    subprocess.run(['jupyter',  'nbconvert', '--inplace', '--ClearOutputPreprocessor.enabled=True', notebook])

def strip_output_cells():
    """Strip output cells from the notebooks"""
    templates = glob.glob("templates/*")
    for t in templates:
        strip_notebook_output_cells(t)
    strip_notebook_output_cells('01-Starting.ipynb')


def delete_tutorial_artifacts():
    """Remove the renku-tutorial-flights folder"""
    pass


print("Stripping output cells from notebooks.")
strip_output_cells()

# print("Delete the renku-tutorial-flights folder.")
# delete_tutorial_artifacts()
