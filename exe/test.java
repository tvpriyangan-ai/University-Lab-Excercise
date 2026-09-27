public class main{
    public static void main(string[]args){
        String name="priyangan";
        int age=26;
        String field="ai";

    System.out.println(name);
    System.out.println(age);
    System.out.println(field);

    }
}


int a =10;
int b=20;

System.out.println(a+b);
System.out.println(a%b);


int age = 20;
System.out.println(age==20);


int age=28;
if (age>=27){
    System.out.println("Adult");
else{
    System.out.println("Minor");
}

}


if (age<18 || age>60){
    System.out.println("Working");


}

boolean active = true;
if (!active){
    System.out.println("Inactive");
}


import java.util.scanner;
public class main{
    public static void main (string[]args){
        scanner input =new scanner (System.in);
       
        System.out.print("ENTER YOUR NAME:");
        String name=input.nextLine();

        System.out.print("Enter your age:");
        int age=input.nextLine();

        System.out.println("Name:"+name);
        System.out.println("Age:"+age);

    }
}



import java.util.Scanner;
public class Main{
    static void checkAge(int age){
        if(age>=18){
            System.out.println("Adult");
        }
        else{
            System.out.println("Minor");
        }
    }
    public static void Main(String[]args){
        Scanner input = new Scanner (System.in);
        System.out.print("Enter your age:");
        int age= input.nextInt();
        checkAge(age);
    }
}



import {useState} from "react";

function App(){
    const [name,setName]=useState("");
    return(
        <div>
            <h1> My Name </h1>

            <input
                type="text"
                placeholder="Enter your name:"
                value={name}
                onChange={(e)=>setName(e.target.value)}
            />

            <h2>{name}</h2>
        </div>


    );

}
export default App;



import {useState} from "react";
function App(){
    const [count,setCount]=useState(0);

    return(
        <div>
            <h1>Count:{count}</h1>
            <button onClick={()=>setCount(count+1)}>
               Add
            </button>
        </div>
    );
}
export default App;





import {useState} from "react";

function App(){
    const[name, setName]=useState("");
    const[age,setAge]=useState("");
    const[field,setFiel]=useState("");

    const handleSubmit=(e)=>{
        e.preventDefault();

        if (!name.trim() || !age){
            alert("Please fill in all fields.");
            return;
        }

        console.log("Name:", name);
        console.log("Age:",age);
        console.log("Field:", field);
    };

    retun(
        <div>
            <h1> Student Form</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Name"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    />
                    <br/><br/>

                    <input
                    type="number"
                    placeholder="Age"
                    value={age}
                    onChange={(e)=>setAge(e.target.value)}
                    />
                    <br/> <br/>

                    <input
                    type="text"
                    placeholder="field"
                    value={field}
                    onChange={(e)=>setField(e.target.value)}
                    />
                    <br/> <br/>

                    <button type="submit">
                        Add Student
                    </button>

                </form>
            </div>

    );    
}




import {useState, useEffect} from "react";
function App(){
    const[students, setStudents]=useState([]);

    const fetchStudents=async()=>{
        const response =await fetch(
            "http://127.0.0.1:8000/students"
        );
        const data =await response.json();
        setStudents(data);

    };
    useEffect(()=>{
        fetchStudents();

    },[]);

    return(
        <div>
            <h1> Student List</h1>

            {students.map((student)=>(
                <div key={student.id}>
                <h3>{student.name}>/h3>
                <p>Age:{student.age}
                <p>Field:{student.field}</p>
                <hr/>
            </div>
            ))}
        </div>
    );
}

export default Add;



