"""Pointed-ear collie face with open lower neck, cheek blaze and smile.
Plan: mirrored ears and cheeks share the x24 axis; two eyes and an open curved mouth clarify the dog's face.
Keyshape VRECT_L centerline (8,4)-(40,44). Lucide dog informed the spare face marks; the reference supplies the tall collie ears and cheek pattern.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "4731ca55-af71-4c3b-9bfa-b1c641a0b9a5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pointed-ear-collie-face/20260927T170245Z-thuan-mac-1/reference/border collie_4731ca55-af71-4c3b-9bfa-b1c641a0b9a5.svg"
AUTHOR = "gpt-6"
class PointedEarCollieFace(Solo48):
 icon_id = "pointed-ear-collie-face"
 keyshape = Keyshape.VRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "animals"
 aliases = ("border-collie-face",)
 keywords = ("collie", "dog", "face", "ears", "muzzle")
 def build(self):
  self.add_line("neck-left",(10,44),(10,36))
  self.add_bezier("cheek-left",(10,36),(((10,30),(8,26),(8,20))))
  self.add_line("ear-left-outer",(8,20),(8,4))
  self.add_bezier("ear-left-inner",(8,4),(((13,6),(17,9),(20,14))))
  self.add_line("forehead",(20,14),(28,14))
  self.add_bezier("ear-right-inner",(28,14),(((31,9),(35,6),(40,4))))
  self.add_line("ear-right-outer",(40,4),(40,20))
  self.add_bezier("cheek-right",(40,20),(((40,26),(38,30),(38,36))))
  self.add_line("neck-right",(38,36),(38,44))
  self.add_contour("head","neck-left","cheek-left","ear-left-outer","ear-left-inner","forehead","ear-right-inner","ear-right-outer","cheek-right","neck-right")
  self.add_bezier("blaze-left",(10,36),(((16,34),(21,30),(24,28))))
  self.add_bezier("blaze-right",(24,28),(((27,30),(32,34),(38,36))))
  self.add_contour("blaze","blaze-left","blaze-right")
  self.relate("connect","head","blaze")
  self.add_dot("eye-left",(18,22))
  self.add_dot("eye-right",(30,22))
  self.add_arc("smile",(21,40),(27,40),radius_x=3,sweep=False)
