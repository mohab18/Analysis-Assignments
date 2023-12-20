public class SeqAlignment {

    public static void main(String[] args) {
        String x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC";
        String y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC";

        double[][] scoringMatrix = {
                {1, -0.8, -0.2, -2.3, -0.6},
                {-0.8, 1, -1.1, -0.7, -1.5},
                {-0.2, -1.1, 1, -0.5, -0.9},
                {-2.3, -0.7, -0.5, 1, -1},
                {-0.6, -1.5, -0.9, -1, Double.NaN}
        };

        String[] result = Alignment(x, y, scoringMatrix);

        System.out.println("Aligned X: " + result[0]);
        System.out.println("Aligned Y: " + result[1]);
        System.out.println("Alignment Score: " + result[2]);
    }

    public static String[] Alignment(String x, String y, double[][] scoringMatrix) {
        int n = x.length();
        int m = y.length();

   
        double[][] tmp = new double[n + 1][m + 1];

     
        for (int i = 1; i <= n; i++) {
            tmp[i][0] = tmp[i - 1][0] + scoringMatrix[getIndex('-')][getIndex(x.charAt(i - 1))];
        }

        for (int j = 1; j <= m; j++) {
            tmp[0][j] = tmp[0][j - 1] + scoringMatrix[getIndex(y.charAt(j - 1))][getIndex('-')];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                double matchScore = tmp[i - 1][j - 1] + scoringMatrix[getIndex(x.charAt(i - 1))][getIndex(y.charAt(j - 1))];
                double gapXScore = tmp[i - 1][j] + scoringMatrix[getIndex('-')][getIndex(x.charAt(i - 1))];
                double gapYScore = tmp[i][j - 1] + scoringMatrix[getIndex(y.charAt(j - 1))][getIndex('-')];

                tmp[i][j] = Math.max(matchScore, Math.max(gapXScore, gapYScore));
            }
        }

     
        String newX = "";
        String newY = "";
        int i = n;
        int j = m;

        while (i > 0 || j > 0) {
            if (i > 0 && tmp[i][j] == tmp[i - 1][j] + scoringMatrix[getIndex('-')][getIndex(x.charAt(i - 1))]) {
                newX = x.charAt(i - 1) + newX;
                newY = '-' + newY;
                i--;
            } else if (j > 0 && tmp[i][j] == tmp[i][j - 1] + scoringMatrix[getIndex(y.charAt(j - 1))][getIndex('-')]) {
                newX = '-' + newX;
                newY = y.charAt(j - 1) + newY;
                j--;
            } else {
                newX = x.charAt(i - 1) + newX;
                newY = y.charAt(j - 1) + newY;
                i--;
                j--;
            }
        }



        return new String[]{newX, newY, "" + tmp[n][m]};
    }

    public static int getIndex(char x) {
        switch (x) {
            case 'A':
                return 0;
            case 'G':
                return 1;
            case 'T':
                return 2;
            case 'C':
                return 3;
            case '-':
                return 4;
            default:
                return -1;
        }
    }
}
