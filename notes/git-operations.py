# git-operations.py
# contains information related to git-operations and how staging areas and workig directory are affected

1. git operations like "git mv", "git rm" etc., can be performed on only those files that are visible to or tracked by git (git ls-files)
2. Whatever might be the operation, the result is reflected in staging area because the changes made by the operations should be able to
   commit. But since the changes are staged with git-operation alone, the changes are also reflected back in working directory to match the
   staged area i.e., in case of rename of a file, the file is renamed in working directory and also in case of delete the file is deleted in
   the working directory.
3. Now if the changes are made undo by using "git reset HEAD file_name", the staged area for the file is reset to the HEAD which has the
   following impact for the operations:
	-git rm file_name
		here,
			doing "git reset HEAD file_name" actually removes the deletion operation from the staged area and in such case, doing "git status"
		shows the file in unstaged area of tracked file as the reset is not reflected in the working directory. Now if the file has to appear
		back in the working directory as in HEAD, do "git checkout -- file_name".
		
	-git mv old_file_name new_file_name
		here,
			since a rename is a delete and add operation (deletion of old_file_name and addition of new_file_name), doing "git reset HEAD 
			new_file_name" will remove the addition from staged area and "git status" will show that new_file_name is untracked. Now if the
			old_file_name is reset as "git reset HEAD old_file_name", this will remove the deletion from staged area and "git status" will
			show that the old_file_name is deleted but not yet added to staged area. In such case, to have the old_file_name back in working
			directory, one should do "git checkout -- old_file_name" which adds file from HEAD to working directory and the new_file_name can
			be deleted in working directory.