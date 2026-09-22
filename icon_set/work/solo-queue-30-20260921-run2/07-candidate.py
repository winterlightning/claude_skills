from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
class Drawing(Solo48):
 icon_id='crossed-stockinged-legs-candidate'
 keyshape=Keyshape.VRECT_L
 semantic_role='MAIN'
 semantic_kind='noun'
 def build(self):
  self.add_bezier('forward-outer',(16,4),((16,10),(8,14),(8,20)),((8,24),(28,26),(28,28)),((28,30),(12,36),(12,40)),((12,42),(12,44),(16,44)))
  self.add_bezier('forward-inner',(28,4),((28,10),(28,12),(28,14)),((34,18),(40,20),(40,24)),((40,32),(23,35),(22,40)))
  self.add_polyline('rear-leg',(16,28),(16,36))
