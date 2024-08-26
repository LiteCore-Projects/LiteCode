# LiteCode Programming Language Functions

## Core Functions

### `print`, `echo`, `write`
- **Description:** Prints text to the terminal.
- **Syntax:** `print <text>`
- **Example:** `print Hello World!`
- **Color Usage:** `print <red blue>Red text on blue background`

### `insert`
- **Description:** Inserts text at a specific terminal coordinate.
- **Syntax:** `insert <x> <y> <text>`
- **Example:** `insert 10 5 Hello`
- **Color Usage:** `insert 10 5 <green>Green text`

### `run`
- **Description:** Runs another LiteCode script.
- **Syntax:** `run <filename>`
- **Example:** `run script.lc`

### `wait`
- **Description:** Pauses execution for a specified number of seconds.
- **Syntax:** `wait <seconds>`
- **Example:** `wait 5`

### `set`
- **Description:** Sets a variable's value.
- **Syntax:** `set <variable>=<value>`
- **Example:** `set myVar=10`

### `if`
- **Description:** Conditional execution of code.
- **Syntax:** `if <condition>`
- **Example:** `if $myVar == 10`

### `math`
- **Description:** Performs a mathematical operation and stores the result.
- **Syntax:** `math <expression>`
- **Example:** `math $myVar + 5`

### `size`
- **Description:** Sets the terminal size.
- **Syntax:** `size <columns> <lines>`
- **Example:** `size 80 24`

### `input`
- **Description:** Prompts for user input and stores it in a variable.
- **Syntax:** `input <prompt>`
- **Example:** `input Enter your name:`

### `split`
- **Description:** Splits a variable by spaces and stores the parts in sequential variables.
- **Syntax:** `split <variable>`
- **Example:** `split $myVar`

### `clear`, `cls`
- **Description:** Clears the terminal screen.
- **Syntax:** `clear`

### `cd`
- **Description:** Changes the current directory.
- **Syntax:** `cd <target_folder>`
- **Example:** `cd /path/to/folder`

### `loop`
- **Description:** Enables or disables looping of the script.
- **Syntax:** `loop <true|false>`
- **Example:** `loop true`

### `exit`
- **Description:** Exits the script.
- **Syntax:** `exit`

### `random`
- **Description:** Generates a random number within a specified range and stores it in a variable.
- **Syntax:** `random <min> <max>`
- **Example:** `random 1 100`

### `delete`
- **Description:** Deletes a specified file.
- **Syntax:** `delete <filename>`
- **Example:** `delete temp.txt`

### `download`
- **Description:** Downloads a file from a URL.
- **Syntax:** `download <url> <target_path>`
- **Example:** `download http://example.com/file.txt file.txt`

### `read`
- **Description:** Reads a specific line from a file.
- **Syntax:** `read <filename> <line_number>`
- **Example:** `read myfile.txt 5`

### `edit`
- **Description:** Edits a specific line in a file.
- **Syntax:** `edit <filename> <line_number> <new_text>`
- **Example:** `edit myfile.txt 3 New content`

### `del`
- **Description:** Deletes a specific line from a file.
- **Syntax:** `del <filename> <line_number>`
- **Example:** `del myfile.txt 2`

### `dir`
- **Description:** Lists the contents of a directory.
- **Syntax:** `dir <directory_path>`
- **Example:** `dir /path/to/folder`

### `send`
- **Description:** Sends a file to a cloud database.
- **Syntax:** `send <filename> <cloud_directory>`
- **Example:** `send myfile.txt cloud_folder`

### `get`
- **Description:** Retrieves data from a cloud database and saves it to a file.
- **Syntax:** `get <filename>`
- **Example:** `get myfile.txt`

### `list`
- **Description:** Lists data from the cloud database.
- **Syntax:** `list`
