# Pandoc

## md to PDF

```shell
 pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont='Maple Mono Normal NF'
 ```


```shell
pandoc CHECKLIST.md -o ~/tmp/checklist.pdf --from markdown --template eisvogel --listings --pdf-engine=xelatex
```


https://github.com/Wandmalfarbe/pandoc-latex-template/issues/202


https://github.com/Wandmalfarbe/pandoc-latex-template/issues/96#issuecomment-3016690275

