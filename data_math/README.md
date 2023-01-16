# Data Math
**v1.0.0** - **By the Brane Development Team**

The `data_math` package contains various functions for performing on arithmetic on datasets of a certain shape (a "kind").

Currently, the following dataset kinds are supported:
- `vector`: A file called `data` with constants in it, separated by spaces.

See [below](#functions) for an overview of the functions that this package contributes.


## Installation
To install this package, simply run the following command in your terminal (we assume that Brane's Command-Line Interface is installed):
```bash
brane import epi-project/brane-std ./data_math/container.yml
```
Don't forget to push the package to the remote repository if you want to use it in a (public) Brane instance.

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Classes
This package does not define any custom classes.


## Functions
This package contributes the following functions:
- `func add_const(data, const, kind)`
  - _Description:_ Adds `const` to all of elements in the `data` dataset or result.
  - _Arguments:_
    - `data: IntermediateResult`: The dataset to which we want to add the constant.
    - `const: real`: The constant to add to each element in the dataset.
    - `kind: string`: The kind of the dataset that we are adding. See the top of this README for an overview.
  - _Output:_
    - `IntermediateResult`: A new result with the same `kind` as the given `data`, having as value the element-wise addition of `data` and `const`.
  - _Output result:_
    - The output results will have the same shape as the input `data` dataset.


## Examples
For example, the following can be used to do an element-wise addition (using the [cat](/epi-project/brane-std/tree/main/cat) and [data_init](/epi-project/brane-std/tree/main/data_init) packages):
```branescript
import cat;         // provides 'cat()'
import data_init;   // provides 'zeroes()'
import data_math;   // provides 'add_const()'

let zeroes := zeroes(5, "vector");
let ones   := add_const(zeroes, 1, "vector");
println(cat(ones, "data"))

// Should print:
// 1 1 1 1 1
```
