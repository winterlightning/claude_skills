"""Three-Person Organization Hierarchy.
Plan: Three circular heads, radius2, and open rounded shoulder arches. Parent center(24,8), body top18; child centers(12,28),(36,28), bodies top38: exactly 8 centerline / 4 ink gaps. Hierarchy connects parent shoulder ends to child head crowns. Bounds (6,6)-(42,42).
References: human_ref/user.svg circular heads and broad open shoulders; Lucide network for shared hierarchy branches.
Reduction: Closed bust baselines and neck details omitted to preserve all three people and their exact detached head spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a9dfee64-d94e-5290-9f2d-1568f42ab28b'
SOURCE_PATH = 'pictographic-primitives/companies/workflow teamwork hierarchy_a9dfee64-d94e-5290-9f2d-1568f42ab28b.svg'
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


def rectangle(icon,name,x1,y1,x2,y2,r=2,knots=()):
    """One box owns its radii and splits receiving walls at true attachment nodes."""
    xs=sorted({(x1+x2)//2,*knots})
    xs=[x for x in xs if x1+r<x<x2-r]
    ym=(y1+y2)//2
    steps=[('L',(x,y1)) for x in xs]
    steps += [('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True)]
    if y1+r<ym<y2-r:steps += [('L',(x2,ym))]
    steps += [('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True)]
    steps += [('L',(x,y2)) for x in reversed(xs)]
    steps += [('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True)]
    if y1+r<ym<y2-r:steps += [('L',(x1,ym))]
    steps += [('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)]
    path(icon,name,(x1+r,y1),*steps,closed=True)

class ThreePersonOrganizationHierarchy(Solo48):
    icon_id = 'three-person-organization-hierarchy'
    keyshape = Keyshape.SQUARE
    category = 'companies'
    categories = ('primitives', 'companies')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('three-person', 'organization', 'hierarchy')
    def build(self):
        for name,cx,cy in (('parent',24,8),('left',12,28),('right',36,28)):
         circle(self,name+'-head',cx,cy,2)
         top=cy+2+8
         path(self,name+'-body',(cx-6,top+4),('A',(cx,top),6,4,True),('A',(cx+6,top+4),6,4,True))
         self.mark_human_figure(name,head=name+'-head',torso=name+'-body-1',torso_junction='end')
        self.add_polyline('branch-left',(18,22),(12,22),(12,26))
        self.add_polyline('branch-right',(30,22),(36,22),(36,26))
        for side in ('left','right'):
         self.relate('connect','parent-body','branch-'+side)
         self.relate('connect',side+'-head','branch-'+side)
