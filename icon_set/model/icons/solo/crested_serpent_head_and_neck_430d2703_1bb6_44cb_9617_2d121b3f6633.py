"""Crested Serpent Head and Neck
Plan: Swept crest and long serpentine neck
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful Lucide match; source directional silhouette.
Reduction: Remove eye and tongue to preserve broad flowing neck."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '430d2703-1bb6-44cb-9617-2d121b3f6633'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/basilisk_430d2703-1bb6-44cb-9617-2d121b3f6633.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crested-serpent-head-and-neck'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('serpent', 'basilisk', 'crest', 'snake', 'head', 'tongue', 'mythical')

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
        path('serpent',(8,44),[('C',(18,18),(30,40),(12,30)),('L',(10,10)),('L',(24,14)),('L',(22,4)),('L',(34,12)),('L',(40,18)),('L',(40,26)),('L',(30,26)),('C',(24,44),(42,38),(32,44))])
