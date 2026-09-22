from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
class Trial(Solo48):
 icon_id='lobster-with-pointed-closed-claws';keyshape=Keyshape.HRECT_L
 def build(self):
  self.add_polyline('body',(20,24),(20,32),(16,40),(32,40),(28,32),(28,24))
  self.add_arc('head',(28,24),(20,24),radius_x=4,sweep=False)
  self.relate('connect','head','body')
  for side in (-1,1):
   x=lambda a:24+side*a
   self.add_bezier(f'claw{side}',(x(16),22),((x(22),18),(x(20),12),(x(16),8)),((x(12),12),(x(10),18),(x(16),22)))
   self.add_line(f'arm{side}',(x(16),22),(x(4),24))
   self.add_line(f'antenna{side}',(x(4),24),(x(4),8))
   self.add_polyline(f'leg{side}',(x(4),32),(x(12),32),(x(20),34))
   for a,b in [(f'arm{side}',f'claw{side}'),(f'arm{side}','body'),(f'arm{side}','head'),(f'antenna{side}','body'),(f'antenna{side}','head'),(f'antenna{side}',f'arm{side}'),(f'leg{side}','body')]:self.relate('connect',a,b)
