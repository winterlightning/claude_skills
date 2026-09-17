'person-connected-to-six-nodes: Restore a recognizable central head-and-shoulders avatar surrounded by six connected circular nodes. Repaired original in place.'
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
    keyshape = Keyshape.FREE
    category = 'business'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'connected', 'to', 'six', 'nodes')

    def build(self):
        # Symbol plan: Restore a recognizable central head-and-shoulders avatar surrounded by six connected circular nodes.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        circle('head',24,16,4)
        path('bust',(14,38),[('A',(24,28),10,10,True),('A',(34,38),10,10,True),('L',(14,38))],True)
        for n,x,y in [('tl',5,5),('tr',43,5),('ml',5,24),('mr',43,24),('bl',5,43),('br',43,43)]:circle(n,x,y,3)
        for n,a,b,node in [('top-l',(8,7),(20,16),'tl'),('top-r',(40,7),(28,16),'tr'),('middle-l',(8,24),(17,31),'ml'),('middle-r',(40,24),(31,31),'mr'),('bottom-l',(8,41),(14,38),'bl'),('bottom-r',(40,41),(34,38),'br')]:
         line(n,a,b);join(n,node);join(n,'head' if n.startswith('top') else 'bust')
