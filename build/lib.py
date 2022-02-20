def wrap(wrap, content, 
        tag_id = "", 
        tag_class = "", 
        tag_href = ""):
    """Wraps a content in an html tag"""
    def attributize(attr, val):
        if val:
            return f"{attr}=\"{val}\""
        return ""
    tag_id = attributize("id", tag_id)
    tag_class = attributize("class", tag_class)
    tag_href = attributize("href", tag_href)
    return f"<{wrap} {tag_id}{tag_class}{tag_href}>{content}</{wrap}>"
