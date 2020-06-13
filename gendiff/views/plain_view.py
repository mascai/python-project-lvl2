import gendiff.diff as diff


def format_value(value):
    if isinstance(value, dict):
        return 'complex value'
    else:
        return value


def make_strings(ast, parent=''):
    strings = []
    for key, (status, value) in sorted(ast.items()):
        if status == diff.NESTED:
            strings.append(
                "{}{}".format(parent, make_strings(value, parent=(key + ".")))
            )
        if status == diff.ADDED:
            strings.append("{}{}' was added with value: '{}'".format(
                parent, key, format_value(value))
            )
        if status == diff.REMOVED:
            strings.append("{}{}\' was removed".format(parent, key))
        if status == diff.CHANGED:
            old, new = value
            strings.append("{}{}' was changed. From '{}' to '{}'".format(
                parent, key, format_value(old), format_value(new))
            )
    return '\n'.join(strings)


def add_prefix(strings):
    result = strings.split('\n')
    for (index, elem) in enumerate(result):
        result[index] = "Property '" + elem
    return result


def format(ast):
    strings = make_strings(ast)
    result = add_prefix(strings)
    return '\n'.join(result)
