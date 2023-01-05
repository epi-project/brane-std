# Copy Result
**v1.1.0** - **By the Brane Development Team**

Currently, Brane has a feature that is very unfortunate.

Consider the following snippet:
```branescript
// This function returns an IntermediateResult
let res := initialization_function();
for (let i := 0; i < 10; i := i + 1) {
    // We keep writing to the same res based on that of the previous step
    res := processing_function(res);
}
```
One would expect this to work. However, in practice, the `res` result is empty when passed to `processing_function()`! And what's worse, this only the case in the _second iteration and up_ in this loop.

This is due to Brane eagerly wiping intermediate results before they are being handed to a container. This means that if the input folder and the output folder are the same, the input folder is wiped together with the output folder before the results can be used. Nasty!

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> The reason that this only happens the second iteration and upwards, is due to Brane assigning a distinct intermediate result to each function. You can verify this by running the `brane` executable with the `--debug` flag, and checking the compiled workflow.

To circumvent this issue until a good fix is found, the `copy_result` package is introduced.

This package abuses Brane's result naming scheme to decouple the input of a function from its output. Specifically, it provides a single function (`copy_result`) that takes an IntermediateResult and outputs another IntermediateResult that is a copy of the given one.

This may seem silly, but this fixed the bug above when we apply it to the result of `processing_function`:
```branescript
let res := initialization_function();
for (let i := 0; i < 10; i := i + 1) {
    res := processing_function(res);

    // New!
    res := copy_result(res);
}
```
By adding the `res := copy_result(res);` line, Brane decouples the input from the output, and your function should work as expected again.


## Installation
To install this package, simply run the following command in your terminal (we assume that Brane's Command-Line Interface is installed):
```bash
brane import epi-project/brane-std ./copy_result/container.yml
```
Don't forget to push the package to the remote repository if you want to use it in a (public) Brane instance.

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Classes
This package does not define any custom classes.


## Functions
This package contributes the following functions:
- `func copy_result(result)`
  - _Description:_ Copies the given `result` into a new IntermediateResult, decoupling it from itself (see the [introduction](#copy-result) on why this is useful).
  - _Arguments:_
    - `result: IntermediateResult`: The input result to copy.
  - _Output:_
    - `IntermediateResult`: The output result that is a clone of the input. If the input is a single file, then the output will still be a directory, with a single file `contents` that has the original contents.
  - _Input datasets/results:_
    - `result`: Any IntermediateResult is accepted, as long as its contents can be copied using a simple `cp -rf ...` command.
  - _Output result:_
    - The output result has the same format as the given input result (provided everything can be copied using a simple `cp -rf ...`).


## Examples
A more concise example using the [data_init](/epi-project/brane-std/tree/main/data_init) and the [data_math](/epi-project/brane-std/tree/main/data_math) packages:
```branescript
import data_init;     // Provides 'zeroes()`
import data_math;     // Provides 'add_const()'
import copy_result;   // Provides 'copy_result()'

// Initialize the dataset
let data := zeroes(1);

// Add 'i' to the dataset every iteration
for (let i := 0; i < 10; i++) {
    // We need 'copy_result()' for this to decouple the in- and outputs
    data := copy_result(add_const(data, i));
}
```

Another example, that uses the [cat](/epi-project/brane-std/tree/main/cat) package to show the difference when copying single-file datasets:
```branescript
import cat;           // Provides 'cat()'
import copy_result;   // Provides 'copy_result()'

// The dataset is a single-file
let data := new Data{ name := "some_single_file_data" };
println(cat(data, "-"));

// Copy it
let copy := copy_result(data);

// Now we have to inspect the "contents" file instead of the root:
println(cat(data, "contents"));   // Should print the same as above
```
