Static vocabularies
-------------------

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

organizers = SimpleVocabulary(
    [SimpleTerm(value=u'Bill', title=_(u'Bill')),
     SimpleTerm(value=u'Bob', title=_(u'Bob')),
     SimpleTerm(value=u'Jim', title=_(u'Jim'))]
    )

organizer = schema.Choice(
            title=_(u"Organiser"),
            vocabulary=organizers,
            required=False,
        )

Since required is False, there will be a no value option in the drop-down list.


class SimpleTerm(object):
    """Simple tokenized term used by SimpleVocabulary."""

    def __init__(self, value, token=None, title=None):
        """Create a term for value and token. If token is omitted,
        str(value) is used for the token.  If title is provided, 
        term implements ITitledTokenizedTerm.
        """
        self.value = value
        if token is None:
            token = value
        self.token = str(token)
        self.title = title
        if title is not None:
            directlyProvides(self, ITitledTokenizedTerm)




When working with vocabularies, you’ll come across some terminology that is worth explaining:

A term is an entry in the vocabulary. The term has a value. Most terms are tokenised terms which also have a token, and some terms are titled, meaning they have a title that is different to the token.
The token must be an ASCII string. It is the value passed with the request when the form is submitted. A token must uniquely identify a term.
The value is the actual value stored on the object. This is not passed to the browser or used in the form. The value is often a unicode object, but can be any type of object.
The title is a unicode object or translatable message. It is used in the form.

The SimpleVocabulary class contains two class methods that can be used to create vocabularies from lists:

fromValues()
takes a simple list of values and returns a tokenised vocabulary where the values are the items in the list, and the tokens are created by calling str() on the values.
fromItems()
takes a list of (token, value) tuples and creates a tokenised vocabulary with the token and value specified.

