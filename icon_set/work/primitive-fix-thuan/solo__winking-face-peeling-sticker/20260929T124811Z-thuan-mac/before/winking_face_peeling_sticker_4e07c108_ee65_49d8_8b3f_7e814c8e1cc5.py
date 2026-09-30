"""Winking Face Sticker.

Plan: Circle center24 radius20, detached wink/dot eye, shallow smile, and an enlarged lower-right peel.
Construction: Lucide sticky-note original/debug: explicit fold junction; circular smiling sticker retained.
Reduction: Smile shortened to clear the peel; wink retained as a small arch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e07c108-ee65-49d8-8b3f-7e814c8e1cc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/13-4e07c108-ee65-49d8-8b3f-7e814c8e1cc5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'winking-face-peeling-sticker'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('winking', 'face', 'peeling', 'sticker')

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
        path('sticker',(40,36),[('A',(24,4),20,20,False),('A',(4,24),20,20,False),('A',(24,44),20,20,False),('L',(40,36))],True)
        path('fold',(24,44),[('C',(40,36),(24,34),(31,32))]);join('sticker','fold')
        self.add_dot('eye',(15,17));path('wink',(27,18),[('A',(33,18),3,2,True)])
        path('smile',(13,27),[('C',(23,28),(15,30),(20,31))])
