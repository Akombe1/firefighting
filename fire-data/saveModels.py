# saveModels.py

import joblib
import os

def save_model(model, filename='model.pkl', directory='models'):
    """
    Save a trained model as a .pkl file inside the specified directory.
    Creates the directory if it does not exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    path = os.path.join(directory, filename)
    joblib.dump(model, path)
    print(f"✅ Model saved successfully to {path}")


def load_model(filename='model.pkl', directory='models'):
    """
    Load a saved model from a .pkl file.
    """
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")

    model = joblib.load(path)
    print(f"📦 Model loaded from {path}")
    return model


# Example Usage:
# from trainFire import train_fire_model
# from trainCategories import train_category_model
#
# fire_model = train_fire_model('fireData.csv')
# category_model = train_category_model('fireData.csv')
#
# save_model(fire_model, 'fire_model.pkl')
# save_model(category_model, 'category_model.pkl')
#
# loaded_fire = load_model('fire_model.pkl')