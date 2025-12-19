import streamlit as st
from streamlit_carousel_uui import uui_carousel

st.set_page_config(page_title="Carousel UUI Demo", layout="wide")

st.title("🎠 Untitled UI Carousel Component")
st.markdown("A beautiful carousel component for Streamlit, based on Untitled UI design.")

st.divider()

# Example 1: Medium Carousel
st.header("Medium Carousel (variant='md')")
st.markdown("Default size with medium buttons and indicators.")

slides_md = [
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

uui_carousel(items=slides_md, variant="md", key="carousel_md")

st.divider()

# Example 2: Large Carousel
st.header("Large Carousel (variant='lg')")
st.markdown("Larger buttons and indicators for better visibility.")

slides_lg = [
    {
        "image": "https://www.untitledui.com/application/plants.webp",
        "title": "Beautiful Plants",
        "description": "Bringing nature indoors."
    },
    {
        "image": "https://images.unsplash.com/photo-1484506097116-1bcba4fa7568?q=80&w=2970",
        "title": "Urban Landscape",
        "description": "Modern architecture meets design."
    },
    {
        "image": "https://images.unsplash.com/photo-1471899236350-e3016bf1e69e?q=80&w=2971",
        "title": "Countryside",
        "description": "Peaceful rural scenery."
    },
]

uui_carousel(items=slides_lg, variant="lg", key="carousel_lg")

st.divider()

# Example 3: Without titles and descriptions
st.header("Images Only")
st.markdown("Carousel with just images, no text overlay.")

slides_images_only = [
    {"image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e"},
    {"image": "https://images.unsplash.com/photo-1511593358241-7eea1f3c84e5"},
    {"image": "https://images.unsplash.com/photo-1433086966358-54859d0ed716"},
]

uui_carousel(items=slides_images_only, key="carousel_no_text")

st.divider()

# Show code
st.header("Usage Example")
st.markdown("Here's how to use the carousel in your Streamlit app:")

code = """
import streamlit as st
from streamlit_carousel_uui import uui_carousel

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
]

# Display the carousel
uui_carousel(items=slides, variant="md")
"""

st.code(code, language="python")

# Info section
st.divider()
st.info("""
**Features:**
- 🎨 Beautiful Untitled UI design
- 🖼️ Smooth image transitions
- 🎯 Navigation arrows and indicator dots
- 📱 Responsive design
- ⚡ Built with Embla Carousel and React
""")
