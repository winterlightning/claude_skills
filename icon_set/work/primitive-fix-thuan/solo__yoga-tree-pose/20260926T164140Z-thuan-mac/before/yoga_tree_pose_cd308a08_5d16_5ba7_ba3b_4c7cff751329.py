'Circular head framed by curved overhead arms, straight support leg and outward bent knee.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='cd308a08-5d16-5ba7-ba3b-4c7cff751329'
SOURCE_PATH='pictographic-primitives/sports/yoga tree pose_cd308a08-5d16-5ba7-ba3b-4c7cff751329.svg'
AUTHOR='gpt-6'
PLAN='Circular head framed by curved overhead arms, straight support leg and outward bent knee.'
CONSTRUCTION_REFERENCE='human_ref/full_body_ref.png: outlined head and simple limbs; Lucide person-standing shared joints.'
class Drawing(Solo48):
    icon_id='yoga-tree-pose'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('yoga', 'tree', 'pose')
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
        self.circle('head',24,14,4)
        self.path('left-arm',(16,4),[('C',(8,16),(10,4),(8,10)),('L',(8,18)),('A',(16,26),8,8,False)])
        self.path('right-arm',(32,26),[('A',(40,18),8,8,False),('L',(40,16)),('C',(32,4),(40,10),(38,4))])
        self.add_polyline('shoulders',(16,26),(24,26),(32,26))
        self.add_line('torso',(24,26),(24,44))
        self.add_polyline('bent-leg',(24,34),(40,37),(24,44))
        for a,b in [('left-arm','shoulders'),('right-arm','shoulders'),('shoulders','torso'),('torso','bent-leg')]:self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

# Keyshape: VRECT_L gives the overhead arms and standing leg their vertical reach.
# Visual review: Curved overhead arms replace straight prongs. Clear torso leads to an outward folded knee. The folded foot rests low against the support leg as a compact pose reduction.
OMISSIONS='Outlined body reduced to shared stick-figure vocabulary. Folded leg is lowered and compressed to preserve a clear torso and pass spacing.'
HUMAN_REVIEW={'reference': 'icon_set/references/human_ref/full_body_ref.png', 'head_center': [24, 14], 'radius': 4, 'torso_junction': [24, 26], 'centerline_gap': 8, 'ink_gap': 4, 'proof': '26-(14+4)=8. Torso is vertical and head lies on the same axis.'}
