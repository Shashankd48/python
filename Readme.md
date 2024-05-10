# Change enviroment in python 

Certainly! Here's how you can structure the README file to include the steps for setting up a virtual environment and installing packages for the project only:

---

# Project Name

## Description

[Provide a brief description of your project here.]

## Installation

### Prerequisites

- Python 3.x

### Setting Up a Virtual Environment

1. Open your terminal or command prompt.
2. Navigate to your project directory using the `cd` command:

   ```
   cd path/to/your/project
   ```

3. Create a virtual environment by running the following command:

   ```
   python -m venv venv
   ```

   Replace `venv` with the desired name for your virtual environment.

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```
     source venv/bin/activate
     ```

   You should see `(venv)` appear at the beginning of your terminal prompt, indicating that the virtual environment is active.

### Installing Packages for the Project Only

5. With the virtual environment activated, you can now install packages specific to your project using pip. For example:

   ```
   pip install <package_name>
   ```

   Replace `<package_name>` with the name of the package you want to install.

### Deactivating the Virtual Environment (Optional)

6. When you're done working on your project, you can deactivate the virtual environment by running:

   ```
   deactivate
   ```

   This will return you to the system's default Python environment.

---

Feel free to customize the README file further with additional sections or information relevant to your project.