import os, sys
import pathlib

def os_directory():
    # https://linuxize.com/post/python-get-change-current-working-directory/
    current_working_directory = os.getcwd()
    current_file_path = os.path.abspath(__file__)

    current_file_directory_fake = os.path.join(current_file_path, os.pardir)
    current_file_directory = os.path.realpath(current_file_directory_fake)
    current_file_directory2 = sys.path[0]
    current_file_directory3 = os.path.dirname(current_file_path)

    print(current_working_directory)
    print(current_file_path)
    print(current_file_directory)
    print(current_file_directory2)
    print(current_file_directory3)
# os_directory()

def pathlib_study():
    # https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
    # https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath
    current_file_path = pathlib.Path(__file__)
    parent_path = pathlib.Path(__file__).parent.absolute()
    current_working_directory = pathlib.Path().absolute()
    current_working_directory2 = pathlib.Path().cwd()
    join_path_test = current_working_directory.joinpath('cryptography')
    print(__file__)
    print(current_file_path)
    print(current_file_path.name)
    print(parent_path, type(parent_path), sep='\t')
    print(current_working_directory)
    print(current_working_directory2)
    print(join_path_test)
pathlib_study()
