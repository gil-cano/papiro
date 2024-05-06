# $\LaTeX$

```shell
brew install mactex
```

## compilers

See [Choosing a LaTeX Compiler](https://es.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler)
>    * LaTeX supports only .eps and .ps image formats for use with \includegraphics. If all the images in your project are .eps files, then this compiler setting is recommended.
>    * pdfLaTeX supports .png, .jpg, .pdf image formats. It will convert .eps images to .pdf on-the-fly during compilation, which may prolong the compilation time required. (pdfLaTeX may not be able to handle pstricks well on Overleaf.)
>    * XeLaTeX and LuaLaTeX both supports UTF-8 robustly out of the box, as well as Truetype and OpenType. They are therefore recommended if you need to typeset non-Latin scripts on Overleaf, in conjunction with the polyglossia pacakge. They also support all of the .png, .jpg, .pdf and .eps image formats.
>    * XeLaTeX supports pstricks; but LuaLaTeX doesn't.
>    * You can extend LuaLaTeX's capabilities by embedding Lua code directly in your document.
>
> In some cases, when your document includes cross-references, you must compile the source twice. It is necessary to include the correct numbers in the table of contents, list of images, reference numbers to theorems and so on.
>
> During the first compilation the LaTeX compiler writes the .aux file for informations about different numbering and during the second one the compiler reads these informations in order to properly generate a table of contents, bibliography, etc.
>
> This process can be automatized by the command latexmk. For example, to create a pdf out of the "mydocument.tex" file, run
>
> latexmk -pdf mydocument.tex


## VSCode

[LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop/wiki)

USer > setting.json

```json
   "latex-workshop.latex.tools": [

        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-shell-escape",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        }
   ]
```

\usepackage{minted}

```shell
pipx install pygments
```

