"""Clipped document with broad matched 90-degree angle brackets."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a7885b17-70fa-431a-8397-cf8f653fa82c'
SOURCE_PATH='pictographic-primitives/other/file code left_a7885b17-70fa-431a-8397-cf8f653fa82c.svg'
AUTHOR='gpt-6'
PLAN='Bracket tips lie at x15 and x33, with endpoints at x20 and x28. Matching angles are wider and clearer than the old narrow glyphs.'
CONSTRUCTION_REFERENCE='file-code original and atomic-debug: opposing chevrons and continuous paper contour.'
OMISSIONS='No defining features omitted. Document proportions broadened.'

class Drawing(Solo48):
    icon_id='source-code-file'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('file', 'code', 'left')

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
        axis=24
        self.add_polyline('left-bracket',(20,18),(15,24),(20,30))
        self.add_polyline('right-bracket',(2*axis-20,18),(2*axis-15,24),(2*axis-20,30))

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '48c27dca8c49c5cc0868fcc902102dbc9a718ff41f55d6206718e5f7908b2959', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'a7885b17-70fa-431a-8397-cf8f653fa82c'}
