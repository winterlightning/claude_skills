"""Facial Sheet Mask with Openings
Plan: Symmetric fabric mask with two eyes and an oval mouth opening.
Keyshape: CIRCLE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Fabric perimeter regularized to a circle; three openings kept round for native clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '513a2427-485b-41c7-9e82-bb9224e8b448'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/body care mask_513a2427-485b-41c7-9e82-bb9224e8b448.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'facial-sheet-mask-with-openings'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mask', 'facial', 'skincare', 'sheet', 'eyes', 'mouth', 'beauty')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        circle('mask',24,24,20)
        for x in (17,31):circle(f'eye-{x}',x,19,3)
        circle('mouth',24,32,3)
