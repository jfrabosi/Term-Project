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
                The task_share and cotask scripts were scrips that were shared with
                us in lecture in order to imoliment cooperative multitasking.
                The task_share file allows us to create shared variables to be used
                among our generators while the cotask file allows us to turn our 
                generators into tasks and run them simultaneously.
                
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
                before proceeding. This will all be done in the initialization
                state S0 shown in the FSM below. Once contact with the radial
                and transverse limit switches has been made, the flag variables for
                each of those motors will be changed to one, and thus the
                task will transition into the next state S1, which is locating the
                radial coordinates. In this state, the task will make its way
                through a provided list of coordinates using a PI controller for
                positional control in order to get as colse to the desired value
                as it can. A constant duty cycle will be applied to the motor
                as it moves from index to index. In case the radial motor reaches
                its desired index value before the transverse motor, it will enter 
                an idler state, S2, where it will wait for the trnasverse motor 
                to reach its index value before continuing. This state also uses
                the aforementioned flag variables to make sure that each motor has
                reached its appropriate index value.
                
                ![](Rad_MotorFSM.png)
                
@subsection 2s5
                ##TRANSVERSE MOTOR TASK
                The transverse motor task will be responsible for the transverse
                motion of our nozzle, and is very similar in functionality to the
                radial motor task. The task begins by locating itself in the 
                initialization state S0 in the same manner as the radial motor task,
                the only difference being that this task is also responsible for
                updating the flag variable for the extrusion task so that it can begin 
                its cycle. After the task has gone through the initialization state, it 
                moves onto S1, locating coordinates. In the same manner as the radial
                motor task, this tak also has its own list that it iterates through
                using positional control to get as close to the desired values as it
                possibly can. This task also contains an idler state in case it reaches its
                index value before the radial motor task. Once both tasks reach their index
                value the flag variables are updated and they move onto the next value
                in their respective lists.

                ![](Trans_MotorFSM.png)
                
@subsection 2s6
                ##EXTRUSION MOTOR TASK
                The extrusion motor task will be responsible for the actuation of
                syringe that will dispense our pancake batter onto the plotting
                surface. The task stats by first moving the motor to make sure that
                no pressure is being applied on the syringe. Once this is done, the
                task begins going through its list of actuation values. This list 
                simply contains 0's and 1's, a one indicating to extrude batter. In order
                to make sure that batter is only extruded once the radial and transverse
                motor tasks have rached their proper locations, a shared index variable
                is used. This variable is sent to the extrusion task after both the
                radial and transverse motor tasks have reached their location, and it 
                ensures that all three tasks are operating on the same index, and thus
                batter is only being extruded at the proper locations. Since the
                syringe we are using only holds 150 ml of batter, we used positional
                control to ensure that once the syringe has been supressed 150 ml,
                the motor will stop. We also used a constant feed rate for our 
                extrusion motor.

'''

