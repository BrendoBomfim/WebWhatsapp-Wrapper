import six


def safe_str(text):
    if not text:
        return "(empty)"
    assert isinstance(text, six.string_types), "obj is not a string: %r" % text
    return str(text) if text else "(empty)"
