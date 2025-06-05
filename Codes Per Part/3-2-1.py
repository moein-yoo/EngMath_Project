def noise(a, L, type):
    if type == "Normal":
        return np.random.normal(0, a, L)
    elif type == "Uniform":
        return np.random.uniform(-a, a, L)