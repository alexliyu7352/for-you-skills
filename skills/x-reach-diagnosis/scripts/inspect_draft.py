"""Inspect supplied draft text and a limited video-index predicate; no X scoring."""
import argparse
import json
import sys
import math
from pathlib import Path

SNAPSHOT = "5ed796374ea48ee26058aab66ab10c266bea2bef"

def inspect_text(text, article_title=""):
    normalized = text.strip()
    return {
        "raw_characters": len(text),
        "raw_preview_4000": text[:4000],
        "characters": len(normalized),
        "preview_4000": normalized[:4000].rstrip(),
        "after_4000_characters": max(0, len(normalized) - 4000),
        "article_title_preview_200": article_title.strip()[:200].rstrip(),
        "normalization": "characters and preview_4000 trim leading/trailing whitespace; raw_characters and raw_preview_4000 preserve the supplied string. Counts are Unicode code points, not grapheme clusters or X weighted-length units.",
        "scope": "Editorial preview of supplied strings, not reconstructed production renderer input; not a publishing limit.",
    }

def inspect_video_gate(media, complete=True):
    reasons = []
    unknown = not complete
    has_video = False
    if not media:
        return {"status": "not_applicable" if complete else "unknown", "reasons": ["No complete video media list provided."], "scope": "Limited type/duration predicate only; not total indexing eligibility or exposure."}
    for index, item in enumerate(media, 1):
        kind = item.get("type")
        if kind in ("video", "TweetVideo", "AmplifyVideo"):
            has_video = True
            value = item.get("duration_ms")
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                unknown = True
            elif value <= 10000:
                reasons.append(f"Media {index}: duration is not strictly greater than 10000 ms.")
        elif kind in ("image", "photo", "gif", "other"):
            reasons.append(f"Media {index}: not an accepted video type in this predicate.")
        else:
            unknown = True
    status = "fails" if reasons else ("unknown" if unknown or not has_video else "passes")
    return {
        "status": status, "reasons": reasons,
        "scope": "Limited supplied type/duration predicate only. Generic video means the caller has verified an accepted ordinary X video type; no other indexing, metadata, safety, retrieval or ranking conditions are evaluated.",
    }

def main():
    # JSON is always UTF-8, including redirected output on legacy Windows locales.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", required=True, help="UTF-8 full draft path; not an X URL")
    parser.add_argument("--article-title", default="")
    parser.add_argument("--media-json", help='JSON list or {"media":[{"type":"video","duration_ms":10001}],"complete":true}; unknown duration must be null or omitted')
    args = parser.parse_args()
    try:
        # Preserve the decoded input, including CRLF/lone CR, before strip().
        with Path(args.text).open(encoding="utf-8", newline="") as draft:
            text = draft.read()
    except (OSError, UnicodeError) as exc:
        parser.error(f"cannot read UTF-8 draft: {exc}")
    result = {"source_snapshot": SNAPSHOT, "text": inspect_text(text, args.article_title)}
    if args.media_json:
        try:
            raw = json.loads(Path(args.media_json).read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            parser.error(f"cannot read media JSON: {exc}")
        if isinstance(raw, list):
            media, complete = raw, True
        elif isinstance(raw, dict):
            media, complete = raw.get("media"), raw.get("complete", True)
        else:
            parser.error("media JSON must be a list or an object containing media")
        if not isinstance(media, list) or not all(isinstance(x, dict) for x in media) or not isinstance(complete, bool):
            parser.error("media must be a list of objects and complete must be boolean")
        result["video_index_partial_check"] = inspect_video_gate(media, complete)
    else:
        result["video_index_partial_check"] = {"status": "unknown", "reason": "No media metadata supplied."}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
