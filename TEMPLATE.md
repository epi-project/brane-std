# \<PACKAGE_NAME\>
**v\<VERSION\>** - **By \<YOUR NAME(S)\>**

\<high-level description\>


## Installation
To install this package, simply run the following command in your terminal (we assume that Brane's Command-Line Interface is installed):
```bash
brane import https://github.com/epi-project/brane-std --file ./<PACKAGE_ID>/<CONTAINER_YML>
```
Don't forget to push the package to the remote repository if you want to use it in a (public) Brane instance.

> <img src="../assets/img/info.png" alt="info" width="16" style="margin-top: 3px; margin-bottom: -3px;"/> If you are running an unreleased version of Brane, you can add `--init <path/to/branelet>` to use a custom-compiled `branelet` executable, just as you can with `brane build`.


## Classes
This package contributes the following classes:
- `class <CLASS NAME\>`
  - _Description:_ \<DESCRIPTION\>
  - _Fields:_
    - `<FIELD NAME>: <BRANE TYPE>`: \<DESCRIPTION\>
    - \<...\>
  - _Functions:_
    - \<see functions below\>
    - \<...\>
- \<...\>


## Functions
This package contributes the following functions:
- `func <FUNCTION NAME>(<ARG>, <...>)`
  - _Description:_ \<DESCRIPTION\>
  - _Arguments:_
    - `<ARG>: <BRANE TYPE>`: \<DESCRIPTION\>
    - \<...\>
  - _Input datasets/results:_
    - `<ARG>`: \<provide a description of the expected dataset format for this argument\>
    - \<...\>
  - _Output result:_
    - `\<provide a description of the produced output format for this function if any\>
