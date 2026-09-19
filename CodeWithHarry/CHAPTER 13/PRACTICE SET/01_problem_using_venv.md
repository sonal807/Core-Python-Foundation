# Creating a Similar Virtual Environment Using `venv`

## 📌 Question

**Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?**

---

## 🎯 Objective

Create two virtual environments using Python's built-in `venv` module.

Install some packages in the first environment, save their names and versions in a `requirements.txt` file, and then use that file to install the same packages in the second environment.

---

# 🔹 Step 1: Create Two Virtual Environments

First, create two virtual environments:

```powershell
python -m venv env1
python -m venv env2
```

### What does this do?

The command:

```powershell
python -m venv env1
```

creates a virtual environment named `env1`.

Similarly:

```powershell
python -m venv env2
```

creates another virtual environment named `env2`.

The two environments are separate from each other.

---

# 🔹 Step 2: Activate the First Environment

On Windows PowerShell:

```powershell
.\env1\Scripts\Activate.ps1
```

After activation, the terminal will show something similar to:

```text
(env1) PS C:\Your\Project>
```

This means that commands such as `python` and `pip` are now working inside `env1`.

---

# 🔹 Step 3: Install Packages in the First Environment

Install a few packages:

```powershell
pip install numpy pandas requests
```

These packages will be installed inside `env1`.

They will not automatically be installed in `env2`.

---

# 🔹 Step 4: Check the Installed Packages

We can check the packages using:

```powershell
pip list
```

Or:

```powershell
pip freeze
```

`pip freeze` displays the installed packages along with their versions.

Example:

```text
numpy==...
pandas==...
requests==...
```

---

# 🔹 Step 5: Create `requirements.txt`

Now save the installed packages and their versions:

```powershell
pip freeze > requirements.txt
```

### What does this command mean?

```text
pip freeze
```

generates a list of installed packages and their versions.

```text
>
```

redirects the output into a file.

```text
requirements.txt
```

is the file where the package information is stored.

So:

```powershell
pip freeze > requirements.txt
```

means:

> Save the installed packages and their versions into `requirements.txt`.

---

# 📄 Example `requirements.txt`

It may look similar to:

```text
numpy==2.x.x
pandas==2.x.x
requests==2.x.x
```

The exact versions depend on the versions installed in your environment.

---

# 🔹 Step 6: Deactivate the First Environment

After saving the dependencies, deactivate `env1`:

```powershell
deactivate
```

The `(env1)` indicator will disappear from the terminal.

---

# 🔹 Step 7: Activate the Second Environment

Now activate `env2`:

```powershell
.\env2\Scripts\Activate.ps1
```

The terminal should now show:

```text
(env2) PS C:\Your\Project>
```

This confirms that the second environment is active.

---

# 🔹 Step 8: Install Packages from `requirements.txt`

Now install the packages recorded from `env1`:

```powershell
pip install -r requirements.txt
```

### What does `-r` mean?

`-r` tells `pip` to read the package requirements from the specified file.

So:

```powershell
pip install -r requirements.txt
```

means:

> Read `requirements.txt` and install the packages listed inside it.

---

# 🔹 Step 9: Verify the Second Environment

Check the installed packages:

```powershell
pip freeze
```

The second environment should now contain the same package names and versions that were recorded from the first environment.

---

# 🔄 Complete Workflow

```text
Create env1
     ↓
Activate env1
     ↓
Install packages
     ↓
pip freeze > requirements.txt
     ↓
Deactivate env1
     ↓
Activate env2
     ↓
pip install -r requirements.txt
     ↓
Same package dependencies
```

---

# 💻 Complete Commands

```powershell
python -m venv env1
python -m venv env2

.\env1\Scripts\Activate.ps1

pip install numpy pandas requests

pip freeze > requirements.txt

deactivate

.\env2\Scripts\Activate.ps1

pip install -r requirements.txt

pip freeze
```

---

# 📌 Key Commands

| Command | Purpose |
|---|---|
| `python -m venv env1` | Create a virtual environment |
| `python -m venv env2` | Create another virtual environment |
| `.\env1\Scripts\Activate.ps1` | Activate `env1` |
| `pip install package_name` | Install a package |
| `pip list` | Display installed packages |
| `pip freeze` | Display packages with versions |
| `pip freeze > requirements.txt` | Save dependencies to a file |
| `deactivate` | Exit the virtual environment |
| `pip install -r requirements.txt` | Install dependencies from the file |

---

# 🧠 Why Does This Work?

The first environment contains:

```text
env1
 │
 ├── numpy
 ├── pandas
 └── requests
```

We use:

```powershell
pip freeze > requirements.txt
```

to create a record of these dependencies.

Then:

```text
requirements.txt
        ↓
      env2
```

and:

```powershell
pip install -r requirements.txt
```

installs those recorded dependencies into `env2`.

---

# ⚠️ Important Note

This process reproduces the **Python package dependencies and their specified versions**.

It does not guarantee that every aspect of two environments is identical.

For example, the following can still differ:

```text
Python version
Operating system
System-level dependencies
Hardware
Environment-specific configuration
```

For this practice question, the main goal is to reproduce the installed Python packages.

---

# 🤖 AI Engineer Relevance

This workflow is important in AI/ML projects because different projects may require specific versions of packages such as:

```text
NumPy
Pandas
Scikit-learn
PyTorch
Transformers
FastAPI
```

For example:

```text
AI Project
    ↓
requirements.txt
    ↓
Another Computer
    ↓
pip install -r requirements.txt
```

This makes it easier to reproduce a project's Python dependencies.

---

# 🎯 Interview / Exam Answer

To create a similar environment, first save the installed packages and their versions from the first environment:

```powershell
pip freeze > requirements.txt
```

Then activate the second virtual environment and install the packages using:

```powershell
pip install -r requirements.txt
```

This reproduces the Python package dependencies recorded from the first environment in the second environment.

---

# 📝 Key Takeaway

```text
pip freeze
      ↓
requirements.txt
      ↓
pip install -r requirements.txt
      ↓
Recreate package dependencies
```