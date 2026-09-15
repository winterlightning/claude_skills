from pathlib import Path
import json
AUTHOR='gpt-6'
SOURCE_PATH='icon_set/work/latest-variant-cleanup/additional-applied-plan.json'
SOURCE_ICON_ID=None
W=Path(__file__).parent
P={g['root']:Path(g['target_file']) for g in json.loads((W/'additional-applied-plan.json').read_text())}
def edit(n,changes):
 p=P[n];b=W/'latest-sources'/p.name
 if not b.exists():b.write_bytes(p.read_bytes())
 s=b.read_text()
 for a,z in changes:
  assert a in s,(n,a)
  s=s.replace(a,z)
 p.write_text(s)
edit('airplane-departing-runway',[("('L', (18, 18))","('L', (14, 18))"),("('L', (12, 26))","('L', (6, 26))"),("(26, 18), (20, 6)","(26, 18), (26, 6)")])
edit('airplane-horizontal', [('(12, 18)','(12, 16)'),('(18, 18)','(18, 16)'),('(32, 18)','(32, 16)'),('(38, 18)','(38, 16)'),('(38, 30), 6, 6','(38, 32), 8, 8'),('(32, 30)','(32, 32)'),('(18, 30)','(18, 32)'),('(12, 30)','(12, 32)')])
edit('airplane-with-landing-wheel',[("path('plane', (4, 12), [('L', (12, 16)), ('L', (16, 20)), ('L', (20, 20)), ('L', (16, 8)), ('L', (24, 8)), ('L', (32, 20)), ('L', (40, 20)), ('A', (40, 28), 4, 4, True), ('L', (32, 28)), ('L', (24, 36)), ('L', (16, 36)), ('L', (20, 28)), ('L', (12, 28)), ('L', (4, 12))], True)","path('plane', (4, 8), [('L', (12, 8)), ('L', (12, 16)), ('L', (20, 16)), ('L', (16, 8)), ('L', (24, 8)), ('L', (32, 16)), ('L', (40, 16)), ('A', (40, 24), 4, 4, True), ('L', (32, 24)), ('L', (24, 32)), ('L', (16, 32)), ('L', (20, 24)), ('L', (4, 24)), ('L', (4, 8))], True)"),("(40, 28), (40, 34)","(40, 24), (40, 34)")])
edit('apple-logo',[("(22, 12), [('C', (34, 4), (22, 6), (28, 4)), ('C', (22, 12), (34, 10), (28, 12))]","(14, 12), [('C', (34, 4), (14, 4), (24, 4)), ('C', (14, 12), (34, 12), (24, 12))]")])
edit('atv-side-view',[("(4, 33), [('L', (4, 20)), ('L', (28, 20)), ('L', (38, 20)), ('A', (44, 26), 6, 6, True), ('L', (44, 33))]","(4, 17), [('L', (11, 17)), ('L', (28, 17)), ('L', (37, 17)), ('L', (44, 17))]"),("(28, 20), (24, 8)","(28, 17), (24, 8)"),("join(n, 'body')","line(n+'-support', (x,17), (x,26))\n            join(n+'-support','body')\n            join(n+'-support',n)")])
edit('badge-3',[("('A', (12, 28), 8, 8, False)","('L', (4, 32)), ('L', (12, 32))"),("('A', (36, 28), 8, 8, True)","('L', (44, 32)), ('L', (36, 32))")])
edit('bean',[("(16, 32), [('A', (34, 18), 18, 18, False)]","(16, 30), [('A', (34, 18), 18, 18, False)]")])
p=P['airplane-horizontal'];p.write_text(p.read_text().replace("(38, 32), 8, 8", "(38, 32), 6, 8"))
p=P['airplane-with-landing-wheel'];s=p.read_text().replace("('L', (12, 8)), ('L', (12, 16)), ('L', (20, 16))", "('L', (8, 8)), ('L', (8, 16)), ('L', (16, 16))").replace("('L', (20, 24))", "('L', (16, 24))");p.write_text(s)
p=P['bean'];p.write_text(p.read_text().replace("(16, 30), [('A', (34, 18), 18, 18, False)]", "(24, 29), [('C', (34, 18), (30, 29), (34, 24))]"))
p=P['airplane-with-landing-wheel'];s=p.read_text().replace("('L', (8, 8)), ('L', (8, 16)), ('L', (16, 16)), ('L', (16, 8)), ('L', (24, 8)), ('L', (32, 16))", "('L', (12, 8)), ('L', (12, 16)), ('L', (24, 16)), ('L', (24, 8)), ('L', (32, 8)), ('L', (36, 16))");p.write_text(s)
p=P['bean'];p.write_text(p.read_text().replace("(24, 29), [('C', (34, 18), (30, 29), (34, 24))]", "(24, 28), [('C', (34, 18), (29, 28), (33, 23))]"))
p=P['bean'];p.write_text(p.read_text().replace("(24, 28), [('C', (34, 18), (29, 28), (33, 23))]", "(24, 29), [('C', (34, 18), (27, 29), (32, 24))]"))
edit('aircraft-releasing-bomb',[("('L', (32, 6))", "('L', (33, 6))")])
