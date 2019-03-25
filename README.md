# Lecture Notes for nyc-mhtn-ds-031119

## To update a local repo after forking and cloning

Add the learn-co lecture notes repo as the remote
```
git remote add upstream https://github.com/learn-co-students/nyc-mhtn-ds-031119-lectures.git
```

Check the remote is set and your lecture notes repo is correct
You should see your forked repo after *origin* 
And the learn-co-students repo after *upstream*

```
git remote -v
```

Update the changes from the upstream learn-co lecture notes repo
```
git fetch upstream
```

Check that the master branch is selected
```
git branch
```

Merge the new changes from the upstream learn-co lecture notes repo, with a commit message
```
git merge upstream/master -m 'what you updated'
```

Push the changes to the forked lecture repo
```
git push
```
