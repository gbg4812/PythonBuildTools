import subprocess
import platform

print(
"""
\033[35m
  ___  ____   ___    ____  _  _    ____  ____  ____  _  _  ____ 
 / __)(  _ \ / __)  (  _ \( \/ )  / ___)(  __)(_  _)/ )( \(  _ \\
( (_ \ ) _ (( (_ \   ) __/ )  /   \___ \ ) _)   )(  ) \/ ( ) __/
 \___/(____/ \___/  (__)  (__/    (____/(____) (__) \____/(__)  

\033[0m

"""
)

if platform.system() == "Windows":
    proc = subprocess.Popen("powershell .\setup/setup.ps1", stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.wait()

    while True:
        line = proc.stdout.readline().decode()
        if not line:
            break
        else:
            print(line)


    while True:
        line = proc.stderr.readline().decode()
        if not line:
            break
        else:
            print("\033[91m" + line + "\033[0m")


    print("\033[92m" +

"""The environment has been created, if you want to start develouping you 
should activate the venv environment using the next command: 
        
.\\.venv/Scripts/activate
        
"""
    + "\033[0m"
    )

else:
    #pendent to set up
    pass
