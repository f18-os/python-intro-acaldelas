#! usr/bin/env python3
######################
#Alan Caldelas
#9-16-19
#Shell lab
######################

import os, sys, time, re

pid = os.getpid()


def cmd_pipe(cmd):
    pid = os.getpid()

    pr,pw = os.pipe()

    for f in (pr, pw):
        os.set_inheritable(f, True)
    print(f"pipe fds: pr={pr}, pw={pw}")

    import fileinput

    rc = os.fork()

    if rc < 0:
        print("for failed, returning %d\n"% rc, file=sys.stderr)
        sys.exit(1)
    elif rc ==0:
        print("Child: My pid=%d. Parent's pid=%d" % (os.getpid(),pid), file=sys.stderr)
        args =[cmd[0]]
        cmd_1(args)
        args = [cmd[2]]
        os.close(1)
        os.dup(pw)
        for fd in (pr, pw):
            os.close(fd)
    else:
        print("Parent: %d. Child pid=%d" %(os.getpid(),rc), file= sys.stderr)
      #  cmd_1(args2)
        os.close(0)
        os.dup(pr)
        
        for fd in (pw,pr):
            os.close(fd)
        for line in fileinput.input():
            print("From child: %s" % line)



        
def cmd_2(cmd):
    print("Hello we gotta do some redirecting here...")
    rc = os.fork()
    if rc < 0:
        os.write(2,("Fork failed, returning %d\n" %rc).encode())
        sys.exit(1)
    elif rc == 0:
        args = cmd
        args.remove('>')
        os.close(1)
        sys.stdout = open(args[2], "w")
        os.set_inheritable(1, True)
        for dir in re.split(":", os.environ['PATH']):
            program ="%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                pass
        os.write(2, ("Child: Error: could not exec %s\n" % args[0]).encode())
        sys.exit(1)
    else:
        os.write(1,("Parrent: pid = $%d. Child pid = %d\n" % (pid,rc)).encode())
        childPid = os.wait()
        os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPid).encode())
    
#No redirect just a simple command
def cmd_1(cmd):
    rc = os.fork()
    if rc < 0:
        os.write(2,("Fork failed, returning %d\n" %rc).encode())
        sys.exit(1)
    elif rc ==0:
        args = cmd
        for dir in re.split(":", os.environ['PATH']):
            
            program = "%s/%s" % (dir, args[0])
            os.write(1, ("Child: ... Trying to exec %s\n" %program).encode())
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                pass
        os.write(2,("\nChild: Could not exec %s\n" %args[0]).encode())
        os.close(1)
        sys.exit(1)
    else:
        os.write(1,("Parent: pid = $%d. Child pid = %d\n" % (pid,rc)).encode())
        childPid = os.wait()
        os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPid).encode())
def change_dir(command):
    try:
        os.chdir(command)
    except EOFError:
        print("Invalid path")
while(True):
    print(pid)
    try:
        prompt = input("$ ")
    except EOFError:
        print("\n")
        exit()
    cmd_arr = prompt.split()
    print(f"You entered:{cmd_arr}, {len(cmd_arr)}")
    if cmd_arr[0] == "exit" :
        exit()
    elif '>' in cmd_arr:
        cmd_2(cmd_arr)
        os.wait()
    elif '|' in cmd_arr:
        cmd_pipe(cmd_arr)
        pass
    elif 'cd' in cmd_arr:
        change_dir(cmd_arr[1])
    else:
        print("Entering command one")
        cmd_1(cmd_arr)
    
