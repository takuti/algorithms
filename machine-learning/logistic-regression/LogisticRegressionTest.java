class LogisticRegression {

    // model parameters
    private final float[] w;

    // number of dimensions of input vector
    private final int n;

    // learning rate
    private final float eta;

    // number of iterations
    private final int iter;

    public LogisticRegression(int n, float eta, int iter) {
        this.n = n;
        this.w = new float[n];
        this.eta = eta;
        this.iter = iter;
    }

    public void trainSGD(final float[][] X, final int[] y) {
        for (int it = 0; it < iter; it++) {
            for (int i = 0, m = X.length; i < m; i++) {
                train(X[i], y[i]);
            }
        }
    }

    public float predict(final float[] x) {
        float wx = 0.f;
        for (int i = 0; i < n; i++) {
            wx += w[i] * x[i];
        }
        return sigmoid(wx);
    }

    private void train(final float[] x, final int label) {
        float pred = predict(x);
        for (int i = 0; i < n; i++) {
            this.w[i] = w[i] + eta * (label - pred) * x[i];
        }
    }

    private float sigmoid(final float x) {
        return 1.f / (1.f + (float) Math.exp(-x));
    }
}


class LogisticRegressionTest {

    public static void main(String... args) {
        LogisticRegression lr = new LogisticRegression(5, 0.01f, 10);

        float[][] X = new float[][] {
                { 0.1f, 1.2f, 10.0f,  2.2f,  -1.0f},
                { 0.0f, 0.0f,  1.2f, -5.2f, 100.0f},
                { 7.3f, 3.1f,  4.7f, -2.1f,   0.2f},
                {-1.2f, 0.9f,  2.7f,  1.2f,   4.4f}
        };
        int[] y = new int[] {0, 1, 1, 0};

        lr.trainSGD(X, y);

        System.out.println(lr.predict(X[0])); // ~ 0
        System.out.println(lr.predict(X[1])); // ~ 1
    }
}
