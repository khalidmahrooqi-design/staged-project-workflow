"""Check package metadata, local Markdown links, and accidental private paths."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / "skills/staged-project-workflow/SKILL.md"
text = skill.read_text(encoding="utf-8")
assert text.startswith("---\n"), "Missing frontmatter"
frontmatter = text.split("---\n", 2)[1]
assert re.search(r"^name: staged-project-workflow$", frontmatter, re.M), "Invalid name"
assert re.search(r"^description: .+", frontmatter, re.M), "Missing description"
assert re.search(r"^license: MIT$", frontmatter, re.M), "Missing license"
assert len(text.split("---\n", 2)[2].strip()) > 100, "Missing instructions"
assert "[TODO:" not in text, "Unfinished scaffold"
for file in root.rglob("*.md"):
    if any(part in {".git", "Codex", "verification"} for part in file.relative_to(root).parts):
        continue
    content = file.read_text(encoding="utf-8")
    assert not re.search(r"/Users/|OneDrive-|github_pat_|gh[pousr]_[A-Za-z0-9]{20,}", content), f"Private content in {file}"
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        if re.match(r"https?://|#|mailto:", target):
            continue
        assert (file.parent / target.split("#")[0]).exists(), f"Broken link in {file}: {target}"
assert (root / "LICENSE").read_text().startswith("MIT License"), "Missing MIT license"
print("Package metadata, local links, and private-path checks passed.")
