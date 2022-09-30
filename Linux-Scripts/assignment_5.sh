#! /bin/bash
add(){
echo -e "Addition"
read numa numb
echo -e "Output is  $((numa + numb))"
}
subtract(){
echo -e "subtraction"

read numa numb
echo -e "Output is  $((numa - numb))"

}
multiply(){
echo -e "multiplication"
read numa numb
echo -e "Output is  $((numa * numb))"

}
echo -ne "
MENU
1) ADD
2)SUBTRACT
3)MULTIPLY
*) Any key to EXIT
Choose an option:  "
read  choice

#case block
case $choice in

  1)
    add
    ;;

  2) 
    subtract
    ;;

  3) 
    multiply
    ;;

  *) 
    exit
    ;;
esac
