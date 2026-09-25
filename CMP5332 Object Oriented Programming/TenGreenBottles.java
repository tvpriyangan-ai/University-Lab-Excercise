package lab1;

public class TenGreenBottles {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int n=10; n>0; n--) {
			
			String word;
			if (n==1) {
				word="bottle";
			}
			else {
				word="bottles";
			
			}
			
			System.out.println(n+"green bottles,hanging onn the wall");
			System.out.println(n+"green bottles,hanging onn the wall");
			System.out.println(n+"And if one green bottle ");
			System.out.println("should accidently fall");
			System.out.println("There'll be" + (n-1) + "green bottles,");
			System.out.println("hanging onn the wall");
			System.out.println();
			
			
			
			
		}

	}

}
