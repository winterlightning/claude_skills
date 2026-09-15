from pathlib import Path
import json,ast
W=Path(__file__).parent;R=json.loads((W/'revisions.json').read_text())
def change(n,replace):
 p=W/'snapshot'/R[str(n)]['file'];s=p.read_text()
 for a,b in replace:
  if a not in s:raise ValueError((n,a))
  s=s.replace(a,b)
 p.write_text(s)
change(150,[('(20, 23), (24, 26), (28, 22)','(20, 22), (24, 26), (28, 22)')])
change(232,[('(33, 22), (33, 27)','(33, 22), (33, 26)')])
change(167,[("self.add_line('result', (21, 21), (27, 27))", "# The result divider is omitted because it closes two undersized apertures."),("self.relate('connect', 'result', 'window')",'')])
change(182,[('(24, 24), (34, 30), (42, 22)','(24, 24), (34, 24), (42, 16)')])
change(197,[('(12, 24), (25, 34), (34, 24)','(12, 24), (28, 34), (34, 24)')])
change(236,[('(11, 31), (24, 31), (30, 18)','(11, 31), (19, 25)')])
change(234,[("line('sail-seam', (28, 20), (36, 20))",''),("join('sail-seam', 'sail')",''),("join('sail-seam', 'mast')",'')])
change(229,[("(11, 26), (18, 17), (29, 29), (34, 17), (18, 17)","(11, 26), (18, 17), (25, 29), (34, 17)")])
change(113,[("(24, 34), (x(14), 34)","(x(6), 27), (x(14), 36)"),("join('lower-leg--1', 'lower-leg-1')",''),("join('tail', 'lower-leg--1')",''),("join('tail', 'lower-leg-1')",'')])
change(50,[("(8, 32), (8, 36), (8, 42)","(8, 32), (8, 24)"),("(40, 32), (40, 36), (40, 42)","(40, 32), (40, 24)")])
