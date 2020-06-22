def transpile(parser, path, target='bash'):
    if target == 'bash':
        transpile2bash(parser, path)
    else:
        print('not possible to choose this target: {}'.format(target))

def transpile2bash(parser, path):
    # trnsplant
    bt = BashTranspiler(parser)
    content = bt.content
    with open(path, 'w') as f:
        f.write(content)


class BashTranspiler:
    def __init__(self, parser):
        self.parser = parser

        self.buf = []
        self.shebang = '#!/bin/bash'
        self.help_fn = self._get_help(self.parser.prog, self.parser.description)
        self.main_fn = self._get_main(self.parser.prog)
        self.buf.append(self.shebang)
        if len(self.help_fn) > 0:
            self.buf.extend(self.help_fn)
        if len(self.main_fn) > 0:
            self.buf.extend(self.main_fn)
        self.content = '\n'.join(self.buf)

    def _get_help(self, argname, description):
        head = 'usage: {} [-h]'.format(argname)
        indent = ' ' * 4
        subindent = ' ' * 2
        empl = indent + self._echo(' ')
        args = '-h, --help  show this help message and exit'
        start = 'arg_help () {'
        end = '}'
        help_fn = [start,
                   indent + self._echo(head),
                   empl,
                   indent + self._echo(description),
                   empl,
                   indent + self._echo('optional arguments:'),
                   indent + self._echo(subindent + args),
                   end
        ]
        return help_fn

    def _get_main(self, argname):
        return ['arg_help']

    def _echo(self, msg):
        return 'echo "{}"'.format(msg)