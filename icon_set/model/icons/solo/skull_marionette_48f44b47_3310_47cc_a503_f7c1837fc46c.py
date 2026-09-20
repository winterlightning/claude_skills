"""Skeleton Skull Puppet.

Plan: Skull beneath crossed marionette bars, two short strings; bounds (8,4)-(40,44).
Construction: Lucide skull: domed cranium, eye sockets and short jaw; crossed bars establish marionette.
Reduction: Tooth seams reduced to one and tiny nose omitted; two strings retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48f44b47-3310-47cc-a503-f7c1837fc46c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/07-48f44b47-3310-47cc-a503-f7c1837fc46c.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'skull-marionette'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('skull', 'marionette')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        poly('bar-one',(8,4),(24,9),(40,14));poly('bar-two',(8,14),(24,9),(40,4));join('bar-one','bar-two')
        path('skull',(10,33),[('A',(24,19),14,14,True),('A',(38,33),14,14,True),('L',(32,36)),('L',(32,44)),('L',(16,44)),('L',(16,36)),('L',(10,33))],True)
        self.add_dot('eye-left',(20,29));self.add_dot('eye-right',(28,29))
        line('teeth',(24,36),(24,44));join('skull','teeth')
        line('string-left',(8,14),(8,17));line('string-right',(40,14),(40,17));join('bar-two','string-left');join('bar-one','string-right')
