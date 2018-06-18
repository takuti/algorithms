import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.LinkedHashSet;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map.Entry;

class TfIdf {
    private static Map<String, Double> computeTf(List<String> doc) {
        Map<String, Double> tf = new HashMap<>();
        for (String word : doc) {
            if (!tf.containsKey(word)) {
                tf.put(word, 0.d);
            }
            tf.put(word, tf.get(word) + 1);
        }
        int n = doc.size();
        for (Entry<String, Double> e : tf.entrySet()) {
            String word = e.getKey();
            tf.put(word, e.getValue() / (double) n);
        }
        return tf;
    }

    private static Map<String, Double> computeIdf(Map<Integer, List<String>> docs) {
        Map<String, Double> idf = new HashMap<>();
        for (List<String> doc : docs.values()) {
            for (String word : new LinkedHashSet<>(doc)) {
                if (!idf.containsKey(word)) {
                    idf.put(word, 0.d);
                }
                idf.put(word, idf.get(word) + 1);
            }
        }
        int n = docs.size();
        for (Entry<String, Double> e : idf.entrySet()) {
            String word = e.getKey();
            idf.put(word, Math.log10((double) n / e.getValue()) + 1);
        }
        return idf;
    }

    private static Map<Integer, Map<String, Double>> computeTfIdf(Map<Integer, List<String>> docs) {
        Map<String, Double> idf = computeIdf(docs);

        Map<Integer, Map<String, Double>> res = new HashMap<>();

        for (Entry<Integer, List<String>> e : docs.entrySet()) {
            Map<String, Double> tfidf = new HashMap<>();
            Map<String, Double> tf = computeTf(e.getValue());
            for (Entry<String, Double> wordTf : tf.entrySet()) {
                String word = wordTf.getKey();
                tfidf.put(word, wordTf.getValue() * idf.get(word));
            }
            res.put(e.getKey(), tfidf);
        }

        return res;
    }

    public static void main(String[] args) {
        Map<Integer, List<String>> docs = new HashMap<>();
        docs.put(1, Arrays.asList("りんご", "レモン", "レモン"));
        docs.put(2, Arrays.asList("りんご", "みかん"));

        Map<Integer, Map<String, Double>> res = computeTfIdf(docs);
        for (Entry<Integer, Map<String, Double>> e : res.entrySet()) {
            System.out.println(e.getKey());
            System.out.println("===");
            for (Entry<String, Double> tfidf : e.getValue().entrySet()) {
                System.out.println(tfidf.getKey() + " " + tfidf.getValue());
            }
            System.out.println();
        }
    }
}
