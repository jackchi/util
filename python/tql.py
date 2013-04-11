#############################################################
#####            TQL : Thumbtack Query Language          ####
#############################################################
### Jack Chi github:jackchi
### SET [name] [value]: Set a variable [name] to the value [value]. Neither variable names or values will ever contain spaces.
### GET [name]: Print out the value stored under the variable [name]. Print NULL if that variable name hasn't been set.
### UNSET [name]: Unset the variable [name]
### NUMEQUALTO [value]: Return the number of variables equal to [value]. If no values are equal, this should output 0.
### END: Exit the program

### Transactional Commands
### BEGIN: Open a transactional block
### ROLLBACK: Rollback all of the commands from the most recent transaction block. If no transactional block is open, print out INVALID ROLLBACK
### COMMIT: Permanently store all of the operations from any presently open transactional blocks

DB = dict()
DBlist = []
begun = False   # Indicates whether or not we are in a transactional block
editCommands = ['END', 'SET', 'GET', 'UNSET', 'NUMEQUALTO']
transCommands = ['BEGIN', 'ROLLBACK', 'COMMIT', 'SHOW']  # test all of these at beginning
trans = False


def dbEdit(database, prompt):
    """
    dbEdit(database, prompt):
        (database) is the current working copy of the DB
        (prompt) is the lower-cased user command
    """

    global begun


    if cmd == 'SET':
        try:
            database[prompt[1]] = prompt[2]
            print database
        except:
            print 'invalid number of arguments for SET'
    elif cmd == 'GET':
        try:
            print database[prompt[1]]
        except:
            print 'NULL'
    elif cmd == 'UNSET':
        try:
            del database[prompt[1]]
            print database
        except:
            print "%s has not been assigned" % (prompt[1])
    elif cmd == 'NUMEQUALTO':
        counter = 0
        for X in database:
            if database[X] == prompt[1]:
                counter += 1
        print counter
    # return database

def dbTransact(cmd):
    """
    dbTransact(cmd): Transactional Block Helper Function
        (cmd) is the lower-cased user command
    """

    global begun, DB, DBlist

    if cmd == 'BEGIN':
        print "beginning transactional block"
        if begun:  # we are already in a transactional block
            # we have to use dict(DBlist) because if you implicitly set it with =, it copies its reference
            tDB = dict(DBlist[-1])
        else:
            begun = True
            tDB = dict(DB)
        # We append it twice to keep a copy of the previous working DB
        DBlist.append(tDB)
        DBlist.append(tDB)
    elif cmd == 'COMMIT':
        # in a Transactional Block
        if begun:
            DB = dict(DBlist[-1])
            DBlist = []
            begun = False
            print DB
        else:
            print "Nothing to COMMIT"
    elif cmd == 'ROLLBACK':
        try:
            if begun:
                #sanity check
                if len(DBlist) >= 2:
                    DBlist.pop()
                    DBlist.pop()
                    if len(DBlist) == 0:
                        begun = False
                        print DB
                    else:
                        print DBlist[-1]
            else:
                print "No BEGIN to ROLLBACK"
        except Exception, e:
            print 'ROLLBACK FAILED' + str(e)
    elif cmd == 'SHOW':
        print "The committed database: " , DB
        print "The queued database: " , DBlist

while True:

    # this allows prompt to have multiple whitespaces
    prompt = str(raw_input('> ')).split()
    cmd = prompt[0]
    cmd = cmd.upper()
    if cmd not in transCommands and cmd not in editCommands:
            print 'undefined command'
    elif cmd == 'END':
        break
    elif cmd in transCommands:
        dbTransact(cmd)
    elif cmd in editCommands:
        if begun:
            dbEdit(DBlist[-1], prompt)
        else:
            dbEdit(DB, prompt)

