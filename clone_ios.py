from git import Repo
import os
import shutil

print('deleting local ios dev directory and cloning into current')

# delete current dev dir
shutil.rmtree('/Users/tylerfrith/Desktop/SDK/ios/development')

# clone dev sdk
repo = Repo.clone_from('git@github.com:arubanetworks/meridian-ios.git', '/Users/tylerfrith/Desktop/SDK/ios/development', branch='development', recursive=True)

print('done!')