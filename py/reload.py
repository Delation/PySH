def reload(*args):
    if not 'administrator' in account.flags:
        raise Exception('insufficient permissions')
    import io
    commands = {}

    i = []
    for (path, dirs, files) in os.walk(bin):
        i.extend(files)
        break
    i = [ i[:-3] for i in i if i.endswith('.py') ]
    for var in globals():
        if var in i:
            with io.open(bin + var + '.py','r') as file:
                exec(file.read(), globals(), None)
    return 'Reloaded from file'
