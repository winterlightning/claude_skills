'keypad-office-telephone. Plan: Broad handset above trapezoid base; equal keypad row. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide phone: smooth receiver. Reduction: Nine keypad marks reduced to two evenly spaced dots; curved receiver and tapered desk base remain.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c56980d4-fcc1-42c9-bdff-b4c9ba3e1d71'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/phone office_c56980d4-fcc1-42c9-bdff-b4c9ba3e1d71.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'keypad-office-telephone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('telephone', 'phone', 'keypad', 'desk', 'receiver', 'communication')

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
        path('receiver',(4,16),[('C',(24,8),(4,8),(16,8)),('C',(44,16),(32,8),(44,8))])
        path('base',(12,20),[('L',(36,20)),('L',(44,40)),('L',(4,40)),('L',(12,20))],True)
        for x in (20,28):self.add_dot(f'key-{x}',(x,30))
