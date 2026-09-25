"""Menstrual Cup.
Plan: Centerline extremes (8,4)-(40,44). Shared rounded rolled rim, deep bowl, and solid retrieval stem; wavy liquid line retained.
References: supplied original source; Lucide cup-soda: broad rim and coherent tapered vessel; supplied source shape.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42b78900-5220-4809-83cc-cc84fdce2130'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/menstrual cup wave_42b78900-5220-4809-83cc-cc84fdce2130.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'menstrual-cup-42b78900'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('menstrual-cup',)
    keywords = ('menstrual', 'cup')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members=[]
            for j,s in enumerate(segments):
                member=f"{name}-{j}"
                if len(s)==1: self.add_line(member,start,s[0])
                else: self.add_arc(member,start,s[0],radius_x=s[1],radius_y=s[2],sweep=s[3],large_arc=s[4] if len(s)>4 else False)
                members.append(member);start=s[0]
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            stroke(name,(cx-r,cy),[((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)],True)
        stroke("rim",(12,4),[((36,4),),((40,8),4,4,True),((36,12),4,4,True),((12,12),),((8,8),4,4,True),((12,4),4,4,True)],True)
        stroke("bowl",(12,12),[((12,22),),((12,24),),((24,36),12,12,False),((36,24),12,12,False),((36,22),),((36,12),)])
        self.relate("connect","rim","bowl")
        self.add_line("stem",(24,36),(24,44));self.relate("connect","bowl","stem")
        stroke("surface",(12,22),[((24,22),6,2,True),((36,22),6,2,False)]);self.relate("connect","bowl","surface")

