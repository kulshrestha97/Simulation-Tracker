# Simulation-Tracker

## A System Automation Tool for Engineers and Managers.


Summer Internship Project.

## Contents

- Abstract
- Introduction
- Workflow
- Development Environment and Frameworks
- Module Division
- Working Snapshots
- Conclusion


## 1. Abstract

Today in this modern world, technology has a huge hunger for data, and vice versa.
We are moving into the age of Artificial Intelligence (A.I), users are generating more
data than ever before. As stated earlier both data and technology depend on each
other, the more data we generate the more advanced processing capabilities we need,
in order to get sufficient insights, similarly, the more advanced technology we have
we will be needing more and more data, in order to not let the resource
under – utilized.

The later requires a great supervision of codes and Design under Test (DUT). This
project aims to reduce the numbers of steps that are required for a proper supervision
of the progress for the Design under Test. As such perfectly aligned to the definition
of Automation. The important details are discussed later.

## 2. Introduction

Simulation Tracker is a system automation tool that eases the working process for
both Engineers and Managers. The Project is made on the base of two design
patterns, one for Engineers and the other one for Managers. As it was important to
provide proper working channel for both the classes.

This tool will help the developers to automate their code base by simply specify the
instructions in the DO – File. On the other hand it will help the management by
providing them the direct code insight of the DUT. And hence directing the team, as
regarding how to further proceed in the project.

Agile Development methodologies are the need of today’s software or code
development, and as such this project proves to be a crucial step in going forward in
the said direction.


## 3. Workflow

The workflow of the project is defined as follows:


![](https://github.com/kulshrestha97/Simulation-Tracker/blob/master/ProjectPhotos/Figure1.png)


_Figure 1 Workflow of Simulation Tracker._

## 4. Development Environment and Frameworks

For this project, Python was chosen as the sole language. Python 3.6 was used, in
order to ensure that project is developed on latest industry standards.

Frameworks and Packages that are used in the packages:


- **Subprocess:** Subprocess is a python package that is used to run the system
commands, in layman’s terms it mimics a command prompt. It basically
executes a child process, which runs the command that is supplied as an
argument.


- **OS:** OS is a fundamental python module, which provides an interface for
harnessing the functionalities which are dependent on Operating System.


- **RE:** re is a fundamental python module, which provides the capabilities of
using Regular Expression. Regular Expression is a compact yet powerful way,
of describing sets of string that conform to a pattern. It basically represents a
form of grammar, under which a set of strings are acceptable.


- **MySQLdb:** MySQLdb is a pythonic wrapper around MySQL, which is used for
the purpose of database connectivity, for the purpose of data harnessing, data
manipulations, and similar operations.


- **Flask:** Flask is a micro framework for web development in Python.


- **Jinja:** Jinja is a template generating framework that is integrated with Flask.

## 5. Module Division

Our project was modularized into three major parts:

1. **Commands:** Commands module is the main driving force of this project. This
    module comprises of one class, which is the “command” class. Command class
    has the behavior of executing various HDL and HVL scripts. It depends on the
    rest of the modules also, for mimicking complete expected behavior.
2. **SQLdatabase:** SQLdatabase module is responsible for maintaining the
    database for the project, it comprises of two classes, namely database and
    displaydata. We can insert data, create tables, and display the existing tables.


3. **Reportparser:** Reportparser module is responsible for parsing various reports
    and returning the results for the same.

![](https://github.com/kulshrestha97/Simulation-Tracker/blob/master/ProjectPhotos/Figure2.png)


_Figure 2 Module wise description of project_

## 6. Working Snapshots

![](https://github.com/kulshrestha97/Simulation-Tracker/blob/master/ProjectPhotos/Figure3.png)


_Figure 3 Introductory Page, it provides the option of different working channels._


![](https://github.com/kulshrestha97/Simulation-Tracker/blob/master/ProjectPhotos/Figure4.png)


_Figure 4 Tracker initially asks for directory, then it asks for the DO file.
If there isn't a DO file, it has the capability to make a DO file and execute the same._

![](https://github.com/kulshrestha97/Simulation-Tracker/blob/master/ProjectPhotos/Figure5.png)


_Figure 5 Tracker than asks for the text file name, after that it asks for the folder in which html report is stored. The tracker than
stores the parsed the values in database._


![](https://github.com/kulshrestha97/Simulation-Tracker/blob/master/ProjectPhotos/Figure6.png)


_Figure 6 the generated report comprises of the progress of various DUTs ordered by the recent actions._

## 7. Conclusion

In this pacing world, Simulation Tracker is a tool that helps the system automation
for execution of various Hardware Descriptive Languages (HDLs) and Hardware
Verification Languages (HVLs). It eases the work primarily for the management of
the company, as ideally, everything has to be done on time. As such monitoring the
progress of the Design under Test (DUT) running status, gives a good estimation and
hence a better precision.


