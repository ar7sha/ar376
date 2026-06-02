# ar376 untested hash algorithm - currently closed
**DO NOT USE IN PRODUCTION**
ar376 is a **password** hash algorithm that i make for fun and learning.
it was my first time that i make a hash algorithm.
It's output is always 376-bit , it can use salt.
## Why it's untested?
Because it's too slow.
## Who is it work?
In short, I will summarize.
Fisrt it read data from a file in 106-bits blocks.
Then 3 bits(the first,the middle,the last and the one left to the last) in the block are chosen as something for making something like 3 keys.
After that in the function liner for each bit ,some operations are performed including all 6 gates and..., i won't say all of them because its a lot , you can see at the code lines 25 to 61, it's not complex but will say some points from it here that are a little vague:
line 26 : salt will have effect on i , and i will have effect on all gates and it will have effect on all of the output.Salt is a byte.
line 34 : inheritance is a int that each block make change on it and make it bigger.
line 36 to 55 : any variable in this range will never equal zero.
line 58 and 57 : 1000000000007 and 1000000000001 are just a celing so that the process doesn't slow down.
If there was anything else that was unclear, you can ask or refer to the code again.
After liner function liner we have mk_hazy function , as you guessed from the function name this function make the linear output vague and with f1 and f2 you can set up the speed of process and it maybe will have effect on the output.Don't use 0 for f1 and f2 , that you will get error.
function mix is so clear and needs no explanation
## About it security
I know it's Deterministic, Fixed Output Length,Pre-image Resistance
Other criteria are untested.
If there was anything else that was unclear, you can ask or refer to the code again.
This project is currently closed as I'm working on a new hash, but I'm open to feedback, ideas, and questions.🙂🙃
