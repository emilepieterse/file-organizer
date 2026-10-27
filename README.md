# File Organizer

A Python script that sorts files in a folder into subfolders based on file type (Images, Documents, Videos, Audio, Archives, Other).

## How it works

Point it at a folder and it moves every file in that folder (not subfolders) into a category folder based on its extension. New category folders are created automatically if they don't exist. If a file with the same name already exists at the destination, it adds `(1)`, `(2)`, etc. instead of overwriting it.

## How to run

```
python organize.py <folder_path>
```

Use `--dry-run` to see what would move without actually moving anything:

```
python organize.py <folder_path> --dry-run
```

Example:

```
python organize.py sample_folder
```

See `sample_output.txt` for example output, and `sample_folder/` for the result of running it.

## Tech used

- Python 3 (standard library only, no dependencies)
