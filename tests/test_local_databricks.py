# -*- coding: utf-8 -*-
"""Imports unit test."""

def test_import():
    import local_databricks

def test_example():
    import os
    path = "tests/samples/note1.py"
    os.system(f"python {path}")
