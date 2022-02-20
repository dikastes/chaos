#!/usr/bin/python

import glob
import lib

def readfile(filename):
    with open(filename) as file:
        text = file.read()
    title = text.split("<h2>")[1].split("</h2>")[0]
    return text, title, filename

def translate_path(filename, prepend = "", append = ""):
    if len(filename.split("html/")) > 1 and prepend:
        filename = prepend + filename.split("html/")[1]
    if append:
        filename = filename.split(".html")[0] + append
    return filename

def writefile(header, footer, body, title, filename):
    body = lib.wrap("body", header + body + footer)
    title = lib.wrap("title", "Chaos Theory &ndash; " + title)
    script_name = translate_path(filename, prepend = "js/", append = ".js")
    script_tag = f"<script src=\"{script_name}\"></script>"
    head = lib.wrap("head", title + script_tag)
    html = lib.wrap("html", head + body)
    dest = translate_path(filename, prepend = "dist/")
    print("write " + dest)
    with open(dest, "w") as file:
        file.write(html)


html_files = glob.glob("html/*")

header = lib.wrap("h1", "Chaos Theory")
footer = lib.wrap("a", "Overview", tag_href = "../index.html")

parsed_files = [ readfile(file) for file in html_files ]
toc_links = [ lib.wrap("a", title, 
    tag_href=translate_path(filename, prepend="dist/"))
    for _, title, filename in parsed_files ]
toc_lis = [ lib.wrap("li", link) for link in toc_links ]
toc = lib.wrap("ul", "".join(toc_lis))

writefile(header, footer, toc, "", "index.html")

for html, title, filename in parsed_files:
    writefile(header, footer, html, title, filename)
