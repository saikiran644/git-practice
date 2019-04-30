# remember

1. If there are any changes to the same file between the local and remote repository, one has to do a git pull. In such cases, git tries to
   do a auto-merge. But in some cases if there is change in the same lines, then auto-merge fails and in such cases manually file has to be
   merged and then it should be staged and committed. Without doing the merge, the changes to the file cannot be commited and cannot be pushed
   as git will throw an error saying that the current branch is not up to date with the git repository contents.
   
