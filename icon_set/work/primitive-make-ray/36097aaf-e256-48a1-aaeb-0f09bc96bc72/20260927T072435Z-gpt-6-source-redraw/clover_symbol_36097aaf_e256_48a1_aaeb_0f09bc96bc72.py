"""Fresh SOLO48 revision of clover-symbol from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '36097aaf-e256-48a1-aaeb-0f09bc96bc72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clover-symbol/20260927T071330Z-thuan-mac-1/reference/clover_36097aaf-e256-48a1-aaeb-0f09bc96bc72.svg'
AUTHOR = 'gpt-6'

class CloverSymbol(Solo48):
    icon_id = 'clover-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('clover', 'symbol', 'solo-ai-next100')

    def build(self) -> None:

        # Four balanced heart leaves share one center; stem is added for clover.
        shape=[('L',(14,14)),('C',(14,8),(16,6),(19,6)),
               ('C',(22,6),(24,9),(24,11)),
               ('C',(24,9),(26,6),(29,6)),
               ('C',(32,6),(34,8),(34,14)),('L',(24,24))]
        def turn(p,n):
            for _ in range(n):p=(48-p[1],p[0])
            return p
        for n in range(4):
            commands=[]
            for item in shape:
                kind,*points=item
                commands.append(tuple([kind]+[turn(p,n) for p in points]))
            path(self,f'leaf-{n}',(24,24),*commands,closed=True)
        contacts(self)
