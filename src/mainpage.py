'''!

@file                mainpage.py
@brief               Brief doc for mainpage.py
@details             Detailed doc for mainpage.py 


@mainpage

@section sec_1  HARDWARE DESIGN
                This section describes the mechanisms, mechanical design, and
                manufacturing techniques for each component of our 2.5D plotter.
                Each subsection below describes a different component of the design,
                explaining how and why we made the decisions that we did.
                
@subsection 1s1 
                ##GENERAL IDEA
                Our interpretation of a 2.5D plotter is a pancake plotter: a mechanism
                that can convert G-Code of an image to carefully-positioned pancake
                batter deposited onto a hot griddle, ideally making a pancake in the
                shape of the chosen image.
                
                Our team plans to accomplish this using three axes of motion: one
                rotational, one transverse, and one
                also-transverse-but-it's-for-dispensing-batter. The finished mechanism
                almost resembles a windshield wiper with a nozzle that moves along the
                length of the blade, allowing us to cover a wide area with two motors.
                A third motor will dispense the batter using a lead screw for precise
                depositing. A GIF of the mechanism can be seen below.
                
                ## FULL MECH GIF
                
                It should be noted that the rotational-transverse design
                is a challenge: surely a Cartesian (X-Y) plotter would be simpler. But
                hey, we're Cal Poly MEs; we can take the challenge.
                
                A Bill of Materials (BOM) can be found at the end of this section, listing
                names, suppliers, quantities, and costs for each purchased or designed item.
                
                Additionally, all CAD files can be found in the /docs/SOLIDWORKS directory
                of this repository.
                
@subsection 1s2 
                ##GRIDDLE
                This is the most straight-forward component. In order to make pancakes,
                you need a griddle or other hot-implement. Our team chose the griddle below,
                purchased from Amazon for $27, due to its reasonable price and fast shipping
                time (did I mention this project only took four weeks?).
                
                ## GRIDDLE IMAGE
                
                There's really not much else for this one. It's a griddle.

@subsection 1s3 
                ##SUPPORT STRUCTURE
                In order to effectively position and control our motors, our design first
                needed a support structure. We designed the base of the support structure
                from aluminum extrusions due to their versatility (used for both the
                supports and the actuating rail!), low cost, and fast shipping. Our team
                purchased L-shaped brackets that fit within the extrusion rails for securing
                multiple components to the support structure - these brackets were used in
                almost every component of the design. We were able to laser-cut a piece
                of plywood to create our support rail that the mechanism rests and slides
                on in our on-campus machine shops. Lastly, we designed and 3D-printed some
                inserts / risers that elevated the support rail above the griddle. The risers
                were printed in PLA and are positioned far enough from the heating element
                to reduce the risk of heat deformation.
                
                ## SUPPORT STRUCTURE IMAGE
                
                Purchasing aluminum extrusions and L-brackets, laser-cutting the plywood
                on-campus, and 3D-printing the risers allowed us to keep costs low,
                reduced our manufacturing time (as opposed to machining metal), and
                allowed for rapid prototyping and design changes (of which there were many)!

@subsection 1s4 
                ##BATTER DISPENSER
                Time for moving parts!
                
                ## BATTER DISPENSER GIF
                
                This component is the "0.5" axis of our 2.5 axis plotter. It dispenses batter
                at a constant rate when told to by the microcontroller, and is made up of a
                syringe for holding batter, an endstop for securing the syringe, a plunger
                mechanism for pushing the batter, a motor and lead screw for creating linear
                dispensing motion, and a PVC tube for moving batter to the nozzle holder.
                
                ## LABELED DISPENSER IMAGE

@subsection 1s5 
                ##TRANSVERSE MOTION

@subsection 1s6 
                ##ROTATIONAL MOTION

@subsection 1s7 
                ##LIMIT SWITCHES AND "ZEROING"

@subsection 1s8 
                ##ELECTRONICS HOUSING

@subsection 1s9 
                ##BILL OF MATERIALS

@section sec_2  SOFTWARE DESIGN
                This section will cover the tasks that we plan on utilizing for
                our 2.5 axis machine. The main taks that we will need include 
                a G-Code task thatconverts G-code into usable coordinates, a
                radial motor task, a transverse motor task, and a syringe motor 
                task. The task diagram below shows how we plan on implimenting
                these tasks into our design through the use of queue and share 
                objects. each task will be discussed more i depth in the following 
                sections.
                
                ## Include picture of task diagram
                

@subsection 2s1 
                ##G-CODE TASK
                The G-Code task will be responsible for the conversion a G-Code
                into coordinates that can be used by our machine. This will be
                accomplished by first converting the G-Code file into cartesian
                coordinates through the use of splicing and appending. These 
                will then be converted to polar coordinates using conversion
                formulas. The radial and transverese coordinates will then be 
                split into seperate quees and then sent off to the appropiaate
                motor task.
                
                ## FSM?
                
@subsection 2s2 
                ##RADIAL MOTOR TASK
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
                
@subsection 2s3 
                ##TRANSVERSE MOTOR TASK
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
                
@subsection 2s4 
                ##SYRINGE MOTOR TASK
                The syringe motor task will be responsible for the dispersion
                of the pancake mixture.
'''

