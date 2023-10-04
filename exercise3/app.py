from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')
        allowed_orgs = ["Science Club", "Music Club", "Drama Club", "Sports Club", "Debate Club"]
        
        if not name or not organization or organization not in allowed_orgs:
            return "Invalid Input!", 400
        students[name] = organization
        return redirect(url_for('list_students'))
    
    return render_template('home.html')

@app.route('/list')
def list_students():
    return render_template('list.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
