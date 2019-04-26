# basics

basic commands

1. status:
	-to give the status of the current git directory
	-specifies the branch names and also shows if there are any changes with the current code
	-if there are no changes needed, it displays "nothing to commit, working directory clean"
	

2. add files into the staging area
	-git add file/files_separated_by_space
	
	
3. git commit
	-git commit -m "message"  --> this will take up the changes in staging area and will do a commit
	-if default editor already configured, then there is no need to specify -m "message", git commit will be enough and that will open up
	 the default editor where the message can be written and saved
	 
	 
4. git push
	-this will push the local git repository changes to the remote repository
	-to do this, either a project has to be cloned or the configuration of the account where the changes have to be pushed have to be specified
	
	
5. git init
	-git init project_name  --> this will create a fresh git project (which includes all the necessary git files, so that it can be treated as a git project)
	-git init  --> this will add .git folder to the current director making it a git project
	
	
6. git clone
	-git clone clone_url  --> clones the repository locally as a git project
	

7. fork
	-forking in git is actually copying repository of someone to another account, this can be done by selecting fork option in the target repository and selecting
	 the account to which it has to be forked. One can login/signin to add that to fork.
	 

8. git pull
	-just before doing git push, one can do a git pull to fetch any latest changes made to the remote git repository. If at all there are any changes, they will be
     added to the local git repository and the same files will be used hereafter. This will be useful in cases where a huge team is working and the code will be updated
	 quite often
	 

9. remove files from staging area:
	-git reset HEAD filename/s
		This is used to remove the files that are already in staging area. This will not get the files back to the local directory but will remove from the staging area.
	 So, once it is removed it is lost.
	 ***Once a new file is added to staging area, it is considered as tracked file. But if the same file is removed using "git reset HEAD" command, then the file in local
	    directory is considered as untracked file as it is not available even in staging area
	 ***in cases where the changes are made to the local directory with git commands like "git mv", "git rm" etc., and then "git reset" is used, the changes are not directly
		added to the local directory but can be viewed with "git status" and if needed they can be added to the local directory with the help of "git checkout --" command 
		
		
10. git checkout
	-git checkout -- filename
		this will revert or bring back the file "filename" to the contents of the file that is in the current statged area
	
	
11. recursive adding
	-git add .
		using a "." (dot) will recursively add all the files that are changed in the local directory to the staging area. In includes files that are deep inside folders.
		
		
12. rename or moving:
		renaming of moving of files can be done in two ways:
			-using normal linux commands
				mv origin_file destination_file
				.this will be treated as a file deletion and another file addition from the git end as git has no idea about the system command executed. But once it is added
			 to the staging area, it will see if the contents of the new file and the deleted file are same and if same, will be treated as a rename
				.also it is to be noted that doing git status before adding to the staged area will show it like a new file and a deleted file.
				.In such cases, if required after adding to the staging area, one can use "git add -u" to update the staging area files properly and see the consolidated status
				
			-using git mv command
				git mv origin_file destination_file
				.this will treat the file as renamed and will do the same thereafter.
				.using git mv will automatically add it to the staging area as the rename has to be commited
				.Also it is to be noted that only those files that are already in .git repository can be used with git mv as git will know about these. But new files which are not
				 even in staging area cannot be used with git mv command. So in such cases even if a new file is moved to staging area and then its name is changed using git mv command
				 it is still treated as a new file as git is having it for the first time but not as rename
		***Changes done to the file in the GUI will also be reflected in the git as a system command rename not as git rename
		***Renaming at os level will not add it to staging area and when added, it confirms that it is rename only if the data is same for both the files but with git rename, it 
		***It is to be noted that "git mv" is actually a add and delete operation and when using "git reset" on the same it is treated as add and delete operation
		
13. check files tracked by git:
		git ls-files
		only on these files git commands like "git rm", "git mv, git checkout" etc., can be used
		
		
