import importlib
import os
import time

INPUT_FILE = "input.txt"

def read_input():
    """Read script name and arguments from input.txt"""
    if not os.path.exists(INPUT_FILE):
        print("input.txt not found!")
        return None, []

    with open(INPUT_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("input.txt is empty!")
        return None, []

    script_name = lines[0]  # first line = script name
    args = lines[1:]        # rest = arguments
    return script_name, args

def run_script(script_name, args):
    """Dynamically import and run the script from scripts/"""
    try:
        module = importlib.import_module(f"scripts.{script_name}")
    except ModuleNotFoundError:
        print(f"Script '{script_name}' not found in scripts/")
        return

    if not hasattr(module, "main"):
        print(f"Script '{script_name}' does not have a main() function")
        return

    try:
        module.main(args)
    except Exception as e:
        print(f"Error while running {script_name}: {e}")

def main():
    print("Watching input.txt for changes... (Ctrl+C to stop)")
    last_mtime = None

    while True:
        try:
            if os.path.exists(INPUT_FILE):
                mtime = os.path.getmtime(INPUT_FILE)
                if last_mtime is None or mtime != last_mtime:
                    last_mtime = mtime
                    script_name, args = read_input()
                    if script_name:
                        print("\n--- Running script ---")
                        run_script(script_name, args)
                        print("--- Done ---\n")
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nStopped mathRunner.")
            break

if __name__ == "__main__":
    main()
