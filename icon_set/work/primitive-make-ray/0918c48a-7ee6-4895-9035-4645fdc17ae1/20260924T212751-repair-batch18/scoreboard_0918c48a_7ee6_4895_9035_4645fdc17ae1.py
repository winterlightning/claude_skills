"""A hanging scoreboard showing 2:0.
Symbol plan and construction: app-window: framed display; source supplies the complete hand-drawn score and two hangers.
Keyshape: HRECT_L gives the score its widest available panel.
Omissions: Hangers stop at the frame instead of extending into the score; all digits and colon retained.
Review: Blocked: colon-to-digit gaps range from 3.0712 to 5.09902 instead of 8; curved frame/number margins still require review. Full score remains congested in both themes. Five repair rounds and a final better-candidate selection are saved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0918c48a-7ee6-4895-9035-4645fdc17ae1'
SOURCE_PATH = 'pictographic-primitives/sports/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='scoreboard'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('scoreboard',)


    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)


    def score(self,y):
        self.add_arc('two-top',(12,y+4),(20,y+4),radius_x=4)
        self.add_polyline('two-bottom',(20,y+4),(12,y+12),(20,y+12));self.relate('connect','two-top','two-bottom')
        for i,cy in enumerate((y+3,y+11)):self.add_dot(f'colon-{i}',(25,cy))
        self.box('zero',28,y,8,12,4)



    def build(self):
        self.add_polyline('panel',(13,12),(35,12),(44,12),(44,40),(4,40),(4,12),closed=True)
        for i,x in enumerate((13,35)):
         self.add_line(f'hanger-{i}',(x,8),(x,12));self.relate('connect','panel',f'hanger-{i}')
        self.score(20)
