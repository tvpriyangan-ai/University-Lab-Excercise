package lab2;

public class Circle {

	
	Vector center;
	double radius;
	
	Circle (Vector center, double radius){
		this.center=center;
		this.radius=radius;
	}
	
	double getDiameter() {
		return 2*radius;
	}
	
	double  getArea() {
		return Math.PI*(radius*radius);

	}
	boolean contains(Vector point) {
		Vector offset=point.subtract(center);
		return offset.length()<=radius;
		
	}
	Rectangle boundingBox() {
		double cx=center.x;
		double cy=center.y;
		
		Vector p1=new Vector (cx-radius, cy-radius);
		Vector p2=new Vector (cx+radius, cy+radius);
		return new Rectangle(p1,p2);
	}
		
		

	}


