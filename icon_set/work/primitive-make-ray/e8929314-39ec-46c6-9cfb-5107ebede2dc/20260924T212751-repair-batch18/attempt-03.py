"""Binary rows 10100 and 01100 above two water wave lines.
Symbol plan: waves: repeated smooth lobes; source supplies literal binary strings.
Reduction: Wave count reduced from three to two lobes per row; all ten digits retained.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e8929314-39ec-46c6-9cfb-5107ebede2dc'
SOURCE_PATH = 'pictographic-primitives/programing/data lake code_e8929314-39ec-46c6-9cfb-5107ebede2dc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='data-lake-code'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('data', 'lake', 'code')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        for row,(text,starts) in enumerate([('10100',(8,12,20,24,32)),('01100',(8,18,22,24,32))]):
            y=4+row*16
            for col,(digit,x) in enumerate(zip(text,starts)):
                n=f'digit-{row}-{col}'
                if digit=='1':self.add_line(n,(x,y),(x,y+8))
                else:
                    self.add_arc(n+'-top',(x,y+4),(x+8,y+4),radius_x=4,radius_y=4)
                    self.add_arc(n+'-bottom',(x+8,y+4),(x,y+4),radius_x=4,radius_y=4)
                    self.add_contour(n,n+'-top',n+'-bottom',closed=True)
        for row,y in enumerate((34,42)):
            for col in range(2):
                x=8+16*col
                self.add_bezier(f'wave-{row}-{col}',(x,y),((x+3,y+2),(x+6,y+2),(x+9,y+2)),((x+12,y+2),(x+15,y+2),(x+16,y)))
            self.add_contour(f'water-{row}',f'wave-{row}-0',f'wave-{row}-1')

    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)

