# Course Schedule Search Program

## Overview
A Python command-line application for managing and searching college course schedules using tree data structures (BST and AVL).

## Project Structure
```
├── main.py              # Entry point - choose BST or AVL version
├── run_bst.py           # Direct BST version entry point
├── run_avl.py           # Direct AVL version entry point
├── courses.csv          # Course schedule data
├── shared/              # Shared code
│   ├── schedule_item.py # ScheduleItem dataclass with fields and key generation
│   └── csv_loader.py    # CSV loading using DictReader with UTF-8-sig
├── bst_app/             # BST implementation
│   ├── tree.py          # Binary Search Tree with insert/search/inorder/height
│   └── schedule.py      # Schedule adapter using BST
└── avl_app/             # AVL implementation
    ├── tree.py          # AVL Tree with rotations and height tracking
    └── schedule.py      # Schedule adapter using AVL
```

## Rubric Compliance
- **Data Model (ScheduleItem)**: Correct dataclass with all 9 fields, get_key() for composite key, CSV parsing
- **BSTMap Integration**: Full BST with insert, search, inorder traversal, height()
- **AVLTreeMap Integration**: Self-balancing AVL with rotations, maintains balance on insert
- **CSV Loading**: Uses csv.DictReader with UTF-8-sig encoding
- **Search & Reporting**: Subject search, subject+catalog search, instructor search, formatted output
- **Height Implementation**: height() method in both BST and AVL trees
- **Documentation & Style**: Docstrings, comments, modular design across packages

## Program Flow
1. User chooses BST or AVL version
2. CSV data loaded into tree structure (key: subject, catalog, section)
3. Tree height displayed after loading (demonstrates AVL balancing)
4. User selects menu option (display all, search by subject, search by subject+catalog, search by instructor, quit)
5. Tree traversal used to find and display results

## Recent Changes
- 2025-12-01: Added height() method and documentation per rubric requirements
- 2025-12-01: Refactored to BST and AVL tree implementations
- 2025-11-26: Updated to course schedule format
- 2025-11-18: Initial project setup with Python 3.11

## Features
- Two tree implementations: BST and AVL
- Composite key ordering: (subject, catalog, section)
- Prefix-based search for subject and subject+catalog queries
- In-order traversal for displaying all items
- AVL auto-balancing with rotations (height 5 vs BST height 12)
- height() method in both trees

## User Preferences
- Clean, simplified code structure
- Tree data structures instead of dict/list
- Course schedule format for academic use
- Full documentation per grading rubric
