'looped-cord-and-two-pin-plug. Plan: Single serpentine cord feeding a right-facing two-pin plug. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide cable: coherent cable path and plug attachments. Reduction: Two broad cable turns feed a rectangular plug with two actual projecting pins; removed additional original loops.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1427d2c-be06-40e8-b02b-6218ce9bc520'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cord_e1427d2c-be06-40e8-b02b-6218ce9bc520.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'looped-cord-and-two-pin-plug'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cord', 'cable', 'plug', 'electric', 'power', 'loop', 'connector')

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

        path('cord',(36,8),[('L',(12,8)),('A',(12,24),8,8,False),('A',(12,40),8,8,True),('L',(28,40))])
        rect('plug',28,24,12,16,0);self.relate('connect','cord','plug')
        for y in (28,36):
         self.add_line(f'pin-{y}',(40,y),(44,y));self.relate('connect','plug',f'pin-{y}')
