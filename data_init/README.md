# Data Init
**v1.0.0** - **By the Brane Development Team**

The `data_init` package contains various functions for initializing intermediate results and, therefore, datasets.

Currently, the following dataset kinds are supported:
- `vector`: A file called `data` with constants in it, separated by spaces.

See [below](#functions) for an overview of the functions that this package contributes.


## Installation
To install this package, simply run the following command in your terminal (we assume that Brane's Command-Line Interface is installed):
```bash
brane import epi-project/brane-std ./data_init/container.yml
```
Don't forget to push the package to the remote repository if you want to use it in a (public) Brane instance.

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Classes
This package does not define any custom classes.


## Functions
This package contributes the following functions:
- `func zeroes(number, kind)`
  - _Description:_ Generates a file that is a simple sequence of `number` zeroes.
  - _Arguments:_
    - `number: int`: The number of zeroes to generate.
    - `kind: string`: The kind/shape of the output dataset. See the top of this README for an overview.
  - _Output:_
    - `IntermediateResult`: The generated intermediate results.
  - _Output result:_
    - The output results will have a shape defined by the `kind` field.


## Examples
For example, the following function can be used to generate a few intermediate results (using the [cat](/epi-project/brane-std/tree/main/cat) package):
```branescript
import cat;         // provides 'cat()'
import data_init;   // provides 'zeroes()'

let zeroes := zeroes(5, "vector");
println(cat(zeroes, "data"))

// Should print:
// 0 0 0 0 0
```
