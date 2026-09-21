'round-dial-desk-telephone. Plan: Smooth receiver, tapered body and circular rotary dial. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide phone: broad receiver curve. Reduction: Squarer base enlarges the rotary dial and preserves a visible circular hole.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ac72916-7ade-454e-ab5a-35dfc8365bf8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/phone rotary_1ac72916-7ade-454e-ab5a-35dfc8365bf8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-dial-desk-telephone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('telephone', 'rotary', 'dial', 'receiver', 'desk', 'phone')

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
        path('receiver',(6,14),[('C',(24,6),(6,6),(16,6)),('C',(42,14),(32,6),(42,6))])
        path('base',(14,18),[('L',(34,18)),('L',(42,42)),('L',(6,42)),('L',(14,18))],True)
        circle('dial',24,30,3)
