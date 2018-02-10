#test python
msg = "Hello World"
#print(msg)

#OF COURSE, WITH SMALL CORRECTIONAL EDITS, TOO SPECIFIC TO CODE

#actor
def make_actor (file_name):
    with open(file_name) as fp:
        print("INSERT INTO Actor (name, website) values")        
        for line in fp:
            line = line.rstrip()
            name = line.split("with", 1)[0].strip()
            website = line.split("with", 1)[1].strip().rstrip('.')
            print("('" + name + "', " + "'" + website + "'),")

make_actor('actor.txt')