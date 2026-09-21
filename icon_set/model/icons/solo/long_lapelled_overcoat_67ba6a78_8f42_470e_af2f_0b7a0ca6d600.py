'long-lapelled-overcoat. Plan: Shared shoulder and hem axes; long coat silhouette with central opening. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide shirt: connected sleeve silhouette. Reduction: Omit pocket slits and secondary lapel notches.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67ba6a78-8f42-470e-af2f-0b7a0ca6d600'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/overcoat_67ba6a78-8f42-470e-af2f-0b7a0ca6d600.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-lapelled-overcoat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('overcoat', 'coat', 'clothing', 'lapels', 'sleeves', 'outerwear')

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
        path('coat',(18,4),[('L',(30,4)),('L',(36,10)),('L',(40,32)),('L',(32,32)),('L',(32,44)),('L',(16,44)),('L',(16,32)),('L',(8,32)),('L',(12,10)),('L',(18,4))],True)
        self.add_polyline('opening',(18,4),(24,20),(30,4));self.relate('connect','coat','opening')
        self.add_line('seam',(24,20),(24,44));self.relate('connect','opening','seam');self.relate('connect','coat','seam')
