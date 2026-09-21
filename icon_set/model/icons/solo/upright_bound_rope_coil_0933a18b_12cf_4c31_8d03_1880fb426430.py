'upright-bound-rope-coil. Plan: Vertical rope loop with central binding and curled free end. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide cable: coherent curve and rounded turns. Reduction: Reduce three binding wraps to one wide wrap and inner loops to open regions.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0933a18b-12cf-4c31-8d03-1880fb426430'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/outdoors rope_0933a18b-12cf-4c31-8d03-1880fb426430.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-bound-rope-coil'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rope', 'coil', 'climbing', 'binding', 'loops', 'cord')

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
        rect('binding',8,20,24,8,4)
        path('upper-loop',(12,20),[('L',(12,12)),('A',(28,12),8,8,True),('L',(28,20))]);self.relate('connect','binding','upper-loop')
        path('lower-loop',(12,28),[('L',(12,36)),('A',(28,36),8,8,False),('L',(28,28))]);self.relate('connect','binding','lower-loop')
        path('tail',(32,24),[('L',(36,24)),('A',(40,28),4,4,True),('L',(40,40))]);self.relate('connect','binding','tail')
