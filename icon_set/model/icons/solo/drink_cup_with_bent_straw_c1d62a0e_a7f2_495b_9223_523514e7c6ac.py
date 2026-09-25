'drink-cup-with-bent-straw. Plan: Tapered cup, bent straw and joined wavy liquid edge. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide cup-soda: tapered body and bent straw. Reduction: Preserve liquid wave; omit rim thickness.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1d62a0e-a7f2-495b-9223-523514e7c6ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bubble tea special_c1d62a0e-a7f2-495b-9223-523514e7c6ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'drink-cup-with-bent-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('drink', 'cup', 'straw', 'liquid', 'beverage', 'glass', 'refreshment')

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
        path('cup',(8,16),[('L',(40,16)),('L',(36,40)),('A',(32,44),4,4,True),('L',(16,44)),('A',(12,40),4,4,True),('L',(8,16))],True)
        self.add_polyline('straw',(24,16),(28,4),(36,4));self.relate('connect','cup','straw')
        path('liquid',(10,28),[('C',(24,28),(16,32),(20,32)),('C',(38,28),(28,24),(34,24))]);self.relate('connect','cup','liquid')
