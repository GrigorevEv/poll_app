from django import template
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.filter(name='plural')
def adds_endings_to_a_word(number_of_votes: int) -> str:
    '''
    Adds endings to a word on russian language
    for a word "голос"
    '''
    if number_of_votes % 100 in [11, 12, 13, 14, 15, 16, 17, 18, 19] \
    or number_of_votes % 10 in [0, 5, 6, 7, 8, 9]:
        return 'ов'
    elif number_of_votes % 10 in [2, 3, 4]:
        return 'а'
    else:
        return ''

@register.filter(name='markdown')
def markdown_format(text:str) -> str:
    '''
    Adds the ability to fill the body of the article
    with markdown formatting
    '''
    return mark_safe(markdown.markdown(text))

