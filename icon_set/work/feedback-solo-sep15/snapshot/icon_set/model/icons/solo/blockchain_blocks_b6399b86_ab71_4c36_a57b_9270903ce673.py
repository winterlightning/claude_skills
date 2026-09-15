"""Two linked blocks form a directed sequence. Lucide workflow informs the stepped arrangement and connected block edges. Blocks step diagonally to retain square openings on the compact profile; the rightward flow bends downward.
Fresh SOLO48 geometry. Keyshape SQUARE; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6399b86-ab71-4c36-a57b-9270903ce673'
SOURCE_PATH = 'pictographic-primitives/programing/amazon managed blockchain_b6399b86-ab71-4c36-a57b-9270903ce673.svg'
AUTHOR = 'gpt-6'

class BlockchainBlocks(Solo48):
    icon_id = 'blockchain-blocks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/programming"
    aliases = ()
    keywords = ('blockchain', 'blocks', 'chain', 'ledger', 'link', 'sequence', 'crypto', 'arrow')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.add_polyline('first-block',(6,6),(20,6),(20,13),(20,20),(6,20),closed=True)
        self.add_polyline('second-block',(28,28),(35,28),(42,28),(42,42),(28,42),closed=True)
        self.add_polyline('link',(20,13),(35,13),(35,28))
        self.add_polyline('arrow',(30,23),(35,28),(40,23))
        for a,b in (('first-block','link'),('second-block','link'),('second-block','arrow'),('link','arrow')):
            self.relate('connect',a,b)
