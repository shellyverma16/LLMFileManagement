# LLM File System Assistant

This small project provides tools for reading, listing, writing and searching files (resumes), plus a simple LLM-integrated assistant that can call those tools.

Setup

1. Create a Python environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Optional: set `OPENAI_API_KEY` to enable OpenAI function-calling.

Usage

- Run the simple REPL assistant:

```bash
python ai_resume_tools/llm_file_assistant.py
```

Example prompts:

- "Read all resumes in sample_resumes"
- "Find resumes mentioning Python"
- "Create a summary file for resume_john_doe.txt"

Files

- `ai_resume_tools/fs_tools.py` — core tools: `read_file`, `list_files`, `write_file`, `search_in_file`.
- `ai_resume_tools/llm_file_assistant.py` — small assistant with OpenAI function-calling and a fallback router.
- `ai_resume_tools/sample_resumes/` — sample resume files for testing.

Deliverables checklist

- Source code: present in `ai_resume_tools`
- `requirements.txt`: present
- Sample data: included
- `README.md`: this file
- Demo video: create a 2–3 minute screencast showing the assistant in action (suggest using OBS or built-in OS recorder)
