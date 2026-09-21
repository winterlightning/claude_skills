'bucket-with-draped-cleaning-cloth. Plan: Tapered bucket with broad cloth overlapping left rim. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide cup-soda: tapered bowl; source cloth overlap. Reduction: Cloth hides the bucket rim and left wall; removed rolled rim and crease instead of drawing overlapping hidden edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebba6b28-aad4-41af-8355-36c8928b07d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleaning bucket cloth_ebba6b28-aad4-41af-8355-36c8928b07d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bucket-with-draped-cleaning-cloth'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bucket', 'cloth', 'cleaning', 'rag', 'rim', 'household', 'pail')

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

        path('bucket',(24,12),[('L',(40,12)),('L',(36,40)),('A',(32,44),4,4,True),('L',(16,44)),('A',(12,40),4,4,True),('L',(12,28))])
        path('cloth',(8,12),[('A',(16,4),8,8,True),('L',(24,4)),('L',(24,12)),('L',(24,28)),('L',(12,28)),('L',(8,28)),('L',(8,12))],True)
        self.relate('connect','bucket','cloth')
