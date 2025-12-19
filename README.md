# Streamlit Carousel UUI

A Streamlit component that implements the beautiful Untitled UI carousel design. This component provides a sleek, modern carousel with navigation buttons and indicator dots, perfect for showcasing images in your Streamlit applications.

![preview.mp4](preview.gif)

## Features

- 🎨 Beautiful Untitled UI design
- 🖼️ Smooth image transitions
- 🎯 Navigation arrows and indicator dots
- 📱 Responsive design
- ⚡ Built with Embla Carousel and React
- 🎭 Two size variants (md and lg)
- 🔧 Easy to use and customize

## Installation

You can install the package using pip:

```bash
pip install streamlit-carousel-uui
```

Or install from source:

```bash
git clone https://github.com/janduplessis883/streamlit_carousel_uui.git
cd streamlit_carousel_uui
pip install -e .
```

## Usage

```python
import streamlit as st
from streamlit_carousel_uui import uui_carousel

st.title("Untitled UI Carousel Demo")

# Define your carousel items
slides = [
    {
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "title": "Mountain View",
        "description": "Explore the majestic peaks and valleys."
    },
    {
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
        "title": "Lake Side",
        "description": "Serene waters reflecting the sky."
    },
    {
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
        "title": "Forest Path",
        "description": "A journey through nature's canopy."
    },
]

# Display the carousel
uui_carousel(items=slides, variant="md")
```

## API Reference

### `uui_carousel(items, variant="md", key=None)`

Display an Untitled UI styled carousel component.

#### Parameters

- **items** (list of dict): List of carousel items. Each item should contain:
  - `image` (str, required): URL or path to the image
  - `title` (str, optional): Title text displayed on the slide
  - `description` (str, optional): Description text displayed on the slide

- **variant** (str, optional): Size variant of the carousel
  - `"md"` (default): Medium size buttons and indicators
  - `"lg"`: Large size buttons and indicators

- **key** (str or None, optional): An optional key that uniquely identifies this component

## Development

### Prerequisites

- Python >= 3.7
- Node.js >= 14
- npm or yarn

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/janduplessis883/streamlit_carousel_uui.git
cd streamlit_carousel_uui
```

2. Install Python dependencies:
```bash
pip install -e .
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

4. Start the development server:
```bash
npm start
```

5. In another terminal, run your Streamlit app:
```bash
streamlit run example.py
```

### Building for Production

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. Build the Python package:
```bash
python setup.py sdist bdist_wheel
```

3. Upload to PyPI:
```bash
twine upload dist/*
```

## Credits

This component is based on the carousel design from [Untitled UI](https://github.com/untitleduico/react), implemented as a Streamlit component.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/janduplessis883/streamlit_carousel_uui/issues) on GitHub.
