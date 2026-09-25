"""Circular face beneath parted hair above a long simple dress with short sleeves; symmetric full-body silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='45881775-2179-41cc-98a1-78a598c550c1'
SOURCE_PATH='pictographic-primitives/avatars/girl full body_45881775-2179-41cc-98a1-78a598c550c1.svg'
AUTHOR='gpt-6'
PLAN='Circular face with outward hair curls; sleeves and long central torso replace the old skirt and added legs. Head bottom y20 and body top y28 give exactly 4 units of detached ink gap. Paired arcs mirror about x24.'
CONSTRUCTION_REFERENCE='human_ref/user.svg and full_body_ref.png: circular head and coherent symmetric body; source retains sleeves and hair curls. This is an outlined figure, not a stick figure.'
OMISSIONS='Interior hair part and duplicate hair cap omitted to avoid a pinched cap opening. No legs added, matching the source.'

class Drawing(Solo48):
    icon_id='girl-full-body'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    aliases=()
    keywords=('girl', 'full', 'body')

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
        self.circle('head',24,12,8)
        self.add_arc('hair-left',(16,12),(10,20),radius_x=8)
        self.add_arc('hair-right',(38,20),(32,12),radius_x=8)
        self.relate('connect','head','hair-left')
        self.relate('connect','head','hair-right')
        self.path('body',(24,28),[('A',(10,36),14,8,False),('L',(18,36)),('L',(18,44)),('L',(30,44)),('L',(30,36)),('L',(38,36)),('A',(24,28),14,8,False)],True)

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '6047873f9ca7839e308473aa87fb3445ffd14b2eede10c031387a6473484ed6c', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '45881775-2179-41cc-98a1-78a598c550c1'}
