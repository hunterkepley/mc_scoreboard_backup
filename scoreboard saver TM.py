from shutil import copyfile
import os
import time

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

    print("Luigi this shit will take a minute to update, have a good day, it's loaded xd lmao hehe content lul 4head just build nice keyboard")

    while(True):
        print("Backin up the damn scoreboard mr lugi")
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
