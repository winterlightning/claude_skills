"""Boxing Glove
Plan: Rounded boxing glove, curled thumb and separate wrist cuff.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '552d0a5b-427c-4de3-acdb-1a7a7bbb5bdc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/video game boxing_552d0a5b-427c-4de3-acdb-1a7a7bbb5bdc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boxing-glove-reference-552d0a5b'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('boxing', 'glove', 'sport', 'punch', 'fist', 'equipment')

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
        path('glove',(16,36),[('C',(8,20),(8,31),(8,26)),('L',(8,14)),('A',(18,4),10,10,True),('L',(30,4)),('A',(40,14),10,10,True),('L',(40,22)),('C',(32,36),(40,31),(36,34)),('L',(16,36))],True)
        self.add_polyline('cuff',(16,36),(16,44),(32,44),(32,36));self.relate('connect','cuff','glove')
        path('thumb',(17,15),[('A',(25,23),8,8,False),('L',(40,23))]);self.relate('connect','thumb','glove')
