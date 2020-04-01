from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        response = request.form
        fever = int(response['fever'])
        age = int(response['age'])
        pain = int(response['pain'])
        runnyNose = int(response['runnyNose'])
        diffBreath = int(response['diffBreath'])
        # Code for inference
        input_features = [fever, pain, age, runnyNose, diffBreath]
        infectionProbability = clf.predict_proba([input_features])[0][1]
        print(infectionProbability)
        return render_template('show.html', inf=round(infectionProbability*100))
    return render_template('index.html')
    # return 'Hello, World!' + str(infectionProbability)


if __name__ == '__main__':
    app.run(debug=True)
