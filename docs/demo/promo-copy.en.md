# For You Skills: launch copy

Does your second post of the day really lose 40% of its reach?

I wanted to see the code behind that advice.

I turned my analysis of the public X.com / Twitter recommendation code into For You Skills: an open-source skill pack you can ask questions in plain language.

Ask about posting frequency, ranking weights, images, links, or choosing a Post versus an Article. It uses a bundled knowledge base to explain the relevant code, suggest what to do, and link to the original sources. It also states where the evidence runs out.

Bring a draft and it can review the opening, length, images, and argument, then propose concrete edits.

The demo shows two actual runs: checking the “second post” claim and turning my own Article-reach observation into an introductory Post. The source code and full outputs are retained. My impression counts are not a claim about the skill's performance.

For Claude Code, Codex, Cursor, and other compatible agents. Install the router and ask your question; you don't need to learn eight skill names.

https://github.com/alexliyu7352/for-you-skills

Try it with a question you have actually struggled with.

---

## Installation and research

```bash
npx skills add alexliyu7352/for-you-skills --skill x-assistant
```

Research: https://blog.go5.si/posts/x-algorithm-teardown/

Mainline-following research updates: https://x.com/alexlee20122022

This demonstration uses public code snapshot `5ed7963` and a knowledge cutoff of 2026-10-29. Public code and defaults do not establish every live configuration.

The current video is in Simplified Chinese, with all explanations on screen and no voiceover. It is an edited replay of actual results, not a live generation or installation recording. The complete English launch copy above is supplied for adaptation; it has not been posted.
