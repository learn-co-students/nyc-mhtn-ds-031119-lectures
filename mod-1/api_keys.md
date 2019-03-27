# Instructions for API keys on github :key: :lock:

## Create a new project repo
* Initialize the repo with a README 
* Add a .gitignore Python file.
## Edit the .gitignore file on your github page.
  This is to deal with sqlite, the DS_Store file, and API keys.  <br />
  
```
# Logs and databases 
*.log
*.sql
*.sqlite

# OS generated files 
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# config file
config.py
```

* From here add your partner as a collaborator. <br />
* Each collaborator will clone the repo to their local machine. <br />
* Each collaborator will put their API keys/tokens for the project in a config.py file. <br /> <br />
## Make a config.py file 
```# .gitignore should include reference to config.py
api_key = "YOUR_KEY"
api_secret = "YOUR_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
token_secret = "YOUR_TOKEN_SECRET" 
``` 
From here make branches :palm_tree:, commit :ring: , push :bicyclist:, and merge files :ok_hand: .
<img width="549" alt="Screen Shot 2019-03-26 at 3 40 13 PM" src="https://user-images.githubusercontent.com/39356742/55028179-7b821480-4fdd-11e9-93be-1e8e4fe06225.png">
