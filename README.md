# Brane Standard Library
This repository provides a standard collection of packages for a running [Brane](https://github.com/epi-project/brane) instance.


## Repository structure
The individual packages are located under each folder in the repository root under the same name as their Brane identifier. For example, the `cat` package is available in the folder `/cat`. Each folder contains a README.md with more information about that package.

For a brief overview, see the table [below](#overview).

To download a package, you can run the following command on your local machine (we assume that you have the [Brane Command-Line Interface](https://github.com/epi-project/brane/releases/latest) installed):
```bash
brane import epi-project/brane-std ./<package_name>/container.yml
```
where you should replace `<package_name>` with the name of the package you like to install (e.g., `cat`).

> <img src="./assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Overview
This repository currently includes the following packages:
- `hello_world`: A package that contains the simplest function of all. Used in the [official Wiki](https://wiki.enablingpersonalizedinterventions.nl).
- `cat`: A package for quickly inspecting dataset contents. Used in the [official Wiki](https://wiki.enablingpersonalizedinterventions.nl).
- `copy_result`: A "necessary evil" package that takes an intermediate result and renames it. Necessary if you are writing to the same result as you're reading from (i.e., a loop).


## Contributing
If you like to contribute to this repository by adding your own package, please make a pull request where you provide your package in the same structure as provided above. Please use `TEMPLATE.md` to write the README for your package, and include a `CHANGELOG.md` based on [this](https://keepachangelog.com/en/1.0.0/) format so users can see what has changed.

If you have suggestions about the individual packages, feel free to raise issues or create pull requests as well. Any help is appreciated!


## Attribution
The icons used in this repository (<img src="./assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/>, <img src="./assets/img/warning.png" alt="warning" width="16" style="margin-top: 3px; margin-bottom: -3px;"/>) are provided by [Flaticon](https://flaticon.com).
