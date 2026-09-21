"""Three-Tined Spork with Rounded Handle
Plan: Three-tined broad bowl joins a rounded handle.
Keyshape: VRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af4b0bcf-b76c-4768-8a09-e4eb2d20860e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spork_af4b0bcf-b76c-4768-8a09-e4eb2d20860e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-tined-spork-with-rounded-handle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('spork', 'utensil', 'spoon', 'fork', 'tines', 'cutlery')

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
        path('spork',(14,4),[('C',(10,20),(11,8),(10,12)),('A',(18,28),8,8,False),('L',(18,38)),('A',(30,38),6,6,False),('L',(30,28)),('A',(38,20),8,8,False),('C',(34,4),(38,12),(37,8)),('L',(34,12)),('A',(24,12),5,5,True),('L',(24,4)),('L',(24,12)),('A',(14,12),5,5,True),('L',(14,4))],True)
