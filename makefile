GIT=git

COMMIT=commit
ADD=add
PUSH=push
BRANCH=$(shell git branch | grep -E "^\* .+" -o | grep -E "[^* ]+" -o)

commit:* .gitignore
	-$(GIT) $(ADD) $^
	$(GIT) $(COMMIT)

push:commit
	$(GIT) $(PUSH) origin $(BRANCH)
