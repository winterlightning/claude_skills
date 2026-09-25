"""Five upright equalizer strokes at9-unit intervals; heights vary toward taller middle. Outlined bar widths reduced to single strokes because five hollow bars cannot fit with SOLO48 clearance. Centerline6,6–42,42.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5914bd56-799d-4aed-872f-a8f85da47371'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/logos/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='audio-equalizer-sound-bars-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "logos"
    aliases=()
    keywords=('audio', 'equalizer', 'sound', 'bars')
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

        for i,(x,y0,y1) in enumerate([(6,20,34),(15,12,38),(24,8,42),(33,6,38),(42,18,32)]):self.add_line('bar'+str(i),(x,y0),(x,y1))
