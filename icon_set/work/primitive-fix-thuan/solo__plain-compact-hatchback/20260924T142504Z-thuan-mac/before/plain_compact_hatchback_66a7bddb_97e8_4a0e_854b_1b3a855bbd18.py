'plain-compact-hatchback. Plan: Plain compact car outline and two equal circular wheels. Keyshape: HRECT_M, exact SOLO48 bounds. Construction: Lucide car: coherent shell and wheel attachments. Reduction: Kept the plain body and two equal wheels; adjusted wheel attachments to avoid crowded overlaps.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66a7bddb-97e8-4a0e-854b-1b3a855bbd18'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car side_66a7bddb-97e8-4a0e-854b-1b3a855bbd18.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-compact-hatchback'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('car', 'hatchback', 'vehicle', 'compact', 'wheels', 'transport', 'profile')

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
        path('body',(8,34),[('L',(4,28)),('L',(4,24)),('C',(14,18),(4,20),(10,20)),('C',(22,10),(18,14),(18,10)),('L',(30,10)),('C',(44,24),(34,10),(44,18)),('L',(44,28)),('L',(40,34))])
        self.add_line('sill',(16,34),(32,34))
        for x in (12,36):
         circle(f'wheel-{x}',x,34,4);self.relate('connect','body',f'wheel-{x}');self.relate('connect','sill',f'wheel-{x}')
