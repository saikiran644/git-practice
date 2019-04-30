# Rebasing
Rebasing is actually rewining the current branch to the latest commit in the origin branch (from which it got branched) and re-apply the current
branch commits on top of that. This is generally done in case of any commits in the origin branch. So the graph looks like the current branch is
actually branched after all the changes.
So if the branch is rebased at every origin branch change, then while merging there will be no conflicts, it will be like a fast forward merge

commands:

1. git rebase branchname_towhich_torebase
	this will rewine the current branch object to the point of branchname_towhich_torebase HEAD and then the changes are applied on top of that
	
2. git pull --rebase origin master
	this is used to rebase the current branch to the origin master
	
3. In case of any conflict happening with git rebase, then it'll be in branch|REBASE state and one can choose any of the 3 options:
	-git rebase --continue
		after the conflict is resolved, doing this with continue and do the rebasing
	-git rebase --skip
		this will do the rebase from the beginning skipping the current commit that caused the problem
	-git rebase --abort
		this will abort the rebasing process and will bring back the current state to the one that is before the actual rebasing


Conflict:
	When the rebase couldn't be handled automatically by git, then the rebase goes in to conflict stage and is marked by branch|REBASE state. In
such cases, either the conflict can be resolved manually or it can be aborted.

***It is to be noted that rebasing will actually overwrite the history,so it has to be done carefully