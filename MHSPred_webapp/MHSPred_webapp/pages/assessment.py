import reflex as rx
from .. import navigation
from ..ui.base import base_page
from ..utils.Stepper_progress_bar import stepper_progress_bar


class AssessmentFormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data


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
                                                                rx.text("1- We assume that the user is a New York state resident", size = "3"),
                                                                rx.text("2- No question should be left unanswered", size = "3"),
                                                                rx.text("3- Kindely refer to the video down below for a tutorial", size = "3"),
                                                                rx.text("", size = "3"),
                                                                rx.text("NB: The answers given are stored anonymely in a database for futur model improvement", size = "3"),
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
                            rx.box( 
                                    rx.vstack(
                                        rx.box(rx.heading(" Assessment-Form", size = "5", align='left')),
                                
                                        rx.scroll_area(
                                                rx.card(
                                                rx.vstack(
                                                        #rx.heading("Question 1"),
                                                        rx.form.root(
                                                                rx.vstack(
                                                                    
                                                                rx.text("Question 1", size="3"),
                                                                rx.radio_group(
                                                                        ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                                                                        name="question1", #Change here to the column name
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Question 2", size="3"),
                                                                rx.radio_group(
                                                                        ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                                                                        name="question2",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Question 3", size="3"),
                                                                rx.radio_group(
                                                                        ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                                                                        name="question3",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Question 4", size="3"),
                                                                rx.radio_group(
                                                                        ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                                                                        name="question4", 
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Question 5", size="3"),
                                                                rx.radio_group(
                                                                        ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                                                                        name="question5",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.center(rx.button("Submit", type="submit")),
                                                                width="100%",
                                                                spacing="4",
                                                        
                                                            ),

                                                        on_submit=AssessmentFormState.handle_submit,
                                                        reset_on_submit=True,

                                                        #align_items="center",
                                                        width="80%",
                                                        spacing="4",
                                                        ),
                                                        width="50%",
                                                ),
                                        
                                            ),

                                        ),

                                        rx.divider(),
                                        rx.hstack(
                                                rx.heading("Result:", color_scheme="green"),
                                                rx.badge(AssessmentFormState.form_data.to_string())
                                                #rx.cond(
                                                       # AssessmentFormState.form_data != {},
                                                        #str(AssessmentFormState.form_data),
                                                        #"No responses yet."
                                                        #),

                                        ),
                                        
                                   
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
                                width ="90%",
                                height="80vh",
                                padding="8px"

                            ),
                     ),
                ),
      
                                      

    return base_page(my_child)