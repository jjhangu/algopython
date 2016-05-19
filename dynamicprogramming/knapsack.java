package codefight;

public class knapsack {
	public static void main(String args[]) {
		int val[] = { 12, 10,  6 };
		int wt[] = { 3, 2,  1 };

		int W = 5;

		int max = knapSack(W, wt, val, wt.length);
		System.out.println(max);
	}

	public static int knapSack(int W, int wt[], int val[], int n) {
		int[][] dp = new int[n + 1][W + 1];

		for (int i = 0; i <= n; i++) {
			for (int w = 0; w <= W; w++) {
				
				if(i==0 || w==0){
					dp[i][w] =0;
				}else{
					if(wt[i-1]<=w){
						dp[i][w] = Math.max(dp[i-1][w], val[i-1] +  dp[i-1][w-wt[i-1]]); 
					}else{
						dp[i][w] =dp[i-1][w];
					}
				}
			}
		}
		
		print(dp);
		
		return dp[n][W];
	}
	
	public static void print(int[][] dp){
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[0].length; j++) {
				System.out.print(dp[i][j] +", ");
			}
			System.out.println();
		}
	}
}
