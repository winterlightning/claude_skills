'broad-stemmed-chalice. Plan: Bowl with flat rim, deep half ellipse, central stem and wide foot. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide coffee: smooth bowl construction. Reduction: Use single stem and straight foot; omit doubled stem outline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fba39cd7-3b5f-45a3-a869-00c17e14563b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/chalice_fba39cd7-3b5f-45a3-a869-00c17e14563b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-stemmed-chalice'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('chalice', 'goblet', 'cup', 'stem', 'bowl', 'drink', 'tableware')

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
        path('bowl',(8,4),[('L',(40,4)),('L',(40,12)),('A',(24,28),16,16,True),('A',(8,12),16,16,True),('L',(8,4))],True)
        self.add_line('stem',(24,28),(24,44));self.relate('connect','bowl','stem')
        self.add_line('foot',(12,44),(36,44));self.relate('connect','stem','foot')
