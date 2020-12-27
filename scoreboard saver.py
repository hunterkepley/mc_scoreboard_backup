from shutil import copyfile
import os
import time

def main():
    print("COPYIN THE SCOREBOARD OVER INTO THE SERVER")
    try:
        copyfile("scoreboard_backup/scoreboard.dat.bak", "data/scoreboard.dat")
    except:
        try:
            os.mkdir('scoreboard_backup')
        except FileExistsError:
            print("scoreboard_backup directory exists in location 'scoreboard_backup")
        print("Scoreboard file not found.")

    print("This will take a minute to update")

    while(True):
        print("Backing up the scoreboard")
        try:
            copyfile("data/scoreboard.dat", "scoreboard_backup/scoreboard.dat.bak")
        except:
            try:
                os.mkdir('scoreboard_backup')
                copyfile("data/scoreboard.dat", "scoreboard_backup/scoreboard.dat.bak")
            except FileExistsError:
                print("scoreboard_backup directory exists in location 'scoreboard_backup")
            copyfile("data/scoreboard.dat", "scoreboard_backup/scoreboard.dat.bak")
        
        time.sleep(300)

if __name__ == "__main__":
    main()
