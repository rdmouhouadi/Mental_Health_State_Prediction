from datetime import datetime
import reflex as rx

import sqlalchemy
from sqlmodel import SQLModel, Field

from . import utils

# MHSPred Database

class ContactEntryModel(rx.Model, table=True):
    '''TABLE for the contact page'''
    first_name: str
    last_name: str | None = None
    email: str
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False
    )

class AssessmentEntryModel(rx.Model, Table = True):
    '''TABLE for the assessment responses'''

    Program_Category: str = Field(
        alias="Program Category",
        sa_column=sqlalchemy.Column("Program Category", sqlalchemy.String))

    Region_Served: str  = Field(
        alias="Region Served",
        sa_column=sqlalchemy.Column("Region Served", sqlalchemy.String)) 

    Age_Group:str  = Field(
        alias="Age Group",
        sa_column=sqlalchemy.Column("Age Group", sqlalchemy.String)) 

    Sex:str
    Religious_Preference: str  = Field(
        alias="Religious Preference",
        sa_column=sqlalchemy.Column("Religious Preference", sqlalchemy.String))  

    Veteran_Status: str  = Field(
        alias="Veterant Status",
        sa_column=sqlalchemy.Column("Veterant Status", sqlalchemy.String))
     
    Cultural_Group: str  = Field(
        alias="Cultural Group",
        sa_column=sqlalchemy.Column("Cultural Group", sqlalchemy.String))
    
    Serious_Mental_Illness: str  = Field(
        alias="Serious Mental Illness",
        sa_column=sqlalchemy.Column("Serious Mental Illness", sqlalchemy.String)) 
    
    Smokes: str 
    Diagnosis: str 

    Disorder_Group: str  = Field(
        alias="Disorder Group",
        sa_column=sqlalchemy.Column("Disorder Group", sqlalchemy.String))
    
    Mental_disability: str  = Field(
        alias="Veterant Status",
        sa_column=sqlalchemy.Column("Veterant Status", sqlalchemy.String))
    
    Impairment_Group: str  = Field(
        alias="Veterant Status",
        sa_column=sqlalchemy.Column("Veterant Status", sqlalchemy.String))
     
    Chronical_diseases: str  = Field(
        alias="Chronical diseases",
        sa_column=sqlalchemy.Column("Chronical diseases", sqlalchemy.String))
    
    Users_Canabis : str  = Field(
        alias="Users Canabis",
        sa_column=sqlalchemy.Column("Users Canabis", sqlalchemy.String))

    Smoking_treatment: str  = Field(
        alias="Smoking treatment",
        sa_column=sqlalchemy.Column("Smoking treatment", sqlalchemy.String))
    Service_drug_alcohol_opiod: str
    Other_testchronic_group: str 
    Heartchronic: str 
    Brainchronic: str
    Otherchron_group: str

    Household_Composition: str  = Field(
        alias="Household Composition",
        sa_column=sqlalchemy.Column("Household Composiiton", sqlalchemy.String))

    Employment_Status: str  = Field(
        alias="Employement Status",
        sa_column=sqlalchemy.Column("Employement Status", sqlalchemy.String))

    Cash_Assistance_Situation: str  = Field(
        alias="Cash Assistance Situation",
        sa_column=sqlalchemy.Column("Cash Assistance Situation", sqlalchemy.String))
    
    Education_Group: str  = Field(
        alias="Education Group",
        sa_column=sqlalchemy.Column("Education Group", sqlalchemy.String))
    
    Unknown_Insurance_Coverage: str  = Field(
        alias="Unknown Insurance Coverage",
        sa_column=sqlalchemy.Column("Unknown Insurance Coverage", sqlalchemy.String)) 
    
    Insured_or_Not: str 
    Has_Public_Insurance: str
    Has_Private_or_Other_Insurance: str 
    Confirmed_Medicaid_Managed: str

    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False)