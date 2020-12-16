import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'poutcome_success': 1.0, 'emp_var_rate':-1.8, 'month_may': 0.0, 'duration':363.0, 'month_mar': 1.0, 'contact_telephone': 0.0, 'default_unknown': 0.0, 'job_blue_collar': 0.0, 'job_retired': 0.0, 'previous':1.0, 'month_sep':0.0, 'month_oct':0.0, 'campaign':2.0, 'poutcome_nonexistent':0.0, 'month_dec':0.0})

print(r.json())