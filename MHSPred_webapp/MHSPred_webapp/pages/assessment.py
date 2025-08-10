import reflex as rx
from .. import navigation
from ..ui.base import base_page
from ..utils.Stepper_progress_bar import stepper_progress_bar
from ..utils.assessment_processing import prediction


class AssessmentFormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        #print(form_data)
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
                                                                    
                                                                rx.text("What type of program category best describes the care you receive?", size="3"), #1 
                                                                rx.radio_group(
                                                                        ["OUTPATIENT", "COMMUNITY/SUPPORTIVE", "CRISIS/INPATIENT"],
                                                                        name="Program Category", #Change here to the column name
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Which part of the state are you served in?", size="3"), #2
                                                                rx.radio_group(
                                                                        ["DOWNSTATE", "NEW YORK CITY", "UPSTATE"],
                                                                        name="Region Served",
                                                                        spacing="9",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What's your age group?", size="3"), #3
                                                                rx.radio_group(
                                                                        ["ADULT", "CHILD", "UNKNOWN"],
                                                                        name="Age Group",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your sex?", size="3"), #4
                                                                rx.radio_group(
                                                                        ["MALE", "FEMALE", "UNKNOWN"],
                                                                        name="Sex", 
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your religious preference?", size="3"), # 5
                                                                rx.radio_group(
                                                                        ["UNKNOWN", "RELIGIOUS", "SPIRITUAL/NON-RELIGIOUS"],
                                                                        name="Religious Preference",
                                                                        spacing="9",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your veteran status", size="3"), #6
                                                                rx.radio_group(
                                                                        ["NON-VETERAN/UNKNOWN", "VETERAN"],
                                                                        name="Veteran Status",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Which cultural group do you identify with?", size="3"),
                                                                rx.radio_group(
                                                                        ["Hispanic", "Majority US", "Unknown", "Immigrant/Other Lang"],
                                                                        name="Cultural group",
                                                                        spacing="9",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have a serious mental illness diagnosis?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO", "YES","UNKNOWN"],
                                                                        name="Serious Mental Illness",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you smoke?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO", "YES","UNKNOWN"],
                                                                        name="Smokes",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your primary diagnosis status?", size="3"),
                                                                rx.radio_group(
                                                                        ["MENTAL ILLNESS", "NOT MI/DEVELOPMENT/ORGANIC/SUBSTANCEADDICTIVE/DISORDER", "NO ADDITIONAL DIAGNOSIS", "UNKNOWN"],
                                                                        name="Diagnosis",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have any substance use disorder?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO DISORDER", "ALCOHOL/DRUG"],
                                                                        name="Disorder Group",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have a mental disability?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO DISABILITY", "INTELECTUAL/AUTISM/DEVELOP DISABILITY", "UNKNOWN"],
                                                                        name="Mental Disability",
                                                                        spacing="9",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have any physical impairment?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO PHYSICAL IMPAIRMENT", "PHYSICAL IMPAIRMENT", "UNKNOWN"],
                                                                        name="Imparment Group",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have any chronic diseases?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO CHRONICAL MEDICAL CONDITION", "CHRONICAL MEDICAL CONDITION"],
                                                                        name="Chronical diseases",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you use cannabis?", size="3"),
                                                                rx.radio_group(
                                                                        ["No use cannabis", "Use Cannabis Medical/recreational", "UNKNOWN"],
                                                                        name="Users Canabis",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Have you received smoking treatment?", size="3"),
                                                                rx.radio_group(
                                                                        ["No Received Smoking Medication/counseling", "Received Smoking Medication/counseling", "UNKNOWN"],
                                                                        name="Smoking treatment",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you use services for drug/alcohol/opioid issues?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO SERVICE ALCOHOL DRUG USE", "SERVICE ALCOHOL DRUG USE", "UNKNOWN"],
                                                                        name="Service_drug_alcohol_opiod",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have conditions like high blood pressure, obesity, or hyperlipidemia?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO, HYPERLIPIDEMIA/HIGHBLOODPRESSURE/OBESITY", "YES, HYPERLIPIDEMIA/HIGHBLOODPRESSURE/OBESITY", "UNKNOWN"],
                                                                        name="Other_testchronic_group",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have chronic heart disease?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO, HEART CHRONIC ILLNESS", "YES, HEART CHRONIC ILLNESS", "UNKNOWN"],
                                                                        name="Heartchronic",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have chronic brain-related illness?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO, BRAIN CHRONIC ILLNESS", "YES, BRAIN CHRONIC ILLNESS", "UNKNOWN"],
                                                                        name="Brainchronic",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have other chronic illnesses?", size="3"),
                                                                rx.radio_group(
                                                                        ["NO, CHRONIC ILLNESS", "YES, CHRONIC ILLNESS"],
                                                                        name="Otherchron_group",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your household composition?", size="3"),
                                                                rx.radio_group(
                                                                        ["COHABITANTS", "LIVES ALONE", "NOT APPLICABLE/UNKOWN"],
                                                                        name="Household Composition",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your employment status?", size="3"),
                                                                rx.radio_group(
                                                                        ["EMPLOYED", "NOT IN LABOR FORCE", "UNEMPLOYED/UNKNOW"],
                                                                        name="Employment Status",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("What is your cash assistance situation?", size="3"),
                                                                rx.radio_group(
                                                                        ["No/Unknown","Receiving Cash Assistance"],
                                                                        name="Cash Assistance Situation",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Is your insurance coverage status unknown?", size="3"),
                                                                rx.radio_group(
                                                                        ["Educated", "Others/Unknown", "Low Educated"],
                                                                        name="Education Group",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Is your insurance coverage status unknown?", size="3"),
                                                                rx.radio_group(
                                                                        ["False", "True"],
                                                                        name="Unknown Insurance Coverage",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Are you insured?", size="3"),
                                                                rx.radio_group(
                                                                        ["YES", "NO"],
                                                                        name="Insured_or_not",
                                                                        spacing="6",
                                                                        required=True,
                                                                        direction="row",
                                                                ),

                                                                rx.text("Do you have public insurance?", size="3"),
                                                                rx.radio_group(
                                                                        ["YES", "NO"],
                                                                        name="Has_Public_Insurance",
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
                                            type="hover",
                                            scrollbars="both",
                                            style={"height": 180},
                                            width = "90%",
                                            height = "80vh"

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