# T1W8 Saturday

# Virtual Environments
- They help create isolated environments for your projects, ensuring each project has its own dependancies

# Testing
- Allows us to confirm whether the application works as intended or not.
- Helps catch bugs early and ensure that your code behaves smoothly.

## Types of Testing
- Manual vs Automated
    - Manual: When a person manually performs tasks, cased on events
    - Automated: Programmed tests, also called scripts, to automatically perform tasks without human envolvement.

- Unit testing: Testing specific componenets/functions/methods
- Integration testing: Testing the compaibility with other modules/packages.
- Chaos testing: Making a program break on purpose by disabling a function or feature to see how errors are handled.
- Stress testing: Testing in high value of data/inputs (depending on use-case)
- End to end / Acceptance testing: Testing done towards the end of the project, when its almost complete, to ensure things work effectively.

Note: Great idea to organise your directory structure for maintenance and easy access.

## pytest
- Power and user-friendly testing framework
- Simple yet powerful.
- pytest follows the principle of 'assert'-ing that things are true in order for a test to pass.
- For a test to pass, the assert value must be true.

- Reading test output: '.' means pass , 'F' means failed , 'E' means exceptions

### Exceptions
- Used to check what happens when things go wrong.
- How your program is handled when things go wrong.

### Parameterized tests
- Might want to test the same function with multiple inputs
- Parameterize creates different test case for all the inputs provided.
- Make sure you initialize the packages to use them in other folders.

### Fixtures
- Arrange and prepare data before running tests.
- Reusable code.
- Fixture Scopes: function, class, module, package, session (when to destory the fixture)

# File Handling
- Read and write data from and to files
- Operations:
    - Open
    - Read
    - Write
    - Close (Why close? Ensures buffers are flused and resources are freed)
- 'with' statement: automatically closes file when you're done.

## Different file types
- CSV file
- JSON file

# Demo: Terminal App
- Application that manages and analyzes Euro Cup Match Data. The features:
    - Load match data from a JSON file.
    - Display all match data.
    - Add a new match.
    - Calculate and display total goals scored.
    - Filter and display high-scoring matches.
    - Error handling for user input and file operations.

- To make a .sh file an executable, run this command: chmod +x run.sh