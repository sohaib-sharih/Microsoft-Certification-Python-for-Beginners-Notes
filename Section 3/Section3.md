<h1>Creating Packages Python</h1>
    <ol type="1">
        <li>Sometimes you have used python version and libraries of a different version that might conflict with the
            target machine, therefor you create an <i>environment that works in isolation.</i></li>
        <li>You will want to use libraries written by others to speed up the process of development. You might be using
            them in different files composed to build your program.</li>
        <li>When you want to use specific libraries and modules, and specific versions of them in your project, python
            can help you manage this by creating a <b>virtual environment.</b></li>
        <li>A virtual environment is a <b>self contained</b>copy of libraries that work in isolation just specific to
            your program/project files. That won't affect other programs.</li>
        <li>You can create a <i>virtual environment by calling the <b>venv module</b></i>, that helps you create folders
            for files to keep in. The cmd used for this is <b> python -m venv env</b></li>
        <li>You can keep all your program files inside <b>src folder</b>, the env folder allows python to keep track of
            the version of modules, libraries and python version you are using.</li>
        <li>You will have to <b>activate the env</b>, to do this use the command <i>activate.</i> By calling the
            activate script. <i>you will have to install <b>bash</b></i> </li>
        <li>
            <h3>How to activate using virtual environment? </h3>
            <br>
            <img src="/images/activate.PNG" alt="">
        </li>
        <ol type="a">
            <li>You will need to install Bash CLI or simply install Microsoft extension for Powershell, then run the
                command <b>.\env\Scripts\activate</b> on the root folder. <i>You don't have to mention the entire path,
                    it really depends which folder you are in, infact if you are in env\scripts folder, then you can
                    simply use the command <b>.\activate</b> to run the file.</i> </li>
            <li>enter cmd <b>deactivate</b> to revert to the normal <i>terminal prompt path</i> from <i>env path</i>.
            </li>
            <li>you can use the cmd <b>pip freeze</b> to check what packages are installed in the virtual environment.
            </li>
            
</ol>
        
</ol>
    <h1>Insalling a package</h1>
    <ol type="1">
        <li>To install a package created by other deveelopers to speed up the development process, use the command
            <b>pip</b> in the env directory</li>
        <li>Example: pip install python-dateutil</li>
        <li>This package is used for parsing the .yml file format</li>
        <li>You can find lots of other packages <a href="https://pypi.org/">here</a>. PIP is Python Package Index OR
            PyPi for short.</li>
        <li><b>pip freeze</b> shows you the installed packages in python. The reason why you will see more than 1
            package install is because datetime package itself uses another package that it needs to fetch. As shown
            below: <br>
            <img src="/images/01.PNG" alt="">
        </li>
        <li> To check if the packages only exist in the virtual environment, you need to use the command Deactivate. The
            <b>terminal prompt</b>will change from (env) to normal path on the terminal. And now when you run the
            command Pip Freeze, it will give you a longer list of dependencies install in the machine that is outside
            the environment.</li>
        
</ol>
    <h1>More ways to install a package</h1>
    <ol type="1">
        <li>You can run the command Python3 -m pip install</li>
        <li>you can see below other ways: <br>
            <img src="/images/02.PNG" alt="">
        </li>
        
</ol>
    <h1>To run a program using a package</h1>
    <ol>
        <li>You can import datetime package, the following way to run it: <br>
            <img src="/images/03.PNG" alt="">
        </li>
        <li>To run the program you can either use py format, python nameofFile.py command, or just use jypyter.</li>
       
</ol>

<h1>Working with Project Files: List</h1>
    <ol type="1">
        <li>You dont have to check through all the package files, instead just check the list of files. This takes up
            less space as compared to downloading/uploading all packages to github.</li>
        <li>To create a requirements.txt file for all the packages to be listed automaticalled, use the command <b>pip
                freeze > requirement.txt</b></li>
        <li>Create a <i>gitignore file</i></li>

</ol>

<h1>How to consume a project?</h1>
    <ol type="1">
        <li>First you need to fetch the files from github.</li>
        <li>Create a <b>virtual environment</b> and place yourself in it. by using the command .\activate, before you
            activate you need to run the command for <b>env</b> <i>python -m venv env</i></li>
        <li>Then you can run the command pip freeze > requirements.txt</li>
        <li></li>
    </ol>

<h1>Managing Dependencies</h1>
    <ol type="1">
        <li>Sometimes some packages may be outdated and new releases are available due to many reasons such as <i>bug
                fixes, security issues or new releases/features.</i> Therefore, its a good idea to keep your packages up
            to date.</li>
        <li>To install a specific version of a library you can use the following command: <b>pip install
                python-dateutil==1.4</b> enter the version number after the == sign.</li>
        <li>There are many ways to find out what versions are available. You can use the following command to check for
            available versions from the output of errors it gives:
            <br>
            <b>pip install python-dateutil==randomwords</b>
        </li>
        <li><b>Upgrade a package:</b> You can upgrade any package without mentioning the version by the following
            command: <br>
            <b>pip install 'packageName' --upgrade</b>
        </li>
        <li>Packaging uses something called <b>semantic versioning</b> Sometimes, you dont want to upgrade the entire
            package because your program is synced with the major arguments and methods that were defined previously. A
            semantic version is defined by 3 digits followed by dots notation.
            <ol type="a">
                <li> <b>Major change:</b> This means that the overall methods or variables or arguments may have
                    changed.</li>
                <li><b>Minor:</b> This indicates that there was an update in features or new features added.</li>
                <li><b>Patch: </b> this indicates that there is a patch intalled to fix a bug that existed before.</li>
            </ol>
        </li>
        <li>If you want to only upgrade your version by <i>Patches</i> you can use the following command: <br>
            <b>pip install "python-dateutil==2.7.*" --upgrade</b>
        </li>
        <li>You can uninstall a package using the following command: <b>pip uninstal python-dateutil</b></li>
        <li>Sometimes you want all packages and libraries to be uninstalled, you can use the command: <b>pip freeze >
                requirements.txt</b> to write all the packages installed, then <b>pip uninstall -r requirements.txt
                -y</b></li>
    </ol>
    <h1>Excercise: Create and Manage a project File</h1>
    <ol type="1">
        <li>Before you start, create a virtual environment using the following command:
            <br> <b>python -m venv env</b>
        </li>
        <li>To activate the virtual environment use the following command after entering the folder that has the scripts
            of activate. usually Scripts/activate, the command is <br>
            <b>.\activate</b> if you are a folder behind then example <b>.\scripts\activate</b>
        </li>
        <li>If you want to install <b>dependencies</b> that are available in the requirements.txt file, use the
            following command <br>
            <b>pip install -r requirements.txt</b>
        </li>
        <li>If the program files that you have fetched from a Github repo, then you can also create the requirements.txt
            file using the following steps:
            <ol type="a">
                <li>first create the virtual environment using <b>python -m venv env</b></li>
                <li>create a folder <b>md src</b></li>
                <li>createa a file using git bash OR new Microsoft Terminal extension of vscode: <b>touch app.py</b>
                </li>
                <li>create the requirements file <b>touch requirements.txt</b></li>
                <li>Create an <b>example</b> app.py file to test run the <b>date function</b> using the following code
                    <br>
                    from datetime import * <br>
                    from dateutil.relativedelta import *<br>
                    now = datetime.now() <br>
                    print(now) <br>
                    <br>
                    now = now + relativedelta(months=1, weeks=1, hour=10) <br>

                    print(now)
</li>
                <li>Manually add the following content in requirements.txt file <br>
                    python-dateutil==2.8.2 <br>
                    six==1.16.0</li>
                <li>To install the contents of <b>requirements.txt</b> use the following command:
                    <br> <b>pip install -r requirements.txt</b>
                </li>
            </ol>
        <li><b>How to UPGRADE the packages?</b>
            <ol type="a">
                <li>If you want to install a specific version of the package use the command <br>
                <b>pip install python-dateutil=2.4.4</b></li>
                <li>If you want to upgrade only the <b>package's patch version</b> run the following command <br>
                <b>pip install "python-dateutill=2.4.*" --upgrade</b></li>

</ol>
        </li>

</ol>
