# Set up blog on new machine

```bash
git clone git@github.com:sbaack/sbaack.github.io.git
cd sbaack.github.io
# Github user pages require the rendered page in the main branch.
# Therefore, switch to branch containing the source code for editing
git checkout pelican
# Create a new virtualenv using your preferred tool, e.g.:
python -m venv .venv && source .venv/bin/activate
```

To install the project dependencies and set up the necessary submodules you can either use `Gnu Make` (Linux or Mac):

```bash
make init
```

Or [`Invoke`](https://www.pyinvoke.org/) as a cross-platform solution:

```bash
python -m pip install -U pip -Ur requirements-invoke.in
invoke init
```

# How to publish

As a general note, use Chicago Manual of Style 17th edition (author-date) as your citation style to be consistent with the older content.

After you've done some changes or created new content in the `pelican` branch (e.g. a new blog post), do the following:

- Preview your changes before publication. Use `make dev-preview` or `invoke dev-preview`. This (re-)creates an `output` folder containing the updated static files and serves them at <http://localhost:8000/> by default.
- If you didn't encounter any issues in the preview, commit your changes to the `pelican` branch.
- Publish your content with `make github` or `invoke gh-pages`. This first moves and commits the contents of the `output` directory in the `pelican` branch to the `main` branch using `ghp-import`, and then pushes an update to `origin main`.

# Additional information about this setup

`pelican-themes` and `pelican-plugins` are set up as git submodules using the following settings in `.gitmodules`:

```yaml
[submodule "pelican-plugins"]
    path = pelican-plugins
    url = https://github.com/getpelican/pelican-plugins
    ignore = all
    shallow = true
[submodule "pelican-themes"]
    path = pelican-themes
    url = https://github.com/getpelican/pelican-themes
    ignore = all
    shallow = true
```

First, we only make shallow copies of submodules, as we don't need their full commit history. Second, changes to these submodules are ignored. Instead of tracking changes to submodules in this repository (and thus having lots of commits that do nothing but updating pointers to submodules), we rely on the  `--remote` flag when cloning or updating the submodules, which tells git to pull the latest versions of the submodules' remotes. If you want to update the submodules at some point, use `git submodule update --remote` or execute `make init`/`invoke init` again.

However, if you still want to update pointers to the submodules in this repository:

```bash
git submodule update --remote --merge <submodule>
git commit <submodule> -m "Updated submodule <submodule>"
```