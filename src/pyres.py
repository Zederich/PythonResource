import locale
import os
import xml.etree.ElementTree as xmlTree


class RString(object):
    def __init__(self, directory, lang=None):
        """
        Finds the strings_[lang].xml resource files in the directory, parses the xml file for lang (if not specified,
        the system default language is used) them and then adds them as a member variable.

        :rtype : Nones
        :param directory: The directory in which to search for the file
        :param lang: 
        """
        if lang is None:
            lang = locale.getdefaultlocale()[0].lower()
        res_listdir = os.listdir(directory)

        lang_res_name = "".join(("strings_", lang, ".xml"))

        if not lang_res_name in res_listdir:
            lang_res_name = "".join(("strings_", lang[:2:], ".xml"))
            if not lang_res_name in res_listdir:
                lang_res_name = "strings.xml"

        print("using", lang_res_name)
        tree = xmlTree.parse(os.path.join(directory, lang_res_name))
        root = tree.getroot()
        for string in root.iter("str"):
            exec("".join(("self.", str(string.attrib["name"]), "='", str(string.text), "'")))