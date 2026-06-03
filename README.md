# ar376 untested hash algorithm - currently closed
**DO NOT USE IN PRODUCTION**
ar376 is a **password** hash algorithm that I made for fun and learning.
It was my first hash algorithm I ever created.
Its output is always 376 bits , it can use salt.
## Why it's untested?
Because it's too slow.
## How is it work?
In short, I will summarize.
First it reads data from a file in 106 bit blocks.
Then 3 bits(the first, middle, last and second-to-last) in the block are used to derive three key-like values.
After that in the function liner for each bit ,several operations are performed including all 6 gates and..., i won't say all of them because there are many of them, you can see at the code lines 25 to 61, it's not complex but will say some points from it here that are a little vague:

line 26 : salt will affects on i , and i will have affects on all gates and it will have effect on all of the output.the salt is one byte.\n
line 34 : inheritance is an integer that each block modifies it and make it bigger.
line 36 to 55 : variables in this range are prevented from becoming zero.
line 58 and 57 : 1000000000007 and 1000000000001 are just a ceiling so that the process doesn't become too slow.
If there was anything else that was unclear, you can ask or refer to the code again.
After liner function liner we have mk_hazy function , as you guessed from the function name this function make the linear output less predictable and with f1 and f2 you can adjust the processing speed and it may also affect the output. Don't use 0 for f1 and f2 , that you will get error.
The mix function is straightforward and needs no further explanation
## Security status
I know it's deterministic and appears to provide pre-image resistance
It don't has fixed output length
Other criteria are untested.
##
If there was anything else that was unclear, you can ask or refer to the code again.
This project is currently closed as I'm working on a new hash, but I'm open to feedback, ideas, and questions.🙂🙃
