from gendiff.diff import Mode


def format_obj(value, tab):
    for key, value in value.items():
        return '{{\n    {tab}{key}: {value}\n{tab}}}'.format(
            tab=' ' * (tab + 4),
            key=key,
            value=value,
        )


def format_val(value, tab):
    if isinstance(value, dict):
        return format_obj(value, tab)
    else:
        return value


def make_strings(ast, tab=0):
    strings = []
    for key, (status, value) in sorted(ast.items()):
        def make_line(prefix, value_to_show):
            return '  {tab}{prefix} {key}: {value}'.format(
                tab=' ' * tab,
                prefix=prefix,
                key=key,
                value=format_val(value_to_show, tab),
            )
        if status == Mode.NESTED:
            strings.append('    {tab}{key}: {{\n{value}\n    {tab}}}'.format(
                tab=' ' * tab,
                key=key,
                value=make_strings(value, tab + 4),
            ))
        elif status == Mode.EQUAL:
            strings.append(make_line(' ', value))
        elif status == Mode.ADDED:
            strings.append(make_line('+', value))
        elif status == Mode.REMOVED:
            strings.append(make_line('-', value))
        elif status == Mode.CHANGED:
            old, new = value
            strings.append(make_line('+', new))
            strings.append(make_line('-', old))
    return '\n'.join(strings)


def format(ast):
    return '{\n' + make_strings(ast) + '\n}'
