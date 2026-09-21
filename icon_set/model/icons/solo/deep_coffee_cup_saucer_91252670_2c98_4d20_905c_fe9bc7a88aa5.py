'deep-coffee-cup-saucer. Plan: Deep cup with right loop handle and separated saucer. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide coffee: handle joined at exact body points. Reduction: Keep cup and saucer, omit tiny rim thickness.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91252670-2c98-4d20-905c-fe9bc7a88aa5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/porcelain_91252670-2c98-4d20-905c-fe9bc7a88aa5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'deep-coffee-cup-saucer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('coffee', 'cup', 'saucer', 'handle', 'drink', 'ceramic')

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
        path('cup',(4,8),[('L',(32,8)),('L',(32,20)),('A',(18,32),14,12,True),('A',(4,20),14,12,True),('L',(4,8))],True)
        path('handle',(32,8),[('L',(36,8)),('A',(44,16),8,8,True),('A',(36,24),8,8,True),('L',(32,24))]);self.relate('connect','cup','handle')
        self.add_line('saucer',(6,40),(36,40))
