# Repository Guidelines

This document describes the structure and naming conventions used in the HCI notes repository.

## Structure

Theme → Module → Document → Media

## Themes

Themes represent major conceptual areas such as:

- People
- UX
- HCI Research

Rules:

- Folder names start with a number inside square brackets
- Names are written in English

Example

```
[1] People
[2] UX
[3] HCI Research
```

## Modules

Modules group lessons within a theme.

Rules:

- Start with a number
- Followed by `" - "`
- Words separated by spaces

Example

```
0 - Methods
1 - Fundamental Principles of HCI
2 - People
3 - Innovation Methods
```

## Documents

Each module contains a Markdown document.

Rules:

- Filename matches the syllabus title
- No numbers
- No underscores
- Words separated by spaces

Example

```
Fundamental Principles of HCI.md
How People do Things and Human Errors.md
```

## Media Folders

Each document has a dedicated media folder.

Rules:

- Prefix `Media_`
- Spaces replaced with underscores
- Title must match the document title

Example

Document

```
Fundamental Principles of HCI.md
```

Media folder

```
Media_Fundamental_Principles_of_HCI
```

## Update README.md

To update README.md go to the root of the repo after making changes and execute
```
python tools/repo_check.py
```
This will update the navigation table links between the comments ```<!-- AUTO_NAV_START -->``` and ```<!-- AUTO_NAV_END -->``` in the README.md