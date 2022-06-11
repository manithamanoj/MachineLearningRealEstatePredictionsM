import pandas as pd
from urllib import response
import joblib
import os
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy 
from flask import Flask, render_template, request,redirect
app=Flask(__name__)



zip_crime_school={'school_rating': {85003: 94.44,
  85004: 94.44,
  85006: 94.44,
  85007: 94.44,
  85008: 81.79,
  85009: 65.7,
  85012: 72.93,
  85013: 72.93,
  85014: 97.13000000000001,
  85015: 100.04000000000002,
  85016: 97.13,
  85017: 100.04,
  85018: 75.8,
  85019: 100.04,
  85020: 97.13,
  85021: 91.9,
  85022: 99.97,
  85023: 91.9,
  85028: 99.97,
  85029: 91.9,
  85031: 100.04,
  85032: 99.97,
  85033: 95.89,
  85034: 68.34,
  85035: 95.89,
  85037: 85.28,
  85040: 76.54,
  85041: 76.54,
  85042: 76.54,
  85043: 76.86,
  85051: 91.9,
  85053: 91.9,
  85250: 101.35,
  85251: 101.35,
  85254: 99.97,
  85257: 101.34999999999998,
  85258: 101.34999999999998,
  85281: 94.49,
  85282: 94.49,
  85301: 100.04,
  85302: 91.9,
  85303: 95.89,
  85304: 91.9,
  85305: 85.28,
  85306: 91.9,
  85339: 94.47,
  85345: 85.28},
 'crime_rate': {85003: 1.1,
  85004: 1.2,
  85006: 1.9,
  85007: 1.6,
  85008: 4.5,
  85009: 4.0,
  85012: 0.6,
  85013: 2.0,
  85014: 1.9,
  85015: 5.5,
  85016: 3.2,
  85017: 4.1,
  85018: 2.2,
  85019: 2.5,
  85020: 2.1,
  85021: 2.8,
  85022: 2.6,
  85023: 3.4,
  85028: 0.6,
  85029: 3.3,
  85031: 2.4,
  85032: 3.1999999999999997,
  85033: 3.0,
  85034: 1.8999999999999997,
  85035: 3.3,
  85037: 1.9,
  85040: 2.8,
  85041: 4.5,
  85042: 2.9,
  85043: 3.2,
  85051: 4.3,
  85053: 1.5,
  85250: 2.5,
  85251: 0.0,
  85254: 1.1,
  85257: 2.5,
  85258: 0.0,
  85281: 0.0,
  85282: 0.0,
  85301: 0.0,
  85302: 0.0,
  85303: 0.0,
  85304: 0.2,
  85305: 2.5,
  85306: 0.3,
  85339: 2.0,
  85345: 0.0}}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def ValuePredictor():
      if request.method=='POST':
        if request.form["SQFT"] =='':
            sqft=1715.25
        else:
            sqft=request.form["SQFT"]
            sqft=float(sqft)
        if request.form["Bedrooms"] =='':
            Bedrooms=3
        else:
            Bedrooms=request.form["Bedrooms"]
            Bedrooms=int(Bedrooms)
        if request.form["Bathrooms"] =='':
            Bathrooms=2
        else:
            Bathrooms=request.form["Bathrooms"]
            Bathrooms=float(Bathrooms)
        if request.form["Year_Built"]=='':
            Year_Built=1986
        else:
            Year_Built=int(request.form["Year_Built"])
        if request.form["zip"]=='':
            Zipcode=85015
        else:
            Zipcode=int(request.form["zip"])
        School=float(zip_crime_school['school_rating'][Zipcode])
        Crime=float(zip_crime_school['crime_rate'][Zipcode])
        x=[[Zipcode,Year_Built,Bedrooms,Bathrooms,sqft,Crime,School]]
        loaded_model = joblib.load(open('final_model.joblib','rb'))
        result = loaded_model.predict(x)
        return render_template('index.html',result=f"${round(result[0],2):,}")
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/visualization')
def visualization():
    return render_template('visualization.html')
@app.route('/data')
def data():
    return render_template('data.html')
    # engine = create_engine(os.environ.get('DATABASE_URL', ''))
    # conn = engine.connect()
    # df = pd.read_sql("SELECT * FROM combined_data", con = engine)
    # # df1 = pd.read_sql("SELECT * FROM education_data", con = engine)
    # # merged_df=df.merge(df1, how='left', on='zip')
    # # merged_df.rename(columns={'price':"House Price",'zip':"Zipcode",'status':"Status",'year_built':'Year','bedrooms':'Bedrooms','bathrooms':'Bathrooms','approx_sqft':'Approx SQFT','crimerate':'Crime Rate','elem_school_district':'Elem School District','highest_rated_school':'School Ratings'},inplace=True)
    # # merged_df.reset_index() 
    # # housing_data=merged_df[["House Price","Zipcode","Status",'Year','Bedrooms','Bathrooms','Approx SQFT','Crime Rate','Elem School District','School Ratings']]
    # return render_template('data.html',tables=[df.to_html(classes='data table')], titles=df.columns.values)

if __name__ == '__main__':
 app.run(debug=True)
 