You are generating a new Python script for my mathRunner project.

### Context:
- The project has this structure:

mathRunner/
├── mathRunner.py         # main runner
├── input.yaml            # user inputs
└── scripts/              # all scripts live here
    ├── __init__.py
    ├── add.py
    ├── divide.py
    ├── factorial.py
    └── bin_to_hex.py

- Each script must be placed inside the `scripts/` folder with a filename matching the script’s purpose (e.g., `circle_area.py`).
- Each script **must define**:
  1. `INPUTS`: a list of (name: str, type: Python type) for all required arguments.
     - Types can only be: `int`, `float`, `str`, `bool`.
  2. `main(args: dict) -> Any`: the main entry function that takes arguments from `input.yaml` and returns the final result.

- The runner will:
  - Read `input.yaml`.
  - Call `main(args)` of the script.


### Requirements for Script:
- Validate input when needed (e.g., avoid division by zero).
- Return the **final result only** (no prints inside the script).
- Keep code short, clean, and compatible with the above system.

---

### Task:
Generate a script named: `<SCRIPT_NAME>`
It should: `<DESCRIPTION OF WHAT THE SCRIPT DOES>`

Return only the complete script code, nothing else.

--------------------------------------------------



