"""Mirrored Gherkin silhouette with smooth curve tangents and a single diagonal glazing band.
Omissions: Lower facade band and dense glazing omitted to preserve negative space.
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4836dd68-7a04-4bdf-9a6e-f17bd69f11c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/26-4836dd68-7a04-4bdf-9a6e-f17bd69f11c0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='gherkin-tower-silhouette'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('gherik', 'london')

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
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('tower',(24,4),[('C',(14,16),(21,4),(17,10)),('C',(10,28),(11,22),(10,24)),('C',(11,35),(10,31),(10,32)),('C',(16,44),(12,38),(14,42)),('L',(32,44)),('C',(37,35),(34,42),(36,38)),('C',(38,28),(38,32),(38,31)),('C',(34,16),(38,24),(37,22)),('C',(24,4),(31,10),(27,4))],True)
        self.add_line('facade-one',(14,16),(37,35))
        self.relate('connect','tower','facade-one')
