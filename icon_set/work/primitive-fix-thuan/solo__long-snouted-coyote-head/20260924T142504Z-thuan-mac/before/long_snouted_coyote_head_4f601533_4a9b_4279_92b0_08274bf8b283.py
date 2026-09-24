"""Long Snouted Coyote Head
Plan: Two tall ears and long right-facing muzzle
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful Lucide match; source silhouette.
Reduction: Remove eye and inner ear lines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f601533-4a9b-4279-92b0-08274bf8b283'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/coyote_4f601533-4a9b-4279-92b0-08274bf8b283.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-snouted-coyote-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('coyote', 'canine', 'head', 'animal', 'wildlife', 'ears', 'muzzle')

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
        path('head',(8,44),[('L',(12,28)),('L',(8,4)),('L',(20,16)),('L',(26,4)),('L',(28,20)),('L',(40,26)),('L',(36,34)),('L',(24,34)),('L',(20,44))])
