"""Two descending rockets over a curved horizon. Lucide rocket informs pointed bodies and attached fins. Exhaust pairs reduce to one stroke per rocket, and the crowded wing bands become swept shoulders. The right rocket remains higher.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6'
SOURCE_PATH='pictographic-primitives/programing/network firewall rocket_cfa6fcad-81e5-4bf3-ad9e-2a0d1f969fa6.svg'
AUTHOR='gpt-6'

class RocketsOverHorizon(Solo48):
    icon_id='rockets-over-horizon'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('rockets', 'missiles', 'firewall', 'launch', 'defense', 'horizon', 'security', 'attack')

    def build(self) -> None:
        def ring(name,x,y,r):
            points=((x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r))
            members=[]
            for i,(a,b) in enumerate(zip(points,points[1:])):
                member=f'{name}-{i}'
                self.add_arc(member,a,b,radius_x=r)
                members.append(member)
            self.add_contour(name,*members,closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        for name,x,y in (('left',12,18),('right',36,16)):
            self.add_polyline(name+'-body',(x-4,y),(x+4,y),(x+4,y+6),(x,y+10),(x-4,y+6),closed=True)
            self.add_line(name+'-left-fin',(x-4,y),(x-8,y+4))
            self.add_line(name+'-right-fin',(x+4,y),(x+8,y+4))
            join(name+'-body',name+'-left-fin')
            join(name+'-body',name+'-right-fin')
            self.add_line(name+'-exhaust',(x,8),(x,y-8))
        self.add_arc('horizon',(4,40),(44,40),radius_x=101)
