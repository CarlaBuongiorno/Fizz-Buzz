def fizz_buzz(number):
    if number / 3:
        return 'Fizz'



'''
What is git init?
 - Initializing a repository.
Where is this happening?
 - On your local computer.
How do I know that I have run git init?
 - `ls -a` in your terminal will show .git
 - This means a repository has been initialized.
My project consists of a few folders:
- Documents/Python/python-2025/fizz-buzz
- Documents/Python/python-2025/conway-again
At which level of the project do I run git init?
 - For each separate project -> `fizz-buzz` and `conway-again`
At which level do I create the virtual environment?
 - Same as above -> for each separate project/repository.
Why is it important to be in the venv when it 
appears that everything works the same without it?
 - Each project will have specific libraries/modules that it uses,
   you don't want to add those to the entire machine. There would eventually be
   a very long list. Also, if someone wants to clone your repo,
   it's easier to see which dependencies need to be installed
   for that project. 

Setting up pytest...??? How?
`pip install pytest` or `sudo apt install python3-pytest` ??
 - `pip install pytest` installs it in my virtual environment - as long as venv is already activated
  - > if not in venv, `pip install pytest` will install it globally.
 - `sudo apt install python3-pytest` installs it globally on my machine - whether or not you're in your venv
 
Do I need to import pytest?
 - Not always: pytest is the name of a program that you run for tests, it is also the name of a module.
 - When you only use it to run test, import is not necessary.
When do I need to import pytest exactly?
 - When you use methods from the pytest module, then import pytest. (eg. pytest raises)

How do I run tests in the terminal?
 - `pytest`

How do I add repo to GitHub?
 - On GitHub -> `New`
                `Name your repo`
                `Follow bottom prompts to connect local and remote repo`

Do I need a token? When and Why?
 - New rule, you always need a token when you push from the terminal.


Tomorrow thing -> venv big pink banner
'''