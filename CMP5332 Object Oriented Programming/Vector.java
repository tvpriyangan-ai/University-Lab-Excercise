package lab2;

public class Vector {
	//field
	double x;
	double y;
	//constructor
	Vector (double x, double y){
		this.x=x;
		this.y=y;
					
	}
	//methods
	double getX() {
		return x;
	}
	
	void setX(double newX) {
		x=newX;
		
	}
	
	Vector scale(double factor) {
		double newX=x*factor;
		double newY=y*factor;
		return new Vector (newX, newY);
	}
	
	Vector subtract (Vector other) {
	    double newX=x-other.x;
	    double newY=y-other.y;
	    return new Vector (newX, newY);
	
	}
	double length() {
		double rsquared = x*x+y*y;
		return Math.sqrt(rsquared);
	}
	Vector add(Vector vector) {
		double newX=x+vector.x;
		double newY=y+vector.y;
		return new Vector(newX, newY);
	}
	void printVector() {
		System.out.println("vector x:"+x);
		System.out.println("vector y:"+y);
		System.out.println("vector length:"+ length());
	}
	}



