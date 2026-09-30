AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
D={}
D['clove-bud-with-pointed-sepals']=('SQUARE','Rejected clove became an upright microphone-like stem and dome. Restore the diagonal long stem, rounded bud and pointed calyx.', '''
        path('clove',(6,38),[('L',(22,22)),('L',(20,10)),('L',(27,14)),('A',(32,6),10,10,True),('A',(42,16),10,10,True),('A',(36,25),10,10,True),('L',(42,28)),('L',(30,28)),('L',(10,42)),('A',(6,38),4,4,True)],True)
''')
D['coin-passing-between-two-hands']=('VRECT_L','Rejected coin is a solid dot far left and both hands are stiff. Restore an outlined coin between smooth opposing open hands.', '''
        path('upper',(40,4),[('L',(30,4)),('L',(22,8)),('A',(24,16),5,5,False),('L',(32,12)),('L',(40,12))])
        circle('coin',16,25,3)
        path('lower',(8,36),[('L',(18,36)),('L',(28,32)),('L',(34,32)),('A',(34,40),4,4,True),('L',(20,44)),('L',(8,44))])
''')
D['computer-monitor-with-code-upload-a3ccb7c42eee5d1f']=('SQUARE','Only the rejected SVG is available. Its code marks are cramped thick parentheses. Use clear angled code chevrons, a balanced screen and aligned stand.', '''
        path('screen',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(24,34)),('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        self.add_polyline('code-left',(19,15),(15,20),(19,25))
        self.add_polyline('code-right',(29,15),(33,20),(29,25))
        self.add_line('stand',(24,34),(24,42));join('stand','screen')
        self.add_polyline('foot',(16,42),(24,42),(32,42));join('foot','stand')
''')
D['cost-explorer']=('SQUARE','Rejected chart uses solid nodes and a tiny magnifier handle. Restore outlined data nodes and a clearer diagonal lens handle; reduce the node count to two for space.', '''
        self.add_polyline('axes',(6,6),(6,30),(6,42),(14,42))
        circle('point-0',17,15,3);circle('point-1',36,9,3)
        self.add_line('series-start',(6,30),(14,15));join('series-start','axes');join('series-start','point-0')
        self.add_line('series-middle',(20,15),(33,9));join('series-middle','point-0');join('series-middle','point-1')
        self.add_line('series-end',(39,9),(42,6));join('series-end','point-1')
        path('lens',(37,40),[('A',(25,24),10,10,True),('A',(37,40),10,10,True)],True)
        self.add_line('handle',(37,40),(42,42));join('handle','lens')
''')
D['diagonal-pencil-writing-line']=('SQUARE','Rejected pencil loses the eraser separator and graphite nib boundary and is too horizontal. Restore a steeper diagonal barrel with distinct rounded cap and nib.', '''
        path('pencil',(6,34),[('L',(10,22)),('L',(26,6)),('A',(38,18),9,9,True),('L',(18,34)),('L',(6,38)),('L',(6,34))],True)
        self.add_line('eraser-seam',(26,6),(38,18));join('eraser-seam','pencil')
        self.add_line('nib-base',(10,22),(18,34));join('nib-base','pencil')
        self.add_line('baseline',(20,42),(42,42))
''')
D['diagonal-slashed-circle-with-notch-upload-6656f349e715eebc']=('SQUARE','Only the rejected SVG is available. Rebalance its diagonal stroke over a round ring and retain the short upper-right protrusion with cleaner joins.', '''
        circle('ring',24,24,15)
        self.add_line('slash',(6,6),(42,42));join('slash','ring')
        self.add_line('notch',(33,12),(39,6));join('notch','ring')
''')
D['donkey-pinata-banded-body']=('HRECT_L','Rejected pinata has square joints and a narrow triangular leg opening. Round the back and hooves while preserving ear, donkey muzzle and horizontal band.', '''
        path('outline',(4,36),[('L',(4,24)),('L',(4,20)),('A',(8,16),4,4,True),('L',(24,16)),('L',(28,8)),('L',(34,14)),('L',(44,18)),('L',(44,24)),('L',(36,24)),('L',(36,40)),('L',(28,40)),('L',(26,32)),('L',(16,32)),('L',(14,40)),('L',(8,40)),('A',(4,36),4,4,True)],True)
        self.add_line('band',(4,24),(36,24));join('band','outline')
''')
D['drag-gesture-in-all-directions']=('SQUARE','Rejected arrows are thick isolated chevrons with virtually no shafts. Restore four explicit arrow shafts around the centered fingertip.', '''
        path('finger',(18,28),[('L',(18,25)),('A',(30,25),6,6,True),('L',(30,28))])
        self.add_polyline('up-head',(20,10),(24,6),(28,10));self.add_line('up-shaft',(24,6),(24,11));join('up-head','up-shaft')
        self.add_polyline('down-head',(20,38),(24,42),(28,38));self.add_line('down-shaft',(24,36),(24,42));join('down-head','down-shaft')
        self.add_polyline('left-head',(10,20),(6,24),(10,28));self.add_line('left-shaft',(6,24),(10,24));join('left-head','left-shaft')
        self.add_polyline('right-head',(38,20),(42,24),(38,28));self.add_line('right-shaft',(38,24),(42,24));join('right-head','right-shaft')
''')
D['drifting-jellyfish']=('SQUARE','Rejected bell is a narrow crescent. Restore a broad rounded dome above the diagonal rim and three smooth trailing tentacles.', '''
        path('bell',(14,18),[('C',(30,6),(16,10),(22,6)),('C',(42,18),(37,6),(42,11)),('C',(34,38),(42,28),(42,34)),('L',(28,32)),('L',(22,26)),('L',(16,20)),('L',(14,18))],True)
        path('tentacle-0',(16,20),[('C',(6,30),(14,24),(10,27))]);join('tentacle-0','bell')
        path('tentacle-1',(22,26),[('C',(10,38),(20,30),(15,36))]);join('tentacle-1','bell')
        path('tentacle-2',(28,32),[('C',(20,42),(26,36),(23,40))]);join('tentacle-2','bell')
''')
D['dual-mesh-wireless-routers']=('VRECT_L','Rejected routers are shallow trapezoids and smallest wifi arc is a blob. Restore two upright rounded router towers under two clear signal arcs.', '''
        box('router-left',8,27,20,44,3);box('router-right',28,27,40,44,3)
        path('wifi-outer',(8,10),[('A',(40,10),16,6,True)])
        path('wifi-inner',(15,18),[('A',(33,18),9,5,True)])
''')
D['feather']=('VRECT_L','Rejected feather has a broad leaf-like closed vane and loses the open notch. Restore the long pointed vane, visible open notch and diagonal quill.', '''
        path('vane',(14,36),[('C',(8,26),(10,34),(8,30)),('C',(36,4),(8,17),(25,8)),('C',(40,18),(40,8),(40,12)),('L',(34,22))])
        path('vane-lower',(36,30),[('C',(14,36),(30,38),(20,40))]);join('vane','vane-lower')
        self.add_polyline('quill',(8,44),(14,36),(28,14));join('quill','vane');join('quill','vane-lower')
''')
D['female-user-profile-icon-upload-ba893b6ce54bc48b']=('SQUARE','Only the rejected SVG is available. Its head floats far above a blocky torso. Enlarge the circular head, bring it into proper bust contact and soften the shoulders while retaining the tapered female torso.', '''
        circle('head',24,14,8)
        path('body',(6,36),[('L',(12,30)),('A',(24,26),12,4,True),('A',(36,30),12,4,True),('L',(42,36)),('L',(32,36)),('L',(28,42)),('L',(20,42)),('L',(16,36)),('L',(6,36))],True);join('head','body')
''')
D['finger-point']=('VRECT_L','Rejected long central finger can read as a middle-finger gesture. Move the raised index to the left of the folded finger group and restore a broader thumb and palm.', '''
        path('hand',(8,32),[('C',(16,22),(8,25),(11,22)),('L',(16,8)),('A',(24,8),4,4,True),('L',(24,20)),('A',(32,20),4,4,True),('L',(32,24)),('A',(40,24),4,4,True),('L',(40,32)),('A',(24,44),16,12,True),('A',(8,32),16,12,True)],True)
        self.add_line('thumb-fold',(16,22),(16,30));join('thumb-fold','hand')
        self.add_line('finger-fold',(24,20),(24,26));join('finger-fold','hand')
        self.add_line('little-fold',(32,24),(32,28));join('little-fold','hand')
''')
D['four-diamond-flecks']=('SQUARE','Rejected large diamonds have equal sizes, losing the size hierarchy. Rebalance the upper-left diamond and retain a larger lower-right fleck with two smaller companions.', '''
        for name,x,y,r in [('upper-large',13,13,7),('lower-large',34,34,8),('upper-small',36,12,6),('lower-small',12,36,6)]:
            self.add_polyline(name,(x,y-r),(x+r,y),(x,y+r),(x-r,y),closed=True)
''')
D['gabled-house-paired-windows']=('HRECT_L','Rejected square windows became horizontal dashes. Restore two outlined square windows beneath the gable; omit the secondary doorway to give the paired windows enough space.', '''
        self.add_polyline('house',(4,18),(24,8),(44,18),(44,40),(4,40),closed=True)
        for name,x in [('left',12),('right',28)]:box('window-'+name,x,24,x+8,32,0)
''')
D['game-immersive-vr']=('HRECT_M','Rejected visor is too tall and narrow, with a blob-like X and angular nose cut. Broaden the visor, soften the nose recess and enlarge the central cross.', '''
        path('visor',(16,10),[('L',(32,10)),('A',(40,18),8,8,True),('L',(40,24)),('L',(40,30)),('A',(32,38),8,8,True),('C',(24,34),(28,38),(28,34)),('C',(16,38),(20,34),(20,38)),('A',(8,30),8,8,True),('L',(8,24)),('L',(8,18)),('A',(16,10),8,8,True)],True)
        self.add_line('strap-left',(4,24),(8,24));join('strap-left','visor')
        self.add_line('strap-right',(40,24),(44,24));join('strap-right','visor')
        self.add_line('cross-a',(20,18),(28,24));self.add_line('cross-b',(20,24),(28,18));join('cross-a','cross-b')
''')
D['glasses-sun']=('SQUARE','Rejected lenses are deep bowls and the sun is centered with dot rays. Restore shallower sunglasses and an upper-right outlined sun with short line rays.', '''
        for side,cx in [('left',13),('right',35)]:
            path('lens-'+side,(cx-7,32),[('L',(cx+7,32)),('A',(cx-7,32),7,10,True)],True)
        self.add_line('bridge',(20,32),(28,32));join('bridge','lens-left');join('bridge','lens-right')
        self.add_line('arm-left',(6,32),(12,24));join('arm-left','lens-left')
        self.add_line('arm-right',(42,32),(38,24));join('arm-right','lens-right')
        circle('sun',32,11,5)
        self.add_line('ray-upper-left',(17,6),(19,7));self.add_line('ray-left',(14,15),(18,15))
''')
D['hand-gesture-swipe-up']=('SQUARE','Rejected contact arc is a jagged polyline and finger is too thin. Round the contact arc and widen the horizontal fingertip while preserving the upward arrow.', '''
        path('finger',(6,25),[('L',(26,25)),('A',(26,35),5,5,True),('L',(6,35))])
        path('contact',(34,18),[('C',(42,29),(40,18),(42,23)),('C',(32,42),(42,35),(38,40))])
        self.add_polyline('arrowhead',(20,10),(24,6),(28,10));self.add_line('shaft',(24,6),(24,14));join('arrowhead','shaft')
''')
D['hand-gesture-vertical-swipe-down']=('HRECT_L','Rejected pointing hand and swipe path are angular polygons. Restore rounded fingertip, thumb and a continuous smooth downward arrow curve.', '''
        path('hand',(4,30),[('L',(4,22)),('L',(14,12)),('C',(19,16),(18,8),(24,12)),('L',(17,18)),('L',(26,18)),('A',(26,26),4,4,True),('L',(20,26)),('L',(18,34)),('L',(4,32)),('L',(4,30))],True)
        path('swipe',(40,8),[('C',(44,22),(44,14),(44,17)),('C',(32,40),(44,30),(40,35))])
        self.add_polyline('arrowhead',(34,32),(32,40),(40,38));join('arrowhead','swipe')
''')
D['hand-swipe-up-gesture']=('HRECT_L','Rejected index finger ends in an arrow-like point and the thumb is square. Restore a round fingertip and a softly hooked thumb below the finger.', '''
        path('hand',(4,38),[('L',(4,28)),('L',(18,22)),('L',(40,22)),('A',(40,30),4,4,True),('L',(26,30)),('L',(26,34)),('C',(22,40),(32,34),(30,40)),('L',(4,38))],True)
        self.add_polyline('arrowhead',(20,12),(24,8),(28,12));self.add_line('shaft',(24,8),(24,14));join('arrowhead','shaft')
''')
