var a=123;
var rev =0;
var rem=0;
var num=0;

var rnum=reverse(a);
console.log(rnum);

function reverse(num)
{
    while(num>0)
    {
        rem=num%10;
        rev=rev*10+rem;
        num=parseInt(num/10);
    }
    return rev;
}
