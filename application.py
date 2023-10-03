from flask import Flask, request, make_response, jsonify
from src.pipeliens.prediction_pipeline import CustomData, ClassifyPipeline  # Updated import

application = Flask(__name__)

@application.route('/')
def home_page():
    return "Welcome to the Thyroid Detection App"

@application.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    data = request.form

    custom_data = CustomData(
    age=request.form.get('age'),
    sex=request.form.get('sex'),
    on_thyroxine=request.form.get('on_thyroxine'),
    query_on_thyroxine=request.form.get('query_on_thyroxine'),
    on_antithyroid_medication=request.form.get('on_antithyroid_medication'),
    sick=request.form.get('sick'),
    pregnant=request.form.get('pregnant'),
    thyroid_surgery=request.form.get('thyroid_surgery'),
    i131_treatment=request.form.get('i131_treatment'),
    query_hypothyroid=request.form.get('query_hypothyroid'),
    query_hyperthyroid=request.form.get('query_hyperthyroid'),
    lithium=request.form.get('lithium'),
    goitre=request.form.get('goitre'),
    tumor=request.form.get('tumor'),
    hypopituitary=request.form.get('hypopituitary'),
    psych=request.form.get('psych'),
    TSH_measured=request.form.get('TSH_measured'),
    TSH=request.form.get('TSH'),
    T3_measured=request.form.get('T3_measured'),
    T3=request.form.get('T3'),
    TT4_measured=request.form.get('TT4_measured'),
    TT4=request.form.get('TT4'),
    T4U_measured=request.form.get('T4U_measured'),
    T4U=request.form.get('T4U'),
    FTI_measured=request.form.get('FTI_measured'),
    FTI=request.form.get('FTI'),
    TBG_measured=request.form.get('TBG_measured'),
    TBG=request.form.get('TBG'),
    referral_source=request.form.get('referral_source')
)


    final_new_data = custom_data.get_data_as_dataframe()
    classify_pipeline = ClassifyPipeline()
    pred = classify_pipeline.classify(final_new_data)

    results = pred[0]  # Assuming pred is an array of class predictions

    response = make_response(f"Predicted Result: {results}")
    return response

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
