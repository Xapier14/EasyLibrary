# EasyLibrary
A simple library management system.

## Getting Started
***Optional: ***You might want to set-up a virtualenv just to keep things tidy.
### Clone the repo and install dependencies:
```Shell
git clone https://github.com/Xapier14/EasyLibrary.git
pip install -r requirements.txt
```
### Run the program:
```Shell
python ./main.py
```

## Features
- [x] User Authentication
- [ ] Self-Operate Kiosk Mode (User-Level Authorization)
- [ ] Operated/Attended Mode (Administrator-Level Authorization)
- [ ] Book Database
    - [ ] Add
    - [ ] Delete
    - [ ] Edit
    - [ ] Search
    - [ ] Book Cover & General Info
- [ ] Book Item Inventory Database
    - [ ] Book Location
    - [ ] Duplicate Count
- [ ] User Database
    - [x] Add
    - [ ] Delete
    - [ ] Edit
    - [ ] Search
    - [ ] User Types
        - [ ] Administrator
        - [ ] User
- [ ] Borrowing System
    - [ ] Borrow
    - [ ] Return

## Dependencies
- PySimpleGUI
- bcrypt