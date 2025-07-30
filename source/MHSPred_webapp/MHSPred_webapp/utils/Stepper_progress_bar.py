import reflex as rx

def stepper_bar(icone1: rx.Component, icone2: rx.Component,icone3: rx.Component,icone4: rx.Component, #not good
                         colour1 = "blue", colour2 = "blue",colour3 = "blue",colour4 = "blue", ) -> rx.Component:
    stepper = rx.hstack(
                #icon + step 1 
                rx.vstack(
                    rx.icon(icone1, colour=colour1),
                    rx.text("STEP 1")
                ),
                # separator
                rx.divider(),
                #icon + step 2 
                rx.vstack(
                    rx.icon(icone2, colour=colour2),
                    rx.text("STEP 2")
                ),
                # separator
                rx.divider(),
                #icon + step  
                rx.vstack(
                    rx.icon(icone3, colour=colour3),
                    rx.text("STEP 3")
                ),
                # separator
                rx.divider(),
                #icon + step 2 
                rx.vstack(
                    rx.icon(icone4, colour=colour4),
                    rx.text("STEP 4")
                ),
                # separator
                rx.divider(),
    )
    return stepper

def step(icon: str, label: str, color: str) -> rx.Component:
    return rx.vstack(
        rx.icon(tag=icon, size=30, color=color),
        rx.text(label, font_size="12px"),
        align="center",
    )

def line(color: str) -> rx.Component:
    return rx.box(
        height="3px",
        width="80px",
        bg=color,
        border_radius="md",
    )

def stepper_progress_bar(
    icon1: str, color1: str, line1: str,
    icon2: str, color2: str, line2: str,
    icon3: str, color3: str, line3: str,
    icon4: str, color4: str,
) -> rx.Component:
    return rx.hstack(
        step(icon1, "STEP 1", color1),
        line(line1),
        step(icon2, "STEP 2", color2),
        line(line2),
        step(icon3, "STEP 3", color3),
        line(line3),
        step(icon4, "STEP 4", color4),
        spacing="4",
        align="center",
        justify="center",
    )
   
