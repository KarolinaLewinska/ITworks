# ITWorks

## Table of Contents
1. [Short Description](#1-short-description)
2. [Interfaces](#2-interfaces)
3. [Authors](#3-authors)
4. [Requirements Specifications](#4-requirements-specifications)
5. [UML Diagrams](#5-uml-diagrams)
6. [Software Architecture](#6-software-architecture)

### 1. Short Description
- ITworks – search courses and develop your IT skills.<br> 
- Website which allows to search for courses offers in information technology.<br> 

### 2. Interfaces
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/ranking.PNG)<br/>
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/browser.PNG)<br/>
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/results.PNG)<br/>
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/error404.PNG)<br/>

### 3. Authors
**Authors:** [Karolina Lewińska](https://github.com/KarolinaLewinska), [Justyna Gapys](https://github.com/justynagapys), [Marcin Wiśniewski](https://github.com/marcinwisniewski98)<br> 

### 4. Requirements Specifications

| ID | Category      | Subcategory                 | Short name              | Description                                                               | Priority |
| -- | --------------- | ------------------------ | ------------------------- | ------------------------------------------------------------------ | --------- |
| F1 | Functional | Main Page | Displaying Ranking | System allows to display rankings with the number of available courses by the popularity of programming languages and by the popularity of subjects.| high |
| F2 | Functional | Navigation | Navigation to browser | System allows to redirect an user to courses' browser via menu button. | high |
| F3 | Functional | Searching Results | Searching results by keyword | System allows to search courses by keyword. Results are diisplayed in alphabetical order. | high |
| F4 | Functional | Navigation | Navigation to course page | System allows to redirect an user to the website of course. | high |
| F5 | Functional | Navigation | Navigation to rankings | System allows to return to rankings' page via menu button. | high |
| F6 | Functional | Searching Results | No Results | System allows to display text information when there is no results. | medium |
| F7 | Functional | Searching Results | Searching by category | System allows to find courses by clicking one of the button with the name of category (Java, JavaScript, HTML5, PHP, Python, C++, C#, C, SQL) | medium |
| F8 | Functional | Searching Results | Message to authors | System allows to write an email message to the authors. | low |
| F9 | Functional  | Error Handling | Error page | System allows to display error page for 500, 404 and statuses. | low |
| F10 | Functional  | Searching Results | Displaying searching offers | System allows to display offers which an user wants to search. | high |
| NF1 | Non-functional | Project | Type of application | ITWorks is a web application. | high |
| NF2 | Non-functional | Project | Technology | It is used free and available technology. | high |
| NF3 | Non-functional | Project | Supported browsers | Application supports Google Chrome, Internet Explorer, Safari, Opera and Mozilla Firefox browsers. | high |
| NF4 | Non-functional | Project | Access to the Internet | Application must be always under Internet connection. | high |
| NF5 | Non-functional | Security | Testing | Application must be tested before release. | high |
| NF6 | Non-functional | Security | Backup | Application must have backup from version control (git). | high |
| NF7 | Non-functional | Security | Offerts' websites | Offers must came from verified websites. | medium |
| NF8 | Non-functional | User Interface | Language| Application is dedicated to polish users. | high |
| NF9 | Non-functional | User Interface | Navigation | All subpages must be easy to find by user. | high |
| NF10 | Non-functional | User Interface | Displaying offers | List of offers must be clearly presented for an user. | high |
| NF11 | Non-functional | User Interface | Navigation to link offers | Links to offers must clearly present possibility to visit the courses' websites. | high |
| NF12 | Non-functional | User Interface | Interfaces' presentation | User interfaces must be aesthetically consistent. | high |
| NF13 | Non-functional | User Interface | Logo | Application must have the logo. | medium |
| NF14 | Non-functional | User Interface | Responsiveness | Application must be fully responsive. | low |
| NF15 | Non-functional | Performance | Time of loading results | Time of loading results must be lower than 3 seconds. | medium |
| NF16 | Non-functional | Performance | Time of reaction| The reaction time of user activity must be lower than 3 seconds. | medium |
| NF17 | Non-functional | Performance | Number of users | The maximal number of users which use application at the same time must be 500. | low |
| NF18 | Non-functional | Ergonomy | New functionalities | Code of applicatiom must let implement easily new functionalities. | medium |
| NF19 | Non-functional | Ergonomy | Maintenance | The project' structure and code must be easy to maintain. | medium |
| NF20 | Non-functional | Ergonomy | Updating database | Application has one script, which lets update the database. | medium |

### 5. UML diagrams

**Use Case Diagram**
![UseCaseDiagram](https://github.com/KarolinaLewinska/ITworks_Flask/blob/main/uml/use-case.PNG)

**Activity Diagram**
![ActivityDiagram](https://github.com/KarolinaLewinska/ITworks_Flask/blob/main/uml/activity-diagram.PNG)

### 6. Software Architecture

**Webistes from where were taken courses:** [alx.pl](https://www.alx.pl/), [cts.com.pl](https://cts.com.pl/), [itschool.pl](https://itschool.pl/), [luxoft-training.pl](https://www.luxoft-training.pl/), [videopoint.pl](https://videopoint.pl/).

|  | Name | Usage | Version |
| --- | -------------- | ------------------------- | ------ |
| 1 | Python | Backend and web scrapping | 3.9.2 (19.02.2021) |
| 2 | Flask | Backend | 1.1.2 (03.04.2020) |
| 3 | SQLite | Database | 3.33.0 (14.08.2020) |
| 4 | Beautiful Soup | Web scraping | 4.9.3 (03.10.2020) |
| 5 | Requests | Simplifying HTTP requests | 2.25.0 (11.11.2020) |
| 6 | Matplotlib | Rankings' charts | 3.1.3 (02.02.2020) |
| 7 | HTML5 | Structures of views | 1.4938 (01.11.2016) |
| 8 | CSS3 | Appearance of view | v. 3 (07.06.2011)|
| 9 | Bootstrap | Appearance of view | 4.4.1 (28.11.2019) |
| 10 | Visual Paradigm | UML diagrams | (2020) |
| 11 | Git | Version control system | 2.31.1 (26.03.2021) |
