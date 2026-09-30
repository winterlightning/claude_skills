"""Standing Mountain Lion in Profile
Plan: Long-bodied right-facing mountain lion with small pointed ear and trailing tail.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22e27c10-01b3-4e0b-9a9f-8c3e35390cda'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cougar_22e27c10-01b3-4e0b-9a9f-8c3e35390cda.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-mountain-lion-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cougar', 'lion', 'mountain', 'cat', 'wildlife', 'animal', 'standing')

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
        path('cat',(6,32),[('C',(15,20),(6,22),(9,20)),('L',(27,20)),('L',(33,10)),('L',(36,8)),('L',(38,13)),('C',(44,19),(43,14),(44,16)),('L',(39,24)),('L',(38,40)),('L',(29,40)),('L',(28,30)),('L',(17,30)),('L',(14,40)),('L',(6,40)),('L',(6,32))],True)
        path('tail',(6,32),[('C',(4,35),(6,34),(5,35))]);self.relate('connect','tail','cat')
