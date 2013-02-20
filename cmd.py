import sys
import time as t

locked = True
adminlocked = True
dat_users = open("data/users.dat", "a+")
users = []
for user in dat_users:
	userparts = user.split(",")
	users.append((userparts[0], userparts[1], int(userparts[2])))
    
currdir = ["#"]

def recursive():
    global locked, adminlocked
    cmdraw = raw_input("!> ")
    cmd = cmdraw.split()
    if len(cmd) == 0:
        pass
    elif cmd[0] == "LOGIN" or cmd[0] == "LGI":
        for user in users:
            if cmd[1] == user[0]:
                if cmd[2] == user[1]:
                    locked = False
                    print "Welcome,", user[0]
                    if user[2] == 1:
                        print "You are logged in as an administrator."
                        adminlocked = False
        if locked == True:
            print "Error: The username or password is incorrect."
    elif cmd[0] == "LOGOUT" or cmd[0] == "LGO":
        if locked:
            print "Error: You are not logged in."
        else:
            print "Goodbye."
            locked, adminlocked = True, True
    elif cmd[0] == "HELP":
        print """---Commands---
Format: COMMAND <mandatory_arg> [optional_arg] | COMMAND fixed_text [one_or_more_args]* - Description. Aliases: CMD
CD - Alias for CDIR
CDIR <dir> - Changes working directory to the called directory. If the called directory does not exist, creates it. Aliases: CD
CFG - Alias for CONFIG
CONFIG <value> [node]* - In progress.
D - Alias for DIR
DIR - Lists the current directory. Aliases: D
EXIT - Quits NRAOS. Aliases: QUIT
HELP [cmd] - Displays help docs. If called with a command, displays detailed command docs for that command.
LGI - Alias for LOGIN
LGO - Alias for LOGOUT
LOGIN <user> <pass> - Log in to the system. Aliases: LGI
LOGOUT - Log out of the system. Aliases: LGO
QUIT - Alias for EXIT
        """
    elif cmd[0] == "EXIT" or cmd[0] == "QUIT":
        sys.exit(0)
    elif cmd[0] == "DIR" or cmd[0] == "D":
        for dirpart in currdir:
            sys.stdout.write(dirpart + ">")
        print
    elif cmd[0] == "CDIR" or cmd[0] == "CD":
        if len(cmd) == 1:
            print "Error: Invalid syntax"
        elif cmd[1] == "<":
            currdir.pop()
        else:
            currdir.append(cmd[1])
    else:
        print "Error: Command not recognized."
    recursive()

print "NRaOS (NotReallyanOS) - v0.1"
recursive()
