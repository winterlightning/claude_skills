"""Person Connected to Six Nodes.
Plan: A central circular head and open rounded bust own six actual graph links. Six equal nodes derive from mirrored x positions and a three-row series. Bounds (6,6)-(42,42). Head bottom y19, torso top y27: exactly 8 centerline units.
References: human_ref/user.svg circular head and rounded shoulders; Lucide network shared graph junctions.
Reduction: Bust baseline removed to retain a readable open shoulder outline; all six nodes and links retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bdd049c3-18b8-4342-b482-804021271d94'
SOURCE_PATH = 'pictographic-primitives/business/user network_bdd049c3-18b8-4342-b482-804021271d94.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


def symmetric(icon, name, start, left_steps, axis=24):
    """One half owns the whole outline; reflect and reverse its traversal."""
    flip = lambda p: (2*axis-p[0], p[1])
    prior = start
    reverse = []
    for kind, end, *args in left_steps:
        if kind == 'B':
            reverse.append((kind, flip(prior), flip(args[1]), flip(args[0])))
        else:
            reverse.append((kind, flip(prior), *args))
        prior = end
    path(icon, name, start, *left_steps, *reversed(reverse), closed=True)


class PersonConnectedToSixNodes(Solo48):
    icon_id = 'person-connected-to-six-nodes'
    keyshape = Keyshape.SQUARE
    category = 'business'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'connected', 'to', 'six', 'nodes')

    def build(self):
        axis=24
        circle(self,'head',axis,16,3)
        path(self,'body',(20,33),('L',(20,31)),('A',(axis,27),4,4,True),('A',(28,31),4,4,True),('L',(28,33)))
        for side in (-1,1):
         x=axis+side*15
         for row,y in enumerate((9,24,39)):
          name=f'node-{side}-{row}'
          circle(self,name,x,y,3)
          start=(x-side*3,y)
          end=((axis+side*3,16),(axis+side*4,31),(axis+side*4,33))[row]
          self.add_line('link-'+name,start,end)
          self.relate('connect',name,'link-'+name)
          self.relate('connect','head' if row==0 else 'body','link-'+name)
        self.mark_human_figure('person',head='head',torso='body-2',torso_junction='end')
