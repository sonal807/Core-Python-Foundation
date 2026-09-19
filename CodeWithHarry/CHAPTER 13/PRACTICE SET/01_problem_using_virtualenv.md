# Creating a Virtual Environment Using `virtualenv`

## 📌 Question

**Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?**

---

## 🎯 Objective

Learn how to create Python virtual environments using the third-party `virtualenv` package.

Then install packages in the first environment and use `requirements.txt` to reproduce those package dependencies in another environment.

---

# 🔹 Step 1: Install `virtualenv`

`virtualenv` is a third-party Python package used to create isolated Python environments.

Install it using:

```powershell
pip install virtualenv
```

### Important

Unlike `venv`, which is included with modern Python installations, `virtualenv` must be installed separately.

---

# 🔹 Step 2: Create the First Virtual Environment

Create the first environment:

```powershell
virtualenv env1
```

This creates a virtual environment named:

```text
env1
```

---

# 🔹 Step 3: Create the Second Virtual Environment

Create another environment:

```powershell
virtualenv env2
```

Now we have:

```text
env1
env2
```

These are two separate virtual environments.

---

# 🔹 Step 4: Activate the First Environment

On Windows PowerShell:

```powershell
.\env1\Scripts\Activate.ps1
```

After activation, the terminal will show something similar to:

```text
(env1) PS C:\Your\Project>
```

This indicates that `env1` is active.

---

# 🔹 Step 5: Install Packages in `env1`

Install a few packages:

```powershell
pip install numpy pandas requests
```

These packages are installed inside `env1`.

---

# 🔹 Step 6: Check Installed Packages

Use:

```powershell
pip freeze
```

This displays the installed packages along with their versions.

Example:

```text
numpy==...
pandas==...
requests==...
```

---

# 🔹 Step 7: Save Package Information

Save the installed packages and versions into a requirements file:

```powershell
pip freeze > requirements.txt
```

### What happens here?

```text
pip freeze
     ↓
Gets installed packages + versions
     ↓
>
Redirects output
     ↓
requirements.txt
     ↓
Stores dependency information
```

---

# 🔹 Step 8: Deactivate `env1`

After creating the requirements file:

```powershell
deactivate
```

This exits the first virtual environment.

---

# 🔹 Step 9: Activate `env2`

Activate the second environment:

```powershell
.\env2\Scripts\Activate.ps1
```

The terminal should now show:

```text
(env2) PS C:\Your\Project>
```

This confirms that `env2` is active.

---

# 🔹 Step 10: Install the Same Packages

Use the requirements file:

```powershell
pip install -r requirements.txt
```

This reads the packages and versions recorded in `requirements.txt` and installs them into `env2`.

---

# 🔹 Step 11: Verify the Installation

Run:

```powershell
pip freeze
```

The output should contain the same package dependencies and versions recorded from `env1`.

---

# 🔄 Complete Workflow

```text
Install virtualenv
        ↓
Create env1
        ↓
Create env2
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
pip install virtualenv

virtualenv env1
virtualenv env2

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
| `pip install virtualenv` | Install the `virtualenv` tool |
| `virtualenv env1` | Create `env1` |
| `virtualenv env2` | Create `env2` |
| `.\env1\Scripts\Activate.ps1` | Activate `env1` |
| `pip install package_name` | Install a package |
| `pip freeze` | Show installed packages and versions |
| `pip freeze > requirements.txt` | Save dependencies |
| `deactivate` | Exit the environment |
| `.\env2\Scripts\Activate.ps1` | Activate `env2` |
| `pip install -r requirements.txt` | Install dependencies from the file |

---

# 🆚 `venv` vs `virtualenv`

| Feature | `venv` | `virtualenv` |
|---|---|---|
| Type | Built-in Python module | Third-party package |
| Installation | No separate installation normally required | `pip install virtualenv` |
| Creation | `python -m venv env1` | `virtualenv env1` |
| Purpose | Create isolated environments | Create isolated environments |
| Common use | Standard Python projects | Alternative environment tool |

---

# 🧠 Main Difference

With `venv`:

```powershell
python -m venv env1
```

With `virtualenv`:

```powershell
virtualenv env1
```

The method of reproducing package dependencies remains the same:

```powershell
pip freeze > requirements.txt
```

then:

```powershell
pip install -r requirements.txt
```

So the important concept is not the environment-creation tool itself.

The important dependency-reproduction workflow is:

```text
Environment 1
      ↓
pip freeze
      ↓
requirements.txt
      ↓
Environment 2
      ↓
pip install -r requirements.txt
```

---

# ⚠️ Important Note

`virtualenv` and `venv` are tools for creating isolated environments.

`requirements.txt` is used to record and reproduce Python package dependencies.

Therefore, they solve different parts of the workflow:

```text
venv / virtualenv
        ↓
Create isolated environment

requirements.txt
        ↓
Record dependencies

pip install -r
        ↓
Install recorded dependencies
```

---

# 🤖 AI Engineer Relevance

AI/ML projects often depend on many external Python packages.

For example:

```text
NumPy
Pandas
Scikit-learn
PyTorch
Transformers
FastAPI
```

A project may require specific versions of these packages.

Using:

```powershell
pip freeze > requirements.txt
```

and:

```powershell
pip install -r requirements.txt
```

helps reproduce the project's Python dependencies.

This becomes especially useful when:

```text
Developing locally
       ↓
Sharing project
       ↓
Moving to another computer
       ↓
Deploying application
```

---

# 🎯 Interview / Exam Answer

`virtualenv` can be used to create isolated Python environments.

First install it:

```powershell
pip install virtualenv
```

Create and activate the first environment:

```powershell
virtualenv env1
.\env1\Scripts\Activate.ps1
```

Install packages and save their versions:

```powershell
pip install numpy pandas requests
pip freeze > requirements.txt
```

Then activate the second environment and install the same dependencies:

```powershell
.\env2\Scripts\Activate.ps1
pip install -r requirements.txt
```

This reproduces the Python package dependencies from the first environment in the second environment.

---

# 📝 Key Takeaway

```text
virtualenv
     ↓
Create isolated environment

pip freeze
     ↓
Save installed packages + versions

requirements.txt
     ↓
Dependency record

pip install -r requirements.txt
     ↓
Recreate dependencies in another environment
```