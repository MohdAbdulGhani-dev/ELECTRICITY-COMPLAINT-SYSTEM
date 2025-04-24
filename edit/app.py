# from flask import Flask, render_template, jsonify
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('dashboard.html')

# @app.route('/get_complaints')
# def get_complaints():
#     df = pd.read_excel('complaints.xlsx')
#     data = df.to_dict(orient='records')
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)


# # ... from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd

# app = Flask(__name__) 

# # Sample route for the dashboard
# @app.route('/')
# def dashboard():
#     # Read data from Excel file
#     df = pd.read_excel('complaints.xlsx')  # Replace with the path to your Excel file
    
#     # Render the dashboard page with complaint data
#     return render_template('dashboard.html', complaints=df.to_dict(orient='records'))

# # Route for filing a new complaint
# @app.route('/file_complaint', methods=['GET', 'POST'])
# def file_complaint():
#     if request.method == 'POST':
#         complaint_title = request.form['title']
#         complaint_description = request.form['description']
        
#         # Process the complaint and save to the Excel file (for simplicity, appending to the file)
#         new_complaint = pd.DataFrame({
#             'Title': [complaint_title],
#             'Description': [complaint_description],
#             'Status': ['Pending']
#         })
        
#         new_complaint.to_excel('complaints.xlsx', index=False, mode='a', header=False)
#         return redirect(url_for('dashboard'))

#     return render_template('file_complaint.html')

# # Route for tracking complaint status
# @app.route('/track_status/<int:complaint_id>', methods=['GET', 'POST'])
# def track_status(complaint_id):
#     df = pd.read_excel('complaints.xlsx')
#     complaint = df.iloc[complaint_id]  # Fetch complaint by index
    
#     if request.method == 'POST':
#         new_status = request.form['status']
#         df.at[complaint_id, 'Status'] = new_status
#         df.to_excel('complaints.xlsx', index=False)
#         return redirect(url_for('dashboard'))
    
#     return render_template('track_status.html', complaint=complaint)

# if __name__ == '__main__':
#     app.run(debug=True)







from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from flask import jsonify  # Import jsonify to send JSON responses

app = Flask(__name__)

EXCEL_FILE = 'complaints.xlsx'  # Define the Excel file name

# Sample route for the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html') # No need to pass complaints here initially

# Route to fetch complaint data for the history section
@app.route('/get_complaints')
def get_complaints():
    try:
        df = pd.read_excel(EXCEL_FILE)
        complaints_data = df.to_dict(orient='records')
        return jsonify(complaints_data) # Return the data as JSON
    except FileNotFoundError:
        return jsonify({'error': 'Excel file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for filing a new complaint
@app.route('/file_complaint', methods=['GET', 'POST'])
def file_complaint():
    if request.method == 'POST':
        # ... (your existing file_complaint logic) ...
        return redirect(url_for('dashboard'))
    return render_template('file_complaint.html')

# Route for tracking complaint status
@app.route('/track_status/<int:complaint_id>', methods=['GET', 'POST'])
def track_status(complaint_id):
    # ... (your existing track_status logic) ...
    return render_template('track_status.html', complaint=complaint)

if __name__ == '__main__':
    app.run(debug=True)
