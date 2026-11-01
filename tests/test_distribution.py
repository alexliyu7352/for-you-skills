import json, pathlib, unittest, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
NAMES = ["x-assistant", "x-explain", "x-myth-check", "x-format-advisor", "x-publish-checklist", "x-review-posts", "x-reach-diagnosis", "x-create-visuals"]

class DistributionTests(unittest.TestCase):
    def test_english_corpus_exists(self):
        files = sorted((ROOT / "knowledge").glob("topic-*.json"))
        self.assertEqual(len(files), 7, "English knowledge topics are missing")
        for path in files:
            self.assertIsNone(re.search(r"[\u3400-\u9fff]", path.read_text(encoding='utf-8')), str(path))

    def test_all_skills_present(self):
        for name in NAMES:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)

if __name__ == "__main__": unittest.main()
