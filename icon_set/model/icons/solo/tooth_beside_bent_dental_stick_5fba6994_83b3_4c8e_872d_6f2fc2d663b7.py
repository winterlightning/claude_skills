"""Tooth with mirrored flowing crown and roots, beside a dental pick with a round bent tip.
Omissions: Double wall of dental pick reduced to a consistent single centerline.
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5fba6994-83b3-4c8e-872d-6f2fc2d663b7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/dental stick tooth_5fba6994-83b3-4c8e-872d-6f2fc2d663b7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tooth-beside-bent-dental-stick'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('dental', 'stick', 'tooth')

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('tooth',(30,9),[('C',(24,6),(27,9),(27,6)),('C',(18,14),(20,6),(18,10)),('C',(21,25),(18,19),(21,21)),('C',(24,35),(21,30),(21,35)),('C',(30,25),(27,35),(27,25)),('C',(36,35),(33,25),(33,35)),('C',(39,25),(39,35),(39,30)),('C',(42,14),(39,21),(42,19)),('C',(36,6),(42,10),(40,6)),('C',(30,9),(33,6),(33,9))],True)
        self.path('pick',(10,12),[('L',(8,15)),('C',(6,20),(6,17),(6,18)),('C',(9,26),(6,22),(7,24)),('L',(16,42))])
