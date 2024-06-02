import subprocess

# 要执行的 Bash 命令
bash_command = "ls"

# 使用 subprocess.run() 函数执行 Bash 命令
result = subprocess.run(bash_command, 
                        shell=True, 
                        check=True, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
