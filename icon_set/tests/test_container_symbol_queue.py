import json
import unittest
from icon_set.tests import test_primitives


class ContainerSymbolQueueTests(unittest.TestCase):
    setUp = test_primitives.GenerationQueueServerTests.setUp
    request = test_primitives.GenerationQueueServerTests.request

    def test_queue_coverage_pagination_and_refresh(self):
        refs = {uid: dict(concept=uid, reference_url=f"combination-originals/{uid}.svg", generated=[])
                for uid in ("covered", "resize", "missing", "failed")}
        rows = [dict(id=str(i), kind="container", sub_id=uid, main_id="host", concept="Document " + uid,
                     sub_generated=[dict(icon_id=uid, key="symbol/" + uid, preview_url="../symbol32/"+uid+".svg")]
                     if uid != "missing" else [])
                for i, uid in enumerate(("covered", "resize", "resize", "missing", "failed"))]
        manifest = dict(icons=[dict(icon_id=uid, family="symbol", profile="SYMBOL32", canvas_size=32,
                                   validation=dict(status="invalid" if uid == "failed" else "valid"),
                                   **({"sizing_mode": "container-content-resize"} if uid == "resize" else {}))
                               for uid in ("covered", "resize", "failed")])
        (self.dist / "symbol32").mkdir()
        mp = self.dist / "symbol32/manifest.json"
        mp.write_text(json.dumps(manifest))
        (self.dist / "gallery/combinations.json").write_text(json.dumps(dict(rows=rows, references=refs)))
        url = "/api/combinations/generation-queue"
        code, body, _ = self.request("GET", url + "?limit=2")
        self.assertEqual(code, 200)
        data = json.loads(body)
        self.assertEqual((data["requirements_total"], data["covered_requirements"], data["total"]), (4, 1, 3))
        self.assertEqual(data["next_offset"], 2)
        tail = json.loads(self.request("GET", url + "?limit=2&offset=2")[1])
        self.assertIsNone(tail["next_offset"])
        self.assertEqual(tail["briefs"][0]["source_id"], "resize")
        self.assertEqual(tail["briefs"][0]["combination_count"], 2)
        self.assertEqual(tail["briefs"][0]["reference_url"], "/gallery/combination-originals/resize.svg")
        self.assertEqual(json.loads(self.request("GET", url + "?q=missing")[1])["total"], 1)
        for query in ("limit=0", "offset=-1", "limit=x", "family=sub", "kind=side"):
            self.assertEqual(self.request("GET", url + "?" + query)[0], 400)
        manifest["icons"][1].pop("sizing_mode")
        mp.write_text(json.dumps(manifest))
        self.assertEqual(json.loads(self.request("GET", url)[1])["total"], 2)
