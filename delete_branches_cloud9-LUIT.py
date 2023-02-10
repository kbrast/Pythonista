# Deletes old branches in AWS Cloud9

import subprocess

stdout = subprocess.check_output('git branch -a'.split())

out = stdout.decode()

branches = [b.strip('* ') for b in out.splitlines()]

print(branches)

current_branch = subprocess.check_output('git rev-parse --abbrev-ref HEAD'.split())

current_branch = [b.strip('* ') for b in current_branch.decode().splitlines()][0]

for branch in branches:
    if(branch != 'main' and 'remotes/' not in branch and current_branch not in branch):
        print(branch)
        delete_out = subprocess.check_output(('git branch -d ' + branch).split())
        delete_out = [b.strip('* ') for b in delete_out.decode().splitlines()][0]
        print(delete_out)
    # TODO : Complete Remove Remotes
    #elif(branch != 'main' and current_branch not in branch and '/HEAD' not in branch):
    #    print(branch)
    #    delete_out = subprocess.check_output(('git push -d origin ' + branch.split('/')[-1]).split())
    #    delete_out = [b.strip('* ') for b in delete_out.decode().splitlines()][0]
    #    print(delete_out)
