# Featherlight Plugin for MkDocs

Simple lightbox plugin for MkDocs. This plugin use the jQuery plugin [featherlight](https://github.com/noelboss/featherlight/) and is mostly based on the work of [https://github.com/mementum/lightgallery-markdown](https://github.com/mementum/lightgallery-markdown)



# Markdown usage

This plugin simply converts all images into lightboxes

```
![Alt title](image.jpg)
```

## Setup
```
pip3 install https://github.com/it-novum/mkdocs-featherlight.git
```

### Alternative setup
```
git clone https://github.com/it-novum/mkdocs-featherlight.git
cd mkdocs-featherlight/
python3 setup.py install
```


## Usage with MkDocs

```yml
extra_javascript:
  - vendor/jquery-3.6.0.min.js
  - vendor/featherlight-v.1.7.14/release/featherlight.min.js

extra_css:
  - vendor/featherlight-v.1.7.14/release/featherlight.min.css

markdown_extensions:
    - featherlight
```

### Javascript dependencies

You have to download the latest versions of [jQuery](https://jquery.com/download/) and [featherlight](https://github.com/noelboss/featherlight/) manually or via a package manager like npm or yarn

Make sure to set the right paths in `mkdocs.yml`

## Support for Light and Dark theme

In case you are using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
you can add support for light and dark mode by adding the following CSS to your `extra_css` files in `mkdocs.yml`

```css
[data-md-color-scheme="slate"] .featherlight .featherlight-content {
    background: #2e303e;
}

[data-md-color-scheme="slate"] .featherlight .featherlight-close-icon {
    background: rgba(255,255,255,.3);
    color: #fff;
}
```

# License
```
MIT License

Copyright (c) 2021 it-novum GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
