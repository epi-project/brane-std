# Cat
**v1.0.0** - **By the Brane Development Team**

The `cat` package can be used to inspect the contents of a dataset. It does so by providing a single function, `cat`, that can be executed and returns a string with the contents of the given dataset.

For binary datasets, it provides the `cat_base64` function, which returns the dataset's contents as a Base64-encoded string. For large datasets, there are also the `cat_range` and `cat_range_base64` functions.


## Installation
To install this package, simply run the following command in your terminal (we assume that Brane's Command-Line Interface is installed):
```bash
brane import epi-project/brane-std ./cat/container.yml
```
Don't forget to push the package to the remote repository if you want to use it in a (public) Brane instance.

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Classes
This package does not define any custom classes.


## Functions
This package contributes the following functions:
- `func cat(dataset, nested_path)`
  - _Description:_ Reads the file specified by `nested_path` in the given `dataset`, returning a string with its contents.
    > <img src="../assets/img/warning.png" alt="warning" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> This function will crash for non-UTF8 datasets. Consider using `cat_base64` for binary datasets or datasets that use a different encoding.

    > <img src="../assets/img/warning.png" alt="warning" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> Because this function will load the dataset entirely into memory (and return it as a single string, doing the same thing), you should use this function only for small dataset. For larger ones, consider the `cat_range` function.
  - _Arguments:_
    - `data: IntermediateResult`: The input dataset / intermediate result to inspect.
    - `nested_path: string`: The path of the file within the input dataset, relative to the dataset's root. Use `-` (a single dash) if the dataset is directly packaging a file and not a directory.
  - _Output:_
    - `string`: The contents of the specified file, as a plain string.
  - _Input datasets/results:_
    - `data`: The given input dataset should have a relatively small, UTF-8 encoded file present at the given `nested_path`.

- `func cat_base64(dataset, nested_path)`
  - _Description:_ Reads the file specified by `nested_path` in the given `dataset`, returning a string with its contents encoded in [Base64](https://en.wikipedia.org/wiki/Base64).
    > <img src="../assets/img/warning.png" alt="warning" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> Because this function will load the dataset entirely into memory (and return it as a single string, doing the same thing), you should use this function only for small dataset. For larger ones, consider the `cat_range_base64` function.
  - _Arguments:_
    - `data: IntermediateResult`: The input dataset / intermediate result to inspect.
    - `nested_path: string`: The path of the file within the input dataset, relative to the dataset's root. Use `-` (a single dash) if the dataset is directly packaging a file and not a directory.
  - _Output:_
    - `string`: The contents of the specified file, as a Base64-encoded string.
  - _Input datasets/results:_
    - `data`: The given input dataset should have a (relatively small) file present at the given `nested_path`.

- `func cat_range(dataset, nested_path, start, end)`
  - _Description:_ Reads a part of the file specified by `nested_path` in the given `dataset`, returning a string with its contents. The part to read is determined by `start` and `end` (both inclusive).
    > <img src="../assets/img/warning.png" alt="warning" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> This function will crash for non-UTF8 datasets. Consider using `cat_base64` for binary datasets or datasets that use a different encoding.
  - _Arguments:_
    - `data: IntermediateResult`: The input dataset / intermediate result to inspect.
    - `nested_path: string`: The path of the file within the input dataset, relative to the dataset's root. Use `-` (a single dash) if the dataset is directly packaging a file and not a directory.
    - `start: int`: The start index of the range to read. This is the number of characters (i.e., bytes) since the start of the file. Inclusive, and automatically clipped to the appropriate end of the file if out-of-range. Assumes an empty range if `start` < `end`.
    - `end: int`: The end index of the range to read. This is the number of characters (i.e., bytes) since the start of the file. Inclusive, and automatically clipped to the appropriate end of the file if out-of-range. Assumes an empty range if `start` < `end`.
  - _Output:_
    - `string`: The contents of the specified file, as a plain string.
  - _Input datasets/results:_
    - `data`: The given input dataset should have an UTF-8 encoded file present at the given `nested_path`.

- `func cat_range_base64(dataset, nested_path)`
  - _Description:_ Reads a part of the file specified by `nested_path` in the given `dataset`, returning a string with its contents encoded in [Base64](https://en.wikipedia.org/wiki/Base64). The part to read is determined by `start` and `end` (both inclusive).
  - _Arguments:_
    - `data: IntermediateResult`: The input dataset / intermediate result to inspect.
    - `nested_path: string`: The path of the file within the input dataset, relative to the dataset's root. Use `-` (a single dash) if the dataset is directly packaging a file and not a directory.
    - `start: int`: The start index of the range to read. This is the number of characters (i.e., bytes) since the start of the file. Inclusive, and automatically clipped to the appropriate end of the file if out-of-range. Assumes an empty range if `start` < `end`.
    - `end: int`: The end index of the range to read. This is the number of characters (i.e., bytes) since the start of the file. Inclusive, and automatically clipped to the appropriate end of the file if out-of-range. Assumes an empty range if `start` < `end`.
  - _Output:_
    - `string`: The contents of the specified file, as a Base64-encoded string.
  - _Input datasets/results:_
    - `data`: The given input dataset should have a file present at the given `nested_path`.
