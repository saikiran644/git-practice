# stashing

In case we are working on a new impementation and in the middle of something and meanwhile some critical issue arises, which needs immediate
attention, in such case one need not simply make a commit to make the working directory clean instead the current changes can be stashed, meaning
the modified tracked files and staged changes will be stored in an area (not the new files - only that are in staged and modified tracked files)
making the current working directory clean (apart from new files which need not be cleaned) so that one can switch branches and do the work.
Once the work is done in the other branch, one can switch to this branch and then apply the stash to the branch and can work on the previous files.
