import os
from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS
from xgboost import XGBRegressor

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "hello upos" 

@app.route("/predapi", methods=['GET'])
def home():
    Power = request.args.get('Power')
    ChilledWater_Delta_T = request.args.get('ChilledWater_Delta_T')
    Part_Load_Ratio = request.args.get('Part_Load_Ratio')
    ChilledWater_eUSRT = request.args.get('ChilledWater_eUSRT')
    ChilledWater_tUSRT = request.args.get('ChilledWater_tUSRT')
    Temperature_Control_Eff = request.args.get('Temperature_Control_Eff')
    Energy_ePUB = request.args.get('Energy_ePUB')
    Energy_tPUB = request.args.get('Energy_tPUB')

    data = {
        'Power': Power, 
        'ChilledWater_Delta_T': ChilledWater_Delta_T, 
        'Part_Load_Ratio': Part_Load_Ratio, 
        'ChilledWater_eUSRT': ChilledWater_eUSRT, 
        'ChilledWater_tUSRT': ChilledWater_tUSRT, 
        'Temperature_Control_Eff': Temperature_Control_Eff, 
        'Energy_ePUB': Energy_ePUB, 
        'Energy_tPUB': Energy_tPUB
    }

    df = pd.DataFrame(data, index=[0])
    xgb_model = joblib.load(open('xgb_predict.pkl', 'rb'))
    preds = xgb_model.predict(df).round()
    pred_json = [{ "pred": str(preds[0]) }]
    return pred_json

if __name__ == '__main__':

   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))