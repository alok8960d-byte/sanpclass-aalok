import numpy as np
from sklearn.svm import SVC
import dlib
import face_recognition_models
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_five_point_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)

        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        encodings.append(np.array(face_descriptor))

    # IMPORTANT:
    # return loop ke bahar hona chahiye
    return encodings


@st.cache_resource
def get_trained_mode():

    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:

        embedding = student.get("face_embedding")
        student_id = student.get("student_id")

        if embedding is not None and student_id is not None:
            X.append(np.array(embedding))
            y.append(student_id)

    # Koi training data nahi hai
    if len(X) == 0:
        return None

    # SVC ko train karne ke liye kam se kam
    # 2 different classes/students chahiye
    unique_students = list(set(y))

    if len(unique_students) < 2:
        return None

    clf = SVC(
        kernel="linear",
        probability=True,
        class_weight="balanced"
    )

    # Train classifier
    clf.fit(X, y)

    return {
        "clf": clf,
        "X": X,
        "y": y
    }


def train_classifier():

    st.cache_resource.clear()

    model_data = get_trained_mode()

    return model_data is not None


def predict_attendance(class_image_np):

    # Get face embeddings from classroom image
    encodings = get_face_embeddings(class_image_np)

    if encodings is None:
        encodings = []

    detected_student = {}

    # Get trained model
    model_data = get_trained_mode()

    if not model_data:
        return detected_student, [], len(encodings)

    clf = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["y"]

    # All students
    all_students = sorted(list(set(y_train)))

    if not all_students:
        return detected_student, [], len(encodings)

    # Check every detected face
    for encoding in encodings:

        # Predict student
        predict_id = clf.predict([encoding])[0]

        # Convert to int if possible
        try:
            predict_id = int(predict_id)
        except (ValueError, TypeError):
            pass

        # Check predicted ID exists in training data
        if predict_id not in y_train:
            continue

        # Get student's training embedding
        student_index = y_train.index(predict_id)

        student_embedding = X_train[student_index]

        # Calculate distance
        best_match_score = np.linalg.norm(
            student_embedding - encoding
        )

        # Similarity threshold
        resemblance_threshold = 0.6

        # Student detected
        if best_match_score <= resemblance_threshold:
            detected_student[predict_id] = True

    return detected_student, all_students, len(encodings)
