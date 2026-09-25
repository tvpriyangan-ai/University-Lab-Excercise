package lab1;

public class EvaluateExpressions {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("1.Arithmetic Operations:");
		System.out.println(7/2);
		System.out.println(11.0/2);
		System.out.println("a"+"b");
		
		System.out.println("String Operations:");
		System.out.println("yellow submarine".startsWith("yellow"));
		
		System.out.println();
		//System.out.println("Variables and types");
		//int age=10;
		//age++; 
		//age--;
		//age=30;
		
		//System.out.println("Age is:"+ age);
		

		
		
		System.out.println("Variables and types");
		int age=19;
		char grade='A';
		double gigawatts =1.21;
		boolean isBlue=true;
		String phoneNumber="555-1234";
		
		System.out.println("Age:"+age);
		System.out.println("Grade:"+grade);
		System.out.println("Gigawatts:"+ gigawatts);
		System.out.println("IsBlue:"+isBlue);
		System.out.println("Phone Number:"+ phoneNumber);
		
		
		System.out.println("Comparison operations");
		System.out.println(1+1==2);
		System.out.println(1+1!=3);
		System.out.println(1<3);
		System.out.println(1>3);
		System.out.println(3<=3);
		System.out.println(3>=1);
		
		System.out.println("Logical Operations");
		System.out.println(true&&true);
		System.out.println(true||false);
		System.out.println(!false);
		
		
		System.out.println("String OPERATIONS");
		System.out.println("HELLO"+"World!");
		System.out.println("Catch"+22);
		System.out.println("A piece of string".length());
		System.out.println("ABCDE".charAt(3));
		System.out.println("MMMM".toLowerCase());
		System.out.println("Yellow Submarine".startsWith("Yellow"));
		
		System.out.println("Type Conversions");
		System.out.println((double)5);
		System.out.println((int)5.3 );
		System.out.println((int)'a');
		System.out.println((char)120);
		System.out.println(String.valueOf(1234));
		System.out.println(Integer.parseInt("5678"));
		System.out.println(Double.parseDouble("3.14159"));
		
		
		
		
		
		
		
	}

}
