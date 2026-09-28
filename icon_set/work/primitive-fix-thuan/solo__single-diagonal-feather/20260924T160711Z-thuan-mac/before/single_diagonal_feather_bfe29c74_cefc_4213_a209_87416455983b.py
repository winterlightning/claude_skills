"""Single Diagonal Feather
Plan: Pointed asymmetric feather with shaft and a notch.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide feather: diagonal shaft and joined vane.
Reduction: Small notch omitted; broad vane and long diagonal inner quill retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfe29c74-cefc-4213-a209-87416455983b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plume_bfe29c74-cefc-4213-a209-87416455983b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-diagonal-feather'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('feather', 'plume', 'quill', 'bird', 'vane', 'writing')

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
        path('vane',(12,36),[('C',(6,24),(6,35),(6,30)),('C',(42,6),(6,10),(26,6)),('C',(12,36),(42,26),(26,42))],True)
        path('quill',(6,42),[('L',(12,36)),('L',(30,18))]);self.relate('connect','vane','quill')
