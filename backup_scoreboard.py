from shutil import copyfile
import os
import time

def main():
    while(True):
        print("Backin up the damn scoreboard mr lugi")
        try:
            copyfile("data/scoreboard.dat", "scoreboard_backup/scoreboard.dat.bak")
        except:
            try:
                os.mkdir('scoreboard_backup')
            except FileExistsError:
                print("scoreboard_backup directory exists in location 'scoreboard_backup")
            copyfile("data/scoreboard.dat", "scoreboard_backup/scoreboard.dat.bak")
        
        time.sleep(300)

if __name__ == "__main__":
    main()