def steps_git_push():
    # Define ANSI escape codes for colors and reset
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Display steps of git
    print(RED + "*--Steps of Git Push--*" + RESET)
    
    steps_git_push = """@01. git status
    @02. git add .
    @03. git status
    @04. git git commit -m "get_df_by_range(…) added"
    @05. git branch #Check current active branch
    @06. git remote -v #Check remote 
    @07. #git push -u origin main #Push to remote one-time
    @08. git push #Push to remote subsequent times"""
    
    print(GREEN + steps_git_push + RESET)

'''
* Example usage:
import avn_utils.git.utils as mygit_utils
mygitutils.steps_git_push()
* This will print steps of git to push changes to remote
'''