#Check that local repo is up to date with github
git status

#Something that saves the current date and time in a file
date > /data/class/cogs106/yezzeldi/COGS106/version

#Update github with the new version file
git add .
git commit -m "Updated Version"
git push --set-upstream origin main
