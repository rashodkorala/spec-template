"""The parts and device platforms this project has. Used by scripts/check, scripts/device-tests and scripts/metrics."""

# Columns in features/*/validation.md, in order. Match parity.md and the templates' "Parts affected:" lines.
PARTS = ["iOS", "Android", "Backend"]

# Platforms a person runs device-tests/ cases on. Each case's platform table and Results log use these names.
DEVICE_PLATFORMS = ["Android", "iOS"]
