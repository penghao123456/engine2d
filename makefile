GIT=git

COMMIT=commit
ADD=add
PUSH=push

commit:* .gitignore
	-$(GIT) $(ADD) $^
	$(GIT) $(COMMIT)

push:commit
	$(GIT) $(PUSH) origin main
