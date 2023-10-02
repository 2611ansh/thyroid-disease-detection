from flask import Flask, request, render_template, jsonify
from src.pipelines.classification_pipeline import CustomData, ClassifyPipeline  # Updated import
import sys

application = Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')

    else:
        data = CustomData(
            age=float(request.form.get('age')),  # Include relevant form fields
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
            T3_measured=request.form.get('T3_measured'),
            TT4_measured=request.form.get('TT4_measured'),
            T4U_measured=request.form.get('T4U_measured'),
            FTI_measured=request.form.get('FTI_measured'),
            TBG_measured=request.form.get('TBG_measured'),
            referral_source=request.form.get('referral_source'),
        )
        final_new_data = data.get_data_as_dataframe()
        classify_pipeline = ClassifyPipeline()
        pred = classify_pipeline.classify(final_new_data)  # Use the classification pipeline

        results = pred[0]  # Assuming pred is an array of class predictions

        return render_template('form.html', final_result=results)  # Update template to display classification results

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
