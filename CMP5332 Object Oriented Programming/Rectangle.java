package lab2;

public class Rectangle {
	Vector v1;
	Vector v2;
	
	Rectangle(Vector v1, Vector v2){
		this.v1=v1;
		this.v2=v2;
		
	}
	double getWidth () {
		return v2.getX()-v1.getX();
		
	}
	
	double getHeight () {
		return v2.getY-v1.getY;
		
	}
	
	double getArea() {
		return getWidth()*getHeight();
		
	}
	Vector getCenter() {
		return v1.add(v2).scale(0.5);
		
	}
	
	void printRectangle() {
		System.out.println("vector v1:");
		v1.printVector();
		System.out.println();
		
		System.out.println("vector v2:");
		v2.printVector();
		
	}
	boolean contains(Vector point) {
	    return v1.getX <= point.getX && point.getX <= v2.getX && v1.getY <=point.getY && point.getY<=v2.getY;
	}
	
	
			
			
			
	

	

}
