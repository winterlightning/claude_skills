"""A blank upright page with a triangular upper-right fold. VRECT_L preserves page proportions; source supplies fold and blank face. Lucide file informs a single rounded perimeter with attached fold. Fold endpoints are shared nodes; no text added."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d047f85-afa5-429d-afe6-932e1b6b7978'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/page_6d047f85-afa5-429d-afe6-932e1b6b7978.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'blank-page-triangular-fold'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Blank Page with Triangular Fold',)
    keywords = ('page', 'document', 'paper', 'fold', 'blank', 'sheet')
    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('page',(24,4),[('L',(12,4)),('A',(8,8),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,20)),('L',(24,4))],True)
        path('fold',(24,4),[('L',(24,16)),('A',(28,20),4,4,False),('L',(40,20))])
        join('page','fold')
