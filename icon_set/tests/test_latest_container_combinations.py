import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.latest_container_combinations import LatestContainerPairs
from icon_set.tests import test_primitives


def fixture(root):
    def write(path, value):
        p = root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(value))
    def record(uid, family, parent=None, date="2026-09-01", sizing=None):
        return dict(icon_id=uid, key=family+"/"+uid, family=family,
                    profile="SYMBOL32" if family=="symbol" else "CONTAINER64",
                    canvas_size=32 if family=="symbol" else 64,
                    variant_of=parent, created_at=date, sizing_mode=sizing,
                    validation=dict(status="valid"))
    host = record("box", "container")
    old = record("plus", "symbol")
    new = record("plus-v2", "symbol", "plus", "2026-09-02")
    resize = record("plus-resize", "symbol", "plus-v2", "2026-09-03", "container-content-resize")
    write("container64/manifest.json", dict(icons=[host]))
    write("symbol32/manifest.json", dict(icons=[old, new, resize]))
    write("gallery/icons.json", dict(icons=[host, old, new, resize]))
    write("gallery/combinations.json", dict(references={"host": {}, "sub": {}}, rows=[
        dict(id="pair", kind="container", concept="Box plus", main_id="host", sub_id="sub",
             main_generated=[host], sub_generated=[old]),
        dict(id="missing", kind="container", concept="Missing", main_id="host", sub_id="sub",
             main_generated=[host], sub_generated=[])]))
    def svg(size, path):
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>'
    doc = svg(64, "M2 2H62V62H2Z")
    (root/"container64/box.svg").write_text(doc)
    (root/"symbol32/plus-v2.svg").write_text(svg(32, "M16 2V30M2 16H30"))
    write("data/container-content-areas.json", dict(areas={"box": dict(
        source_sha256=hashlib.sha256(doc.encode()).hexdigest(),
        method="selected semantic enclosed face", polygon=[[10,10],[54,10],[54,54],[10,54]], center=[32,32])}))
    write("data/container-placement-preferences.json", {})
    return LatestContainerPairs(root, root/"data")


class LatestPairsTests(unittest.TestCase):
    def test_latest_descendant_and_native_composition(self):
        with tempfile.TemporaryDirectory() as temp:
            service = fixture(Path(temp))
            result = service.response({"id": ["pair"]})
            pair = result["pairs"][0]
            self.assertEqual(pair["symbol_key"], "symbol/plus-v2")
            self.assertEqual(pair["status"], "pass")
            self.assertEqual(pair["scale"], 1)
            self.assertEqual(pair["native_symbol_size"], [32, 32])
            self.assertIn("translate(16.0000000000 16.0000000000) scale(1.0000000000)", pair["svg"])
            self.assertFalse(pair["fully_validated"])
            self.assertEqual(service.response({"limit": ["1"]})["next_offset"], 1)
            self.assertEqual(service.response({"id": ["missing"]})["pairs"][0]["status"], "missing")
            for query in ({"sizes": ["all"]}, {"limit": ["0"]}, {"offset": ["-1"]}):
                with self.assertRaises(ValueError): service.response(query)

    def test_stale_area_does_not_claim_fit_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            service = fixture(Path(temp))
            service.areas["box"]["source_sha256"] = "old"
            self.assertEqual(service.response({"id": ["pair"]})["pairs"][0]["status"], "review")


class LatestPairsServerTests(unittest.TestCase):
    setUp = test_primitives.GenerationQueueServerTests.setUp
    request = test_primitives.GenerationQueueServerTests.request

    def test_json_and_svg_routes(self):
        with tempfile.TemporaryDirectory() as temp:
            service = fixture(Path(temp))
            with patch("icon_set.scripts.latest_container_combinations.LatestContainerPairs", return_value=service):
                url = "/api/combinations/container/"
                code, body, _ = self.request("GET", url+"latest?id=pair")
                self.assertEqual(code, 200)
                self.assertEqual(json.loads(body)["pairs"][0]["symbol_key"], "symbol/plus-v2")
                self.assertNotIn("svg", json.loads(body)["pairs"][0])
                code, body, _ = self.request("GET", url+"svg?id=pair")
                self.assertEqual(code, 200)
                self.assertIn(b"<svg", body)
                self.assertEqual(self.request("GET", url+"svg?id=missing")[0], 409)
                self.assertEqual(self.request("GET", url+"svg?id=unknown")[0], 404)
                self.assertEqual(self.request("GET", url+"svg")[0], 400)


    def test_combine_post_and_results_route(self):
        from icon_set.scripts import container_combination_results as saved
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);fixture(root);state=root/"state"
            real_combine,real_listing=saved.combine,saved.listing
            with patch.object(saved,"combine",side_effect=lambda _r,_d,_s,q:real_combine(root,root/"data",state,q)), patch.object(saved,"listing",side_effect=lambda *_:real_listing(root,root/"data",state)):
                code,body,_=self.request("POST","/api/combinations/container/combine",{"limit":10,"offset":0})
                self.assertEqual(code,200)
                self.assertTrue(all("svg" not in p for p in json.loads(body)["pairs"]))
                code,body,_=self.request("GET","/api/combinations/container/results")
                self.assertEqual(code,200)
                self.assertEqual(json.loads(body)["processed"],2)


class SavedCombinationTests(unittest.TestCase):
    def test_saved_batches_counts_and_invalidation(self):
        from icon_set.scripts.container_combination_results import combine, listing, saved_svg
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp); fixture(root)
            state=root/"state"
            before=listing(root,root/"data",state)
            self.assertEqual(before["processed"],0)
            self.assertEqual(before["containers"]["total"],1)
            self.assertEqual(before["symbols"]["total"],1)
            batch=combine(root,root/"data",state,{"limit":["10"],"snapshot":[before["snapshot"]]})
            self.assertTrue(all("svg" not in p for p in batch["pairs"]))
            self.assertIn("<svg",saved_svg(root,root/"data",state,"pair"))
            after=listing(root,root/"data",state)
            self.assertEqual(after["processed"],2)
            self.assertEqual(after["counts"],{"missing":1,"pass":1})
            self.assertEqual(after["selections"]["pair"]["symbol_key"],"symbol/plus-v2")
            gallery=root/"gallery/icons.json"
            content=json.loads(gallery.read_text())
            content["icons"].append(dict(key="solo/unrelated",family="solo",icon_id="unrelated"))
            gallery.write_text(json.dumps(content))
            self.assertEqual(listing(root,root/"data",state)["processed"],2)

            path=root/"symbol32/manifest.json"
            changed=json.loads(path.read_text());changed["icons"][0]["validation"]["status"]="invalid"
            path.write_text(json.dumps(changed))
            self.assertEqual(listing(root,root/"data",state)["processed"],0)
            self.assertIsNone(saved_svg(root,root/"data",state,"pair"))
            with self.assertRaises(ValueError):
                combine(root,root/"data",state,{"snapshot":[before["snapshot"]]})
