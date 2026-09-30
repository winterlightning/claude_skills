"""Replace the build() body of a staged v2 module: rebody.py MODULE.py BODYFILE"""
import sys
path, body = sys.argv[1], open(sys.argv[2]).read()
s = open(path).read()
head = s[:s.index('    def build(self)')]
open(path, 'w').write(head + '    def build(self) -> None:\n' + ''.join('        ' + l + '\n' for l in body.strip().splitlines()))
