"""Restored two full chopsticks, a lifted noodle bundle, bowl contents and a foot under the curved bowl.
Plan and comparison: The bowl lost its foot, round contents and hanging noodles; one chopstick floats separately.
Construction reference: soup: coherent curved bowl and pedestal foot; supplied reference owns chopsticks and hanging noodles
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0e320bcf-f02f-5659-b42d-7ea2762d83bf'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__ramen-bowl-raised-chopsticks/20260929T043142Z-thuan-mac/reference/asian food noodles_0e320bcf-f02f-5659-b42d-7ea2762d83bf.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='ramen-bowl-raised-chopsticks'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # Bowl, foot, noodles and chopsticks are separate physical components.
        self.path('bowl',(4,26),[('L',(44,26)),('A',(4,26),20,14,True)],True)
        self.add_polyline('foot',(17,40),(17,44),(31,44),(31,40))
        self.relate('connect','bowl','foot')
        self.add_line('chopstick-top',(10,9),(44,4))
        self.add_line('chopstick-bottom',(17,13),(44,11))
        self.add_line('noodle-left',(18,8),(18,26))
        self.add_line('noodle-right',(24,7),(24,26))
        self.relate('connect','noodle-left','bowl'); self.relate('connect','noodle-right','bowl')
        self.path('food-left',(8,26),[('A',(14,19),7,7,True)])
        self.path('food-right',(28,26),[('A',(40,26),6,6,True)])
        self.relate('connect','food-left','bowl'); self.relate('connect','food-right','bowl')

Drawing.exception = {'reason': 'The chopstick/noodle crossings, round food and bowl foot require local small openings. These essential food cues remain legible with uniform 4px strokes. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4ed9070b4fc76f2a099415d926be78ba5b0f3544860386113dd99ec6de628687'}
