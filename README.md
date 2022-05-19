# EasyLibrary
A simple library management system.

## Getting Started
***Optional:*** You might want to set-up a virtualenv just to keep things tidy.
### 1. Clone the repo and install dependencies:
```Shell
git clone https://github.com/Xapier14/EasyLibrary.git
cd ./EasyLibrary
pip install -r requirements.txt
```
### 2. Set-up the local datastore:
```
./
├ ...
├ main.py
└ localDb/
    ├ images/
    │   └ default.png -> Default book cover
    ├ globalBooks.json
    ├ inventory.json
    ├ transactions.json
    └ users.json
```
***Important:*** The contents of each new JSON file should be:
```
[]
```
***Note:*** The default admin account generated on an empty user list is:
```
Username: "admin"
Password: "12345678"
```
### 3. Run the program:
```Shell
python ./main.py
```

## Features
- [x] User Authentication
- [x] Self-Operate Kiosk Mode (User-Level Authorization)
- [x] Operated/Attended Mode (Administrator-Level Authorization)
- [x] Book Database
    - [x] Add
    - [ ] Delete (Probably will not be added without related transaction check & deletion)
    - [x] Edit
    - [x] Search
    - [x] Book Cover & General Info
- [x] Book Item Inventory Database
    - [x] Book Location
    - [x] Duplicate Count
- [x] User Database
    - [x] Add
    - [x] Delete
    - [x] Edit
    - [x] Search
    - [x] User Types
        - [x] Administrator
        - [x] User
- [x] Borrowing System
    - [x] Borrow
    - [x] Return

## Further Improvements
- Datamodels should only have getters and the models themselves should be cached.
- Datastores should have setter methods for the datamodels and shall keep a cache of the datamodels to keep transactions fast and tiny.
    - This should allow for concurrent datastore types (SQL, NoSQL, HTTP, TCP/UDP, WebSockets, CosmosDB)

## Dependencies
- PySimpleGUI
- bcrypt
- Pillow