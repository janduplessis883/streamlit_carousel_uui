import os
import streamlit.components.v1 as components

# For development, set to True to use the React dev server
_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "uui_carousel",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("uui_carousel", path=build_dir)

def uui_carousel(items, key=None):
    """
    items: List of dicts with {'image': str, 'title': str, 'description': str}
    """
    return _component_func(items=items, key=key)

# --- Example Usage ---
if __name__ == "__main__":
    import streamlit as st
    st.title("Untitled UI Carousel in Streamlit")

    slides = [
        {"image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb", "title": "Mountain View", "description": "Explore the peaks."},
        {"image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e", "title": "Lake Side", "description": "Quiet waters."},
    ]

    selected = uui_carousel(items=slides)
