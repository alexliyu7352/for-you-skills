# Validation

To check a checkout of this version, run from the repository root:

```bash
python tools/validate.py
python tools/build.py --check
python -m unittest discover -s tests -v
```

These commands check evidence integrity, generated skill bundles and the automated test suite. The test count and supported platforms depend on the checked-out version. Passing these checks does not establish native model execution in every client, live X.com collection, image quality or increased reach.

See the [current validation summary](https://github.com/alexliyu7352/for-you-skills/blob/main/docs/validation/results.md) and [GitHub Actions results](https://github.com/alexliyu7352/for-you-skills/actions/workflows/validate.yml) for current results. Internal development records are not distributed with the package.
