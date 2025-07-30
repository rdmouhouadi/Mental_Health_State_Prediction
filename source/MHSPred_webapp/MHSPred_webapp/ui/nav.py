import reflex as rx

from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                        #src="/MHS_logo__.png",
                        src="/MHS_logo_1.png",
                        width="5em",
                        height="auto",
                        border_radius="25%",
                        ),
                        href = navigation.routes.HOME_ROUTE
                    ),
                    rx.link(
                        rx.heading(
                        "Pred", size="6", weight="bold", color_scheme= "teal"
                        ),
                        href = navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                    spacing="1",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_US_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_US_ROUTE),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
                id = 'my-navbar-hstack-desktop'
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                     rx.link(
                        rx.image(
                        #src="/MHS_logo__.png",
                        src="/MHS_logo_1.png",
                        width="5em",
                        height="auto",
                        border_radius="25%",
                        ),
                        href = navigation.routes.HOME_ROUTE
                    ),
                    rx.link(
                        rx.heading(
                        "Pred", size="6", weight="bold", color_scheme= "teal"
                        ),
                        href = navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                    spacing="1",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigation.NavState.to_home),
                        rx.menu.item("About", on_click=navigation.NavState.to_about_us),
                        rx.menu.item("Contact", on_click=navigation.NavState.to_contact),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
        id = "my-main-nav",
    )