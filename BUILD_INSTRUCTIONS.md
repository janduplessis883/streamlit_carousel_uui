# Build Instructions

## Development Setup

### 1. Install Python Dependencies
```bash
pip install -e .
```

### 2. Install Frontend Dependencies
```bash
cd frontend
npm install
```

### 3. Development Mode

To work in development mode with hot reloading:

1. Start the React development server:
```bash
cd frontend
npm start
```

2. Update `streamlit_carousel_uui/__init__.py` to set `_RELEASE = False`

3. Run your Streamlit app:
```bash
streamlit run example.py
```

## Building for Production

### 1. Build the Frontend
```bash
cd frontend
npm run build
```

### 2. Copy Build to Package
```bash
cp -r frontend/build streamlit_carousel_uui/frontend/
```

### 3. Update Release Mode
In `streamlit_carousel_uui/__init__.py`, set `_RELEASE = True`

### 4. Build Python Package
```bash
python setup.py sdist bdist_wheel
```

### 5. Test Installation Locally
```bash
pip install -e .
```

### 6. Test the Component
```bash
streamlit run example.py
```

## Publishing to PyPI

### 1. Install Twine (if not already installed)
```bash
pip install twine
```

### 2. Upload to PyPI
```bash
twine upload dist/*
```

## Quick Build Script

You can create a shell script `build.sh`:
```bash
#!/bin/bash
cd frontend
npm run build
cd ..
cp -r frontend/build streamlit_carousel_uui/frontend/
python setup.py sdist bdist_wheel
echo "Build complete! Package ready in dist/"
```

Make it executable:
```bash
chmod +x build.sh
```

## Troubleshooting

### Frontend Build Issues
- Make sure Node.js >= 14 is installed
- Delete `node_modules` and `package-lock.json`, then run `npm install` again
- Clear npm cache: `npm cache clean --force`

### Python Package Issues
- Delete `dist/`, `build/`, and `*.egg-info` directories
- Reinstall: `pip uninstall streamlit-carousel-uui` then `pip install -e .`

### Streamlit Component Not Loading
- Ensure `_RELEASE = True` in `__init__.py`
- Verify build folder exists in `streamlit_carousel_uui/frontend/`
- Check browser console for errors
