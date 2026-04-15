# Pandoc

## md to PDF

```shell
 pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont='Maple Mono Normal NF'
 ```


```shell
pandoc CHECKLIST.md -o ~/tmp/checklist.pdf --from markdown --template eisvogel --listings --pdf-engine=xelatex
```
