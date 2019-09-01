# Developer README

## Following steps

*   Make any changes you need and commit it as usual.
*   call verup script in working directory (see verup script)
*   push all changes and tags

Script has 1 parameter with three options:

*   ./verup major - Only for "Breaking changes"
*   ./verup minor - Something new was added to Contract (some big changes).
*   ./verup patch - Contract updates (little changes).

Script should have chmod a+x.

## Example

```bash
    git add .
    git commit -m "add few changes for pypi and version check"
    bash verup patch
    git push && git push --tags
```
