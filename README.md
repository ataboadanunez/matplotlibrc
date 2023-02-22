# matplotlibrc
my personal configuration file for matplotlib

# How to use it

Paste the `matplotlibrc` file in a folder of your preference. For example, I have it in
```bash
/home/user/lib/python/matplotlib/
```
Then export configuration using (for example) your `~/.bashrc` file:
```bash
export MPLCONFIGDRI=$HOME/lib/python/matplotlib/
export MATPLOTLIBRC=$MPLCONFIGDIR/matplotlibrc_v2
```

# Latex packages

LaTex package must be installed in your system or an error will prompt if the mathmode is activated, e.g., in a plot label.
If that happens try installing the following packages:
```bash
sudo apt install texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super
```
