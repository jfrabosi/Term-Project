'''!

@file                mainpage.py
@brief               Brief doc for mainpage.py
@details             Detailed doc for mainpage.py 


@mainpage

@section sec_1  SOFTWARE DESIGN
                This section will cover the tasks that we plan on utilizing for
                our 2.5 axis machine. The main taks that we will need include 
                a G-Code task thatconverts G-code into usable coordinates, a
                radial motor task, a transverse motor task, and a syringe motor 
                task. The task diagram below shows how we plan on implimenting
                these tasks into our design through the use of queue and share 
                objects. each task will be discussed more i depth in the following 
                sections.
                
                ## Include picture of task diagram
                

@subsection     G-CODE TASK
                The G-Code task will be responsible for the conversion a G-Code
                into coordinates that can be used by our machine. This will be
                accomplished by first converting the G-Code file into cartesian
                coordinates through the use of splicing and appending. These 
                will then be converted to polar coordinates using conversion
                formulas. The radial and transverese coordinates will then be 
                split into seperate quees and then sent off to the appropiaate
                motor task.
                
                ## FSM?
                
@subsection     RADIAL MOTOR TASK
                The radial motor task will be responsible for the radial motion
                of our nozzle. This task will function by taking the radial
                coordinates from the G-Code task and using these values as refernece
                point for a controller object. The output of the controller will
                then be used to apply a duty cycle to the radial motor. Since we
                will be utilizing the encoder to measure position, it will be
                important to convert the rotational motion of the encoder to a 
                linear distance that we can compare the radial coordinates against.
                Once the desired coordinate is reached, a flag variable will be sent
                out to the syringe motor task indicating it is ready for pancake
                mix to be dispersed.
                
                ## FSM?
                
@subsection     TRANSVERSE MOTOR TASK
                The transverse motor task will be responsible for the transverse
                motion of our nozzle. This task will function by taking the 
                transverse coorinates coordinates from the G-Code task and using
                these values as reference points for a controller object. The output
                of the controller object will then be used to apply a duty cycle
                toi the transverse motor. Since we will be using the encoders to 
                measure position, we need to make sure that the encoder reads
                degrees and not ticks. Once the desired coordinate is reached,
                a flag variable will be sent out to the syringe motor task
                indicating it is ready for pancake mix to be dispersed.
                
                ## FSM?
                
@subsection     SYRINGE MOTOR TASK
                The syringe motor task will be responsible for the dispersion
                of the pancake mixture. 
'''
