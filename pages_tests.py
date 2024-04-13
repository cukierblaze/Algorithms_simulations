import sys

# Save the standard output to a variable
original_stdout = sys.stdout

# Open a file in write mode to save the output
with open('pages.txt', 'w') as w:
    # Redirect the standard output to the file
    sys.stdout = w
    from frame_generator import Frame_Generator
    Frame_Generator.frame_generator(1, 10, 20)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(2, 10, 20)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(3, 10, 20)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(4, 10, 20)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(5, 10, 20)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(5, 10, 1000)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(5, 10, 500)
    print("\n---------------------------------------------------------------\n")
    Frame_Generator.frame_generator(5, 100, 1000)



