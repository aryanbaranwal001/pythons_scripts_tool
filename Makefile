.PHONY: commit push

commit:
	git add .
	git commit --allow-empty -m "readme"

push: commit
	git push
