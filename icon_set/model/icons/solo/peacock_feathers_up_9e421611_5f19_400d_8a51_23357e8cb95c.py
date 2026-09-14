'Peacock: retain a broad raised fan behind a compact continuous bird silhouette; rebalance the inner bird rather than distorting the tail.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e421611-5f19-400d-8a51-23357e8cb95c'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feathers up_9e421611-5f19-400d-8a51-23357e8cb95c.svg'
AUTHOR = 'gpt-6'


class PeacockWithSpreadTail(Solo48):
    icon_id = 'peacock-with-spread-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('peacock', 'with', 'spread', 'tail')

    def build(self) -> None:
        self.add_arc('fan',(6,40),(42,40),radius_x=18,radius_y=34)
        self.add_arc('head',(20,20),(28,20),radius_x=4)
        self.add_bezier('neck-right',(28,20),((28,24),(27,25),(27,27)))
        self.add_bezier('body',(27,27),((27,31),(31,32),(31,36)),((31,40),(28,42),(24,42)),((20,42),(17,40),(17,36)),((17,32),(21,31),(21,27)))
        self.add_bezier('neck-left',(21,27),((21,24),(20,24),(20,20)))
        self.add_contour('bird','head','neck-right','body','neck-left',closed=True)
