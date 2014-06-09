PythonResource
==============
*PythonResource* is a resource system for Python, inspired by the Android (and .NET) resource systems.

What it Does
------------
Resources are XML files containing predefined values. At the moment the only types of resource files are strings, but soon numbers, drawables and more will be added also.

~~~xml
<StrRes>
    <str name="intro">Thank you for choosing this software.</str>
    <str name="server_error">There is an issue with our server.</str>
    <str name="ask_exit">Are you sure you would like to exit?</str>
</StrRes>
~~~

You can access the values extremely easily.

~~~python
import pyres


R_str = pyres.RString("path/to/res/folder")    

print(R_str.intro) 
~~~

Benefits
--------
- **Modularity and Maintanability:** Using resources instead of hard-coding strings makes them very easiy to change. Update it once, instead replacing every ocurrence of it manually in your code, in every file.
- **Readability:** Of course, Code becomes much more readable having short variables instead of long strings.
- **Localization:** Instead of just having a strings.xml file, you can also add strings_de.xml, or even seperate files for `strings_de-ch.xml` and `strings_de-at`. PythonResource will automatically pick the file that fits the system default language the best. It is also possible to specify a custom language.

Coming Soon
-----------
I will add several more features to the module.

1. Add suport for more resources apart from strings. I will add a `values.xml` which can hold booleans, numbers, lists and tuples.
2. Allow for compression of the resources. I create a small command-line script that compresses them. On loading the resources, they will uncompress.
It will perform following optimizations:
- Shorten XML tags such as `<str>` to `<s>`
- Strip all newlines and comments from the xml
- Remove useless 0's from floats (`1.000` &rarr; `1.0`)
- If this does not slow load: Package the XML files in a compressed archive (bzip, lzma)
3. Improve the performance by not using a full XML parser (xml.etree), but writing a program that only get node text and name attribute may be quicker.
