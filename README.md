# ISS-Assignment-4-Representation of Integers and their Arithmetic
-------

This a project in which we re-wrote the Representation of Integers and their arithmetic experiment from Vlabs using Flask and python fullstack.

## Getting Started
-----
```
git clone the repository
run front_end.py using python3
open localhost:5000 on your webrowser and the website should run

```
### Prerequisites
------
```
python3
Flask
Flask-SQLAlchemy
```

## Built With
-------
* [Flask](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Python](https://www.python.org) - To bring the project together
* HTML,CSS and JS - For all the web development aspects

## Theory
-------
#### ALL ABOUT INTEGER REPRESENTATION.


Computers operate on binary values (as a result of being built from
transistors).


there are different binary representations for integers
possible qualifications:
  1. positive numbers only
  2. positive and negative numbers
  3. ease of human readability
  4. speed of computer operations

there are 4 commonly known (1 not common) integer reprentations.
All have been used at various times for various reasons.
   1. unsigned
   2. sign magnitude
   3. one's complement
   4. two's complement
   5. biased (not commonly known)

virtually all modern computers operate based on 2's complement
 representation.  why?
   1. hardware is faster
   2. hardware is simpler (which makes it faster)


#### UNSIGNED
the standard binary encoding already given
only positive values
range:   0 to 2**n - 1, for n bits

example:   4 bits, values 0 to 15
	   n=4, 2**4 -1 is 15

	   binary decimal hex     binary decimal hex
	   0000      0     0       1000    8      8
	   0001      1     1       1001    9      9
	   0010      2     2       1010    10     a
	   0011      3     3       1011    11     b
	   0100      4     4       1100    12     c
	   0101      5     5       1101    13     d
	   0110      6     6       1110    14     e
	   0111      7     7       1111    15     f



#### ONE's COMPLEMENT
Historically important, and we use this representation to get 2's complement integers.

Now, nobody builds machines that are based on 1's comp. integers.
In the past, early computers built by Semour Cray (while at CDC)
were based on 1's comp. integers.


positive integers use the same representation as unsigned.

     00000 is 0
     00111 is 7,  etc.

Negation (finding an additive inverse) is done by taking a bitwise
complement of the positive representation.

  COMPLEMENT. INVERT. NOT. FLIP. NEGATE.
       a logical operation done on a single bit
	    the complement of 1 is 0.
	    the complement of 0 is 1.


	-1 -->        take +1,    00001
	      complement each bit 11110

              that is -1.

	      don't add or take away any bits.



EXAMPLES:        11100         this must be a negative number.
			       to find out which, find the additive
			       inverse!
		 00011   is +3 by sight,
			 so 11100 must be -3


  things to notice:  1. any negative number will have a 1 in the MSB.
		     2. there are 2 representations for 0,
			00000 and 11111.



#### TWO's COMPLEMENT

a variation on 1's complement that does NOT have 2 representations for
0.  This makes the hardware that does arithmetic faster than for the
other representations.

  a 3 bit example:
  bit pattern:    100   101  110  111  000  001  010  011

  1's comp:       -3     -2   -1    0   0    1    2    3

  2's comp.:      -4     -3   -2   -1   0    1    2    3

  the negative values are all "slid" down by one, eliminating the
  extra zero representation.



  how to get an integer in 2's comp. representation:

    positive values are the same as for sign/mag and 1's comp.
    they will have a 0 in the MSB (but it is NOT a sign bit!)


    positive:   just write down the value as before
    negative:
	      take the positive value    00101 (+5)
	      take the 1's comp.         11010 (-5 in 1's comp)
	      add 1                     +    1
					------
					 11011 (-5 in 2's comp)

  to get the additive inverse of a 2's comp integer,
      1.  take the 1's comp.
      2.  add 1

  to add 1 without really knowing how to add:
    start at LSB, for each bit (working right to left)
      while the bit is a 1, change it to a 0.
      when a 0 is encountered, change it to a 1 and stop.
      the rest of the bits remain the same as they were.

  EXAMPLE:
       what decimal value does the two's complement 110011 represent?

       It must be a negative number, since the most significant bit
       is a 1.  Therefore, find the additive inverse:

	     110011  (2's comp.  ?)

	     001100  (after taking the 1's complement)
		+ 1
	     ------
	     001101  (2's comp.  +13)

	     Therefore, it's additive inverse (110011) must be -13.


#### BIASED REPRESENTATION

an integer representation that skews the bit patterns so as to
look just like unsigned but actually represent negative numbers.

    examples:    given 4 bits, we BIAS values by 2**3 (8)

	  TRUE VALUE to be represented      3
	  add in the bias                  +8
					 ----
	  unsigned value                   11

	  so the bit pattern of 3 in 4-bit biased-8 representation
	  will be  1011



	  going the other way, suppose we were given a
	  biased-8 representation as   0110

	  unsigned 0110  represents 6
	  subtract out the bias   - 8
				  ----
	  TRUE VALUE represented   -2


    this representation allows operations on the biased numbers
    to be the same as for unsigned integers, but actually represents
    both positive and negative values.

    choosing a bias:
      the bias chosen is most often based on the number of bits
      available for representing an integer.  To get an approx.
      equal distribution of true values above and below 0,
      the bias should be    2 ** (n-1)      or   (2**(n-1)) - 1



#### OVERFLOW
sometimes a value cannot be represented in the limited number
of bits allowed.   Examples:
    unsigned, 3 bits:    8 would require at least 4 bits (1000)
    sign mag., 4 bits:   8 would require at least 5 bits (01000)


when a value cannot be represented in the number of bits allowed,
we say that overflow has occurred.  Overflow occurs when doing
arithmetic operations.

      example:          3 bit unsigned representation

	      011 (3)
	    + 110 (6)
	    ---------
	       ?  (9)     it would require 4 bits (1001) to represent
			  the value 9 in unsigned rep.


#### REPRESENTATION OF FLOATING POINT NUMBERS

Computers represent real values in a form similar to that of
scientific notation.  There are standards which define what the
representation means so that across computers there will be consistancy.

Note that this is not the only way to represent floating point
numbers, it is just the IEEE standard way of doing it.

Here's what we do:

the representation

	 -------------------
	 | S |   E   |  F  |
	 -------------------

    S is one bit representing the sign of the number
    E is an 8 bit biased integer representing the exponent
    F is an unsigned integer

 the value represented is:

              S        e
	  (-1)  x f x 2

 where
	    e = E - bias
                   n
	    f = F/2  + 1

 for single precision numbers (the emphasis in this class)
       n = 23
       bias = 127



Now, what does all this mean?  (Everything here is for
IEEE single precision floating point representation.)
  --> S, E, F all represent fields within a representation.  Each
      is just a bunch of bits.

  --> S  is just a sign bit.  0 for positive, 1 for negative.

  --> E  is an exponent field.   The E field is a biased-127 representation.
      So, the true exponent represented is (E - bias).  The radix for
      the number is ALWAYS 2.

      Note:  Computers that did not use this representation, like those
	     built before the standard, did not always use a radix of 2.
	     Example:  some IBM machines had radix of 16.

  --> F  is the mantissa.  It is in a somewhat modified form.  There are
      23 bits available for the mantissa.  It turns out that if fl. pt.
      numbers are always stored in a normalized form, then the leading
      bit (the one on the left, or MSB) is always a 1.  So, why store
      it at all?  It gets put back into the number (giving 24 bits
      of precision for the mantissa) for any calculation, but we only have
      to store 23 bits.

      This MSB is called the HIDDEN BIT.


An example:   put the decimal number 64.2 into the IEEE single
	      precision representation.

	first step:
	  get a binary representation for 64.2
	  to do this, get binary reps. for the stuff to the left
	  and right of the decimal point separately.

	  64  is   1000000

	  .2 can be gotten using the algorithm:

	  .2 x 2 =  0.4      0 (msb)
	  .4 x 2 =  0.8      0
	  .8 x 2 =  1.6      1
	  .6 x 2 =  1.2      1

	  .2 x 2 =  0.4      0  now this whole pattern (0011) repeats.
	  .4 x 2 =  0.8      0
	  .8 x 2 =  1.6      1
	  .6 x 2 =  1.2      1


	    so a binary representation for .2  is    .001100110011. . .



	Putting the halves back together again:
	   64.2  is     1000000.0011001100110011. . .


      second step:
	normalize the binary representation. (make it look like
	scientific notation)

				  6
	1.000000 00110011. . . x 2

      third step:
	6 is the true exponent.  For the standard form, it needs to
	be in biased-127 form.

	      6
	  + 127
	  -----
	    133 (value of biased exponent)

	133 in 8 bit, unsigned representation is 1000 0101

	this is bit pattern used for E in the standard form.

      fourth step:
	the mantissa stored (F) is the stuff to the right of the radix point
	in the normal form.  We need 23 bits of it.

	  000000 00110011001100110


      put it all together (and include the correct sign bit):

	 S     E               F
	 0  10000101  00000000110011001100110

      the values are often given in hex, so here it is

	 0100 0010 1000 0000 0110 0110 0110 0110

     0x   4    2    8    0    6    6    6    6

     or

     42806666h


ADDITION
--------

##### Unsigned:
  just like the simple addition given.

  examples:

      100001           00001010 (10)
     +011101          +00001110 (14)
     -------          ---------
      111110           00011000 (24)

  ignore (throw away) carry out of the msb.
  Why?  Because computers ALWAYS work with a fixed precision.



##### Sign magnitude:

  rules:
    - add magnitudes only (do not carry into the sign bit)
    - throw away any carry out of the msb of the magnitude
      (Due, again, to the fixed precision constraints.)
    - add only integers of like sign ( + to +    or    - to -)
    - sign of result is same as sign of the addends

  examples:

    0  0101 (5)        1  1010 (-10)
    + 0  0011 (3)      + 1  0011 (-3)
    ----------------------------
    0  1000 (8)        1  1101 (-13)

----

    0  01011 (11)
    + 1  01110 (-14)
     ------------------ don't add! must do subtraction!



##### One's complement:

   by example


        00111 (7)         111110 (-1)            11110 (-1)
      + 00101 (5)       + 000010 (2)           + 11100 (-3)
      -----------       ------------           ------------
        01100 (12)      1 000000 (0) wrong!    1 11010 (-5) wrong!
    			+  1                  +  1
    		      ----------             ----------
    		      000001 (1) right!      11011 (-4) right!


   so it seems that if there is a carry out (of 1) from the msb, then
   the result will be off by 1, so add 1 again to get the correct
   result.  (Implementation in HW called an "end around carrry.")


#### Two's complement:

   Rules:
     - just add all the bits
     - throw away any carry out of the msb
     - (same as for unsigned!)

   examples


        00011 (3)         101000               111111 (-1)
      + 11100 (-4)      + 010000             + 001000 (8)
      ------------      --------             --------
        11111 (-1)        111000             1 000111 (7)


after seeing examples for all these representations, you may see
why 2's complement addition requires simpler hardware than
sign mag. or one's complement addition.


#### SUBTRACTION
  general rules:
    1 - 1 = 0
    0 - 0 = 0
    1 - 0 = 1
   10 - 1 = 1
    0 - 1 = borrow!




unsigned:

  -  it only makes sense to subtract a smaller number from a larger one

  examples


         1011 (11)   must borrow
      -  0111 (7)
      ------------
         0100 (4)



Sign magnitude:

  - if the signs are the same, then do subtraction
  - if signs are different, then change the problem to addition
  - compare magnitudes, then subtract smaller from larger
  - if the order is switched, then switch the sign too.

  - when the integers are of the opposite sign, then do
	a - b    becomes   a + (-b)
	a + b    becomes   a - (-b)


examples:

       0 00111 (7)             1 11000 (-24)
     - 0 11000 (24)          - 1 00010 (-2)
     --------------          --------------
                               1 10110 (-22)
    do 0 11000 (24)
     - 0 00111 (7)
     --------------
       1 10001 (-17)
    (switch sign since the order of the subtraction was reversed)





#### OVERFLOW DETECTION IN ADDITION

  unsigned -- when there is a carry out of the msb

	   1000 (8)
	  +1001 (9)
	  -----
	 1 0001 (1)

  sign magnitude -- when there is a carry out of the msb of the magnitude

	 1 1000 (-8)
       + 1 1001 (-9)
	  -----
	 1 0001 (-1)  (carry out of msb of magnitude)

  2's complement -- when the signs of the addends are the same, and the
		    sign of the result is different


	  0011 (3)
	+ 0110 (6)
	----------
	  1001 (-7)   (note that a correct answer would be 9, but
		       9 cannot be represented in 4 bit 2's complement)

  a detail -- you will never get overflow when adding 2 numbers of
	      opposite signs


#### OVERFLOW DETECTION IN SUBTRACTION

   unsigned -- never
   sign magnitude -- never happen when doing subtraction
   2's complement -- we never do subtraction, so use the addition rule
      on the addition operation done.




#### MULTIPLICATION of integers

     0 x 0 = 0
     0 x 1 = 0
     1 x 0 = 0
     1 x 1 = 1

     -- longhand, it looks just like decimal

     -- the result can require 2x as many bits as the larger multiplicand

     -- in 2's complement, to always get the right answer without
	thinking about the problem, sign extend both multiplicands to
	2x as many bits (as the larger).  Then take the correct number
	of result bits from the least significant portion of the result.


    2's complement example:


	     1111 1111        -1
	   x 1111 1001     x  -7
      ----------------    ------
	      11111111         7
	     00000000
	    00000000
           11111111
          11111111
         11111111
        11111111
   +   11111111
       ----------------
        1  00000000111
              --------  (correct answer underlined)


	0011 (3)               0000 0011 (3)
      x 1011 (-5)            x 1111 1011 (-5)
      ------                 -----------
	0011                    00000011
       0011                    00000011
      0000                    00000000
   + 0011                    00000011
   ---------                00000011
     0100001               00000011
  not -15 in any          00000011
   representation!     + 00000011
		      ------------------
		              1011110001

			  take the least significant 8 bits 11110001 = -15



#### DIVISION of integers
     unsigned only!

     example of 15 / 3         1111 / 011

     To do this longhand, use the same algorithm as for decimal integers.



#### LOGICAL OPERATIONS
   done bitwise

                     X =  0011
		     Y =  1010

       X  AND  Y is       0010
       X   OR  Y is       1011
       X  NOR  Y is       0100
       X  XOR  Y is       1001
		etc.


#### SHIFT OPERATIONS
  a way of moving bits around within a word

  3 types:     logical, arithmetic and rotate
	       (each type can go either left or right)

  logical left - move bits to the left, same order
	       - throw away the bit that pops off the msb
	       - introduce a 0 into the lsb


	       00110101

	       01101010 (logically left shifted by 1 bit)


  logical right - move bits to the right, same order
	       - throw away the bit that pops off the lsb
	       - introduce a 0 into the msb

	       00110101

	       00011010  (logically right shifted by 1 bit)


  arithmetic left - move bits to the left, same order
	       - throw away the bit that pops off the msb
	       - introduce a 0 into the lsb
	       - SAME AS LOGICAL LEFT SHIFT!



  arithmetic right - move bits to the right, same order
	       - throw away the bit that pops off the lsb
	       - reproduce the original msb into the new msb
	       - another way of thinking about it:  shift the
		 bits, and then do sign extension

	       00110101 ->  00011010 (arithmetically right shifted by 1 bit)

	       1100 -> 1110   (arithmetically right shifted by 1 bit)



  rotate left - move bits to the left, same order
	      - put the bit that pops off the msb into the lsb,
		so no bits are thrown away or lost.

	       00110101 -> 01101010 (rotated left by 1 place)       
	       1100 -> 1001 (rotated left by 1 place)


  rotate right - move bits to the right, same order
	      - put the bit that pops off the lsb into the msb,
		so no bits are thrown away or lost.

	       00110101 -> 10011010 (rotated right by 1 place)        
	       1100 ->  0110 (rotated right by 1 place)


## Authors

* **Kanish Anand** - [KanishAnand](https://github.com/https://github.com/KanishAnand)
* **Shourja Mukherjee** -  [ShourjaMukherjee](https://github.com/ShourjaMukherjee)

## Acknowledgments

Our Teaching Assistant **Anubhab Sen** who helped us at every step of this project.
