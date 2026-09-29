"""Rejected short hooked ribbon and angular limbs lose the flowing running action. Restore a waved ribbon, an aligned head, outstretched arms and bent running legs."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='64d49871-60a0-4aab-a236-4702ea4500b2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ribbon-gymnast-running/20260929T044747Z-thuan-mac/reference/ribbon person_64d49871-60a0-4aab-a236-4702ea4500b2.svg'
AUTHOR='gpt-6'
PLAN='Rejected short hooked ribbon and angular limbs lose the flowing running action. Restore a waved ribbon, an aligned head, outstretched arms and bent running legs.'
CONSTRUCTION_REFERENCE='Shared full_body_ref.png and approved approaching-ball head alignment: circular head, coherent limbs and analytically exact detached head gap.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='ribbon-gymnast-running'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('head',29,11,5)
        self.add_bezier('torso',(24,23),((23,25),(22,28),(20,30)))
        self.add_polyline('arm-front',(24,23),(33,27),(42,20))
        self.add_polyline('arm-back',(24,23),(16,22),(9,28))
        self.add_polyline('leg-back',(20,30),(13,39),(6,36))
        self.add_polyline('leg-front',(20,30),(31,33),(37,42))
        self.path('ribbon',(6,7),[('C',(12,14),(10,7),(8,14)),('C',(18,7),(17,14),(14,7)),])
        self.relate('connect','torso','arm-front','arm-back','leg-back','leg-front')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
