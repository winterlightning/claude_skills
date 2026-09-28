"""Rounded diagonal paintbrush with long handle, broad ferrule seam and swept lower-left bristles. Centerline6,6–42,42.
Lucide construction reference: paintbrush.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0ceae122-4d52-44c0-84da-c9168dce14c9'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_0ceae122-4d52-44c0-84da-c9168dce14c9.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/brush_0ceae122-4d52-44c0-84da-c9168dce14c9.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/brush_0ceae122-4d52-44c0-84da-c9168dce14c9.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='rounded-artist-paintbrush-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('rounded', 'artist', 'paintbrush')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        path('brush',(6,42),[('B',(12,36),(6,29),(15,26)),('L',(22,22)),('L',(34,6)),('B',(38,6),(42,10),(42,14)),('L',(27,29)),('B',(29,40),(18,42),(6,42))],True)
        self.add_line('ferrule',(15,26),(27,29));self.relate('connect','ferrule','brush')
