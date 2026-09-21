"""Crossed Short Swords
Plan: Two diagonal blades with crossguards and short handles
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide swords crossing construction.
Reduction: Reduce blade interior and handle outlines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52eb993c-4cd6-435c-8e9c-713a9058976f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antique swords_52eb993c-4cd6-435c-8e9c-713a9058976f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-short-swords'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('swords', 'crossed', 'blades', 'weapons', 'antique', 'guards', 'handles')

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
        path('blade-a',(12,30),[('L',(32,10)),('L',(42,6)),('L',(38,16)),('L',(18,36))])
        path('blade-b-top',(24,18),[('L',(16,10)),('L',(6,6)),('L',(10,16)),('L',(18,24))]);self.relate('connect','blade-a','blade-b-top')
        self.add_line('blade-b-bottom',(27,27),(36,36))
        for name,a,b,c,d in [('a',(6,28),(20,42),(14,34),(6,42)),('b',(28,42),(42,28),(34,34),(42,42))]:
            self.add_line('guard-'+name,a,b);self.add_line('handle-'+name,c,d);self.relate('connect','guard-'+name,'handle-'+name)
        self.relate('connect','blade-a','guard-a');self.relate('connect','blade-b-bottom','guard-b')

        self.relate('connect','blade-b-bottom','blade-a')
