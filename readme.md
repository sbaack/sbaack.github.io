# Set up blog on new machine

Clone this repository and set up the theme as a submodule:

```bash
git clone git@github.com:sbaack/sbaack.github.io.git
cd sbaack.github.io
git submodule update --init --remote
```

To be able to preview changes before publication, you need to have [Hugo](https://gohugo.io/) installed (`brew install hugo` if you're on Mac).

# Write new content and publish

Optional but useful, you can quickly generate new Markdown files with YAML headers with the `hugo new` command (the template for generating the Markdown file is `archetypes/default.md`):

```bash
hugo new content/posts/my-new-post.md
hugo new content/pages/my-new-page.md
```

Preview your changes before publication:

```
hugo server
```

If you don't encounter any issues, simply create and push a new commit to `origin main`. Github will then build and deploy the page automatically.

Tip: Because Github takes care of publishing on each push to `main`, you can also update the page by editing or adding files in Github's web interface if you're working on a machine where you don't want or can't install Hugo or Git.

# Additional information about this setup

The git submodule for the [Hugo-Coder theme](https://github.com/luizdepra/hugo-coder) is set up like this:

```bash
[submodule "themes/hugo-coder"]
	path = themes/hugo-coder
	url = https://github.com/luizdepra/hugo-coder.git
	ignore = all
    shallow = true
```

First, we only make a shallow copy, as we don't need the full commit history. Second, changes to the submodule are ignored. Instead of tracking changes to the submodule in this repository (and thus accumulating commits that do nothing but updating pointers to it), we rely on the `--remote` flag when cloning or updating it, which tells git to pull the latest version of the submodule's remote. If you want to update the submodules at some point, use `git submodule update --remote`.

However, if you still want to update pointers to the submodules in this repository:

```bash
git submodule update --remote --merge <submodule>
git commit <submodule> -m "Updated submodule <submodule>"
```
