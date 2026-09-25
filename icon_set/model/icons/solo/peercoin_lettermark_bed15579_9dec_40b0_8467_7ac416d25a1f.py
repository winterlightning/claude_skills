"""Peercoin P with paired upright stems, rounded bowl and a crossing bar. VRECT_L extremes (8,4)-(40,44) preserve its tall letter proportions. Shared bar and bowl nodes. No useful exact Lucide lettermark match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bed15579-9dec-40b0-8467-7ac416d25a1f'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto peercoin_bed15579-9dec-40b0-8467-7ac416d25a1f.svg'
AUTHOR='gpt-6'

class PeercoinLettermark(Solo48):
    icon_id='peercoin-lettermark'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    aliases=()
    keywords=('peercoin', 'lettermark', 'crypto', 'currency', 'symbol', 'p')

    def build(self):
        for name,x in (('outer',14),('inner',22)):
            for n,(y1,y2) in enumerate(((4,24),(24,34),(34,44))):self.add_line(f'{name}-{n}',(x,y1),(x,y2))
            self.add_contour(name,*[f'{name}-{n}' for n in range(3)])
        self.add_line('top-left',(14,4),(22,4))
        self.add_line('top-right',(22,4),(30,4))
        self.add_arc('bowl',(30,4),(30,24),radius_x=10)
        self.add_line('bowl-bottom',(30,24),(22,24))
        self.add_contour('bowl-outline','top-left','top-right','bowl','bowl-bottom')
        for name in ('outer','inner'):self.relate('connect',name,'bowl-outline')
        for n,(a,b) in enumerate(((8,14),(14,22),(22,30))):self.add_line(f'bar-{n}',(a,34),(b,34))
        self.add_contour('bar',*[f'bar-{n}' for n in range(3)])
        for name in ('outer','inner'):self.relate('connect',name,'bar')
