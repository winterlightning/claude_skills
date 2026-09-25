'screen-above-two-classroom-chairs. Plan: Wide screen over two identical chairs in a row. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide sofa: rounded back and direct leg attachments. Reduction: Remove armrests; preserve two chairs and separate screen.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deaa9206-7294-4382-b4df-d842d1f76b4b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/classroom_deaa9206-7294-4382-b4df-d842d1f76b4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'screen-above-two-classroom-chairs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('classroom', 'screen', 'chairs', 'seating', 'education', 'furniture', 'presentation')

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
        rect('screen',6,6,36,16,3)
        for x in (6,30):
         rect(f'chair-{x}',x,30,12,8,2)
         for xx in (x,x+12):
          self.add_line(f'leg-{xx}',(xx,38),(xx,42));self.relate('connect',f'chair-{x}',f'leg-{xx}')
