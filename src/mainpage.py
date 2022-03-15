'''!

@file                mainpage.py
@brief               Brief doc for mainpage.py
@details             Detailed doc for mainpage.py 


@mainpage

@scetion sec_1  SOFTWARE OVERVIEW
                Talk about the drivers used
                ## motor driver
                ## encoder driver
                ## g-code file
                ## limit switch
                ## controller
                ## task_share and cotask
                
@section sec_2  TASK STRUCTURE
                This section will cover the tasks that we plan on utilizing for
                our 2.5 axis machine. The main taks that we will need include 
                a G-Code task thatconverts G-code into usable coordinates, a
                radial motor task, a transverse motor task, and a syringe motor 
                task. The task diagram below shows how we plan on implimenting
                these tasks into our design through the use of share 
                objects. each task will be discussed more in depth in the following 
                sections.
                
                ## Include picture of task diagram
                
@subsection 2s1
                ##RADIAL LIMIT SWITCH TASK
                The radial limit switch task continuouslly checks to see if the 
                limit switch for the radial motor has been actuated. This is 
                accomplished through the use of a shared flag variable. When the
                task is initialized the value of this shared variable is set to 
                zero. When the limit switch is finally actuated, the value of 
                the shared variable is changed to one, this is then used to start
                the plotting portion for the radial motor task.
                
@subsection 2s2
                ##TRANSVERSE LIMIT SWITCH TASK
                The transverse limit switch task continuouslly checks to see if the 
                limit switch for the transverse motor has been actuated. This is 
                accomplished through the use of a shared flag variable. When the
                task is initialized the value of this shared variable is set to 
                zero. When the limit switch is finally actuated, the value of 
                the shared variable is changed to one, this is then used to start
                the plotting portion for the transverse motor task.
@subsection 2s3
                ##EXTRUSION LIMIT SWITCH TASK
                The extrusion limit switch task continuously checks to see if the 
                limit switch for the extrusion motor task has benn actuated.
                
@subsection 2s4 
                ##RADIAL MOTOR TASK
                The radial motor task will be responsible for the radial motion
                of our nozzle. In order to accomplish this the radial motion will
                first locate itself using the limit switch located on its path.
                When the task first runs the radial motor will move the arm 
                slightly away from, and then towards the limit switch until it
                makes contact with it. Once the arm makes contact with the limit
                switch, the position of the encoder is updated to correspond
                with the the position of the limit switch. It will also wait 
                for the transverese motor to make contact with its limit switch 
                before proceeding. Once both the radial and transverse limit 
                switches have been actauted, the radial task will begin to make  
                its way through a set of coordinates in a list moving the motor 
                to the specified list index. The radial task willnot move onto 
                the next index until both the radial and transverse coordinates 
                of the same index have both been reached. A constant duty cycle
                is appied to the motor as it goes through the list, and it
                utilizes PI positional control to make sure it gets as close to
                the specified coordinates as it can.
                
                ## FSM?
                
@subsection 2s5
                ##TRANSVERSE MOTOR TASK
                The transverse motor task will be responsible for the transverse
                motion of our nozzle. Its functionality is very similar to that
                of the radial motor task; however, since this task  The task begins by first locating 
                itself using the limit switch located on its path by mocing the
                nozzle toward the limit switch located at the end of the radial arm
                until it makes contact. Once it makes contact the position of the 
                transverse encoder is updated to match the position of the limit switch.
                It will also wait for the radial motor to make contact with its 
                limit switch until before procedding.Once both the radial and 
                transverse limit  switches have been actauted, the transverse task 
                will begin to make its way through a set of coordinates in a list,
                moving the motor to the specified list index. The transverse task 
                will not move onto the next index until both the radial and 
                transverse coordinates of the same index have both been reached. 
                A constant duty cycle is appied to the motor as it goes through
                the list, and it utilizes PI control to make sure t gets as close
                to the specified coordinates as it can. Also, since this task tries to
                measure linear distance using angular readings, the encoder values 
                must be converted to linear.
                

                ## FSM?
                
@subsection 2s6
                ##EXTRUSION MOTOR TASK
                The syringe motor task will be responsible for the dispersion
                of the pancake mixture.

'''

