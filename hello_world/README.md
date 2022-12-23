# Hello, world!
**v1.0.0** - **By the Brane Development Team**

The `hello_world` package is a toy package for testing Brane setups and learning how to manage packages. It provides only a single function, aptly named `hello_world`, which returns the string: `"Hello, world!"`.


## Installation
To install this package, simply run the following command in your terminal (we assume that Brane's Command-Line Interface is installed):
```bash
brane import epi-project/brane-std ./hello_world/container.yml
```
Don't forget to push the package to the remote repository if you want to use it in a (public) Brane instance.

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Classes
This package does not define any custom classes.


## Functions
This package contributes the following functions:
- `func hello_world(self)`
  - _Description:_ Returns the string `"Hello, world!"`.
  - _Arguments:_
    - `self: HelloWorld`: Reference to this HelloWorld instance.


## Examples
You can use the `hello_world()` function to simple print `Hello, world!` to stdout:
```branescript
import hello_world;

println(hello_world());

// Should print: Hello, world!
```
