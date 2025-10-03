.PHONY: commit push all

# Commit message is the contents of README.md

commit:
	git add .
	git commit -m "reamde"

push: commit
	git push origin main

all: push
