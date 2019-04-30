# comparisons.py
# contains information on how to compare files from different areas like working directory, staged area, different commits, different branches, tags etc.,

1. Working directory and Staging area
	git difftool
	this compares the files that are in working directory but not staged and the files in staged area
	
2. Working directory and Repository
	git difftool pointer-reference
	Ex:
		git difftool HEAD
		
3. Staging Area and Repository
	git difftool --staged pointer-reference
	Ex:
		git difftool --staged HEAD
		
4. Comparison between different commits
	git difftool commit1 commit2
	here,
		commit1 and commit2 can be commit id's or they can also be given in the relative HEAD form

5. Comparing local and remote repositories
	git difftool master origin/master
	
	
***Usually difftool or diff will compare all the files involved

6. Comparing only a selective file
	git difftool -- filename
	`
