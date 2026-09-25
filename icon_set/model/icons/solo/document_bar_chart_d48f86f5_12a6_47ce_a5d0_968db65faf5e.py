"""Upright clipped document with three descending bars sharing an extended baseline."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d48f86f5-12a6-47ce-a5d0-968db65faf5e'
SOURCE_PATH='pictographic-primitives/other/file data bars_d48f86f5-12a6-47ce-a5d0-968db65faf5e.svg'
AUTHOR='gpt-6'
PLAN='Three descending bars join one shared, slightly extended baseline; shared series retains their exact spacing.'
CONSTRUCTION_REFERENCE='file-chart-column original and atomic-debug: equally spaced vertical chart members; source controls descending order.'
OMISSIONS='Document proportions broadened to preserve three clear bars.'

class Drawing(Solo48):
    icon_id='document-bar-chart'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('file', 'data', 'bars')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.file(6,6,42,42)
        for i in range(3):
            x=16+8*i;y=16+5*i
            self.add_line(f'bar-{i}',(x,y),(x,33))
        self.add_polyline('baseline',(15,33),(24,33),(33,33))
        for i in range(3):self.relate('connect',f'bar-{i}','baseline')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '3b6c956206b40800c20100a8e9b7ab682b3e0920a2ffee4608a3f74b1f84ce65', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'd48f86f5-12a6-47ce-a5d0-968db65faf5e'}
