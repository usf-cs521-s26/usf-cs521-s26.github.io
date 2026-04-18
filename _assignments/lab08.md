---
layout: assignment
due: 
permalink: assignments/lab08.html
title: lab08 - SQL Databases
github_url: 
published: true
---

## Requirements

1. For this lab you will use the SQLite developer tools for C to `CREATE` a table `INSERT` at least five rows and `SELECT` to print the table rows
1. When you execute a SQL `SELECT` you will provide a callback function which will be called once per row
1. You can use your resizable array from project03 to pass the values out of the callback

## Given

1. The `sqlite3` command line tool and the developer tools are installed in the `clab` environment
1. You should `#include <sqlite3.h>` in your C source code and link with `-lsqlite3` to include the SQLite3 library in your executable
1. In lecture we will discuss relational modeling, how to program SQL in C, including demo code.

## Rubric

We will again do peer grading
  1. LLM (25 pts) or code walkthrough (50 pts)
  1. Demonstrate your solution printing the results of printing a table with at least five rows (50 pts)
