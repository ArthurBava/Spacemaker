import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="assets/space.ico") ]
cx_Freeze.setup(
    name = "Spacemaker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)
