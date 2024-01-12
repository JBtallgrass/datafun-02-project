import pathlib
from pathlib import Path

# Function to create a project directory
def create_project_directory(directory_name: str) -> None:
    """Creates a project directory.
    :param directory_name: Name of the directory to be created.
    """
    try:
        pathlib.Path(directory_name).mkdir(exist_ok=True)
        print(f"Directory '{directory_name}' created.")
    except Exception as e:
        print(f"Error creating directory '{directory_name}': {e}")

# Function to create annual data directories
def create_annual_data_directories(directory_name: str, start_year: int, end_year: int) -> None:
    """Creates annual data directories within a specified range.
    :param directory_name: Base name for the directories.
    :param start_year: Start year for the directory range.
    :param end_year: End year for the directory range.
    """
    base_path = Path(directory_name)
    for year in range(start_year, end_year + 1):
        year_path = base_path / str(year)
        try:
            year_path.mkdir(parents=True, exist_ok=True)
            print(f"Directory '{year_path}' created.")
        except Exception as e:
            print(f"Error creating directory '{year_path}': {e}")

# Function to create a file or directory based on file name
def create_file_or_directory(fname: str) -> None:
    """Creates a file or directory based on the provided file name.
    :param fname: Name of the file or directory to be created.
    """
    path = Path(fname)
    if '/' in fname or '\\' in fname:
        print("Detected a slash or backslash. Please use Path.joinpath() to combine paths.")
    else:
        try:
            if fname.endswith('.py') or fname.endswith('.md'):
                path.touch(exist_ok=True)
                print(f"File '{fname}' created.")
            else:
                path.mkdir(exist_ok=True)
                print(f"Directory '{fname}' created.")
        except Exception as e:
            print(f"Error creating '{fname}': {e}")

# Main function
def main():
    create_project_directory('JB_test')
    create_project_directory('JB_docs')
    create_annual_data_directories(directory_name='data', start_year=2000, end_year=2024)

# Create day folders
day_list = ["01-Mon", "02-Tue", "03-Wed", "04-Thu", "05-Fri", "06-Sat", "07-Sun"]
for day in day_list:
    folder_name = f"data-{day}"
    create_project_directory(folder_name)

if __name__ == '__main__':
    main()
