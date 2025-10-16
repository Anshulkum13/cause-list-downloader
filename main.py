from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from scraper import fetch_cause_list
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        state = request.form.get('state')
        district = request.form.get('district')
        complex = request.form.get('complex')
        court = request.form.get('court')
        date = request.form.get('date')
        all_courts = request.form.get('allCourts') == 'on'

        # Validate inputs
        if not state or not district or not complex or not date:
            flash("Please fill in all required fields.")
            return redirect(url_for('index'))

        # Call scraper
        pdf_path = fetch_cause_list(state, district, complex, court, date, all_courts)

        if pdf_path and os.path.exists(pdf_path):
            return send_file(pdf_path, as_attachment=True)
        else:
            flash("Failed to fetch cause list. Please try again or check inputs.")
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)