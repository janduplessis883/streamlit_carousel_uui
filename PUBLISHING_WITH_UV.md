# Publishing to PyPI with uv

Yes! You can definitely publish to PyPI using `uv`. Here's how:

## Prerequisites

Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# or
pip install uv
```

## Option 1: Using uv build and uv publish (Recommended)

### 1. Build the package
```bash
uv build
```

This will create distribution files in the `dist/` directory.

### 2. Publish to PyPI
```bash
uv publish
```

You'll be prompted for your PyPI credentials.

### 3. Or publish to Test PyPI first
```bash
uv publish --publish-url https://test.pypi.org/legacy/
```

## Option 2: Using uv with pyproject.toml (Modern Approach)

First, let's convert to pyproject.toml format (recommended for modern Python packaging):

### 1. Create pyproject.toml
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "streamlit-carousel-uui"
version = "0.1.0"
description = "A Streamlit component for displaying an Untitled UI styled carousel"
readme = "README.md"
requires-python = ">=3.7"
license = {text = "MIT"}
authors = [
    {name = "Jan du Plessis"}
]
keywords = ["streamlit", "carousel", "component", "untitled-ui", "react"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "streamlit>=1.0.0",
]

[project.urls]
Homepage = "https://github.com/janduplessis883/streamlit_carousel_uui"
Repository = "https://github.com/janduplessis883/streamlit_carousel_uui"
Issues = "https://github.com/janduplessis883/streamlit_carousel_uui/issues"
```

### 2. Build with uv
```bash
uv build
```

### 3. Publish with uv
```bash
uv publish
```

## Complete Publishing Workflow with uv

```bash
# 1. Make sure frontend is built
cd frontend
npm run build
cd ..

# 2. Copy build to package
cp -r frontend/build streamlit_carousel_uui/frontend/

# 3. Build the package
uv build

# 4. Check the built package (optional)
tar -tzf dist/streamlit-carousel-uui-0.1.0.tar.gz

# 5. Test on Test PyPI first (recommended)
uv publish --publish-url https://test.pypi.org/legacy/

# 6. Install from Test PyPI to verify
pip install --index-url https://test.pypi.org/simple/ streamlit-carousel-uui

# 7. If everything works, publish to real PyPI
uv publish
```

## Environment Variables for Authentication

You can set PyPI credentials as environment variables to avoid prompts:

```bash
export UV_PUBLISH_USERNAME="__token__"
export UV_PUBLISH_PASSWORD="pypi-..."  # Your PyPI API token
```

Or use a `.pypirc` file in your home directory:

```ini
[pypi]
username = __token__
password = pypi-...

[testpypi]
username = __token__
password = pypi-...
```

## Quick Command Reference

```bash
# Build only
uv build

# Build and publish to PyPI
uv build && uv publish

# Build and publish to Test PyPI
uv build && uv publish --publish-url https://test.pypi.org/legacy/

# Build specific formats
uv build --sdist          # Source distribution only
uv build --wheel          # Wheel only
uv build --sdist --wheel  # Both (default)

# Check what will be included
uv build --list
```

## Benefits of Using uv

1. **Faster**: uv is significantly faster than pip/twine
2. **All-in-one**: Build and publish in one tool
3. **Modern**: Built for modern Python packaging
4. **Better errors**: Clearer error messages
5. **No separate upload tool needed**: Replaces twine

## Troubleshooting

### Build fails
```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info
uv build
```

### Missing files in package
Check your `MANIFEST.in` and ensure frontend/build is included.

### Authentication issues
```bash
# Use token authentication (recommended)
uv publish --token pypi-your-token-here

# Or set environment variable
export UV_PUBLISH_TOKEN="pypi-your-token-here"
uv publish
```

## After Publishing

Users can install your package with:
```bash
pip install streamlit-carousel-uui
# or with uv
uv pip install streamlit-carousel-uui
```

## Version Updates

To publish a new version:
1. Update version in `setup.py` (or `pyproject.toml`)
2. Rebuild: `uv build`
3. Publish: `uv publish`

That's it! uv makes the publishing process much simpler and faster than the traditional pip/twine workflow.
