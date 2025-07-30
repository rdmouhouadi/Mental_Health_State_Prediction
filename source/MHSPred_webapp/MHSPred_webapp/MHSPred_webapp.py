"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page
from . import pages

from . import navigation


class State(rx.State):
    """The app state."""
    label = "Welcome to"

    def did_click(self):
        print("did click")
        return rx.redirect(navigation.routes.ASSESSMENT_ROUTE)

def index() -> rx.Component:
    #Welcome Page (Index)
    my_child = rx.box(
                rx.flex(
                        rx.box(
                            rx.vstack(
                                rx.heading(State.label, size = "9"),
                                rx.text(
                                    "check in with your Mental Health State in minutes", size = "5",
                                ),
                                rx.link(
                                    rx.button("Start the assessment"),
                                    href=navigation.routes.ASSESSMENT_ROUTE # redirect to the asssessment page
                                ),
                                spacing = "5",
                                justify="center",
                                align="center",
                                #text_align = "center",
                                min_height="85vh",
                                id ="my-chlid", 
                            )
                        ),
                        rx.stack(
                                rx.box(
                                    rx.image(
                                    #src="/MHS_logo__.png",
                                    src="/MHS_logo_1.png",
                                    width="15em",
                                    height="auto",
                                    border_radius="100%",
                                    ),
                                ),
                                rx.box(
                                        rx.heading(
                                    "Pred", size="9", weight="bold", color_scheme= "teal"
                                    ),
                                ),
                                align_items="center",
                                spacing="1",
                        ),
                        align="center",
                        justify="center"
                    ),
            )
    return base_page(my_child)

app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(pages.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(pages.assessment_page, route=navigation.routes.ASSESSMENT_ROUTE)