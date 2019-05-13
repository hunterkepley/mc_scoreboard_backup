from shutil import copyfile
import subprocess
import os

def main():
    print("COPYIN THAT SCOREBOARD OVER INTO THE SERVER LUIGUS")
    try:
        copyfile("scoreboard_backup/scoreboard.dat.bak", "data/scoreboard.dat")
    except:
        try:
            os.mkdir('scoreboard_backup')
        except FileExistsError:
            print("scoreboard_backup directory exists in location 'scoreboard_backup")
        print("Scoreboard file not found.")

    print("Starting server in 3 seconds")
    subprocess.call([r'../bro just start the server with this are you dumb.bat'])


if __name__ == "__main__":
    main()