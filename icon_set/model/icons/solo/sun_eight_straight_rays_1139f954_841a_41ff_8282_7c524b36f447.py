"""Sun with Eight Straight Rays
Plan: Central circle and eight evenly arranged detached rays. Axis and diagonal ray pairs are shared.
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: Lucide sun: round core with separated rays.
Reduction: Shortened rays to retain the required clear halo.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1139f954-841a-41ff-8282-7c524b36f447'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pompom_1139f954-841a-41ff-8282-7c524b36f447.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-eight-straight-rays'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sun', 'rays', 'daylight', 'weather', 'light', 'circle')

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
        circle('sun',24,24,9)
        for j,(a,b) in enumerate([((24,4),(24,6)),((44,24),(42,24)),((24,44),(24,42)),((4,24),(6,24)),((10,10),(11,11)),((38,10),(37,11)),((38,38),(37,37)),((10,38),(11,37))]):self.add_line(f'ray-{j}',a,b)

SOURCE_REFERENCES = (('9b208226-72aa-4fe0-b384-8dbba87a42dc', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sunbeam_9b208226-72aa-4fe0-b384-8dbba87a42dc.svg'),)
