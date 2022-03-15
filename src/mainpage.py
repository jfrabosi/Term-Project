'''!
@file                mainpage.py
@brief               Brief doc for mainpage.py
@details             Detailed doc for mainpage.py 


@mainpage

@scetion sec_1  SOFTWARE OVERVIEW
                This section will cover the various drivers used in our system
                as well as what tasks they were utilized in. The tasks themselves
                be discussed in a later section.
@subsection 1s1                
                ##MOTOR DRIVER
                The motor driver script contains class files that allow us to
                apply pwm to our dc motors. Since we are utilizing two diffrent
                motor shield we have two separte class files since each motor
                shield utilizes a diffrent amount of pins. The motor driver is
                utilized in all of outr motor tasks in order to apply a duty
                cycle.
                
@subsection 1s2
                ##ENCODER DRIVER
                The encoder driver script contains a class file that allows us
                perform various functions with the encoders on the motors. These
                functions enclude reading the position of the encoder, zeroing
                the position of the encoder and overwriting the position of 
                the encoder wit ha custom value. The encoder driver is used in all
                of our motor tasks in order to locate read out our transverse
                and radial positions.
@subsection 1s3
                ##CONTROLLER
                The controller script contains a class file that allows us to 
                perform PID control. It contains functions for setting our gain
                values and setpoints. It also contains a function to compute the 
                total error in our system. This file is used by our motor tasks
                in order to impliment positional control.
@subsection 1s4
                ##LIMIT SWITCH
                The limit switch script is a short script that contains a class
                file that allows us to check the status of our limit switches.
                It contains a function that will return the pin value when called.
                This file is used in our limit switch tasks in order to update key
                flag variables depending on whether or not the limit switches 
                are actuated.
@subsection 1s5
                ##G-CODE
                The gcode_convert script is a function file that contains a 
                function that takes a .nc file, converts it to three seperate
                lists containing cartesian coordinates, and then conversts those
                lists to cartesian coordinates. This file is used in our execution
                script in order to create the lists that will be used by our
                various motor tasks.
                
@subsection 1s6
                ##TASK_SHARE & COTASK
                
@section sec_2  TASK STRUCTURE
                This section will cover the tasks that we plan on utilizing for
                our 2.5 axis machine. The main taks that we will need include 
                a G-Code task thatconverts G-code into usable coordinates, a
                radial motor task, a transverse motor task, and a syringe motor 
                task. The task diagram below shows how we plan on implimenting
                these tasks into our design through the use of share 
                objects. each task will be discussed more in depth in the following 
                sections.
                
                ![](Task_Diagram.png)
                
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

