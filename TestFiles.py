def main():
    #open a file for writing or create if does not exist
    f=open("textfile.txt", "w+")
    #open a file to append text at the end

    #write lines of datainto a file
    for i in range(10):
        f.write("this is line "+str(i)+"\r\n")


    #close file when done
    f.close()

    #open file backup and read the file



main()