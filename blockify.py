from block_data import *
import json
import io
import os
import argparse

def get_project_ids(arguments):
    """Given input arguments, return a set of all the project IDs."""
    projects = list()
    if arguments.project is not None:
        projects = arguments.project
    return set(projects)

def blockify(jsonfiles, output_directory=os.getcwd(), file_name=None):
    for jsonfile in jsonfiles:
        block_dict = {}
        block_list = []
        with open(jsonfile +'.json') as f:
            data = json.load(f)
        all_blocks = data["targets"]
        for target in all_blocks:
            if target["isStage"] == False:
                for block in target["blocks"]:
                    for names in blocknames:
                        value = names["name"]
                        if target["blocks"][block]["opcode"] == value:
                            if names["label"] not in block_dict.keys():
                                block_list.append(names["label"])
                                block_dict[names["label"]] = 1
                            else:
                                block_dict[names["label"]] += 1       
    return block_list, block_dict      

def get_arguments():
    parser = argparse.ArgumentParser(description="List blocks in Scratch project.")

    # Arguments related to input
    inputs = parser.add_mutually_exclusive_group(required=True)
    #inputs.add_argument("-s", dest="studio", nargs="*", help="Studio ID. Will scrape all projects from the studio with the given ID.")
    inputs.add_argument("-p", dest="project", nargs="*", help="Project ID. Will list blocks for one project for each ID provided.")
    #inputs.add_argument("-f", dest="studio_list", nargs="*", help="File name for a line-separated list of studio URLs (or IDs). Will scrape all projects in all studios.")
    #inputs.add_argument("-g", dest="project_list", nargs="*", help="File name for a line-separated list of project URLs (or IDs). Will scrape all projects.")

    # Arguments related to output
    parser.add_argument("-d", dest="output_directory", help="Output directory. Will save output to this directory, and create the directory if doesn’t exist.")
    parser.add_argument("-n", dest="output_name", help="Name of the output JSON file, if only a single output file is desired. Otherwise, will save projects to individual JSON files.")

    return parser.parse_args()

def main():
    arguments = get_arguments()
    projects = get_project_ids(arguments)
    if arguments.output_directory is None:
        blockify(projects, file_name=arguments.output_name)
    else:
        blockify(projects, output_directory=arguments.output_directory, file_name=arguments.output_name)


if __name__ == "__main__":
    main()