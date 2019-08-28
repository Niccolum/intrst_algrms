Step one: Make any changes you need and commit it as usual.

Step two: call verup script in working directory (see verup script)

Step three: push all changes and tags

Step four: create dist

Step five: upload dist to PYPI

Script has 1 parameter with three options:

    ./verup major - Only for "Breaking changes"
    ./verup minor - Something new was added to Contract (some big changes).
    ./verup patch - Contract updates (little changes).

Script should have chmod a+x.

Example:

```
niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ git add .

niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ git commit -m "add few changes for pypi and version check"
[master 98da39b] add few changes for pypi and version check
 5 files changed, 63 insertions(+), 3 deletions(-)
 create mode 100644 README-DEV.mdn
 rename VERSION.md => VERSION (100%)
 create mode 100755 verup

niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ ./verup patch
Current: 0.1.2
New    : 0.1.3
[master 9a2af51] Version was updated from 0.1.2 to 0.1.3
 1 file changed, 1 insertion(+), 1 deletion(-)

niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ git push && git push --tags
Подсчет объектов: 26, готово.
Delta compression using up to 4 threads.
Сжатие объектов: 100% (21/21), готово.
Запись объектов: 100% (26/26), 3.05 KiB | 347.00 KiB/s, готово.
Total 26 (delta 8), reused 0 (delta 0)
remote: Resolving deltas: 100% (8/8), completed with 3 local objects.
To github.com:Niccolum/intrst_algrms.git
 * [new tag]         0.1.3 -> 0.1.3

niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ source env/bin/activate
(env) niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ python setup.py sdist
...
Writing Intrst_algrms-0.1.3/setup.cfg
Creating tar archive
removing 'Intrst_algrms-0.1.3' (and everything under it)

(env) niccolum@niccolum-HP-ProBook-650-G3:~/projects/github/intrst_algrms$ python3 -m twine upload dist/*
Enter your username: Niccolum
Enter your password: 
Uploading distributions to https://upload.pypi.org/legacy/
Uploading Intrst_algrms-0.1.3.tar.gz
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 825k/825k [00:01<00:00, 462kB/s]


```