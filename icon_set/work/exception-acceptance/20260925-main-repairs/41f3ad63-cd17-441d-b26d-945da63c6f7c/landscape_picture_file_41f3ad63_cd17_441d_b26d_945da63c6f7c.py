"""Clipped document containing a sun and a closed two-peak mountain landscape."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='41f3ad63-cd17-441d-b26d-945da63c6f7c'
SOURCE_PATH='pictographic-primitives/files/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg'
AUTHOR='gpt-6'
PLAN='Two peaks now identify the landscape. Sun is a complete radius-2 circle, using the existing small-circle rule.'
CONSTRUCTION_REFERENCE='file-code original and atomic-debug: clipped document with smooth corner construction; source supplies landscape.'
OMISSIONS='Mountain baseline omitted after the closed two-peak candidate produced a narrow triangular pocket. Sun reduced.'

class Drawing(Solo48):
    icon_id='landscape-picture-file'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('image', 'file')

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
        self.circle('sun',17,17,2)
        self.add_polyline('mountains',(15,33),(20,28),(24,32),(29,23),(33,33))

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'b83128efd9fe9c6826679fee0b049555f10eacf23756b29ad6da3e2abada2c6e', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '41f3ad63-cd17-441d-b26d-945da63c6f7c'}
