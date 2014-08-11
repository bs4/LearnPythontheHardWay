from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

finally:
    txt.close()


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

finally:
    txt.close() 

# The two halves of the script will run independently of eachother

# It might be better to use raw_input to get the filename because you can ask the user a pointed question of what they want to input, instead of hoping they enter the proper argument in the command line