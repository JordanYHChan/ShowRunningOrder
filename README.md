# ShowRunningOrder

## Project Description
This **Dance Show Management System** is a Python-based tool designed to help dance show organizers efficiently schedule and sequence dance performances. It calculates an optimal running order based on dancer availability, dance styles, and other customizable factors, minimizing overlap and conflicts between consecutive performances.

## Features
- Load dance details from a text file, including dance names, dancers, and styles.
- Generate an optimal running order that reduces conflicts between shared dancers and repeated styles.
- Customizable conflict resolution: consider common dancers, common styles, or both.
- Add an intermission or manually set dance positions.
- Easily save and load shows with input/output functions.

## Installation
To install the programme, first clone the github repository to your local device with:
```bash
$ git clone git@github.com:JordanYHChan/ShowRunningOrder.git
```

Then go into the cloned local github repository (which should be named ShowRunningOrder) and create a new conda environment with python 3.10 and pip installed:
```bash
$ cd ShowRunningOrder
$ conda create -n ShowRunningOrder python=3.10 pip
```

Now, go into and update the conda environment and with the requirements.txt:
```bash
$ conda activate ShowRunningOrder
$ pip install -r requirements.txt
```

You should now be in the cloned github repository with a working conda environment.

### Version Control
In order to use appropriate version control best practice and commit hooks to protect the main branch, please run the command:
```bash
$ pre-commit install
```

## Usage

To use this script, follow the steps below:

### 1. Command-line Arguments
You can provide the input and output file locations either as command-line arguments or through user input prompts.

#### Option 1: Command-line Usage
Run the script with the following command, providing the file paths as arguments:

```bash
python script.py <input_file> <output_file>
```

- `<input_file>`: The path to the file containing information about the dances.
- `<output_file>`: The path where the ordered dance show information will be saved.

For example:
```bash
python script.py input/sample_input.txt output/sample_output.txt
```

#### Option 2: Interactive Mode
If no command-line arguments are provided, the script will prompt you to enter the input and output file locations.

### 2. Input File Format
The input file should contain details about the dance names, the number of dancers for each dance, and their respective dance styles. This information will be processed and used to create the dance show.

A sample input file is shown below:

```txt
Ballet, Contemporary, Modern Ballet, Tap
Alice, Bob, Charlie
David, Eve, Frank
Alice, Grace, Hannah
Bob, Charlie, Ivy
Ballet, Contemporary, Ballet, Tap
```

The first line lists all the dance names separated by commas. The following lines list the names of the dancers for each dance separated by commas, in the same order as the first line. The final line should list all the styles of each dance in the same order as the first line.

### 3. User Prompts
After reading the input file, the script will ask you the following questions:

1. **Add an Intermission**:
   - You'll be prompted to add an intermission in the show (`yes` or `no`).

2. **Position Specific Dances**:
   - You can specify the position of any dance by entering the dance name and its desired position (e.g., `first`, `last`, `before intermission`, `after intermission`, or a specific number).
   - Type `done` when finished positioning dances.

3. **Order Considerations**:
   - The script will ask whether to consider **common dancers** and **common dance styles** when ordering the dances. Answer `yes` or `no` to these prompts.

### 4. Output
Once the dance order has been finalized, the program will save the ordered dance show to the specified output file.

The output file will contain:
- The running order of the dances.
- Details on any intermission and the final arrangement considering common dancers and styles.

### Example Interaction

```bash
$ python script.py
Enter the input file location: input/sample_input.txt
Enter the output file location: output/sample_output.txt
Do you want to add an intermission (yes/no)? yes
Enter the dance name to position (or 'done'): Ballet
Enter the position to place the dance: first
Enter the dance name to position (or 'done'): done
Consider common dancers (yes/no)? yes
Consider common styles (yes/no)? no
```

The final dance order will be saved in the `output/sample_output.txt` file as:

```txt
Ballet, Contemporary, Modern Ballet, Tap
```

## Documentation
To read the documentation of the code, Doxygen is utilised inside the docs folder, where running the command:
```bash
$ cd docs
$ doxygen
```
will auto-generate html and latex documentation of the code.

## Authors and acknowledgment
Written by J. Y. H. Chan.

## License
The code is licensed under the MIT License.
