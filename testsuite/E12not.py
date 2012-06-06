if (
        x == (
            3
        ) or
        y == 4):
    pass

y = x == 2 \
    or x == 3

if x == 2 \
    or y > 1 \
        or x == 3:
    pass

if x == 2 \
        or y > 1 \
        or x == 3:
    pass


if (foo == bar and
        baz == frop):
    pass

if (
    foo == bar and
    baz == frop
):
    pass


a = (
)

a = (123,
     )


#


if start[1] > end_col and not (
        over_indent == 4 and indent_next):
    return(0, "E121 continuation line over-"
           "indented for visual indent")


print "OK", ("visual",
             "indent")

print "Okay", ("visual",
               "indent_three"
               )

print "a-ok", (
    "there",
    "dude",
)

print "hello", (
    "there",
    "dude")

print "hello", (

    "there",
    # "john",
    "dude")

print "hello", (
    "there", "dude")

print "hello", (
    "there", "dude",
)

# Aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

#
# Extra indentation is not necessary.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


a = 'AAA'    \
    'BBB'    \
    'CCC'

bbb = 'AAA'    \
      'BBB'    \
      'CCC'

cc = ('AAA'
      'BBB'
      'CCC')

cc = {'text': 'AAA'
              'BBB'
              'CCC'}

cc = dict(text='AAA'
               'BBB')

a = 'AAA'    \
    'BBB'    \
    'iii'    \
    'CCC'

a = 3 + \
    4 + \
    5 + 6


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

if ((row < 0 or self.moduleCount <= row or
     col < 0 or self.moduleCount <= col)):
    raise Exception("%s,%s - %s" % (row, col, self.moduleCount))


result = {
    'foo': [
        'bar', {
            'baz': 'frop',
        }
    ]
}


foo = my.func({
    "foo": "bar",
}, "baz")

#
if bar:
    return(
        start, 'E121 lines starting with a '
        'closing bracket should be indented '
        "to match that of the opening "
        "bracket's line"
    )
#
# you want vertical alignment, so use a parens
if ((foo.bar("baz") and
     foo.bar("frop")
     )):
    print "yes"

# also ok, but starting to look like LISP
if ((foo.bar("baz") and
     foo.bar("frop"))):
    print "yes"

if (a == 2 or
    b == "abc def ghi"
         "jkl mno"):
    return True

if (a == 2 or
    b == """abc def ghi
jkl mno"""):
    return True

if length > options.max_line_length:
    return options.max_line_length, \
        "E501 line too long (%d characters)" % length


#


print 'l.{line}\t{pos}\t{name}\t{text}'.format(
    line=token[2][0],
    pos=pos,
    name=tokenize.tok_name[token[0]],
    text=repr(token[1]),
)

print('%-7d %s per second (%d total)' % (
      options.counters[key] / elapsed, key,
      options.counters[key]))


if os.path.exists(os.path.join(path, PEP8_BIN)):
    cmd = ([os.path.join(path, PEP8_BIN)] +
           self._pep8_options(targetfile))


fixed = (re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] +
         target[c + 1:])

fixed = (
    re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] +
    target[c + 1:]
)


if foo is None and bar is "frop" and \
        blah == 'yeah':
    blah = 'yeahnah'


"""This is a multi-line
   docstring."""


if blah:
    # is this actually readable?  :)
    multiline_literal = """
while True:
    if True:
        1
""".lstrip()
    multiline_literal = (
        """
while True:
    if True:
        1
""".lstrip()
    )
    multiline_literal = (
        """
while True:
    if True:
        1
"""
        .lstrip()
    )


if blah:
    multiline_visual = ("""
while True:
    if True:
        1
"""
                        .lstrip())


rv = {'aaa': 42}
rv.update(dict.fromkeys((
    'qualif_nr', 'reasonComment_en', 'reasonComment_fr',
    'reasonComment_de', 'reasonComment_it'), '?'))

rv.update(dict.fromkeys(('qualif_nr', 'reasonComment_en',
                         'reasonComment_fr', 'reasonComment_de',
                         'reasonComment_it'), '?'))

rv.update(dict.fromkeys(('qualif_nr', 'reasonComment_en', 'reasonComment_fr',
          'reasonComment_de', 'reasonComment_it'), '?'))


rv.update(dict.fromkeys(
    ('qualif_nr', 'reasonComment_en', 'reasonComment_fr',
     'reasonComment_de', 'reasonComment_it'), '?'
), "foo", context={
    'alpha': 4, 'beta': 53242234, 'gamma': 17,
})


rv.update(
    dict.fromkeys((
        'qualif_nr', 'reasonComment_en', 'reasonComment_fr',
        'reasonComment_de', 'reasonComment_it'), '?'),
    "foo",
    context={
        'alpha': 4, 'beta': 53242234, 'gamma': 17,
    },
)


#


event_obj.write(cursor, user_id, {
    'user': user,
    'summary': text,
    'data': data,
})

event_obj.write(cursor, user_id, {
    'user': user,
    'summary': text,
    'data': {'aaa': 1, 'bbb': 2},
})

event_obj.write(cursor, user_id, {
    'user': user,
    'summary': text,
    'data': {
        'aaa': 1,
        'bbb': 2},
})

event_obj.write(cursor, user_id, {
    'user': user,
    'summary': text,
    'data': {'timestamp': now, 'content': {
        'aaa': 1,
        'bbb': 2
    }},
})


def qualify_by_address(
        self, cr, uid, ids, context=None,
        params_to_check=frozenset(QUALIF_BY_ADDRESS_PARAM)):
    """ This gets called by the web server """


def qualify_by_address(self, cr, uid, ids, context=None,
                       params_to_check=frozenset(QUALIF_BY_ADDRESS_PARAM)):
    """ This gets called by the web server """


_ipv4_re = re.compile('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                      '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                      '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
                      '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')


fct("""
    AAA """ + status_2_string)


if context:
    msg = """\
action: GET-CONFIG
payload:
    ip_address: "%(ip)s"
    username: "%(username)s"
""" % context


if context:
    msg = """\
action: \
GET-CONFIG
""" % context


if context:
    msg = """\
action: """\
"""GET-CONFIG
""" % context


def unicode2html(s):
    """Convert the characters &<>'" in string s to HTML-safe sequences.
    Convert newline to <br> too."""
    return unicode((s or '').replace('&', '&amp;')
                            .replace('>', '&gt;')
                            .replace('<', '&lt;')
                            .replace("'", '&#39;')
                            .replace('"', '&#34;')
                            .replace('\n', '<br>\n'))

#
parser.add_option('--count', action='store_true',
                  help="print total number of errors and warnings "
                       "to standard error and set exit code to 1 if "
                       "total is not null")

parser.add_option('--exclude', metavar='patterns', default=DEFAULT_EXCLUDE,
                  help="exclude files or directories which match these "
                       "comma separated patterns (default: %s)" %
                       DEFAULT_EXCLUDE)

add_option('--count',
           help="print total number of errors "
           "to standard error total is not null")

add_option('--count',
           help="print total number of errors "
                "to standard error "
                "total is not null")


#


help = ("print total number of errors " +
        "to standard error")

help = "print total number of errors " \
       "to standard error"

d = dict('foo', help="exclude files or directories which match these "
                     "comma separated patterns (default: %s)" %
                     DEFAULT_EXCLUDE)

d = dict('foo',
         help="exclude files or directories which match these "
              "comma separated patterns (default: %s)" %
              DEFAULT_EXCLUDE)

d = dict('foo',
         help="exclude files or directories which match these "
              "comma separated patterns (default: %s, %s)" %
              (DEFAULT_EXCLUDE, DEFAULT_IGNORE)
         )

d = dict('foo',
         help="exclude files or directories which match these "
              "comma separated patterns (default: %s, %s)" %
              # who knows what might happen here?
              (DEFAULT_EXCLUDE, DEFAULT_IGNORE)
         )

# parens used to allow the indenting.
troublefree_hash = {
    "hash": "value",
    "long": ("the quick brown fox jumps over the lazy dog before doing a "
             "somersault"),
    "long key that tends to happen more when you're indented": (
        "stringwithalongtoken you don't want to break"
    ),
}

# another accepted form
troublefree_hash = {
    "hash": "value",
    "long": "the quick brown fox jumps over the lazy dog before doing "
            "a somersault",
    ("long key that tends to happen more "
     "when you're indented"): "stringwithalongtoken you don't want to break",
}

foo(1, 2, 3,
    4, 5, 6)
#: Okay
d = dict('foo',
         help="exclude files or directories which match these "
              "comma separated patterns (default: %s)" %
              DEFAULT_EXCLUDE
         )
d = dict('foo',
         help="exclude files or directories which match these "
              "comma separated patterns (default: %s)" % DEFAULT_EXCLUDE,
         foobar="this clearly should work, because it is at "
                "the right indent level",
         )
