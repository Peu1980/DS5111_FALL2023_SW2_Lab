# DS5111_FALL2023_SW2_Lab

What did you have to do to get make to work?
# run "sudo apt update" and "sudo apt install make"

Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)
# I had to run "sudo apt install python3.10-venv". This is what the error message said. THe error message was very helpful to quickly resolve it.

Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;
# It is executing each line as a single entity. commands in two lines will execute seperately. That means, command is not going to run within the activated environment if the activation and the command are in 2 seperate lines.

As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?
# run is sourcing the clockdemo_param.py 
# as long as the file has an extention, it is okay to have a file called run. If there is a file run with no extention, then either change the file name or change the name of the job run. 

The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?
# It is to append the running directory, so that the  clockdeco_param.py is sourcing from from the bin folder.


#############################################################
## Extra Credit
#############################################################
1 point: Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.
# sudo apt install tree
# tree /env

1 point: Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in __pycache__ folders. What is the meaning of the **/* ?
# any folder in the repository and any file ending _pycache

1 point: do a pip list or pip freeze and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.
# 

1 points: In the sample code from the book, why does the line if __name__=="__main__": allow the script to run if called directly, but not otherwise? What's going on there?
# 

1 point: If you add two print statements, (or any statements for that matter), one above and one below the if __name__... line, what would happen when I do an import of the file? What happens when I call the file directly with python <filename>. Most importantly, why?.
# 
