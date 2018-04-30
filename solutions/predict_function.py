def predict_text(model, target_names, text):
    """
    Return human-readable predicted category given text.

    Parameters:
        model        (obj) : Sklearn model for prediction
        text         (str) : text to use for prediction
        target_names (list): list of target names

    Returns:
        label (str)
    """
    return target_names[model.predict(StringIO(text))[0]]

