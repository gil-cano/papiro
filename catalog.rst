ZCatalog
========

ZCatalog Indexes
----------------

* TextIndex
* FieldIndex
* KeywordIndex
* PathIndex


Other Indexes
-------------

ZCTextIndex
~~~~~~~~~~~

A ZCTextIndex is an index for performing full text searches over
bodies of text. It includes the following features:

- A new query language, supporting both explicit and implicit Boolean
operators, parentheses, globbing, and phrase searching.  Apart from
explicit operators and globbing, the syntax is roughly the same as
that popularized by Google.

- Two selectable relevance scoring algorithms: 
The Cosine ranking from the Managing Gigabytes book, and Okapi from 
more recent research papers.  Okapi usually does better, so it is 
the default.

ZCTextIndex is designed as a replacement for standard TextIndex, and
has several advantages over it.


TopicIndex
~~~~~~~~~~



DateRangeIndex
~~~~~~~~~~~~~~

    Index for date ranges, such as the "effective-expiration" range in CMF.

    Any object may return None for either the start or the end date: for the
    start date, this should be the logical equivalent of "since the beginning
    of time"; for the end date, "until the end of time".

    Therefore, divide the space of indexed objects into four containers:

    - Objects which always match (i.e., they returned None for both);

    - Objects which match after a given time (i.e., they returned None for the
      end date);

    - Objects which match until a given time (i.e., they returned None for the
      start date);

    - Objects which match only during a specific interval.


