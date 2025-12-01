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
│   ├── schedule_item.py # ScheduleItem dataclass
│   └── csv_loader.py    # CSV loading utility
├── bst_app/             # BST implementation
│   ├── tree.py          # Binary Search Tree
│   └── schedule.py      # Schedule adapter using BST
└── avl_app/             # AVL implementation
    ├── tree.py          # AVL Tree with rotations
    └── schedule.py      # Schedule adapter using AVL
```

## Program Flow
1. User chooses BST or AVL version
2. CSV data loaded into tree structure (key: subject, catalog, section)
3. User selects menu option (display all, search by subject, search by subject+catalog, search by instructor, quit)
4. Tree traversal used to find and display results

## Recent Changes
- 2025-12-01: Refactored to BST and AVL tree implementations
- 2025-11-26: Updated to course schedule format
- 2025-11-18: Initial project setup with Python 3.11

## Features
- Two tree implementations: BST and AVL
- Composite key ordering: (subject, catalog, section)
- Prefix-based search for subject and subject+catalog queries
- In-order traversal for displaying all items
- AVL auto-balancing with rotations

## User Preferences
- Clean, simplified code structure
- Tree data structures instead of dict/list
- Course schedule format for academic use
