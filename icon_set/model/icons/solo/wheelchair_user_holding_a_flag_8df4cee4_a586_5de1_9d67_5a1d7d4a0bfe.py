"""Fresh reconstruction of flag from the supplied reference.
Construction references: human_ref/full_body_ref.png and Lucide accessibility/flag. Symbol plan recorded in build().
Profile SOLO48, keyshape SQUARE; final findings are recorded alongside this module.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe'
SOURCE_PATH = 'pictographic-primitives/rewards/flag_8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wheelchair-user-holding-a-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('flag',)

    def circle(self, n, x, y, r):
        self.add_arc(n+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(n+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def box(self,n,l,t,r,b,k=4,top=(),bottom=()):
        p=[(l+k,t),*[(x,t) for x in sorted(top)],(r-k,t),(r,t+k),(r,b-k),(r-k,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,(a,z) in enumerate(zip(p,p[1:]+p[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if a[0]!=z[0] and a[1]!=z[1]:self.add_arc(name,a,z,radius_x=k)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Head center (16,11), r5; actual torso junction (16,24): 13-5=8.
        self.circle('head',16,11,5)
        self.add_line('torso',(16,24),(16,28))
        self.add_arc('hip',(16,28),(20,32),radius_x=4,sweep=False)
        self.add_polyline('seat-leg',(20,32),(26,32),(34,42))
        self.relate('connect','torso','hip')
        self.relate('connect','hip','seat-leg')
        # Hip arc shares tangent endpoints with the torso and seat.
        self.add_arc('wheel-back',(10,24),(6,32),radius_x=10,sweep=False)
        self.add_arc('wheel-bottom',(6,32),(26,32),radius_x=10,sweep=False)
        self.add_contour('wheel','wheel-back','wheel-bottom')
        self.relate('connect','wheel','seat-leg')
        self.add_line('upper-arm',(16,24),(24,24))
        self.add_bezier('forearm',(24,24),((27,24),(29,22),(30,20)))
        self.add_contour('arm','upper-arm','forearm')
        self.relate('connect','torso','arm')
        self.add_polyline('pole',(30,6),(30,16),(30,20),(30,24))
        self.add_bezier('flag-top',(30,6),((34,6),(36,10),(42,8)))
        self.add_line('flag-tip',(42,8),(42,18))
        self.add_bezier('flag-bottom',(42,18),((36,20),(34,16),(30,16)))
        self.add_contour('flag','flag-top','flag-tip','flag-bottom')
        self.relate('connect','pole','flag')
        self.relate('connect','pole','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

    icon_id = 'wheelchair-user-holding-a-flag'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('award', 'reward', 'wheelchair-user-holding-a-flag')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
