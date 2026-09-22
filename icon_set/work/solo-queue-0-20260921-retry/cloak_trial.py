from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
class Trial(Solo48):
 icon_id='open-front-hooded-cloak';keyshape=Keyshape.VRECT_L
 def build(self):
  self.add_polyline('body-left',(16,44),(8,44),(12,26),(16,22))
  self.add_bezier('hood-left',(16,22),((14,21),(12,19),(12,16)))
  self.add_arc('hood-top',(12,16),(36,16),radius_x=12,radius_y=12)
  self.add_bezier('hood-right',(36,16),((36,19),(34,21),(32,22)))
  self.add_polyline('body-right',(32,22),(36,26),(40,44),(32,44),(16,44))
  self.add_bezier('opening-left',(24,24),((22,22),(20,19),(20,16)))
  self.add_arc('opening-top',(20,16),(28,16),radius_x=4)
  self.add_bezier('opening-right',(28,16),((28,19),(26,22),(24,24)))
  self.add_contour('opening','opening-left','opening-top','opening-right',closed=True)
  self.add_bezier('panel-left',(16,44),((22,37),(24,30),(24,24)))
  self.add_bezier('panel-right',(24,24),((24,30),(26,37),(32,44)))
  for a,b in [('body-left','hood-left'),('hood-left','hood-top'),('hood-top','hood-right'),('hood-right','body-right'),('body-right','body-left'),('panel-left','opening'),('panel-right','opening'),('panel-left','panel-right'),('body-left','panel-left'),('body-right','panel-left'),('body-right','panel-right')]: self.relate('connect',a,b)
