# branching

Usage:
	Any new feature that needs to be added to the project is usually not done in the master itself. The master is branched and then the changes are made
in the branch, once the changes are good to go then the branch is merged in to the master. The merge is also like a commit. So the master now has the
changes made in the branch but the branch is still at its last save point (any changes made to master meanwhile are not reflected into the branch)

Fast-forward merging:
	Consider new_branch is branched from master, now if changes are made in the new branch and then they are merged into the master, then by default
fast-forward merge happens in case there are no changes in the master from the time the new_branch is branched.
	This makes the log graph look in a way that both the master and new_branch points to the same commit after the merge and there will be no branch
shown in the graph

***To disable the fast-forward merging and to preserve the branch in the graph, --no-ff flag can be used when merging into the master


Commands:
	
1. git branch -a
	show the available branches - both local and remote (only updated ones)
	
2. git branch new_branch_name
	create a new branch new_branch_name from the current one
	
3. git checkout branch_name
	checksout the branch_name information to the working directory + the untracked files overall + the tracked files common to both the branches will
   exist in the working directory. Also, in case of any staging that is done, then the files will still be there in the staging area.
   
4. git branch -d/D branch_name
	deletes the branch. -d for normal delete. If there are any unstaged or uncommitted changes in the branch, git won't delete the branch instead it
   will throw an error. Used -D to force the deletion
   
   
***How the working directory is changed as we switch branches:
	once we switch to a branch, the working directory is restoed to the HEAD of the branch. Also the files that are currently being modified (files already
    tracked by the git and new untracked files for the git) will still be there in the working directory.
	In case of any decrepencies like a file f1 that exists in the commit of branch b1 and is not available in branch b2. In such cases if we are switching from
	b1 to b2 and the working directory has the file f1 in unstaged area then the branch switch is not possible as this file cannot be in the working directory
	when we switch branches (as b2 doesn't have file f1 in its latest commit) and also git cannot checkout to b2 discarding the modifications to f1 in b1. So,
	in such cases the changes to the working directory needs to be stashed or can be committed and switched to b2.
	*It is always a good practice to clean the working directory and switch branches

Branching:
	Branch b1 is the branch in which the merge is going to be happenned from branch b2.
	1. No changes in b1:
		b2 is branched from b1 and no changes are made in b1 since branching, by default fast-forward merge happens
	2. Changes in b1:
		changes are made in b1 but the changes doesn't conflict with b2, auto-merge will be made by the git
	3. Merge conflicts:
		In cases where there are merge conflicts, then the current state is branch|MERGING stage and the merge conflicts has to be resolved manually. In
	   such cases, mergetool or merge can be used on the conflict branch and then the commit can happen. Now the stage changes from branch|MERGING to branch