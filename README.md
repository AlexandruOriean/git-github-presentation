# git and Github basics

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=true} -->

<!-- code_chunk_output -->

1. [Preamble](#preamble)
2. [Creating a new project](#creating-a-new-project)
3. [Contributing to an existing project](#contributing-to-an-existing-project)
4. [Commands](#commands)
   1. [Setting up](#setting-up)
   2. [`git init`](#git-init)
   3. [`git add`](#git-add)
   4. [`git commit`](#git-commit)
   5. [`git status`](#git-status)
   6. [`git log`](#git-log)
   7. [`git show`](#git-show)
   8. [`git diff`](#git-diff)
   9. [`git clone`](#git-clone)
   10. [`git branch`](#git-branch)
   11. [`git checkout`](#git-checkout)
   12. [`git push`](#git-push)
   13. [`git fetch`](#git-fetch)
   14. [`git merge`](#git-merge)
   15. [`git pull`](#git-pull)
   16. [`git remote`](#git-remote)

<!-- /code_chunk_output -->

---

## Preamble

Below you will find the [list of git commands](#commands), the typical workflow for [creating a new project](#creating-a-new-project) as well as the workflow for [contributing to an existing project](#contributing-to-an-existing-project).

The commands to be typed in the terminal will show up like this:

```bash
$ git log
```

(The `$` indicates the prompt)

Please note that the text in `<angle brackets>` should be replaced with your own text. Aditionally, text in `[square brackets]` is optional, i.e. you can skip it.

The sample output of a command will show up like this:

> ```bash
> commit 356f63e55190eb33eb513ff2699259b1a80bd9f3
> Author: Alex Sincai <alex.sincai@yahoo.co.uk>
> Date:   Tue Nov 12 14:50:17 2019 +0200
>
>    Updated style
> ```

[Back to top](#git-and-github-basics "to top")

---

## Creating a new project

Let's start by creating a new project. Create a new folder and add some content; in this case, it will be a python script that computes the area of a circle, given a radius. I shall call this script `area_of_circle.py`.

Navigate to your github page and [create a new repository](https://github.com/new). Give it a name, a description, and click "Create".

Once you have the repository, go to your folder and run `git init` to start tracking this project.

After you have some content, use `git add area_of_circle.py` to let git know about this file.

Create your first commit, by running `git commit -m "Added script"`

Finally, push your changes, so that they are visible to github. Do this with the command `git push origin master`.

For this project, I have created a test suite and created the corresponding commits.

To recap:

1. Create a repo on github
2. Navigate to your folder
3. `git init`
4. `git remote add origin <repo URL>`
5. Modify / add files
6. `git add <all relevant files>`
7. `git commit -m "Commit message"`
8. `git push origin master`
9. Repeat steps 5 - 8 as needed

[Back to top](#git-and-github-basics "to top")

---

## Contributing to an existing project

Navigate to the project's repo URL and clone it with `git clone <URL>`. Create a new branch with `git checkout -b <new branch name>` and make all required changes. Add the changed files with `git add <list of files>`, commit with the relevant message (`git commit -m "<message>"`), and push the branch (`git push origin <branchname>`).

Then, go to the github page of the project, click the "Pull requests" tab, and hit the "New pull request" button. Compare the `base: master` with the `compare: <branch name>` and click "Create pull request". Fill in the details, and click "Create pull request" again.

If you see any conflicts, resolve them, otherwise wait for the repo owner to merge your changes.

To recap:

1. `git clone <URL>`
1. `git checkout -b <new branch name>`
1. Make the necessary changes
1. `git add <files>`
1. `git commit -m "<descriptive massage>"`
1. `git push origin <branch name>`
1. Create a new pull request with a descriptive message
1. Solve any conflicts
1. Wait for the repo owner to do this

[Back to top](#git-and-github-basics "to top")

---

## Commands

### Setting up

`git` (and github) needs to know about you. Run these commands to configure it:

```bash
$ git config --global credential.helper store
$ git config --global user.name "<github username>"
$ git config --global user.email "<github email adress>"
$ git config --global user.password "<github password>"
```

[Back to top](#git-and-github-basics "to top")

---

### `git init`

Create or navigate to the folder where you will work, then initialize git

```bash
$ git init
```

[Back to top](#git-and-github-basics "to top")

---

### `git add`

Let git know about new / modified files

To add a single file:

```bash
$ git add <file>
```

To add several files:

```bash
$ git add <file 1> <file 2> ... <file n>
```

To add the current folder:

```bash
$ git add .
```

[Back to top](#git-and-github-basics "to top")

---

### `git commit`

Have git track the desired files

```bash
$ git commit -m "<descriptive message>"
```

[Back to top](#git-and-github-basics "to top")

---

### `git status`

See the status of the files (untracked, new, modified, deleted) on the current branch

```bash
$ git status
```

> ```bash
> On branch master
>
> No commits yet
>
> Untracked files:
>  (use "git add <file>..." to include in what will be committed)
>
> 	index.html
>
> nothing added to commit but untracked files present (use "git add" to track)
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git log`

For the current branch, it shows the **commit hash**, author's **name** and **email**, the **date** and the **commit message**

```bash
$ git log
```

> ```bash
> commit 356f63e55190eb33eb513ff2699259b1a80bd9f3
> Author: Alex Sincai <alex.sincai@yahoo.co.uk>
> Date:   Tue Nov 12 14:50:17 2019 +0200
>
>    Updated style
>
> commit 21e40ae300061b7849417f9bc8de783ebb17c7ba
> Author: Alex Sincai <alex.sincai@yahoo.co.uk>
> Date:   Tue Nov 12 14:44:18 2019 +0200
>
>    Added style
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git show`

Shows the details of a certain commit

```bash
$ git show <hash>
```

> ```diff
> commit 356f63e55190eb33eb513ff2699259b1a80bd9f3
> Author: Alex Sincai <alex.sincai@yahoo.co.uk>
> Date:   Tue Nov 12 14:50:17 2019 +0200
>
>    Updated style
>
> diff --git a/style.css b/style.css
> index 371082a..e9ba78b 100644
> --- a/style.css
> +++ b/style.css
> @@ -1,3 +1,5 @@
> body {
>   font: 16px/1.5 sans-serif;
> +  margin: 0;
> +  padding: 0;
> }
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git diff`

When a local file contains changes that do not exist remotely, `diff` will show the differences between versions.

```bash
$ git diff
```

```bash
$ git diff <file>
```

> ```diff
> diff --git a/style.css b/style.css
> index 1bbf05f..33f3834 100644
> --- a/style.css
> +++ b/style.css
> @@ -5,7 +5,5 @@ body {
> }
>
> h1{
> -
> -color:burgundy;
> -
> -}
> \ No newline at end of file
> +  color: burgundy;
> +}
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git clone`

Allows you to clone a remote repository to your machine.

```bash
$ git clone <remote repository> [<local folder>]
```

> ```bash
> Cloning into 'git-github-presentation'...
> remote: Enumerating objects: 37, done.
> remote: Counting objects: 100% (37/37), done.
> remote: Compressing objects: 100% (26/26), done.
> remote: Total 37 (delta 11), reused 33 (delta 7), pack-reused 0
> Unpacking objects: 100% (37/37), done.
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git branch`

See the list of branches on your repository, or create new ones

Used without arguments, it lists the local branches:

```bash
$ git branch
```

> ```bash
>  color
> * master
> ```

The **\* asterisk** shows the current branch.

Used with the **-a** argument, it also lists the branches that exist remotely:

```bash
$ git branch -a
```

> ```bash
>  color
> * master
>  remotes/origin/HEAD -> origin/master
>  remotes/origin/color
>  remotes/origin/master
> ```

Note the HEAD: it shows that the current branch _for the remote repository_ is the same as the current local branch.

To create a new branch, use

```bash
$ git branch <new name>
```

[Back to top](#git-and-github-basics "to top")

---

### `git checkout`

This sets the HEAD to a specified commit hash or branch

To work on a previous commit:

```bash
$ git checkout <hash>
```

> ```bash
> Note: checking out '21e40ae300061b7849417f9bc8de783ebb17c7ba'.
>
> You are in 'detached HEAD' state. You can look around, make experimental
> changes and commit them, and you can discard any commits you make in this
> state without impacting any branches by performing another checkout.
>
> If you want to create a new branch to retain commits you create, you may
> do so (now or later) by using -b with the checkout command again. Example:
>
>  git checkout -b <new-branch-name>
>
> HEAD is now at 21e40ae Added style
> ```

To work on a different branch:

```bash
$ git checkout <branch>
```

> ```bash
> Switched to branch 'color'
> Your branch is up to date with 'origin/color'.
> ```

You can also create a new branch and work on it with:

```bash
$ git checkout -b <new branch name>
```

> ```bash
> Note: checking out '21e40ae300061b7849417f9bc8de783ebb17c7ba'.
>
> You are in 'detached HEAD' state. You can look around, make experimental
> changes and commit them, and you can discard any commits you make in this
> state without impacting any branches by performing another checkout.
>
> If you want to create a new branch to retain commits you create, you may
> do so (now or later) by using -b with the checkout command again. Example:
>
> git checkout -b <new-branch-name>
>
> HEAD is now at 21e40ae Added style
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git push`

This syncs the current local branch to the remote repository, on the same branch

```bash
$ git push -u origin <branch>
```

Please note that **origin** is just a label, it can be called anything (but really shouldn't...). "origin" is just the standard name for the remote repo's URL.

[Back to top](#git-and-github-basics "to top")

---

### `git fetch`

Gets the content from the remote repository, **without** applying it.

```bash
$ git fetch
```

[Back to top](#git-and-github-basics "to top")

---

### `git merge`

Incorporates fetched changes into the current branch

```bash
$ git merge
```

To incorporate a certain commit, use

```bash
$ git merge <hash>
```

[Back to top](#git-and-github-basics "to top")

---

### `git pull`

Fetches and merges changes from the remote to the specified branch

```bash
$ git pull origin <name>
```

> ```bash
> From https://github.com/alexsincai/git-github-presentation
> * branch            master     -> FETCH_HEAD
> Updating 21e40ae..78b5fbd
> Fast-forward
> index.html | 2 +-
> style.css  | 8 ++++++++
> 2 files changed, 9 insertions(+), 1 deletion(-)
> ```

[Back to top](#git-and-github-basics "to top")

---

### `git remote`

Lets the local repository know about the remote repository

```bash
$ git remote add origin <URL>
```

As stated above, the name of the remote can be something other than **origin**, but it is that by convention; changing this will cause headaches down the road.

[Back to top](#git-and-github-basics "to top")
