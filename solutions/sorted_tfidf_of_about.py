def sorted_tfidf_of_element(tfidf_matrix, row_number,
                            vectorizer):
    """
    Given a TF-IDF Matrix (from fit_transform on a vectorizer),
    a row number and the vectorizer, return the
    TF-IDF weights and their corresponding features in order
    from highest to lowest.

    Parameters
    -----------
        tfidf_matrix: np.ndarray
            TF-IDF matrix from a vectorizer fit_transform
        row_number: int
            number of the row in the matrix you want to
            investigate
        vectorizer: TfidfVectorizer
            TfidfVectorizer that created the matrix.

    Returns
    -------
        sorted list with tuples (feature_name (str),
                                 tfidf_score (float))
    """
    feature_names = vectorizer.get_feature_names()
    row = tfidf_matrix[row_number, :]
    row_as_array = row.toarray().flatten()
    feature_with_score = [(feature_names[index],
                           row_as_array[index]) for index in row.indices]
    return sorted(feature_with_score,
                  key=lambda x: x[1],
                  reverse=True)
