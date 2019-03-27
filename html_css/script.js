function read()
{
    var n=parseInt(document.getElementById("n1").value);
    var m=parseInt(document.getElementById("n2").value);
    var p=parseInt(document.getElementById("operate").value);
    var z=0;
    switch(p)
    {
        case 1:
                z=n+m;
                console.log(z);
                document.getElementById("result").innerHTML=z;
                break;
        case 2:
                z=n-m;
                console.log(z);
                document.getElementById("result").innerHTML=<b>+z+</b>;
                break;
        case 3:
                z=n*m;
                console.log(z);
                document.getElementById("result").innerHTML=<b>+z+</b>;
                break;
        case 4:
                 z=n/m;
                console.log(z);
                document.getElementById("result").innerHTML=<b>+z+</b>;
                break;
    }
}