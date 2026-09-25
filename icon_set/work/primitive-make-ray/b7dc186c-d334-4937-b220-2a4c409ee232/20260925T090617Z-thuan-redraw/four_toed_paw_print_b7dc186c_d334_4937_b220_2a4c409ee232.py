"""Restore four oval toe pads and a broad softly lobed central pad, preserving bilateral symmetry.
Symbol plan: Shared nodes own true connections; repeated nodes, petals and toes use shared dimensions.
Lucide construction: paw-print. Original reference establishes full subject and arrangement.
Keyshape SQUARE; source proportions preserved with explicit exceptions if required.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b7dc186c-d334-4937-b220-2a4c409ee232'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__four-toed-paw-print/20260925T090617Z-thuan-mac/reference/furry_b7dc186c-d334-4937-b220-2a4c409ee232.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='four-toed-paw-print'
    keyshape=Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('four', 'toed', 'paw', 'print')
    def build(self):

        for i,(x,y) in enumerate([(9,22),(17,10),(31,10),(39,22)]):
            self.path('toe-'+str(i),(x,y-5),[('A',(x,y+5),4,5,True),('A',(x,y-5),4,5,True)],True)
        self.path('pad',(24,24),[('C',(34,32),(30,24),(30,29)),('C',(32,44),(41,37),(40,44)),('C',(24,42),(28,44),(27,42)),('C',(16,44),(21,42),(20,44)),('C',(14,32),(8,44),(7,37)),('C',(24,24),(18,29),(18,24))],True)


    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)


