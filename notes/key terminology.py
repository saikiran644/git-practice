# key terminology:

Workflow cycle:
	-Working directory
		-normal working files
	-Staging area
		-git index
		-holding area for queuing up changes for the next commit
		-move files in and out of staging area without impacting the repository
	-Repository
		-hidden folder in working directory
		-.git folder
		-finalised changes and permanently part of the git repository
	
	-Remote repository
		-fourth state
		-just another repository with its own three states internally
		-git can be used without this stage
		
WORKFLOW:
	
		local directory						Staging Area						Repository									Remote Repository
	all local changes and files		files that are added using		  once files are ready in staging				once project is commited they can be
	are present here				git add will come here, these	  area, they can be committed which				push to git account using git push and
									are the files that are ready	  means they are added to the git				then they will be available in the actual
									to be committed. These files      repository that is present locally.			git account. All the added changes with
									can be added or deleted any		  But these changes will not get reflected		commit message will be available in the
									number of times					  in git account as they are still local.		account
		
		
Master branch:
	-branches contain commits
	-default branch is Master
	
	
Tracked and Untracked file:
	A file that is atleast available in the staging area or local git repository. That means git knows about the file. Any file that is committed will be available
in local git repository and therefore it is considered to be tracked file. Even if it is a new file but already added to staging area even then the file will be
considered as a tracked file. The only case where the file is considered untracked is when its a new file and is not even added to the staging area.
	Any tracked file can be directly commited with "-a" option without adding it to the staging area. This "-a" will actually add file to the stagin aread and then will
do the commit, but for a untracked file this doesn't work and it has to be added to staging area with the command "git add untracked_file"

