---
layout: assignment
due: 2026-05-13 23:59:59 -0700
permalink: assignments/project06.html
title: Project06 - Web app backed by SQLite
github_url: https://classroom.github.com/a/uV0Mxyo2
published: true
---

## Requirements

For this project you will:
1. Integrate your web server implementation with your SQLite implementation
1. Design a database schema with at least three columns in addition to the primary key. Your schema can describe anything you're interested in: cars, birds, recipes, etc.
1. Add web pages to insert, query, and search the database (see rubric)

## Given

In lecture, we will:
  1. Discuss the SQLite language and integrating it into a C project, 
  1. Demonstrate using web pages and forms to implement HTTP methods 
  1. Demonstrate using templates to display formatted data using simple HTML
  
## Grading

Logistics
1. We will again to peer grading for this project
1. Since this is due at the end of the semester, we won't do late grading. Bring your best work to our last lecture meeting

Rubric
1. For 80 points, use an LLM to generate code or web pages
1. For 90 points, develop your own code and web pages to display (`GET`)the database table
1. For 100 points develop your own code to implement one of these options:
    1. Make a larger data set (more than 100 rows) including two tables with a foreign key relationship between them.  
    2. Code and web pages to build an HTTP router which can insert, update, and delete rows, displaying the resulting database table
    3. Use a template engine such as [TinyTemplate](https://github.com/cozis/tinytemplate) to read the table and display it in an attractive, professional way. 
1. For 105 points, implement two of those options
