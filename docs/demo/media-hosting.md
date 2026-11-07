# Demo hosting and Git history cleanup

The demo videos are hosted on YouTube:

| Language | Video | Captions |
| --- | --- | --- |
| 中文版 | [Watch on YouTube](https://youtu.be/TQfDplGaFXY?si=mNGTutX1lj7Py08r) | [中文字幕](captions.zh-CN.srt) |
| English | [Watch on YouTube](https://youtu.be/QSL0kNQvs_E?si=VXDbXhogFb7bq7ip) | [English subtitles](captions.en.srt) |

On 2026-11-07, the two MP4 files and the animated GIF preview were removed from all branch and tag history. Static covers, captions, original prompts, answers and execution evidence remain in the repository. The separate 3:49 installation recording has no replacement video URL; its [execution evidence](live/README.md) remains available.

The English demo is a translation and new layout of the archived results. The original code snapshot and evidence limits remain the same. It does not represent a separately rerun English agent session.

## Earlier commit references

Only two existing commits were reconstructed during media removal. Their commit metadata and parent links were recreated; all non-media file bytes were preserved. These mappings refer to their media-free equivalents, before the subsequent documentation update:

| Original commit | Media-free equivalent |
| --- | --- |
| `27ea82bf1c6caa4459f483fd7aacfb362b9189be` | `9d19ec38e5b3d8c51458b0bce83197f6df49d7d7` |
| `8f4e6b1967ef1b04284f40776d684acb0c38e5bb` | `023e94979c498d66dbf8a3ac5ff561f44bba8037` |

Historical evidence files retain the original commit IDs they recorded. For example, `live/installed-byte-check.json` still records `27ea82b`; the installed skill files at its mapped revision are byte-for-byte identical. The `v1.0.0`, `v1.1.0` and `v1.1.1` tags predate the media additions and remain unchanged.

## Existing clones

A normal pull does not remove the old media objects from an existing clone. To get the smaller history, clone into a new directory after saving any uncommitted work or local-only commits:

```bash
git clone --single-branch https://github.com/alexliyu7352/for-you-skills.git for-you-skills-clean
```

The old directory retains its old objects until you remove or clean that clone. Avoid merging its old `main` back into the rewritten branch, which would restore the removed history.

中文说明：影片已迁往上表中的 YouTube 链接，仓库及可获取的分支、标签历史不再包含 MP4 和 GIF 预览。已有克隆仍保留旧对象，普通 `git pull` 不会缩小它；请先保存本地工作，再克隆到新目录。历史核验记录中的提交号保留原值，对照上表即可找到不含视频的对应版本。
