"""Individual shape refinements after the first bounds pass."""
SOURCE_ICON_ID = None
SOURCE_PATH = 'selection.json'
AUTHOR = 'gpt-6'
from pathlib import Path
import json,re
W=Path(__file__).parent;ROOT=W.resolve().parents[2]
s=json.loads((W/'selection.json').read_text())
ns={};exec((W/'repair.py').read_text().split('for n,item in enumerate(selection,1):')[0],{'__file__':str(W/'repair.py')},ns)
# Load the pure source-edit helper without re-running the first pass.
exec('import ast\n'+(W/'repair.py').read_text().split('def edit(')[1].split('\nfor n,item')[0].join(['def edit(','']),globals())
def path(n):return ROOT/s[n-1]['file']
def revise(n,x={},y={},arcs={},subs=()):
 p=path(n);t=edit(p.read_text(),x,y,arcs)
 for a,b in subs:
  assert a in t,(n,a)
  t=t.replace(a,b)
 p.write_text(t)
def body(n,text):
 p=path(n);t=p.read_text();t=t[:t.index('    def build')]+ '    def build(self) -> None:\n'+text;p.write_text(t)
body(1,'''        # Shared human_ref/user.svg construction: circular head, broad shoulders,
        # and exactly 4 units of visible head/body clearance (8 centerline).
        # HRECT_L centerline extremes: (4,8)-(44,40).
        cx, head_cy, head_radius = 14, 14, 6
        body_top = head_cy + head_radius + 8
        self.add_arc('head-right', (cx, 8), (cx, 20), radius_x=head_radius)
        self.add_arc('head-left', (cx, 20), (cx, 8), radius_x=head_radius)
        self.add_contour('head', 'head-right', 'head-left', closed=True)
        self.add_arc('shoulder-left', (4, 40), (cx, body_top), radius_x=10, radius_y=12)
        self.add_arc('shoulder-right', (cx, body_top), (24, 40), radius_x=10, radius_y=12)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-right')
        self.add_polyline('detail-box', (34, 10), (44, 10), (44, 22), (34, 22), closed=True)
        self.add_line('detail-line', (34, 34), (44, 34))
''')
body(8,'''        # Diagonal feeding bottle with two physical handles. Each handle owns
        # its cardinal lobes; its endpoints share the bottle's diagonal seams.
        # SQUARE centerline extrema: (6,6)-(42,42).
        def contour(name, start, pieces, closed=False):
            members = []
            point = start
            for index, (end, radii) in enumerate(pieces):
                member = f'{name}-{index}'
                if radii:
                    rx, ry, sweep = radii
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                else:
                    self.add_line(member, point, end)
                members.append(member)
                point = end
            self.add_contour(name, *members, closed=closed)
        contour('bottle', (6, 26), [
            ((6, 34), None), ((14, 42), (8, 8, False)),
            ((22, 42), None), ((24, 40), None), ((36, 28), None),
            ((38, 26), None), ((22, 10), None), ((20, 12), None),
            ((8, 24), None), ((6, 26), None)], True)
        contour('teat', (22, 10), [
            ((34, 6), None), ((38, 6), None), ((42, 10), (4, 4, True)),
            ((42, 14), None), ((38, 26), None)])
        contour('handle-left', (8, 24), [
            ((6, 16), (2, 8, True)), ((14, 8), (8, 8, True)),
            ((20, 12), (6, 4, True))])
        contour('handle-right', (36, 28), [
            ((42, 34), (6, 6, True)), ((34, 42), (8, 8, True)),
            ((24, 40), (10, 2, True))])
        for part in ('teat', 'handle-left', 'handle-right'):
            self.relate('connect', 'bottle', part)
''')
revise(9,arcs={'tub-2':(15,6)})
revise(33,subs=[('(x, 5)','(x, 8)')])
revise(35,x={20:19,28:29})
revise(39,subs=[("self.add_arc('bell-top', (14, 6), (26, 6), radius_x=20, radius_y=20, sweep=True)","self.add_arc('bell-top', (14, 6), (42, 24), radius_x=28, radius_y=18, sweep=True)"),("        self.add_arc('bell-right', (26, 6), (42, 22), radius_x=20, radius_y=20, sweep=True)\n",''),("self.add_arc('bell-bottom', (42, 22), (38, 38), radius_x=20, radius_y=20, sweep=True)","self.add_arc('bell-bottom', (42, 24), (38, 38), radius_x=4, radius_y=14, sweep=True)"),("'bell-top', 'bell-right', 'bell-bottom'","'bell-top', 'bell-bottom'")])
# Side circles preserve true circular nodes and exact attachment points.
body(42,'''        # Circular root plus a repeated pair of circular branch nodes.
        # SQUARE extremes: root reaches x=6; branch circles reach x=42,y=6,42.
        def circle(name, x, y, radius):
            self.add_arc(name+'-a', (x-radius,y), (x+radius,y), radius_x=radius)
            self.add_arc(name+'-b', (x+radius,y), (x-radius,y), radius_x=radius)
            self.add_contour(name, name+'-a', name+'-b', closed=True)
        circle('root', 14, 24, 8)
        circle('middle', 38, 24, 3)
        self.add_line('middle-branch', (22,24), (35,24))
        self.relate('connect', 'root', 'middle-branch')
        self.relate('connect', 'middle', 'middle-branch')
        for name, y in [('upper',10), ('lower',38)]:
            circle(name, 38, y, 4)
            self.add_line(name+'-branch', (22,24), (34,y))
            self.relate('connect', 'root', name+'-branch')
            self.relate('connect', name, name+'-branch')
            self.relate('connect', 'middle-branch', name+'-branch')
        self.relate('connect', 'upper-branch', 'lower-branch')
''')
revise(44,arcs={'hand':(6,6)})
