package lab2;

public class ShapesMain {
	
	public static void main(String[] args) {
		// This first code uses for Rectangle testing
		Vector v1 = new Vector(1,3);
		Vector v2 =new Vector(4,5);
		
		Rectangle rect = new Rectangle(v1,v2);
		rect.printRectangle();
		Vector p=new Vector (2,4);
		System.out.println("Contains:"+ rect.contains(p));
		
			
		// this code uses for circle testing
		Vector center =new Vector(3,3);
		Circle circle=new Circle (center,5);
		System.out.println("Diameter:"+circle.getDiameter());
		System.out.println("Area:"+circle.getArea());
		Vector point=new Vector (4,4);
		System.out.println("contains point:"+circle.contains(point));
		Rectangle box=circle.boundingBox();
		System.out.println("Bounding box:");
		box.printRectangle();
	}

}
