# configure editor

notepad++ congiguration for windows:
	-Install notepad++
	-Add notepad++ to the environment variables -> path variables (so that it can be directly used as a command)
	-Add an alias for notepad++ for easy invocation everytime. This can be done by using '.bash_profile' file. This file is specific to
	 git bash application and it checks this file when commands are executed where custom commands can be given.
		-Adding alias
			alias npp='notepad++ -multiInst -nosession'  --> this will replace "npp" command with "notepad++ -multiInst -nosession" everytime npp is used
	-Also add notepad++ as the default text editor in git with the following
		-git config --global core.editor "notepad++.exe -multiInst -nosession"	--> this will make notepad++ as the default editor with the given options
	-Check the configuration file
		-git config --global -e  --> git will use the default editor now to edit the configuration file