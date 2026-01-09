####  Module Basics

print(__name__)
def tagify(content, tag):
    return f'<{tag}>{content}</{tag}>'


def emojifier(content, emoji):
    return f'{emoji} {content} {emoji}'

