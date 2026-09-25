"""Five varying audio bars centered around the taller middle. Hollow bar outlines reduced to single rounded strokes because five outlined columns cannot fit required gaps. Centerline4,8–44,40.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5914bd56-799d-4aed-872f-a8f85da47371'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/logos/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='audio-equalizer-sound-bars-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "logos"
    categories = ("logos", "primitives")
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

        for i,(x,top,bottom) in enumerate([(4,20,34),(14,13,37),(24,10,40),(34,8,36),(44,18,32)]):self.add_line('bar'+str(i),(x,top),(x,bottom))
