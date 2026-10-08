# LLM File Management Project

A Python-based resume file management assistant that reads, lists, searches, and summarizes resume files using lightweight file-system utilities and an LLM-style assistant interface.

This project is built to satisfy the assignment requirements for working with resume files in common formats such as `.txt`, `.pdf`, and `.docx`, while also supporting simple prompt-driven file operations.

## Project overview

The application includes:

- file tools for reading and writing files
- recursive directory listing with extension filtering
- keyword search across file content
- resume summary generation
- optional OpenAI-based function-calling integration
- a console-based REPL for local testing and demonstrations

## Folder structure

```text
LLMFileManagement/
├── README.md
├── ai_resume_tools/
│   ├── README.md
│   ├── requirements.txt
│   ├── fs_tools.py
│   ├── llm_file_assistant.py
│   ├── test_smoke.py
│   └── sample_resumes/
│       ├── resume_alex_turner.txt
│       ├── resume_jane_smith.txt
│       ├── resume_john_doe.txt
│       ├── resume_li_wang.txt
│       ├── resume_maria_garcia.txt
│       └── resume_sam_lee.txt
└── ...
```

## Core functionality

### 1. Read files

The `read_file(filepath: str)` function reads resume content from supported formats and returns a structured dictionary containing:

- success status
- content text
- metadata such as file name, size, modified time, and extension
- error details if something goes wrong

Supported file types include:

- `.txt`
- `.md`
- `.pdf`
- `.docx`

### 2. List files

The `list_files(directory: str, extension: str = None)` function:

- scans a directory recursively
- lists matching files
- optionally filters by extension like `.txt` or `.pdf`
- returns metadata in a consistent structure

### 3. Write files

The `write_file(filepath: str, content: str)` function:

- writes text to disk
- creates parent directories automatically
- returns a success or failure response

### 4. Search in files

The `search_in_file(filepath: str, keyword: str)` function:

- reads the file content
- searches for the keyword case-insensitively
- returns matching lines and surrounding context
- provides a count of results

### 5. Summary generation

The assistant supports creating a simple summary file from a resume. This is useful for the assignment requirement that asks for a summary flow.

## Assistant behavior

The assistant in `llm_file_assistant.py` provides a prompt-driven interface for commands like:

- "Read all resumes in sample_resumes"
- "Find resumes mentioning Python"
- "Create a summary file for resume_john_doe.txt"

It includes:

- a direct fallback router for local testing
- OpenAI function-calling support when `OPENAI_API_KEY` is configured
- summary generation for a selected resume file

## Dependencies

The project depends on:

```text
openai
PyPDF2
python-docx
```

These are listed in the requirements file inside the tools folder.

## Setup instructions

1. Open a terminal in the project root.
2. Create a virtual environment:

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r ai_resume_tools/requirements.txt
```

## Running the project

### Run the assistant

```bash
python ai_resume_tools/llm_file_assistant.py
```

Example prompts:

```text
Read all resumes in sample_resumes
Find resumes mentioning Python
Create a summary file for resume_john_doe.txt
```

### Run the smoke test

```bash
python ai_resume_tools/test_smoke.py
```

This verifies that:

- files are listed correctly
- resume keyword search works
- resume content reads properly
- summary file generation succeeds

## Example output structure

### `read_file()` response

```python
{
    "success": True,
    "content": "John Doe\nSoftware Engineer\n...",
    "metadata": {
        "name": "resume_john_doe.txt",
        "path": "C:/.../resume_john_doe.txt",
        "size": 230,
        "modified": "2026-10-08T12:00:00",
        "extension": ".txt"
    }
}
```

### `search_in_file()` response

```python
{
    "success": True,
    "count": 3,
    "matches": [
        {
            "line_no": 5,
            "line": "- Developed web applications in Python and JavaScript.",
            "context": "- Developed web applications in Python and JavaScript."
        }
    ],
    "metadata": {
        "name": "resume_john_doe.txt",
        "extension": ".txt"
    }
}
```

## OpenAI integration

If the environment variable `OPENAI_API_KEY` is set, the assistant can use OpenAI function-calling patterns to decide which tool to invoke based on a natural-language prompt.

Example:

Windows:

```bash
set OPENAI_API_KEY=your_key_here
```

macOS/Linux:

```bash
export OPENAI_API_KEY=your_key_here
```

If no API key is set, the project still works through the fallback local router.

## Assignment alignment

This project directly addresses the assignment requirements:

- Part A: Core File System Tools
  - `read_file()` implemented
  - `list_files()` implemented
  - `write_file()` implemented
  - `search_in_file()` implemented

- Part B: LLM Integration
  - assistant logic created
  - tool-calling structure included
  - natural-language queries supported
  - summary workflow included for resume output generation

## Notes

This implementation is intentionally simple, readable, and focused on the assignment requirements rather than adding unnecessary complexity.

It is suitable for learning, local testing, and demonstration of file-management + LLM-style assistant workflows.

## Future improvements

Possible future enhancements include:

- more robust PDF and DOCX parsing
- better summary generation quality
- support for additional file types
- real LLM orchestration with more advanced query parsing
- a small web or API interface

## Summary

This project demonstrates how to build a resume-processing utility using Python and file system tools, while also exposing those capabilities through a minimal AI assistant interface. It is practical, testable, and aligned with the assignment scope.