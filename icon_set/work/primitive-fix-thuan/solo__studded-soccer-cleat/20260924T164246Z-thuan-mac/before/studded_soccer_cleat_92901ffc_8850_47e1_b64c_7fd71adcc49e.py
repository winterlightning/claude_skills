"""Studded Soccer Cleat
Plan: Left-facing football cleat with raised heel, lace and three studs.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Small lace mark omitted after its interior spacing failed; the cleated sole and shaped upper remain.  Fine studs reduced to three evenly spaced; two lace marks reduced to one."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92901ffc-8850-47e1-b64c-7fd71adcc49e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleat_92901ffc-8850-47e1-b64c-7fd71adcc49e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'studded-soccer-cleat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cleat', 'soccer', 'shoe', 'studs', 'footwear', 'sport', 'boot')

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
        path('shoe',(4,30),[('C',(13,23),(4,25),(8,23)),('L',(24,16)),('L',(27,8)),('C',(37,17),(31,16),(33,20)),('L',(42,10)),('C',(44,24),(44,14),(44,19)),('L',(44,32)),('L',(4,32)),('L',(4,30))],True)
        for x in (10,24,38):self.add_line(f'stud-{x}',(x,32),(x,40));self.relate('connect',f'stud-{x}','shoe')
        # The small lace mark was omitted after strict interior-spacing review.
