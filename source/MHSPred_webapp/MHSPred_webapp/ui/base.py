import reflex as rx

from .nav import navbar

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
        return rx.fragment(
                navbar(),
                rx.box(
                     child, 
                     padding = "1em",
                ),
                #rx.logo(),
                rx.color_mode.button(position="bottom-left", id = "my-light-mode-btn"),
                # padding='10em',
                id="my-base-container"
        )