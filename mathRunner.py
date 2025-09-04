import importlib
import os
import time
import yaml

INPUT_FILE = "input.yaml"

def read_input():
    """Read list of scripts from input.yaml"""
    if not os.path.exists(INPUT_FILE):
        print("input.yaml not found!")
        return []

    try:
        with open(INPUT_FILE, "r") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Invalid YAML in {INPUT_FILE}: {e}")
        return []

    if not isinstance(data, list):
        print("input.yaml must contain a list of scripts")
        return []

    return data

def run_script(script_name, args):
    """Import and run a script from scripts/"""
    try:
        module = importlib.import_module(f"scripts.{script_name}")
    except ModuleNotFoundError:
        return f"[Error] Script '{script_name}' not found."

    if not hasattr(module, "main"):
        return f"[Error] Script '{script_name}' has no main() function."

    try:
        result = module.main(args)
        return result
    except Exception as e:
        return f"[Error while running {script_name}: {e}]"

def print_script_block(script_name, args, result):
    """Format the output for each script"""

    # ANSI color codes
    CYAN_BOLD = "\033[96;1m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    args_str = ", ".join([f"{k}={v}" for k, v in args.items()])

    print(f"{CYAN_BOLD}{script_name}{RESET}")   # colored script name
    print(f"Args: {args_str}")
    print(f"Ans: {GREEN}{result}{RESET}")       # colored result only
    print("─────────────────────────\n")



def main():
    print("Watching input.yaml for changes... (Ctrl+C to stop)")
    last_mtime = None

    while True:
        try:
            if os.path.exists(INPUT_FILE):
                mtime = os.path.getmtime(INPUT_FILE)
                if last_mtime is None or mtime != last_mtime:
                    last_mtime = mtime
                    os.system("clear")  # refresh screen
                    print("========== Run ==========")
                    scripts = read_input()
                    for script in scripts:
                        script_name = script.get("name")
                        args = script.get("args", {})
                        result = run_script(script_name, args)
                        print_script_block(script_name, args, result)
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nStopped mathRunner.")
            break

if __name__ == "__main__":
    main()
