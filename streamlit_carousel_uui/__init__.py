import os
import streamlit.components.v1 as components

# Create a _RELEASE path pointing to the frontend build folder
_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "uui_carousel",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend", "build")
    _component_func = components.declare_component("uui_carousel", path=build_dir)

def uui_carousel(items, variant="md", key=None):
    """
    Display an Untitled UI styled carousel component in Streamlit.

    Parameters
    ----------
    items : list of dict
        List of carousel items. Each item should be a dictionary with:
        - image (str): URL or path to the image
        - title (str, optional): Title text for the slide
        - description (str, optional): Description text for the slide

    variant : str, optional
        Size variant of the carousel. Either "md" (default) or "lg".

    key : str or None, optional
        An optional key that uniquely identifies this component.

    Returns
    -------
    None

    Example
    -------
    >>> import streamlit as st
    >>> from streamlit_carousel_uui import uui_carousel
    >>>
    >>> slides = [
    >>>     {
    >>>         "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    >>>         "title": "Mountain View",
    >>>         "description": "Explore the peaks."
    >>>     },
    >>>     {
    >>>         "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    >>>         "title": "Lake Side",
    >>>         "description": "Quiet waters."
    >>>     },
    >>> ]
    >>>
    >>> uui_carousel(items=slides, variant="md")
    """
    return _component_func(items=items, variant=variant, key=key, default=None)
