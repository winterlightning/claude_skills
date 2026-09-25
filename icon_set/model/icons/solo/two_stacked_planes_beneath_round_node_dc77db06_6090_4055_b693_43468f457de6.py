"""Two Stacked Planes Beneath Round Node
Plan: Two layered diamond planes beneath a round node.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Planes separated vertically; node and both full plane silhouettes retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc77db06-6090-4055-b693-43468f457de6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/elemental mediastore 1_dc77db06-6090-4055-b693-43468f457de6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-stacked-planes-beneath-round-node'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'servers'
    categories = ('servers', 'primitive', 'primitives')
    aliases = ()
    keywords = ('layers', 'planes', 'stack', 'node', 'circle', 'storage', 'diagram')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        circle('node',24,10,6)
        self.add_polyline('top',(8,24),(24,16),(40,24),(28,30),(24,32),(20,30),closed=True);self.relate('connect','node','top')
        self.add_polyline('lower',(20,30),(8,36),(24,44),(40,36),(28,30));self.relate('connect','lower','top')
