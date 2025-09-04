You are generating a new Python script for my mathRunner project.

### Context:
- The project has this structure:

mathRunner/
├── mathRunner.py         # main runner
├── input.yaml            # user inputs
└── scripts/              # all scripts live here
    ├── __init__.py
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
The `result` it returns should be formatted correctly like following

```python
return (
    f"name1 : {value1}\n"
    f"name2 : {value2}\n"
    f"name3 : {value3}"
)
```

inputs will be given in the yaml format like in the following

```yaml
- name: convert_num
  args:
    dec: "34"
```

Make sure arguments have names

- Return only the complete script code with its name, nothing else.
- And also in the code, in the final return, don't return the arguements and just the final answer
--------------------------------------------------



