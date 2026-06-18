from pathlib import Path

# List of directories
directories = [
    "data",
    "notebooks",
    "src",
    "api",
    "deployment",
    "config"
]

for directory in directories:
    path = Path(directory)

    if path.exists():
        print(f"Already exists: {directory}")
    else:
        path.mkdir(parents=True)
        print(f"Created: {directory}")

print("Done!")