import pandas as pd
import pickle
import os
import sklearn  # Safe import for model deserialization

# Define expected columns
ENCODED_COLUMNS = [
    'Veteran Status', 'Chronical diseases', 'Otherchron_group',
    'Cash Assistance Situation', 'Unknown Insurance Coverage',
    'Insured_or_Not', 'Has_Public_Insurance', 'Has_Private_or_Other_Insurance',
    'Confirmed_Medicaid_Managed', 'Program Category_CRISIS/INPATIENT',
    'Program Category_OUTPATIENT', 'Region Served_NEW YORK CITY',
    'Region Served_UPSTATE', 'Age Group_CHILD', 'Age Group_UNKNOWN',
    'Sex_MALE', 'Sex_UNKNOWN', 'Religious Preference_SPIRITUAL/NON-RELIGIOUS',
    'Religious Preference_UNKNOWN', 'Cultural Group_Immigrant/Other Lang',
    'Cultural Group_Majority US', 'Cultural Group_Unknown',
    'Serious Mental Illness_UNKNOWN', 'Serious Mental Illness_YES',
    'Smokes_UNKNOWN',
    'Smokes_YES', 'Diagnosis_NO ADDITIONAL DIAGNOSIS',
    'Diagnosis_NOT MI/DEVELOPMENT/ORGANIC/SUBSTANCEADDICTIVE/DISORDER',
    'Diagnosis_UNKNOWN', 'Disorder Group_NO DISORDER', 'Disorder Group_UNKNOWN',
    'Mental disability_NO DISABILITY', 'Mental disability_UNKNOWN',
    'Impairment Group_PHYSICAL IMPAIRMENT', 'Impairment Group_UNKNOWN',
    'Users Canabis_UNKNOWN', 'Users Canabis_Use Cannabis Medical/recreational',
    'Smoking treatment_Received Smoking Medication/counseling',
    'Smoking treatment_UNKNOWN',
    'Service_drug_alcohol_opiod_SERVICE ALCOHOL DRUG USE',
    'Service_drug_alcohol_opiod_UNKNOWN', 'Other_testchronic_group_UNKNOWN',
    'Other_testchronic_group_YES, HYPERLIPIDEMIA/HIGHBLOODPRESSURE/OBESITY',
    'Heartchronic_UNKNOWN', 'Heartchronic_YES, HEART CHRONIC ILLNESS',
    'Brainchronic_UNKNOWN', 'Brainchronic_YES, BRAIN CHRONIC ILLNESS',
    'Household Composition_LIVES ALONE',
    'Household Composition_NOT APPLICABLE/UNKOWN',
    'Employment Status_NOT IN LABOR FORCE',
    'Employment Status_UNEMPLOYED/UNKNOW', 'Education Group_Low Educated',
    'Education Group_Others/Unknown'
]

# Define one-hot fields map
ONE_HOT_FIELDS = {
    'Program Category': ['Program Category_CRISIS/INPATIENT', 'Program Category_OUTPATIENT'],
    'Region Served': ['Region Served_NEW YORK CITY', 'Region Served_UPSTATE'],
    'Age Group': ['Age Group_CHILD', 'Age Group_UNKNOWN'],
    'Sex': ['Sex_MALE', 'Sex_UNKNOWN'],
    'Religious Preference': ['Religious Preference_SPIRITUAL/NON-RELIGIOUS', 'Religious Preference_UNKNOWN'],
    'Cultural group': ['Cultural Group_Immigrant/Other Lang', 'Cultural Group_Majority US', 'Cultural Group_Unknown'],
    'Serious Mental Illness': ['Serious Mental Illness_UNKNOWN', 'Serious Mental Illness_YES'],
    'Smokes': ['Smokes_UNKNOWN', 'Smokes_YES'],
    'Diagnosis': ['Diagnosis_NO ADDITIONAL DIAGNOSIS',
                  'Diagnosis_NOT MI/DEVELOPMENT/ORGANIC/SUBSTANCEADDICTIVE/DISORDER',
                  'Diagnosis_UNKNOWN'],
    'Disorder Group': ['Disorder Group_NO DISORDER', 'Disorder Group_UNKNOWN'],
    'Mental Disability': ['Mental disability_NO DISABILITY', 'Mental disability_UNKNOWN'],
    'Imparment Group': ['Impairment Group_PHYSICAL IMPAIRMENT', 'Impairment Group_UNKNOWN'],
    'Users Canabis': ['Users Canabis_UNKNOWN', 'Users Canabis_Use Cannabis Medical/recreational'],
    'Smoking treatment': ['Smoking treatment_Received Smoking Medication/counseling', 'Smoking treatment_UNKNOWN'],
    'Service_drug_alcohol_opiod': ['Service_drug_alcohol_opiod_SERVICE ALCOHOL DRUG USE', 'Service_drug_alcohol_opiod_UNKNOWN'],
    'Other_testchronic_group': ['Other_testchronic_group_UNKNOWN', 'Other_testchronic_group_YES, HYPERLIPIDEMIA/HIGHBLOODPRESSURE/OBESITY'],
    'Heartchronic': ['Heartchronic_UNKNOWN', 'Heartchronic_YES, HEART CHRONIC ILLNESS'],
    'Brainchronic': ['Brainchronic_UNKNOWN', 'Brainchronic_YES, BRAIN CHRONIC ILLNESS'],
    'Household Composition': ['Household Composition_LIVES ALONE', 'Household Composition_NOT APPLICABLE/UNKOWN'],
    'Employment Status': ['Employment Status_NOT IN LABOR FORCE', 'Employment Status_UNEMPLOYED/UNKNOW'],
    'Education Group': ['Education Group_Low Educated', 'Education Group_Others/Unknown']
}

# Binary fields
BINARY_FIELDS = [
    'Veteran Status', 'Chronical diseases', 'Otherchron_group',
    'Cash Assistance Situation',
    'Unknown Insurance Coverage', 'Insured_or_Not',
    'Has_Public_Insurance', 'Has_Private_or_Other_Insurance',
    'Confirmed_Medicaid_Managed'
]

# Path to the model (robust)
def load_model(model_name="MLP_model.pkl"):
    model_path = os.path.join(os.path.dirname(__file__), '../../../Models', model_name)
    with open(model_path, 'rb') as f:
        return pickle.load(f)

model = load_model()

def encode_input(input_dict):
    #Initialize the row with the correct feature columns (53 features, excluding "Mental Illness")
    encoded_row = pd.Series(0, index=ENCODED_COLUMNS, dtype='int')  # Ensure 53 columns (no target)

    #Handle binary fields (same as before)
    for field in BINARY_FIELDS:
        if field in input_dict:
            value = str(input_dict[field]).strip().upper()
            encoded_row[field] = 1 if value in ['YES', 'TRUE', '1'] else 0

    # Handle one-hot encoded fields (same as before)
    for field, encoded_options in ONE_HOT_FIELDS.items():
        if field in input_dict:
            input_value = str(input_dict[field]).strip().upper()
            for option in encoded_options:
                if input_value == option.split('_')[-1].strip().upper():
                    encoded_row[option] = 1
                    break

    # Ensure the correct number of features (53 features)
    #print("Encoded DataFrame Columns:", encoded_row.index.tolist())  # Ensure 53 columns
    #print("Encoded DataFrame Shape:", encoded_row.shape)  # Should be (53,)

    #Use .to_numpy() to convert the Series to a NumPy array and reshape it to (1, 53)
    return encoded_row.to_numpy().reshape(1, -1)  # Convert to NumPy array and reshape to (1, 53)



def prediction(input_dict):
    # Ensure that "Mental Illness" is not part of the input
    input_dict = {key: value for key, value in input_dict.items() if key != 'Mental Illness'}

    # Encode the input data (exclude the target column from form input)
    encoded = encode_input(input_dict)

    # Ensure the encoded DataFrame has the correct shape (1 row, 53 features)
    #print("Encoded DataFrame Shape:", encoded.shape)  # Should be (1, 53)

    # Make the prediction
    pred = model.predict(encoded)

    # Return the result as a string
    return "NO MENTAL ILLNESS" if pred == 0 else "HAVE A MENTAL ILLNESS"
