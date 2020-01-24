from git import Repo
import os
import shutil

print('deleting local andorid dev directory and cloning into current')

# delete current dev dir
shutil.rmtree('/Users/tylerfrith/Desktop/SDK/Android/development')

# clone dev sdk
repo = Repo.clone_from('git@github.com:arubanetworks/meridian-android.git', '/Users/tylerfrith/Desktop/SDK/Android/development', branch='master')

print('done!')