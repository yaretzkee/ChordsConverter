# Chords Converter

![Python 3.10](https://img.shields.io/badge/python-3.10-blue)

Simple app that converts guitar chords between different standards.

## Inspirations

--------
Key driver to write this app was a need for quick conversion of widely available formats, like [ChordPro](https://www.chordpro.org/) or [Ultimate Guitar](https://www.ultimate-guitar.com/) to LaTeX with leadnsheets package.

Somewhat inspired by [this project](https://ultimate.ftes.de/) which works ok, but does not cover required formats

## Formats coverage

--------

| Feature                        | Read               | Write             | Comment
|:-------------------------------- |:------------------:|:------------------|:--------
| [Ultimate Guitars](https://www.ultimate-guitar.com/)]                 | :heavy_check_mark: | :heavy_multiplication_x:|
| [ChordPro](https://chordpro.org)                         | :heavy_check_mark: | :heavy_check_mark:|
| Latex with [leadsheets](https://www.ctan.org/pkg/leadsheets)            | :heavy_check_mark: | :heavy_check_mark:|
| Latex with [sOngs](https://ctan.org/pkg/songs)             | :heavy_multiplication_x:           | :heavy_check_mark:|
| HK*                              | :heavy_check_mark: | :heavy_check_mark:|

## Requirements

--------

* Python 3.10
* PySide6

```bash
pip install PySide6
```

## Usage

--------
Clone the repository and simply run

```bash
python songs_converter.pyw
```

### in app

* open file with song or paste content to input text field
* choose input format (if not recognized)
* click convert or hit F5
