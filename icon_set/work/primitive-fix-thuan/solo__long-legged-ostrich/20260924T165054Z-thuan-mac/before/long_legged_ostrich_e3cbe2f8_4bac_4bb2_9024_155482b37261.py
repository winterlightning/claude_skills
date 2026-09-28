"""Long-Legged Ostrich
Plan: Small-headed long-necked ostrich with broad body and two long legs.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Long neck reduced to a single curved stroke; small head, beak, broad body and two legs retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3cbe2f8-4bac-4bb2-9024-155482b37261'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ostrich_e3cbe2f8-4bac-4bb2-9024-155482b37261.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-legged-ostrich'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ostrich', 'bird', 'neck', 'legs', 'wildlife', 'standing')

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
        path('body',(6,28),[('C',(18,20),(11,19),(15,18)),('C',(30,26),(24,20),(28,23)),('C',(28,34),(35,31),(33,34)),('L',(18,34)),('C',(14,31),(16,34),(15,32)),('L',(6,28))],True)
        path('neck',(30,26),[('C',(36,12),(39,25),(36,18))]);self.relate('connect','neck','body')
        circle('head',36,9,3);self.relate('connect','neck','head')
        self.add_line('beak',(39,9),(42,10));self.relate('connect','beak','head')
        self.add_polyline('leg-a',(18,34),(16,42),(21,42));self.add_polyline('leg-b',(28,34),(31,42),(36,42));self.relate('connect','leg-a','body');self.relate('connect','leg-b','body')
