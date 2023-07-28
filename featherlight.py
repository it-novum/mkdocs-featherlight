from markdown import Extension
from markdown.treeprocessors import Treeprocessor
#https://github.com/mkdocs/mkdocs/issues/2892
#from markdown.util import etree
from lxml import etree
import re


class ImagesTreeprocessor(Treeprocessor):
    def __init__(self, md):
        Treeprocessor.__init__(self, md)

    def run(self, root):
        parent_map = {child: parent for parent in root.iter() for child in parent}
        images = root.iter("img")
        for image in images:
            desc = image.attrib["alt"]

            image.set("alt", desc)
            parent = parent_map[image]
            imageIndex = list(parent).index(image)


            a = etree.Element('a')
            a.set("href", "#")
            a.set("data-featherlight", image.attrib["src"])
            a.append(image)

            parent.insert(imageIndex, a)
            parent.remove(image)


class FeatherlightExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(ImagesTreeprocessor(md), "featherlight", 1337)


def makeExtension(*args, **kwargs):
    return FeatherlightExtension(**kwargs)
