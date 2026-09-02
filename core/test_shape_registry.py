#!/usr/bin/env python3
"""Regression tests for registry geometry and shared icon math."""
from __future__ import annotations
import re,unittest
from unittest.mock import patch
from icon_geometry import parse_path,resolve_icon,sample,svg
from shape_registry import BY_ID,SHAPES,Shape,path
class RegistryTests(unittest.TestCase):
    def test_ids_are_unique(self): self.assertEqual(len(BY_ID),len(SHAPES))
    def test_expected_atoms_exist(self):
        required={"circle","ellipse","square","rectangle","dashed-rectangle","water-drop","tapered-spire","rounded-square","rounded-rectangle","pill","triangle","right-triangle","diamond","gable","twin-gable","sloped-box","trapezoid","flared-horn","cut-corner-box","dome","cloud","lens","lobed-drop","stepped-cog","twin-lobed-drop","lightning-bolt","puzzle-piece","phone-handset-outline","quarter-circle","ring","dot","line","diagonal-line","curve","s-bend","arc","quarter-arc","bulb-outline","open-rectangle","arch","hook","faucet","open-end-wrench","open-gable","radial-ticks","hexagon","scalloped-oval","head-profile","worker-profile-solid","broken-pig-outline","holding-hand","bottle-outline","transfer-hand","open-twin-gable","spiral","gapped-rounded-rectangle","corner-gapped-rounded-rectangle","open-shell","oyster-shell","side-gapped-rounded-rectangle","shark-fin","wave-line","gripping-hand","gapped-eye"}; self.assertTrue(required<=set(BY_ID))
    def test_frontend_and_python_registry_ids_match(self):
        frontend=(__import__("pathlib").Path(__file__).resolve().parent.parent/"frontend"/"js"/"shapes.js").read_text()
        ids=re.findall(r"\bid:\s*'([^']+)'",frontend)
        self.assertEqual(ids,[shape.id for shape in SHAPES])
    def test_new_grid_atoms_have_no_cubics(self):
        for shape in SHAPES:
            tag,attrs=shape.geometry(*shape.natural)
            if shape.id!="s-curve" and tag=="path": self.assertNotRegex(str(attrs["d"]),r"[Cc]",shape.id)
    def test_all_nonlegacy_paths_parse(self):
        for shape in SHAPES:
            tag,attrs=shape.geometry(*shape.natural)
            if tag=="path" and shape.id!="s-curve": self.assertTrue(parse_path(str(attrs["d"])),shape.id)
    def test_half_scale_is_exact(self):
        doc={"instances":[{"shapeId":"arch","x":4,"y":6,"w":40,"h":36}]}; paths=resolve_icon(doc); design=svg(paths,48,4); ship=svg(paths,24,2,.5)
        self.assertIn('viewBox="0 0 48 48"',design); self.assertIn('viewBox="0 0 24 24"',ship); self.assertNotRegex(design.replace("currentColor",""),r"[Cc](?=[\s\-0-9.])")

    def test_new_registered_atom_resolves_without_a_second_allowlist(self):
        shape = Shape(
            "quality-first-contour",
            "Quality-first contour",
            False,
            (20, 12),
            (20, 12),
            lambda w, h: path(f"M 0 {h} Q {w / 2} 0 {w} {h}"),
        )
        document = {
            "instances": [
                {
                    "shapeId": shape.id,
                    "x": 4,
                    "y": 8,
                    "w": 20,
                    "h": 12,
                }
            ]
        }
        with patch.dict(BY_ID, {shape.id: shape}):
            resolved = resolve_icon(document)
        self.assertEqual(resolved[0]["shapeId"], shape.id)
        self.assertEqual(
            [command.type for command in resolved[0]["commands"]],
            ["M", "Q"],
        )

    def test_dot_is_a_centered_zero_length_point_line(self):
        for w,h in ((4,4),(8,6),(1,1)):
            commands=parse_path(BY_ID["dot"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M","L"])
            self.assertEqual(commands[0].points[0],(w/2,h/2))
            self.assertEqual(commands[1].points[0],(w/2,h/2))

    def test_hexagon_mitres_are_exactly_45_degrees_and_edge_to_edge(self):
        import math
        for w,h in ((24,16),(40,32),(36,12),(20,20)):
            pts=[(float(a),float(b)) for a,b in re.findall(r"(-?[\d.]+) (-?[\d.]+)",BY_ID["hexagon"].geometry(w,h)[1]["d"])]
            self.assertEqual(len(pts),6,(w,h))
            self.assertEqual((min(x for x,_ in pts),max(x for x,_ in pts)),(0,w))   # edge to edge
            self.assertEqual((min(y for _,y in pts),max(y for _,y in pts)),(0,h))
            self.assertAlmostEqual(pts[0][0],w-pts[1][0],3)                          # symmetric
            for a,b in zip(pts,pts[1:]+pts[:1]):
                dx,dy=b[0]-a[0],b[1]-a[1]
                angle=(math.degrees(math.atan2(dy,dx))+360)%180
                self.assertAlmostEqual(angle,round(angle/15)*15,2,f"{w}x{h} edge {a}->{b}")
    def test_star_is_a_ten_vertex_edge_to_edge_symmetric_outline(self):
        for w,h in ((20,20),(16,16),(24,20)):
            pts=[(float(a),float(b)) for a,b in re.findall(r"(-?[\d.]+) (-?[\d.]+)",BY_ID["star"].geometry(w,h)[1]["d"])]
            self.assertEqual(len(pts),10,(w,h))
            self.assertEqual((min(x for x,_ in pts),max(x for x,_ in pts)),(0,w))   # edge to edge
            self.assertEqual((min(y for _,y in pts),max(y for _,y in pts)),(0,h))
            self.assertAlmostEqual(pts[0][0],w/2,3)                                  # apex on the vertical axis
            for a,b in ((1,9),(2,8),(3,7),(4,6)):                                    # mirrored about that axis
                self.assertAlmostEqual(pts[a][0],w-pts[b][0],3,(w,h)); self.assertAlmostEqual(pts[a][1],pts[b][1],3,(w,h))

    def test_flared_horn_is_closed_quadratic_and_edge_to_edge(self):
        shape=BY_ID["flared-horn"]
        self.assertTrue(shape.closed)
        self.assertEqual(shape.natural,(24,16))
        commands=parse_path(shape.geometry(24,16)[1]["d"])
        self.assertEqual([command.type for command in commands],["M","Q","L","Q","Z"])
        self.assertEqual(commands[0].points[0],(0.0,6.0))
        self.assertEqual(commands[1].points,[(12.0,4.0),(24.0,0.0)])
        self.assertEqual(commands[2].points[0],(24.0,16.0))
        self.assertEqual(commands[3].points,[(12.0,12.0),(0.0,10.0)])
        points,_=sample(commands,32)
        xs=[x for x,_ in points]; ys=[y for _,y in points]
        self.assertAlmostEqual(min(xs),0,6); self.assertAlmostEqual(max(xs),24,6)
        self.assertAlmostEqual(min(ys),0,6); self.assertAlmostEqual(max(ys),16,6)
    def test_scalloped_oval_crests_touch_every_box_edge(self):
        from icon_geometry import parse_path,sample
        for w,h in ((20,20),(40,32),(44,36),(12,8),(26,40)):
            commands=parse_path(BY_ID["scalloped-oval"].geometry(w,h)[1]["d"])
            self.assertEqual(sum(command.type=="Q" for command in commands),8,(w,h))
            pts,_=sample(commands,16); xs=[x for x,_ in pts]; ys=[y for _,y in pts]
            for value,target in ((min(xs),0),(max(xs),w),(min(ys),0),(max(ys),h)):
                self.assertAlmostEqual(value,target,6,f"{w}x{h}")                    # sampler resolves the crests exactly
            self.assertGreaterEqual(min(xs),-1e-2); self.assertLessEqual(max(xs),w+1e-2)
            self.assertGreaterEqual(min(ys),-1e-2); self.assertLessEqual(max(ys),h+1e-2)
    def test_head_profile_is_one_open_all_quadratic_contour_in_its_box(self):
        from icon_geometry import parse_path,sample
        for w,h in ((24,32),(26,40),(20,20),(36,12)):
            commands=parse_path(BY_ID["head-profile"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands][0],"M")
            self.assertEqual({command.type for command in commands[1:]},{"Q"},(w,h))  # no straight segment, no Z
            pts,segments=sample(commands,16)
            self.assertEqual(segments,[],(w,h))                                       # nothing for the angle grid to fail
            xs=[x for x,_ in pts]; ys=[y for _,y in pts]
            for value,target in ((min(xs),0),(max(xs),w),(min(ys),0),(max(ys),h)):
                self.assertAlmostEqual(value,target,1,f"{w}x{h}")

    def test_holding_hand_is_open_cubic_free_and_edge_to_edge(self):
        for w,h in ((24,24),(32,24),(20,32)):
            commands=parse_path(BY_ID["holding-hand"].geometry(w,h)[1]["d"])
            self.assertEqual(commands[0].type,"M")
            self.assertNotIn("Z",[command.type for command in commands])
            self.assertTrue({command.type for command in commands}<={"M","L","Q","A"})
            pts,_=sample(commands,16); xs=[x for x,_ in pts]; ys=[y for _,y in pts]
            self.assertAlmostEqual(min(xs),0,3); self.assertAlmostEqual(max(xs),w,3)
            self.assertAlmostEqual(min(ys),0,3); self.assertAlmostEqual(max(ys),h,3)

    def test_bottle_outline_has_canonical_neck_shoulders_and_round_feet(self):
        shape=BY_ID["bottle-outline"]
        self.assertTrue(shape.closed)
        self.assertEqual(shape.natural,(14,20))
        commands=parse_path(shape.geometry(14,20)[1]["d"])
        self.assertEqual([command.type for command in commands],["M","L","L","L","L","A","L","A","L","L","Z"])
        self.assertEqual(commands[0].points[0],(3.0,0.0))
        self.assertEqual(commands[1].points[0],(11.0,0.0))
        self.assertEqual(commands[3].points[0],(14.0,7.0))
        self.assertEqual(commands[5].arc[:2],(4.0,4.0))
        self.assertEqual(commands[7].arc[:2],(4.0,4.0))

    def test_transfer_hand_is_open_bounded_and_on_grid_at_canonical_size(self):
        commands=parse_path(BY_ID["transfer-hand"].geometry(20,12)[1]["d"])
        self.assertNotIn("Z",[command.type for command in commands])
        self.assertTrue({command.type for command in commands}<={"M","L","Q"})
        points,segments=sample(commands,16)
        xs=[x for x,_ in points]; ys=[y for _,y in points]
        self.assertAlmostEqual(min(xs),0,3); self.assertAlmostEqual(max(xs),20,3)
        self.assertAlmostEqual(min(ys),0,3); self.assertAlmostEqual(max(ys),12,3)
        import math
        for left,right in segments:
            if math.dist(left,right)<1e-6: continue
            angle=(math.degrees(math.atan2(right[1]-left[1],right[0]-left[0]))+360)%180
            self.assertAlmostEqual(angle,round(angle/15)*15,6)

    def test_worker_profile_default_head_clears_identity_opening(self):
        shape=BY_ID["worker-profile"]
        commands=parse_path(shape.geometry(*shape.default)[1]["d"])
        radius=commands[1].arc[0]
        self.assertGreaterEqual(2*radius,7)      # 7u centerline diameter
        self.assertGreaterEqual(2*radius-4,3)   # 3u interior painted clearance

    def test_worker_profile_solid_reuses_the_body_with_a_round_cap_point_head(self):
        shape=BY_ID["worker-profile-solid"]
        self.assertFalse(shape.closed)
        self.assertEqual(shape.natural,(12,24))
        self.assertEqual(shape.default,(12,24))
        for w,h in ((12,24),(18,40),(20,40),(9,18)):
            solid=parse_path(shape.geometry(w,h)[1]["d"])
            outlined=parse_path(BY_ID["worker-profile"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in solid],["M","L","M","Q","Q","M","Q","M","Q"],(w,h))
            radius=min(w*.18,h*.08); centre=(round(w*.45,3),round(radius,3))
            self.assertEqual(solid[0].points[0],centre,(w,h))
            self.assertEqual(solid[1].points[0],centre,(w,h))
            self.assertEqual(solid[3:],outlined[5:],(w,h))
            self.assertEqual({command.type for command in solid[2:]},{"M","Q"},(w,h))

    def test_broken_pig_outline_has_two_closed_proportional_halves(self):
        shape=BY_ID["broken-pig-outline"]
        self.assertTrue(shape.closed)
        self.assertEqual(shape.natural,(40,22))
        self.assertEqual(shape.default,(40,22))
        for w,h in ((40,22),(80,44),(20,11),(32,18)):
            commands=parse_path(shape.geometry(w,h)[1]["d"])
            self.assertEqual(sum(command.type=="M" for command in commands),2,(w,h))
            self.assertEqual(sum(command.type=="Z" for command in commands),2,(w,h))
            self.assertEqual(sum(command.type=="Q" for command in commands),11,(w,h))
            self.assertEqual(sum(command.type=="L" for command in commands),8,(w,h))
            self.assertTrue({command.type for command in commands}<={"M","Q","L","Z"},(w,h))
            points=[point for command in commands for point in command.points]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
            self.assertEqual(commands[0].points[0],(round(w*17/40,3),round(h*4/22,3)))

    def test_broken_pig_outline_matches_the_canonical_40_by_22_paths(self):
        expected=("M17 4 Q16 0 12 0 Q8 2 4 4 Q0 6 0 11 Q0 16 4 17 "
                  "Q4 21 8 22 Q12 22 17 20 "
                  "L13 16 L17 12 L13 8 L17 4 Z "
                  "M27 4 Q30 2 34 4 Q40 4 40 10 Q40 14 35 15 "
                  "Q34 20 30 22 Q26 22 27 20 "
                  "L23 16 L27 12 L23 8 L27 4 Z")
        actual=BY_ID["broken-pig-outline"].geometry(40,22)[1]["d"]
        self.assertEqual(parse_path(actual),parse_path(expected))

    def test_broken_pig_outline_cracks_are_parallel_and_forty_five_degrees(self):
        commands=parse_path(BY_ID["broken-pig-outline"].geometry(40,22)[1]["d"])
        halves=[]; current=[]
        for command in commands:
            if command.type=="M": current=[command]
            else:
                current.append(command)
                if command.type=="Z": halves.append(current)
        self.assertEqual(len(halves),2)
        cracks=[]
        for half in halves:
            curves=[command for command in half if command.type=="Q"]
            lines=[command for command in half if command.type=="L"]
            cracks.append([curves[-1].points[-1]]+[command.points[-1] for command in lines])
        vectors=[]
        for crack in cracks:
            vectors.append([(b[0]-a[0],b[1]-a[1]) for a,b in zip(crack,crack[1:])])
        self.assertEqual(vectors[0],vectors[1])
        for dx,dy in vectors[0]: self.assertEqual(abs(dx),abs(dy))
        for left,right in zip(*cracks): self.assertEqual((right[0]-left[0],right[1]-left[1]),(10.0,0.0))

    def test_corner_gapped_frame_removes_the_lower_left_overlap_zone(self):
        commands=parse_path(BY_ID["corner-gapped-rounded-rectangle"].geometry(28,20)[1]["d"])
        self.assertEqual([command.type for command in commands],["M","A","L","A","L","A","L"])
        self.assertEqual(commands[0].points[0],(0.0,4.0))
        self.assertEqual(commands[-1].points[0],(21.0,20.0))
        self.assertNotIn("Z",[command.type for command in commands])

    def test_new_organic_atoms_are_open_cubic_free_and_bounded(self):
        for shape_id,w,h in (("open-shell",40,32),("oyster-shell",40,32),("side-gapped-rounded-rectangle",20,32),("shark-fin",20,24),("wave-line",40,8),("gripping-hand",24,20),("gapped-eye",40,28)):
            commands=parse_path(BY_ID[shape_id].geometry(w,h)[1]["d"])
            self.assertNotIn("Z",[command.type for command in commands],shape_id)
            self.assertTrue({command.type for command in commands}<={"M","L","Q","A"},shape_id)
            pts,_=sample(commands,32); xs=[x for x,_ in pts]; ys=[y for _,y in pts]
            self.assertGreaterEqual(min(xs),-1e-3,shape_id); self.assertLessEqual(max(xs),w+1e-3,shape_id)
            self.assertGreaterEqual(min(ys),-1e-3,shape_id); self.assertLessEqual(max(ys),h+1e-3,shape_id)
    def test_trapezoid_is_symmetric_on_grid_and_inside_its_box(self):
        import math
        for w,h in ((24,12),(36,12),(16,8),(40,4),(12,20),(8,8)):
            d=BY_ID["trapezoid"].geometry(w,h)[1]["d"]
            pts=[(float(a),float(b)) for a,b in re.findall(r"(-?[\d.]+) (-?[\d.]+)",d)]
            self.assertEqual(len(pts),4,d)
            (tlx,tly),(trx,_),(brx,bry),(blx,bly)=pts
            self.assertEqual((tly,bly,bry,blx),(0,h,h,0))
            self.assertEqual(brx,w)
            self.assertAlmostEqual(tlx,w-trx,3)                       # symmetric
            self.assertGreater(trx-tlx,0)                             # top edge never collapses
            self.assertTrue(0<=tlx<=w and 0<=trx<=w)                  # stays in its box
            inset=tlx
            if inset<w*0.4-1e-9:
                self.assertAlmostEqual(math.degrees(math.atan2(h,inset)),60,2)  # 3-dp registry rounding
            else:
                self.assertAlmostEqual(inset,w*0.4,3)
    def test_gable_and_open_gable_share_vertices(self):
        closed=BY_ID["gable"].geometry(24,32)[1]["d"].rstrip(" Z"); opened=BY_ID["open-gable"].geometry(24,32)[1]["d"]; self.assertEqual(closed,opened)
    def test_hook_has_one_half_circle_bowl_and_unequal_opposing_stems(self):
        for w,h in ((8,16),(8,14),(12,24)):
            commands=parse_path(BY_ID["hook"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M","L","A","L"])
            self.assertEqual(commands[0].points[0],(0.0,0.0))
            self.assertEqual(commands[2].arc[:2],(w/2,w/2))
            self.assertEqual(commands[2].points[0][0],float(w))
            self.assertEqual(commands[3].points[0][0],float(w))
            self.assertGreater(commands[1].points[0][1],commands[3].points[0][1])
    def test_dashed_rectangle_uses_four_unit_dashes_inside_its_box(self):
        for w,h in ((12,20),(20,28),(12,32)):
            commands=parse_path(BY_ID["dashed-rectangle"].geometry(w,h)[1]["d"])
            moves=[command for command in commands if command.type=="M"]
            lines=[command for command in commands if command.type=="L"]
            self.assertGreaterEqual(len(moves),8)
            self.assertGreaterEqual(len(lines),len(moves))
            points=[point for command in commands for point in command.points]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
    def test_radial_ticks_are_twelve_on_grid_rays_between_the_inner_ellipse_and_the_box(self):
        import math
        for w,h in ((20,20),(40,40),(24,16),(12,12)):
            commands=parse_path(BY_ID["radial-ticks"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M","L"]*12)
            cx,cy=w/2,h/2
            for step in range(12):
                inner=commands[step*2].points[0]; outer=commands[step*2+1].points[0]
                angle=math.radians(step*30); cos,sin=math.cos(angle),math.sin(angle)
                self.assertAlmostEqual(inner[0],cx+0.8*cx*cos,3)      # inner endpoint on the 0.8 ellipse
                self.assertAlmostEqual(inner[1],cy+0.8*cy*sin,3)
                self.assertAlmostEqual(outer[0],cx+cx*cos,3)          # outer endpoint on the box edge
                self.assertAlmostEqual(outer[1],cy+cy*sin,3)
                self.assertTrue(0<=outer[0]<=w and 0<=outer[1]<=h)    # stays in its box
            points=[point for command in commands for point in command.points]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
    def test_radial_ticks_stay_on_the_fifteen_degree_grid_in_a_square_box(self):
        import math
        for size in (20,40,48):
            commands=parse_path(BY_ID["radial-ticks"].geometry(size,size)[1]["d"])
            for step in range(12):
                (x0,y0),(x1,y1)=commands[step*2].points[0],commands[step*2+1].points[0]
                angle=(math.degrees(math.atan2(y1-y0,x1-x0))+360)%180
                self.assertLess(abs(angle-round(angle/15)*15),0.01,f"{size} tick {step}")
    def test_water_drop_is_symmetric_quadratic_and_edge_to_edge(self):
        for w,h in ((8,12),(12,18),(16,24)):
            commands=parse_path(BY_ID["water-drop"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M","Q","Q","Q","Q","Z"])
            points=[point for command in commands for point in command.points]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
    def test_tapered_spire_is_symmetric_quadratic_with_flat_base(self):
        for w,h in ((24,32),(32,40),(16,28)):
            commands=parse_path(BY_ID["tapered-spire"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M","Q","L","Q","Z"])
            self.assertEqual(commands[0].points[0],(w/2,0.0))
            self.assertEqual(commands[1].points[-1],(0.0,float(h)))
            self.assertEqual(commands[2].points[-1],(float(w),float(h)))
            self.assertEqual(commands[3].points[-1],(w/2,0.0))
    def test_faucet_has_spout_elbow_outlet_and_t_handle(self):
        commands=parse_path(BY_ID["faucet"].geometry(24,20)[1]["d"])
        self.assertEqual([command.type for command in commands],["M","L","A","L","M","L","M","L"])
        self.assertEqual(commands[0].points[0],(0.0,10.0))
        self.assertEqual(commands[3].points[0],(24.0,20.0))
        self.assertEqual(commands[5].points[0][1],0.0)
    def test_open_end_wrench_has_ring_shaft_and_exact_forty_five_degree_jaws(self):
        for w,h in ((20,8),(24,8),(30,12)):
            commands=parse_path(BY_ID["open-end-wrench"].geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M","A","A","M","L","M","L","M","L"])
            for move_index,line_index in ((5,6),(7,8)):
                start=commands[move_index].points[0]; end=commands[line_index].points[0]
                self.assertAlmostEqual(abs(end[0]-start[0]),abs(end[1]-start[1]),3)
    def test_rounded_rectangle_uses_the_four_unit_corner_token(self):
        for w,h in ((24,32),(32,40),(16,28),(40,16)):
            tag,attrs=BY_ID["rounded-rectangle"].geometry(w,h)
            self.assertEqual(tag,"rect")
            self.assertEqual(attrs["rx"],4.0)
            self.assertEqual((attrs["width"],attrs["height"]),(float(w),float(h)))
    def test_twin_gable_is_symmetric_bounded_and_uses_one_shared_valley(self):
        for w,h in ((40,32),(24,18),(16,8),(12,20)):
            commands=parse_path(BY_ID["twin-gable"].geometry(w,h)[1]["d"])
            points=[command.points[0] for command in commands if command.type in {"M","L"}]
            self.assertEqual(len(points),7)
            self.assertEqual(points[0],(0.0,float(h)))
            self.assertEqual(points[-1],(float(w),float(h)))
            self.assertEqual(points[3][0],w/2)
            self.assertEqual(points[1][1],points[3][1])
            self.assertEqual(points[3][1],points[5][1])
            self.assertEqual(points[2][1],0)
            self.assertEqual(points[4][1],0)
            self.assertEqual(points[2][0]+points[4][0],w)
    def test_s_bend_is_arc_only_edge_to_edge_and_tangent_at_center(self):
        for w,h in ((20,20),(32,24),(12,36)):
            d=BY_ID["s-bend"].geometry(w,h)[1]["d"]
            self.assertNotRegex(d,r"[CcQq]")
            commands=parse_path(d)
            self.assertEqual([command.type for command in commands],["M","A","A"])
            self.assertEqual(commands[0].points[0],(0.0,0.0))
            self.assertEqual(commands[1].points[0],(w/2,h/2))
            self.assertEqual(commands[2].points[0],(float(w),float(h)))
            self.assertEqual(commands[1].arc[4],1)
            self.assertEqual(commands[2].arc[4],0)
    def test_bulb_outline_is_open_symmetric_quadratic_and_edge_to_edge(self):
        for w,h in ((24,32),(18,24),(30,40)):
            d=BY_ID["bulb-outline"].geometry(w,h)[1]["d"]
            self.assertNotRegex(d,r"[CcAaLlZz]")
            commands=parse_path(d)
            self.assertEqual([command.type for command in commands],["M","Q","Q","Q","Q","Q","Q"])
            self.assertEqual(commands[0].points[0],(w/3,h))
            self.assertEqual(commands[-1].points[-1],(2*w/3,h))
            points=[point for command in commands for point in command.points]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
    def test_lobed_drop_is_quadratic_only_and_edge_to_edge(self):
        for w,h in ((20,24),(32,40),(16,32),(28,36)):
            d=BY_ID["lobed-drop"].geometry(w,h)[1]["d"]
            self.assertNotRegex(d,r"[CcAaLl]")
            commands=parse_path(d)
            self.assertEqual(commands[0].type,"M")
            self.assertEqual(commands[-1].type,"Z")
            points=[point for command in commands for point in command.points]
            xs=[point[0] for point in points]; ys=[point[1] for point in points]
            self.assertEqual((min(xs),max(xs)),(0.0,float(w)))
            self.assertEqual((min(ys),max(ys)),(0.0,float(h)))
    def test_stepped_cog_is_orthogonal_symmetric_and_edge_to_edge(self):
        for size in (20,36,44):
            commands=parse_path(BY_ID["stepped-cog"].geometry(size,size)[1]["d"])
            points=[command.points[0] for command in commands if command.type in {"M","L"}]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(size)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(size)))
            for a,b in zip(points,points[1:]+points[:1]):
                self.assertTrue(a[0]==b[0] or a[1]==b[1],(a,b))
    def test_twin_lobed_drop_is_symmetric_quadratic_and_edge_to_edge(self):
        for w,h in ((20,20),(36,36),(32,40)):
            d=BY_ID["twin-lobed-drop"].geometry(w,h)[1]["d"]
            self.assertNotRegex(d,r"[CcAaLl]")
            commands=parse_path(d)
            points=[point for command in commands for point in command.points]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
    def test_lightning_bolt_is_closed_edge_to_edge_and_on_grid_at_canonical_size(self):
        import math
        shape=BY_ID["lightning-bolt"]
        self.assertTrue(shape.closed)
        self.assertEqual(shape.natural,(20,24))
        for w,h in ((20,24),(30,36),(15,24)):
            commands=parse_path(shape.geometry(w,h)[1]["d"])
            self.assertEqual([command.type for command in commands],["M"]+["L"]*5+["Z"],(w,h))
            points,_=sample(commands,4); xs=[x for x,_ in points]; ys=[y for _,y in points]
            self.assertEqual((min(xs),max(xs)),(0.0,float(w)))
            self.assertEqual((min(ys),max(ys)),(0.0,float(h)))
        commands=parse_path(shape.geometry(*shape.natural)[1]["d"])
        points=[command.points[0] for command in commands[:6]]
        self.assertEqual(points,[(14.0,0.0),(0.0,14.0),(8.0,14.0),(8.0,24.0),(20.0,12.0),(14.0,12.0)])
        for left,right in zip(points,points[1:]+points[:1]):
            angle=(math.degrees(math.atan2(right[1]-left[1],right[0]-left[0]))+360)%180
            self.assertAlmostEqual(angle,round(angle/15)*15,6,(left,right))
    def test_puzzle_piece_has_two_tabs_two_sockets_and_stays_bounded(self):
        shape=BY_ID["puzzle-piece"]
        self.assertTrue(shape.closed)
        self.assertEqual(shape.natural,(20,20))
        for w,h in ((20,20),(32,24),(18,30)):
            commands=parse_path(shape.geometry(w,h)[1]["d"])
            self.assertEqual(commands[0].type,"M")
            self.assertEqual(commands[-1].type,"Z")
            self.assertEqual(sum(command.type=="Q" for command in commands),8,(w,h))
            self.assertTrue({command.type for command in commands}<={"M","L","Q","Z"},(w,h))
            points,_=sample(commands,32); xs=[x for x,_ in points]; ys=[y for _,y in points]
            self.assertAlmostEqual(min(xs),0,3); self.assertAlmostEqual(max(xs),w,3)
            self.assertAlmostEqual(min(ys),0,3); self.assertAlmostEqual(max(ys),h,3)
            self.assertIn((round(w*.5,3),0.0),[command.points[-1] for command in commands if command.type=="Q"])
            self.assertIn((float(w),round(h*.5,3)),[command.points[-1] for command in commands if command.type=="Q"])
            self.assertIn((round(w*.5,3),round(h*.8,3)),[command.points[-1] for command in commands if command.type=="Q"])
            self.assertIn((round(w*.2,3),round(h*.5,3)),[command.points[-1] for command in commands if command.type=="Q"])
        commands=parse_path(shape.geometry(*shape.natural)[1]["d"])
        for command in commands:
            if command.type in {"M","L"}:
                self.assertTrue(all(value.is_integer() for point in command.points for value in point),command)
    def test_phone_handset_outline_is_closed_quadratic_and_edge_to_edge(self):
        import math
        shape=BY_ID["phone-handset-outline"]
        self.assertTrue(shape.closed)
        self.assertEqual(shape.natural,(36,36))
        for w,h in ((36,36),(32,24),(20,28)):
            commands=parse_path(shape.geometry(w,h)[1]["d"])
            self.assertEqual(commands[0].type,"M")
            self.assertEqual(commands[-1].type,"Z")
            self.assertTrue({command.type for command in commands}<={"M","L","Q","Z"},(w,h))
            points,_=sample(commands,32); xs=[x for x,_ in points]; ys=[y for _,y in points]
            self.assertAlmostEqual(min(xs),0,3); self.assertAlmostEqual(max(xs),w,3)
            self.assertAlmostEqual(min(ys),0,3); self.assertAlmostEqual(max(ys),h,3)
        _,segments=sample(parse_path(shape.geometry(*shape.natural)[1]["d"]),8)
        for left,right in segments:
            if math.dist(left,right)<1e-6: continue
            angle=(math.degrees(math.atan2(right[1]-left[1],right[0]-left[0]))+360)%180
            self.assertAlmostEqual(angle,round(angle/15)*15,6,(left,right))
    def test_gapped_rounded_rectangle_breaks_only_its_head_and_stays_edge_to_edge(self):
        for w,h in ((32,36),(24,32),(40,20),(20,20),(16,8)):
            commands=parse_path(BY_ID["gapped-rounded-rectangle"].geometry(w,h)[1]["d"])
            self.assertEqual(commands[0].type,"M",(w,h))
            self.assertNotIn("Z",[command.type for command in commands],(w,h))     # one open contour
            self.assertEqual(sum(command.type=="A" for command in commands),4,(w,h))
            start=commands[0].points[0]; end=commands[-1].points[0]
            self.assertEqual((start[1],end[1]),(0,0),(w,h))                        # the break is in the head
            self.assertAlmostEqual(start[0]+end[0],w,6,f"{w}x{h}")                 # centred on the head
            self.assertAlmostEqual(start[0]-end[0],w/2,6,f"{w}x{h}")               # gap is half the width
            radii={command.arc[0] for command in commands if command.arc}
            self.assertEqual(radii,{min(4,w/4,h/2)},(w,h))                         # one clamped 4u corner token
            pts,_=sample(commands,16); xs=[x for x,_ in pts]; ys=[y for _,y in pts]
            for value,target in ((min(xs),0),(max(xs),w),(min(ys),0),(max(ys),h)):
                self.assertAlmostEqual(value,target,6,f"{w}x{h}")                  # edge to edge in its box

    def test_gapped_rounded_rectangle_traces_the_rounded_rectangle_it_breaks(self):
        # Every corner and side the gapped atom keeps must land on the closed
        # rounded-rectangle of the same box, so the two read as one family.
        gapped,_=sample(parse_path(BY_ID["gapped-rounded-rectangle"].geometry(32,36)[1]["d"]),16)
        from icon_geometry import primitive_commands
        closed,_=sample(primitive_commands(*BY_ID["rounded-rectangle"].geometry(32,36)),16)
        import math
        for point in gapped:
            self.assertLess(min(math.dist(point,other) for other in closed),.05,point)

    def test_twin_gable_and_open_twin_gable_share_vertices(self):
        closed=BY_ID["twin-gable"].geometry(40,32)[1]["d"].rstrip(" Z"); opened=BY_ID["open-twin-gable"].geometry(40,32)[1]["d"]; self.assertEqual(closed,opened)
    def test_open_twin_gable_is_two_forty_five_degree_peaks_edge_to_edge(self):
        import math
        for w,h in ((32,8),(40,32),(24,6),(16,20)):
            d=BY_ID["open-twin-gable"].geometry(w,h)[1]["d"]
            self.assertNotRegex(d,r"[CcAaQqZz]")
            commands=parse_path(d)
            points=[command.points[0] for command in commands]
            self.assertEqual((min(x for x,_ in points),max(x for x,_ in points)),(0.0,float(w)))
            self.assertEqual((min(y for _,y in points),max(y for _,y in points)),(0.0,float(h)))
            rise=min(w/4,h)
            self.assertEqual([y for _,y in points if y==0],[0.0,0.0])   # exactly two peaks
            for a,b in zip(points,points[1:]):
                angle=(math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))+360)%180
                self.assertAlmostEqual(angle,round(angle/15)*15,2,(a,b))
                if a[1]!=b[1] and a[0]!=b[0]:
                    self.assertAlmostEqual(abs(b[1]-a[1]),abs(b[0]-a[0]),3)   # 45-degree flanks
            self.assertAlmostEqual(min(y for _,y in points if y>0) if h>rise else rise,rise,3)
    def test_spiral_is_arc_only_edge_to_edge_and_tangent_continuous(self):
        import math
        for w,h in ((22,20),(36,36),(40,24),(12,16)):
            d=BY_ID["spiral"].geometry(w,h)[1]["d"]
            self.assertNotRegex(d,r"[CcQqLlZz]")
            commands=parse_path(d)
            self.assertEqual([command.type for command in commands],["M"]+["A"]*5)
            points=[command.points[0] for command in commands]
            self.assertAlmostEqual(min(x for x,_ in points),0.0,3)
            self.assertAlmostEqual(max(x for x,_ in points),float(w),3)
            self.assertAlmostEqual(min(y for _,y in points),0.0,3)
            self.assertAlmostEqual(max(y for _,y in points),float(h),3)
            radii=[command.arc[0] for command in commands[1:]]
            for previous,current in zip(radii,radii[1:]):
                self.assertAlmostEqual(current/previous,0.86,2)          # winds inward at a constant ratio
            aspect=[command.arc[1]/command.arc[0] for command in commands[1:]]
            for value in aspect:
                self.assertAlmostEqual(value,aspect[0],3)                # one consistent ellipse family
    def test_spiral_turns_stay_apart_at_icon_size(self):
        commands=parse_path(BY_ID["spiral"].geometry(36,36)[1]["d"])
        points,_=sample(commands,8)
        skip=len(points)//8
        closest=min(__import__("math").dist(points[i],points[j])
                    for i in range(len(points)) for j in range(i+skip,len(points)))
        self.assertGreater(closest,8.0)   # 4u painted clearance at the Regular stroke
if __name__=="__main__": unittest.main()
