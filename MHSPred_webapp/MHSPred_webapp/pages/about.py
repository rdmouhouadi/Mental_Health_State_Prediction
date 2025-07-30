import reflex as rx
from .. import navigation
from ..ui.base import base_page

@rx.page(route=navigation.routes.ABOUT_US_ROUTE)
def about_page() -> rx.Component:
    #About page
    my_child = rx.box(
                    rx.flex(
                        rx.grid(
                                rx.container(
                                    rx.box(
                                            #ABOUT-US Section
                                        rx.section(
                                            rx.heading("About Us", size = "9"),
                                            rx.text("We are a group of 4 members that came together for our interest " \
                                            "on a mental health project. The project was completed as part of a mandatory" \
                                            " Machine Learning with Labs course at DataScienceTech Institute (DSTI).",
                                            size = "5"),
                                            spacing="2",
                                            ),
                                        width="90%",
                                        height="100%",
                                        #margin="5px",
                                        padding="8px"
                                        )
                                    
                                    ),
                                rx.box(
                                    rx.container(
                                        rx.vstack(
                                            rx.container(
                                                #TEAM Member Section
                                                rx.section(
                                                    rx.heading("Team Members", size="9"),
                                                    #rx.text("Here, will be placed our images and descriptions", size="5"),
                                                    ),
                                                rx.flex(
                                                    # first team member
                                                    rx.container(
                                                        rx.vstack(
                                                                rx.image(
                                                                    src="/Richie_2.jpg",
                                                                    width="100px",
                                                                    height="100px",
                                                                    border_radius="50px",
                                                                    border="5px solid #555",
                                                                    ),
                                                                rx.text('Richie Mouhouadi, DS'),
                                                                #rx.text('Team Leader'),
                                                                spacing = "2",
                                                                align='center',
                                                                justify='center'
                                                                )  
                                                            ),
                                                    # Second team member
                                                    rx.container( 
                                                        rx.vstack(
                                                                rx.image(
                                                                    src="/Lina_crop1.jpg",
                                                                    width="100px",
                                                                    height="100px",
                                                                    border_radius="50px",
                                                                    border="5px solid #555",
                                                                ),
                                                            rx.text('Lina Bejarano, DA'),
                                                            spacing = "2",
                                                            align='center',
                                                            justify='center'
                                                        )

                                                    ),
                                                    # third team member
                                                    rx.container( 
                                                        rx.vstack(
                                                            rx.image(
                                                                    src="/Lin_crop1.jpg",
                                                                    width="100px",
                                                                    height="100px",
                                                                    border_radius="50px",
                                                                    border="5px solid #555",
                                                                ),
                                                        rx.text('Linh Luong, DA'),
                                                        spacing = "2",
                                                        align='center',
                                                        justify='center'
                                                        )

                                                    ),
                                                    # fourth team member
                                                    rx.container( 
                                                        rx.vstack(
                                                            rx.image(
                                                                    src="/Ram_2.jpg",
                                                                    width="100px",
                                                                    height="100px",
                                                                    border_radius="50px",
                                                                    border="5px solid #555",
                                                                ),
                                                        rx.text("Arigela Surendra, DE"),
                                                        spacing = "2",
                                                        align='center',
                                                        justify='center'
                                                        )

                                                    ),
                                                ),
                                            width="100%",
                                            height="100%",
                                            #margin = "5px",
                                            padding = "8px"
                                        ),
                                        rx.container(
                                            #Teaching Staff Member Section
                                            rx.section(
                                                rx.heading("Teaching Staff", size="9"),
                                                #rx.text("Here, will be placed our images and descriptions", size="5"),
                                                ),
                                            rx.flex(
                                                # Teacher
                                                rx.container(
                                                        rx.vstack(
                                                                rx.image(
                                                                        src="/hanna_2.png",
                                                                        width="100px",
                                                                        height="100px",
                                                                        border_radius="50px",
                                                                        border="5px solid #555",
                                                                        ),
                                                                rx.text('Hanna Abi Akl, Prefessor'),
                                                                spacing = "2",
                                                                align='center',
                                                                justify='center'
                                                            )  
                                                        ),
                                                # Project Mentor
                                                rx.container( 
                                                        rx.vstack(
                                                                rx.image(
                                                                        src="/Pauline_2.png",
                                                                        width="100px",
                                                                        height="100px",
                                                                        border_radius="50px",
                                                                        border="5px solid #555",
                                                                    ),
                                                                rx.text('Pauline Salis, Project Mentor'),
                                                                #rx.text('Project Mentor'),
                                                                spacing = "2",
                                                                align='center',
                                                                justify='center'
                                                            ),
                                                        ),
                                            columns="2",
                                            spacing="3",
                                            #align="stretch",
                                            justify="start",
                                            #direction="column",
                                            wrap="nowrap",
                                            ),
                                        ),
                                columns="2"
                            ),
                        ),
                                    
                    ),
                height = "100vh",
                columns="2"
            ),
        ),
    )
    
    
    return base_page(my_child)