# Report Management System (Archive):

This application consists of baisc Operation (retive, delete, edit, insert) for Report Management System (Archive). 

### Software Requirements Specification:
- :white_check_mark: : Satisfied
- :heavy_multiplication_x: : Not Satisfied
- Some: Partial

| Requirements | Satisfied|
| ------------- | ------------- |
| Each user must have a login, and a role assigned to him/her for viewing, editing and deleting documents.  | :white_check_mark: |
| Assign users to different groups. Each user will be given the ability to view/edit/delete/create a report on different groups by the admin.  | :white_check_mark:  |
| (e.g. when a reportcis belonging to Group A and user doesn’t have permission for Group A then he/she shouldn’t be able to even see reports under this group).  | :heavy_multiplication_x:  |
| A user can have the permission for 1 or more groups.  | Some  |
| Admin, User. And Admin has full authority and can delete other users and assign users to different groups.  | :white_check_mark:  |
| Group Management (CRUD).  | :white_check_mark:  |
| Search using different criteria.  | :heavy_multiplication_x:  |
| Create a new report that includes the tags, group, and related files.  | Some  |
| Upload files  | :heavy_multiplication_x: |

## Stack
- Python
- Flask Framework , Flask-MySQLDB
- WampServer
- HTML/CSS

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask Framework , Flask-MySQLDB.

* [Python](https://www.python.org/downloads/)
* [WampServer](https://www.wampserver.com/en/)

```bash
pip3 install flask
pip3 install Flask-MySQLdb
```

## Difficulties
- Database Connection.
- Upload different types of files to the database.
- Tables integrety.






