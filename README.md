<p align="center">
  <img src="images/logo.svg" alt="Logo das anotações" width="120">
</p>

<h1 align="center">Anotações de Estudo</h1>

<p align="center">
  Especialização em Engenharia e Administração de Sistemas de Banco de Dados<br>
  Faculdade de Tecnologia da Unicamp
</p>

<p align="center">
  <a href="https://www.unicamp.br/"><img src="images/logo-unicamp.svg" alt="Unicamp" height="80"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.extecamp.unicamp.br/"><img src="images/logo-extecamp.png" alt="Extecamp" height="60"></a>
</p>

Resumos das disciplinas da especialização, escritos em LaTeX e sincronizados com o Overleaf. Cada capítulo junta o conteúdo da aula com complementos da bibliografia indicada e da documentação oficial, sempre com a fonte citada na margem.

## Disciplinas

| Código | Disciplina | Situação |
| --- | --- | --- |
| CET 615 | Fundamentos de Sistemas de Banco de Dados | em andamento |

As demais disciplinas estão listadas no prefácio e entram conforme o curso avança.

## Estrutura

```
main.tex                 documento principal (preâmbulo, capa, ordem das partes)
main.bib                 referências
chapters/preface.tex     prefácio com as disciplinas do curso
chapters/cet615/         um arquivo por capítulo da CET 615
images/                  logo e imagens usadas no texto
```

Os arquivos de exemplo do template continuam em `chapters/`, mas não entram no PDF.

## Como compilar

No Overleaf, basta abrir o projeto: ele compila sozinho.

Localmente, com uma distribuição TeX completa (TeX Live, por exemplo):

```
latexmk -pdf main.tex
```

O `latexmk` roda o `pdflatex`, o `biber` e o `makeindex` quantas vezes for preciso.

## Sobre o conteúdo

Os resumos foram escritos com palavras próprias a partir das aulas, dos slides e da bibliografia. Os slides, scripts e listas de exercícios pertencem aos professores de cada disciplina e não estão neste repositório.

O layout usa a classe [kaobook](https://github.com/fmarotta/kaobook), distribuída sob a LaTeX Project Public License (ver `MANIFEST.md`).
