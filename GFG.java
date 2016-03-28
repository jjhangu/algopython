package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class GFG {
	public static void main (String[] args) throws NumberFormatException, IOException {
		/**
		 * 테스트 데이터
		 *  1
			6
			1 3 0 5 8 5
			2 4 6 7 9 9
		 */
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int testCase = Integer.parseInt(reader.readLine().toString());
		for (int i = 0; i < testCase; i++) {
			int activityNum = Integer.parseInt(reader.readLine());
			String start =reader.readLine();
			String end =reader.readLine();
			
			String[] startstr= start.split(" ");
			String[] endstr= end.split(" ");
			
			int[] startint= new int[activityNum];
			int[] endint= new int[activityNum];
			
			System.out.println(Arrays.toString(startstr));
			System.out.println(Arrays.toString(endstr));
			
			for (int j = 0; j < startstr.length; j++) {
				startint[j] = Integer.parseInt(startstr[j]);
				endint[j] = Integer.parseInt(endstr[j]);
			}
			
			
			// 알고리즘 시작
			
			int startNum = 0;
			boolean found = true;
			ArrayList<Integer> list= new ArrayList<Integer>();
			
			while(found){
				found = false;
				// find mininum end Num ;
				int min = Integer.MAX_VALUE;
				int minposition = 0;
				
				for (int j = 0; j < endint.length; j++) {
					if(startint[j] > startNum){
						if(endint[j] < min){
							
							found = true;
							min = endint[j];							
							minposition= j;
						}
					}
				}
				if(found){
					list.add(minposition);
					startNum = min;
				}
			}
			
			System.out.println(list.toString());
		}
	}
}
