'typewriter-with-blank-upright-paper. Plan: Blank sheet, roller and tapered base with shared center axis. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide book: blank paper; rounded rectangle carriage. Reduction: Paper, body and roller share one horizontal carriage edge; removed duplicate strokes and tiny knobs.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '10b0c285-5a68-47d5-aec7-ad4ae1ef562b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__typewriter-with-blank-upright-paper/20260927T140026Z-thuan-mac-1/reference/content typing machine 3_10b0c285-5a68-47d5-aec7-ad4ae1ef562b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'typewriter-with-blank-upright-paper'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('typewriter', 'paper', 'carriage', 'writing', 'machine', 'office', 'vintage')

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

        path('paper',(12,24),[('L',(12,12)),('A',(16,8),4,4,True),('L',(32,8)),('A',(36,12),4,4,True),('L',(36,24))])
        path('base',(12,24),[('L',(4,36)),('L',(4,38)),('A',(6,40),2,2,True),('L',(42,40)),('A',(44,38),2,2,True),('L',(44,36)),('L',(36,24))])
        self.add_line('roller',(4,24),(44,24))
        self.relate('connect','paper','roller');self.relate('connect','base','roller');self.relate('connect','paper','base')
