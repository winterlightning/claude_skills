"""Rejected sticks and trapezoid do not communicate robbery. Restore two distinct people and an unmistakable knife directed toward the victim."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='4d29ffb6-bda5-416a-be77-62a701e144e4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__robbing/20260929T044747Z-thuan-mac/reference/robbing_4d29ffb6-bda5-416a-be77-62a701e144e4.svg'
AUTHOR='gpt-6'
PLAN='Rejected sticks and trapezoid do not communicate robbery. Restore two distinct people and an unmistakable knife directed toward the victim.'
CONSTRUCTION_REFERENCE='Shared human full_body_ref.png: circular heads, aligned torsos and coherent limbs.'
OMISSIONS='Money symbol omitted to keep knife and two opposing people legible; knife retained as the defining robbery cue.'
class Drawing(Solo48):
    icon_id='robbing'
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
        self.circle('robber-head',13,11,5);self.circle('victim-head',40,12,4)
        self.add_line('robber-torso',(13,24),(13,34));self.add_polyline('robber-legs',(7,42),(13,34),(19,42))
        self.add_line('victim-torso',(40,24),(40,33));self.add_polyline('victim-legs',(35,42),(40,33),(45,42))
        self.add_polyline('robber-arm',(13,26),(20,28),(24,28))
        self.path('blade',(24,24),[('L',(28,24)),('C',(34,31),(32,24),(34,27)),('L',(24,31)),('L',(24,24))],True)
        self.add_line('blade-guard',(24,23),(24,33));self.relate('connect','blade','blade-guard','robber-arm');self.relate('connect','robber-torso','robber-arm','robber-legs');self.relate('connect','victim-torso','victim-legs')
        self.mark_human_figure('robber',head='robber-head',torso='robber-torso',torso_junction='start');self.mark_human_figure('victim',head='victim-head',torso='victim-torso',torso_junction='start')

# Human reference: icon_set/references/human_ref/full_body_ref.png.
# Robber (13,11), r5 to neck (13,24): 8 centerline / 4 ink. Victim (40,12), r4 to neck (40,24): same exact gap.

Drawing.exception = {'reason': 'Two people and a broad curved-tip knife make the robbery scene explicit. The short knife-to-victim gap, 3 px blade opening and wider scene envelope are deliberate; head-to-torso gaps remain exactly 4 px.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': 'efb409509467cb83179bc7b277bab4f906f462a3b94a5f76e8732c2771de450a'}
