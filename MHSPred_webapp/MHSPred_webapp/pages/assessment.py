import reflex as rx
from .. import navigation
from ..ui.base import base_page
from ..utils.Stepper_progress_bar import stepper_progress_bar


class AssessmentState(rx.State):
    current_step: int = 1

    @rx.event
    def next_step(self):
        if self.current_step < 5:
            self.current_step += 1
    @rx.event
    def previous_step(self):
        if self.current_step > 1:
            self.current_step -= 1


@rx.page(route=navigation.routes.ASSESSMENT_ROUTE)
def assessment_page() -> rx.Component:
    #assessment page
    
    my_child = rx.box(
                     rx.hstack(
                            #left part->Guideline Section  
                                rx.box(   
                                    rx.vstack(
                                        rx.box(rx.heading("Guidelines", size = "5", align='left')),
                                        rx.scroll_area(
                                                    rx.card(
                                                                #rx.heading("Assessment Guidelines", size = "5", align='left'),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                rx.text("Guidelines of the survey to be put here: mainly explaination" \
                                                                "of some features categories.", size = "3"),
                                                                    spacing="2",
                                                            
                                                        size="1",
                                                        variant="surface",
                                                        #background_color = "lightgray",
                                                        border_radius="2px",
                                                        width = "100%",

                                                    ),
                                            type="hover",
                                            scrollbars="vertical",
                                            style={"height": 180},
                                            width = "90%",
                                            height = "80vh"
                                                        
                                        ),
                                ),
                                width="100%"
                            ),
                                
                            #right part (title + Progress bar + Assessment form)
                            rx.card( 
                                    rx.stack(
                                        rx.heading(" Assessment-Form", size = "5", align='center'),
                                        rx.box(

                                            stepper_progress_bar(
                                                icon1="circle", color1="blue", line1="blue",
                                                icon2="circle", color2="lightgray", line2="lightgray",
                                                icon3="circle", color3= "lightgray", line3="lightgray",
                                                icon4="circle", color4= "lightgray",
                                                )
                                             
                                        ),  
                                        
                                   # rx.text("Question of the survey to be put here: mainly explaination!",
                                    #    size = "3"),
                                     #   spacing="2",
                                        
                                    #width="100%",
                                    #height="100%",
                                    align='center',
                                    direction='column',                  
                                    size="1",
                                    variant="ghost",
                                    border_radius="2px",
                                    width = "100%", 

                                    ),

                                size="1",
                                variant="ghost", 
                                border_radius ="2px",                                
                                width ="100%",
                                height="75vh",
                                padding="8px"

                            ),
                     ),
             ), 
                                      

    return base_page(my_child)