# Python Scripts Runner

A dynamic Python script execution system that watches for changes in `input.txt` and automatically runs scripts from the `scripts/` directory.

## How it Works

1. **mathRunner.py** monitors `input.txt` for changes
2. When the file is modified, it reads the first line as the script name
3. Remaining lines are passed as arguments to the script's `main()` function
4. Scripts are dynamically imported from the `scripts/` directory

## Usage

1. Run the watcher:
   ```bash
   python3 mathRunner.py
   ```

2. Edit `input.txt` with your desired script and arguments:
   ```
   script_name
   arg1
   arg2
   ```

3. The script will automatically execute when you save the file

## Available Scripts

- **hex_to_bin**: Converts hexadecimal numbers to binary
  ```
  hex_to_bin
  FF
  ```
