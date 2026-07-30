import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_from_directory
)

from werkzeug.utils import secure_filename

import tensorflow as tf
import numpy as np

from labels import CLASS_NAMES
from utils import preprocess_image
from disease_info import DISEASE_INFO
from database import (
    init_db,
    save_prediction,
    get_history,
    delete_prediction,
    get_dashboard_stats,
    get_disease_distribution,
    get_prediction_trend,
    get_recent_predictions,
    get_most_common_disease,
    get_best_prediction
)
from pdf_generator import create_pdf
app = Flask(__name__)
latest_prediction = {}
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = tf.keras.models.load_model(
    "model/SkinDisease_EfficientNetB0.keras"
    
)




UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create folders if they don't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Load model
model = tf.keras.models.load_model(
    "model/SkinDisease_EfficientNetB0.keras"
)

# Initialize database
init_db()
model = tf.keras.models.load_model(
    "model/SkinDisease_EfficientNetB0.keras"
)

# Create database and table
init_db()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
@app.route("/predict", methods=["POST"])
def predict():
    try:
        image = request.files["image"]

        filename = secure_filename(image.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        image.save(filepath)

        processed = preprocess_image(filepath)

        prediction = model.predict(processed)

        index = np.argmax(prediction)

        confidence = round(
            float(np.max(prediction) * 100),
            2
        )

        disease = CLASS_NAMES[index]

        info = DISEASE_INFO[disease]
        global latest_prediction

        latest_prediction = {
            "disease": disease,
            "confidence": confidence,
            "info": info,
            "image": filepath
        }
        save_prediction(
        disease,
        confidence,
        filepath
        )
        return render_template(
            "index.html",
            prediction=disease,
            confidence=confidence,
            info=info,
            image_file=filepath,
            
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        return str(e), 500
@app.route("/history")
def history():

    data = get_history()

    return render_template(
        "history.html",
        history=data
    )
@app.route("/download-report")
@app.route("/delete/<int:prediction_id>")
@app.route("/delete/<int:prediction_id>")
def delete(prediction_id):
    delete_prediction(prediction_id)
    return redirect("/history")


@app.route("/download-report")
def download_report():

    if not latest_prediction:
        return "No prediction available.", 400

    filename = create_pdf(
        latest_prediction["disease"],
        latest_prediction["confidence"],
        latest_prediction["info"],
        latest_prediction["image"]
    )

    return send_from_directory(
        "reports",
        filename,
        as_attachment=True
    )
@app.route("/dashboard")
def dashboard():

    stats = get_dashboard_stats()

    distribution = get_disease_distribution()

    trend = get_prediction_trend()

    recent = get_recent_predictions()

    most_common = get_most_common_disease()

    best_prediction = get_best_prediction()

    pie_labels = [x[0] for x in distribution]
    pie_values = [x[1] for x in distribution]

    trend_labels = [x[0] for x in trend]
    trend_values = [x[1] for x in trend]

    return render_template(
        "dashboard.html",
        stats=stats,
        recent=recent,
        pie_labels=pie_labels,
        pie_values=pie_values,
        trend_labels=trend_labels,
        trend_values=trend_values,
        most_common=most_common,
        best_prediction=best_prediction
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)