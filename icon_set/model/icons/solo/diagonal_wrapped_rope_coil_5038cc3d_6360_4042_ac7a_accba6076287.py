'diagonal-wrapped-rope-coil. Plan: Diagonal rope loops attached to one broad crossing wrap. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide cable: rounded return loops. Reduction: Reduce paired wrapping bands to one coherent broad band.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5038cc3d-6360-4042-ac7a-accba6076287'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/outdoors rope 1_5038cc3d-6360-4042-ac7a-accba6076287.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-wrapped-rope-coil'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rope', 'coil', 'climbing', 'loops', 'wrapped', 'camping')

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
        path('wrap',(12,20),[('L',(28,36)),('A',(36,28),6,6,False),('L',(20,12)),('A',(12,20),6,6,False)],True)
        path('upper',(20,12),[('C',(34,6),(26,6),(30,6)),('C',(42,14),(38,6),(42,10)),('C',(36,28),(42,20),(40,24))]);self.relate('connect','wrap','upper')
        path('lower',(12,20),[('C',(6,34),(6,24),(6,30)),('C',(14,42),(6,38),(10,42)),('C',(28,36),(20,42),(24,40))]);self.relate('connect','wrap','lower')
