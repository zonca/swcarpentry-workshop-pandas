## Motivating exercise

we want to publish our Python analysis module and we want
to keep history of changes so we can roll back to any previous version to
reproduce previous results, i.e. when we submitted a paper.

## Git setup

    git init
    git config --global user.name "Firstname Lastname"
    git config --global user.email "yourworkemail@youruniversity.edu"
    git config --global core.editor "notepad.exe" # for windows
    git config --global core.editor "nano" # for MAC and Linux

## Basic git commands

* `git add` # put in the shopping cart
* `git status` # check what is modified, what is ready to be committed
* `git commit` # buy (opens editor to type commit message)
* `git commit -m "Commit message"` # buy (no editor)
* `git log` # show histor


## Do some commits

* initial commit
* improve comments
* add `.gitignore`
* add save png

travel back in history to understand where it is.

Checkout different previous versions and try to run each of them, notice that the commit just before was working, the "Add title" commit breaks the script.

## Github

open github account with same email used in git configuration
create a remote following the instructions on github
git push

make a change from the web interface, that changes nothing locally!
git pull to syncronize

Try another commit locally, push to github

Show different parts of the github GUI, show how research group in the area of the students use github for code or papers.
