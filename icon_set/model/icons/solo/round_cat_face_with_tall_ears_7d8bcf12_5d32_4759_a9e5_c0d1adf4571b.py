"""Round Cat Face with Tall Ears
Plan: Paired tall ears, round face, dot eyes and double smile.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Whiskers omitted to keep smile and eye clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d8bcf12-5d32-4759-a9e5-c0d1adf4571b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/american shorthair_7d8bcf12-5d32-4759-a9e5-c0d1adf4571b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-cat-face-with-tall-ears'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cat', 'face', 'ears', 'whiskers', 'pet', 'feline', 'smile')

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

        path('cat-face',(8,21),[('C',(6,12),(6,17),(6,14)),('C',(10,6),(6,8),(7,6)),('C',(17,13),(13,6),(15,9)),('C',(31,13),(22,11),(26,11)),('C',(38,6),(33,9),(35,6)),('C',(42,12),(41,6),(42,8)),('C',(40,21),(42,14),(42,17)),('C',(42,28),(42,24),(42,26)),('C',(24,42),(42,36),(34,42)),('C',(6,28),(14,42),(6,36)),('C',(8,21),(6,26),(6,24))],True)
        for x in (17,31):self.add_dot(f'eye-{x}',(x,22))
        path('smile',(18,31),[('C',(24,31),(20,33),(22,33)),('C',(30,31),(26,33),(28,33))])
