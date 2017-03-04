import textwrap

def main():

    long_string = "For Windows users, the examples in this guide assume that the option to adjust the system PATH environment variable was selected when installing Python."
    wrapped_lines = textwrap.wrap(long_string)

    for line in wrapped_lines:
        print line

    print "\n=================\n"
    print textwrap.fill(long_string)
    print textwrap.dedent(long_string)




if (__name__=="__main__"):
    main()
