# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:05:10 2020

@author: cbony, rsnyder
"""

from random import randint
from fractions import Fraction


#definitions
problems_per_section = 1

hyp = randint(1,30)
adj = randint(1,hyp)
random_value = randint(1,10)
hyp2 = randint(1,30)
adj2 = randint(1,hyp)
random_value2 = randint(1,10)


#set any answer you get right to 1 instead of 0.

problems = {
        '5.1a' :
            [
                    (f'Find an angle A degrees that is coterminal with an angle measuring {randint(-720,0)} degrees, where 0 <= A < 360.', 0),
                    (f'Find an angle A degrees that is coterminal with an angle measuring {randint(360,1080)} degrees, where 0 <= A < 360.', 0),
                    (f'Find an angle A degrees that is coterminal with an angle measuring {Fraction(randint(-24,0),12)} * pi, where 0 <= A < 2pi.', 0),
                    (f'Find an angle A degrees that is coterminal with an angle measuring {Fraction(randint(24,72),12)} * pi, where 0 <= A < 2pi.', 0),
                    (f'If angle A = {360*randint(-48,72)/24} degrees, what is the measurement of A in radians? Give an exact answer.', 0),
                    (f'If angle A = {Fraction(randint(24,72),12)} * pi radians, what is the measurement of A in degrees? Give an exact answer.', 0),
                    (f'Which quadrant does the angle {randint(-360,360)} degrees terminate in when drawn in the standard position?', 0),
                    (f'Which quadrant does the angle {Fraction(randint(-24,24),12)} * pi terminate in when drawn in the standard position?', 0),
                    (f'Approximate a drawing of the angle {randint(-360,360)} degrees in standard position.', 0),
                    (f'Approximate a drawing of the angle {Fraction(randint(-24,24),12)} * pi radians in standard position.', 0)
            ],
        '5.1b' :
            [
                    (f'The radius of the wheel on a car is {randint(8,23)} inches. If the wheel is revolving at {randint(200,1400)} revolutions per minute, what is the linear speed of the car in miles per hour? Round to the nearest tenth.', 0),
                    (f'Find the area of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {Fraction(randint(0,24),12)} * pi radians. Round answer to the nearest tenth.', 0),
                    (f'Find the area of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {randint(0,360)} degrees. Round answer to the nearest tenth.', 0),
                    (f'Find the length of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {Fraction(randint(0,24),12)} * pi radians. Round answer to the nearest tenth.', 0),
                    (f'Find the length of the sector of a circle of radius {randint(1,20)} units subtended by an angle of {randint(0,360)} degrees. Round answer to the nearest tenth.', 0)
            ],
        '5.2b' :
            [
                    (f'If the terminal side of an angle θ intercepts the unit circle when y is magnitude {["1/2","1/2**(1/2)","3**(1/2)/2"][randint(0,2)]} in quadrant {randint(1,4)}, what is the angle measure of θ?',0),
                    (f'The terminal side of angle θ intersects the unit circle in quadrant {randint(1,4)} at {["x","y"][randint(0,1)]} value {Fraction(randint(1,random_value),random_value)}. What are the exact values of sinθ and cosθ?',0),
                    (f'If the terminal side of angle t goes through the point ({adj}/{hyp},({(hyp**2-adj**2)}**(1/2))/{hyp}) on the unit circle, then what is {["sin(t)","cos(t)"][randint(0,1)]}?',0)
            ],
        '5.2c' :
            [
                    (f'Compute the following using a calculator: {["sin","cos"][randint(0,1)]}({randint(-360,360)}∘). Round your answer to two decimal places.',0),
                    (f'Compute the following using a calculator: {["sin","cos"][randint(0,1)]}({Fraction(randint(-24,24),12)}π). Round your answer to two decimal places.',0),
                    (f'Find the coordinates of the point on the unit circle at an angle of {randint(-360,360)}∘. Give your answer in the form (x,y) and leave any fractions in fraction form.',0),
                    (f'Find the coordinates of the point on the unit circle at an angle of {Fraction(randint(-24,24),12)}π. Give your answer in the form (x,y) and leave any fractions in fraction form.',0),
                    (f'Find the reference angle of {Fraction(randint(-24,24),12)}π. Enter the answer in {["degrees","radians"][randint(0,1)]}.',0),
                    (f'Write {["sin","cos"][randint(0,1)]}({randint(-24,24)*15}∘) in terms of a positive acute angle.',0),
                    (f'Write {["sin","cos"][randint(0,1)]}({Fraction(randint(-24,24),12)}π) in terms of a positive acute angle.',0)
            ],
        '5.3a' :
            [
                    (f'Use a reference angle to write {["sec","csc","tan","cot"][random_value % 4]}{randint(0,360)}∘ in terms of the {["secant","cosecant","tangent","cotangent"][random_value % 4]} of a positive acute angle.',0),
                    (f'The terminal side of angle θ intersects the unit circle in quadrant {randint(1,4)} at {["x","y"][randint(0,1)]} = {adj}. What is {["sec","csc","tan","cot"][randint(0,3)]}θ',0),
                    (f'Compute the following using a calculator: {["sec","csc","tan","cot"][randint(0,3)]}({Fraction(randint(-24,24),12)}π). Round your answer to two decimal places.',0)
            ],
        '5.3b' :
            [
                    (f'Given that {["sin","cos"][random_value % 2]}(θ) has magnitude {Fraction(adj,hyp)}, and θ is in quadrant {randint(1,4)}, what is {["sin","cos","sec","csc","tan","cot"][((random_value % 2)+randint(1,5)) % 6]}(θ)? Give your answer as an exact fraction with a radical, if necessary.',0),
                    (f'Given that {["sec","csc"][random_value % 2]}(θ) has magnitude {Fraction(hyp,adj)}, and θ is in quadrant {randint(1,4)}, what is {["sec","csc","tan","cot","sin","cos"][((random_value % 2)+randint(1,5)) % 6]}(θ)? Give your answer as an exact fraction with a radical, if necessary.',0),
                    (f'Given that {["tan","cot"][random_value % 2]}(θ) has magnitude {hyp**2-adj**2}**(1/2)/{adj}, and θ is in quadrant {randint(1,4)}, what is {["tan","cot","sin","cos","sec","csc"][((random_value % 2)+randint(1,5)) % 6]}(θ)? Give your answer as an exact fraction with a radical, if necessary.',0),
                    (f'Given that the terminal side of angle θ goes through the point ({randint(-20,20),randint(-20,20)}), find {["sin","cos","sec","csc","tan","cot"][randint(0,5)]}(θ)', 0)
            ],
        '5.4b' :
            [
                    (f'A carpenter needs to cut a small triangular piece of wood for part of a jewelry box. She knows the {["opposite","hypotenuse","adjacent"][random_value%3]} length is {randint(1,100)} in and that θ = {randint(1,89)}∘. What is the length of the {["opposite","hypotenuse","adjacent"][(random_value+1+randint(0,1))%3]} side to two decimal places?',0)
            ],
        '5.4c' :
            [
                    (f'Write the following function in terms of its cofunction: {["sin","cos","sec","csc","tan","cot"][randint(0,5)]}({Fraction(randint(0,24),12)}π)',0)
            ],
        '6.1a' :
            [
                    (f'Given that {["sin","cos"][random_value % 2]}(θ) = {randint(0,100)/100}, what is {["sin","cos"][random_value % 2]}(-θ)',0),
                    (f'On the graph of f(x)={["sin","cos"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for which intervals is f(x) strictly {["increasing","decreasing"][randint(0,1)]}?',0),
                    (f'On the graph of f(x)={["sin","cos"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for what value of x does f(x) achieve a {["maximum","minimum"][randint(0,1)]}?',0),
                    (f'On the graph of f(x)={["sin","cos"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for what value(s) of x does f(x) cross the x-axis?',0)
            ],
        '6.1b' :
            [
                    (f'Draw the graph f(x) = {Fraction(randint(-10,10),randint(1,10))}{["sin","cos"][random_value % 2]}({Fraction(randint(-10,10),randint(1,10))}x)',0),
                    (f'Determine the magnitude and direction of the veritcal and phase shift for f(x)={["sin","cos"][random_value % 2]}(x+{Fraction(randint(-12,12),randint(1,6))}π+{Fraction(randint(-10,10),randint(1,10))}',0),
                    (f'Draw the graph f(x) = {["sin","cos"][random_value % 2]}(x+{Fraction(randint(-12,12),randint(1,6))}π+{randint(-5,5)}',0)
            ],
        '6.2a' :
            [
                    (f'Given that {["tan","cot"][random_value % 2]}(θ) = {randint(0,100)/100}, what is {["tan","cot"][random_value % 2]}(-θ)',0),
                    (f'On the graph of f(x)={["tan","cot"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for which intervals is f(x) strictly {["increasing","decreasing"][randint(0,1)]}?',0),
                    (f'On the graph of f(x)={["tan","cot"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for what value(s) of x does f(x) cross the x-axis?',0)
            ],
        '6.2b' :
            [
                    (f'Draw the graph f(x) = {Fraction(randint(-10,10),randint(1,10))}{["tan","cot"][random_value % 2]}({Fraction(randint(-10,10),randint(1,10))}x)',0),
                    (f'Determine the magnitude and direction of the veritcal and phase shift for f(x)={["tan","cot"][random_value % 2]}(x+{Fraction(randint(-12,12),randint(1,6))}π+{Fraction(randint(-10,10),randint(1,10))}',0),
                    (f'Draw the graph f(x) = {["tan","cot"][random_value % 2]}(x+{Fraction(randint(-12,12),randint(1,6))}π+{randint(-5,5)}',0)
            ],
        '6.2c' :
            [
                    (f'Given that {["sec","csc"][random_value % 2]}(θ) = {randint(0,100)/100}, what is {["sec","csc"][random_value % 2]}(-θ)',0),
                    (f'On the graph of f(x)={["sec","csc"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for which intervals is f(x) strictly {["increasing","decreasing"][randint(0,1)]}?',0),
                    (f'On the graph of f(x)={["sec","csc"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for what value of x does f(x) achieve a {["maximum","minimum"][randint(0,1)]}?',0),
                    (f'On the graph of f(x)={["sec","csc"][random_value % 2]}(x) and the domain {["0<=x<2π","2π<=x<4π"][randint(0,1)]}, for what value(s) of x does f(x) cross the x-axis?',0)
            ],
        '6.2d' :
            [
                    (f'Draw the graph f(x) = {Fraction(randint(-10,10),randint(1,10))}{["sec","csc"][random_value % 2]}({Fraction(randint(-10,10),randint(1,10))}x)',0),
                    (f'Determine the magnitude and direction of the veritcal and phase shift for f(x)={["sec","csc"][random_value % 2]}(x+{Fraction(randint(-12,12),randint(1,6))}π+{Fraction(randint(-10,10),randint(1,10))}',0),
                    (f'Draw the graph f(x) = {["sec","csc"][random_value % 2]}(x+{Fraction(randint(-12,12),randint(1,6))}π+{randint(-5,5)}',0)
            ],
        '6.3a' :
            [
                    (f'Evaluate arc{["sin","cos"][randint(0,1)]}({["0","1","-1","1/2","-1/2","1/sqrt(2)","-1/sqrt(2)","sqrt(3)/2","-sqrt(3)/2"][randint(0,8)]})',0),
                    (f'Evaluate arc{["sec","csc"][randint(0,1)]}({["0","1","-1","2","-2","sqrt(2)","sqrt(2)","2/sqrt(3)","-2/sqrt(3)"][randint(0,8)]})',0),
                    (f'Evaluate arc{["tan","cot"][randint(0,1)]}({["0","1","-1","sqrt(3)/2","-sqrt(3)/2","2/sqrt(3)","-2/sqrt(3)"][randint(0,6)]})',0)
            ],
        '6.3b' :
            [
                    (f'Given the side length {"abc"[random_value%3]} = randint(1,25) and the angle {"AB"[random_value%2]} = {randint(1,89)}∘, find the lengths of {"abc"[(random_value+1)%3]} and {"abc"[(random_value+2)%3]} and the angle {"AB"[(random_value+1)%2]}',0),
                    (f'Given a triangle with shorter sides {adj} and {hyp**2-adj**2}**(1/2), find its angles.',0),
                    (f'Given a triangle with side {adj} and hypotenuse {hyp}, find its angles.',0)
            ],
        '6.3c' :
            [
                    (f'What is the exact value of arc{["sec","csc","tan","cot","sin","cos"][random_value % 6]}({["sec","csc","tan","cot","sin","cos"][(random_value+randint(1,5)) % 6]}(θ)), where θ = {Fraction(randint(-144,144),12)}π radians.',0),
                    (f'What is the exact value of {["sin","cos","sec","csc","tan","cot"][random_value%2]}(arc{["sin","cos","sec","csc","tan","cot"][(random_value%2+randint(1,5)) % 6]}(g)), where g has magnitude {Fraction(adj,hyp)}.',0),
                    (f'What is the exact value of {["sec","csc","tan","cot","sin","cos"][random_value%2]}(arc{["sec","csc","tan","cot","sin","cos"][(random_value%2+randint(1,5)) % 6]}(g)), where g has magnitude {Fraction(hyp,adj)}.',0),
                    (f'What is the exact value of {["tan","cot","sec","csc","sin","cos"][random_value%2]}(arc{["tan","cot","sec","csc","sin","cos"][(random_value%2+randint(1,5)) % 6]}(g)), where g has magnitude {adj}/{hyp**2-adj**2}**(1/2).',0)
            ],
        '7.1a' :
            [
                    (f'Simplify {["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({["x","-x"][randint(0,1)]}){["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({["x","-x"][randint(0,1)]}){["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({["x","-x"][randint(0,1)]})',0)
            ],
        '7.1b' :
            [
                    
                    (f'Given that {["sin","cos","sec","csc","tan","cot"][random_value%2]}(θ) has magnitude {Fraction(adj,hyp)} and θ is in quadrant {randint(1,4)}, what is {["sin","cos","sec","csc","tan","cot"][(random_value%2+randint(1,5)) % 6]}(θ)?',0),
                    (f'Given that {["sec","csc","tan","cot","sin","cos"][random_value%2]}(θ) has magnitude {Fraction(hyp,adj)} and θ is in quadrant {randint(1,4)}, what is {["sec","csc","tan","cot","sin","cos"][(random_value%2+randint(1,5)) % 6]}(θ)?',0),
                    (f'Given that {["tan","cot","sec","csc","sin","cos"][random_value%2]}(θ) has magnitude {adj}/{hyp**2-adj**2}**(1/2)and θ is in quadrant {randint(1,4)}, what is {["tan","cot","sec","csc","sin","cos"][(random_value%2+randint(1,5)) % 6]}(θ)?',0)
            ],
        '7.1c' :
            [
                    (f'Simplify cot(x)(sec(x)-1)(sec(x)+1).',0),
                    (f'Simplify tan(x)(1+cos(x))(1-cos(x)).',0),
                    (f'Simplify tan^2(x)(1-sin^2(x))',0),
                    (f'Simplify (1-cos^2(x))/sin^2(x)',0),
                    (f'Simplify (1-sin^2(x))/sin(x)',0),
                    (f'Simplify (1-cos^2(x))/cos^2(x)',0),
                    (f'Simplify (1-cos^2(x))/sin(x)',0),
                    (f'Simplify sin(x)(1-cos^2(x)).',0),
                    (f'Simplify cos(x)(tan^2(x)+1).',0),
                    (f'Simplify (tan^2(x)+1)/sec^3(x).',0)
            ],
        '7.2' :
            [
                    (f'Simplify sec(a)sec(b)sin(a-b).',0),
                    (f'Simplify cos(a-b)/(sin(a)sin(b)).',0),
                    (f'You are given that {["sin","cos"][randint(0,1)]}(a) has magnitude {Fraction(adj,hyp)} in quadrant {randint(1,4)}, and {["sin","cos"][randint(0,1)]}(b) has magnitude {Fraction(adj2,hyp2)} in quadrant {randint(1,4)}, find {["sin","cos"][randint(0,1)]}(a{"+-"[randint(0,1)]}b).',0)
            ],
        '7.3a' :
            [
                    (f'Simplify cos(x)tan(2x).',0),
                    (f'Simplify sin(2x)cos(x).',0),
                    (f'Simplify 1-2sin^2({Fraction(randint(-24,24),12)}π).',0),
                    (f'Simplify cos^2(x)-sin^2(x), where x = {Fraction(randint(-24,24),12)}π.',0)
            ],
        '7.3b' :
            [
                    (f'By using a power reducing formula, reduce {randint(1,30)}{["sin","cos"][randint(0,1)]}^{2*randint(1,2)}(x).',0),
                    (f'If sin(x)={Fraction(adj,hyp)}, and x is in quadrant {randint(1,4)}, then what is tan(x/2)?',0),
                    (f'Use the half-angle formula to find sin({randint(1,90)/2}∘)',0)
            ],
        '7.5a' :
            [
                    (f'If {randint(-20,20)}{["sin","cos"][randint(0,1)]}(x)+{randint(-20,20)}={randint(-20,20)}, where 0<=x<2π, what are the values of x? Give exact answers if possible.',0),
                    (f'If -4cos(x)+7=-2(3**(1/2))+7, where 0<=x<2π, what are the values of x? Give exact answers if possible.',0),
                    (f'If -12cos(x)=-6(3**(1/2)), where 0<=x<2π, what are the values of x? Give exact answers if possible.',0)
            ],
        '7.5b' :
            [
                    (f'Solve for x to the nearest hundredth: {randint(-10,10)}{["tan","cot","sec","csc","sin","cos"][randint(0,5)]}(x)+{randint(-10,10)}={randint(-10,10)}, 0<=x<2π',0)
            ],
        '7.5c' :
            [
                    (f'Solve for x in radians, where 0<=x<2π, {random_value}{["tan","cot","sec","csc","sin","cos"][random_value%6]}^2(x)+{random_value+random_value2}{["tan","cot","sec","csc","sin","cos"][random_value%6]}(x){random_value2}=0',0)
            ],
        '7.5d' :
            [
                    (f'Solve cos({randint(1,5)}x)=0, where 0<=x<2π.',0),
                    (f'Solve sin({randint(1,5)}x)=-(3**(1/2))/2, where 0<=x<2π.',0),
                    (f'Solve cos^3(-x)tan^2(x)+cos^3(-x)=-(2**(1/2))/2, where 0<=x<2π.',0),
                    (f'Solve tan(-x+π/9)=cot(-x+13π/6), where 0<=x<2π.',0)
            ],
        '7.6' :
            [
                    (f'Graph y={randint(-5,-1)}{["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({Fraction(1,randint(1,4))}x+π{Fraction(1,randint(1,6))})+{randint(-2,2)}',0),
                    (f'Graph y={randint(1,5)}{["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({Fraction(1,randint(1,4))}x+π{Fraction(1,randint(1,6))})+{randint(-2,2)}',0),
                    (f'Graph y={randint(-5,-1)}{["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({randint(1,4)}x+π{Fraction(1,randint(1,6))})+{randint(-2,2)}',0),
                    (f'Graph y={randint(1,5)}{["tan","cot","sec","csc","sin","cos"][randint(0,5)]}({randint(1,4)}x+π{Fraction(1,randint(1,6))})+{randint(-2,2)}',0)
            ]
        }
    
#jank code.

#check if done
not_done = False
for section in problems.keys():
    has_remaining = False
    for problem in problems[section]:
        if not problem[1]:
            has_remaining = True
        if has_remaining:
            break
    
    not_done = has_remaining
    if not_done:
        break
    
if not not_done:
    print("Congrats! You're ready!")
    exit()
    
#preset
problem_number = 0


for section in problems.keys():
    print(section)
    
    selection = problems[section]
    
    possible_problems = []
    
    #default at 1 for this purpose.
    max_right = 1
    min_right = -1
    
    #get maximum
    for item in selection:
        if item[1] > max_right:
            max_right = item[1]
        if item[1] < min_right or min_right == -1:
            min_right = item[1]
    
    #give the possibility of decent practice
#    max_right += 1
    
    #create random array of problems
    for item in selection:
        for i in range(0,max_right-item[1]):
            possible_problems.append(item[0])
    
    if possible_problems:        
        #print the problems.
        for i in range(0,problems_per_section):
            #reset variables
            hyp = randint(1,30)
            adj = randint(1,hyp)
            hyp2 = randint(1,30)
            adj2 = randint(1,hyp2)
            random_value = randint(1,10)
            random_value2 = randint(1,10)
            
            problem_choice = randint(0,len(possible_problems)-1)
            problem_number += 1
            print(str(problem_number)+'.\t'+possible_problems.pop(problem_choice))
