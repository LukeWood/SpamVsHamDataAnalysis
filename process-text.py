def remove_code(s):
    while s.find("<code>") != -1:
        start = s.index("<code>")
        end = s.index("</code>") + len("</code>")
        s = s[:start] + s[end:]
    return s

def remove_tags(s):
    return re.sub('<[^<]+?>', '', s)

def process_text(s):
    s = remove_code(s)
    s = remove_tags(s)
    return s.replace('\n', ' ')
