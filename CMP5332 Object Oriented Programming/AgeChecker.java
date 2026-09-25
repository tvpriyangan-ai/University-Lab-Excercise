package lab1;

public class AgeChecker {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int age=11;
		if (age<0) {
			System.out.println("Invalid Age");
		}
			else if (age<=3) {
			System.out.println("Infant");
		} 
			else if (age<=5) {
			System.out.println("todler");
		}
			else if(age<12) {
			System.out.println("child");
		}
			else if (age<18) {
			System.out.println("Adult");
		}
			else if (age>=68) {
			System.out.println("Pensioner");
		}
		}
	

	}

