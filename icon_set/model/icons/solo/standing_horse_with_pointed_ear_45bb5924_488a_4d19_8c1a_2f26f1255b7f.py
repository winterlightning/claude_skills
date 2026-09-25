"""Standing Horse with Pointed Ear
Plan: Standing horse with upright neck, pointed ear and rear hock.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45bb5924-488a-4d19-8c1a-2f26f1255b7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/colt_45bb5924-488a-4d19-8c1a-2f26f1255b7f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-horse-with-pointed-ear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('horse', 'animal', 'standing', 'ear', 'muzzle', 'legs', 'equine')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('horse',(6,30),[('L',(6,25)),('A',(16,15),10,10,True),('L',(27,15)),('L',(35,6)),('L',(35,11)),('L',(42,18)),('C',(38,26),(42,23),(41,27)),('L',(34,23)),('L',(34,42)),('L',(26,42)),('L',(25,29)),('L',(19,27)),('L',(15,34)),('L',(14,42)),('L',(6,42)),('L',(6,30))],True)
