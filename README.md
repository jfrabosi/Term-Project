# Project Proposal
The project our team is planning on developing is a pancake plotter. This system uses a 2.5 axis CNC system to interpret code and plot the batter on a griddle. 
The batter is contained in a 500 mL syringe which is moved along a radial arm via a motor belt system. The raidial arm is mounted to a second motor
which can rotate from -90 to 90 degrees. To reduce the amount of stress on the second motor, a semi-circle will be used to support the end of the radial 
arm. We plan to fabricate the entire system by using 80/20 1" tubing as the structure, using a gridle as a bed, using 3D-printed parts as mounts, and
using laser-cut plywood for the semi-circular support. A bill of materials, breaking down cost, as well as sketches and a gif of our system design can be seen in the figures below.

| Qty. | Part                  | Source                | Est. Cost |
|:----:|:----------------------|:----------------------|:---------:|
|  3   | Pittperson Gearmotors | ME405 Tub             |     -     |
|  1   | Nucleo with Shoe      | ME405 Tub             |     -     |
|  1   | 500 mL Syringe        | Amazon                |   $15.99  |
|  1   | Griddle               | Amazon                |   $26.94  |
|  3   | 80/20 1" Tubing       | Amazon                |   $14.54  |
|  1   | Spool PLA Plastic     | Team's Supply         |     -     |
|  1   | Sheet of Plywood      | Amazon                |   $24.00  |
|  3   | Motor Driver          | ME 405 Tub and Pololu |   $4.95   |


![top down view](https://github.com/jfrabosi/Term-Project/blob/main/docs/TopView.PNG)

FIGURE 1. Top-down view of our overall system.


![close-up](https://github.com/jfrabosi/Term-Project/blob/main/docs/MechanismUpClose.PNG)

Figure 2. Close-up view of our extruder mechanism.


![gif of the assembly](https://github.com/jfrabosi/Term-Project/blob/main/docs/MechanismGif.gif)

Figure 3. Gif of our CAD assembly moving


![real assembly with pen](https://github.com/jfrabosi/Term-Project/blob/main/docs/JustPen.gif)

Figure 4. Gif of our physical assembly plotting a rectangle with a pen attached


![real assembly with batter](https://github.com/jfrabosi/Term-Project/blob/main/docs/slammer.gif)

Figure 5. Gif of our physical assembly strategically disassembling itself


# HARDWARE DESIGN
This section describes the mechanisms, mechanical design, and
manufacturing techniques for each component of our 2.5D plotter.
Each subsection below describes a different component of the design,
explaining how and why we made the decisions that we did.
                
## GENERAL IDEA
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
depositing. A GIF of the mechanism can be seen above in Figure 3.

It should be noted that the rotational-transverse design
is a challenge: surely a Cartesian (X-Y) plotter would be simpler. But
hey, we're Cal Poly MEs; we can take the challenge.

A Bill of Materials (BOM) can be found at the end of this section, listing
names, suppliers, quantities, and costs for each purchased or designed item.

Additionally, all CAD files can be found in the /docs/SOLIDWORKS directory
of this repository.


## GRIDDLE
This is the most straight-forward component. In order to make pancakes,
you need a griddle or other hot-implement. Our team chose the griddle below,
purchased from Amazon for $27, due to its reasonable price and fast shipping
time (did I mention this project only took four weeks?).

![griddle](https://github.com/jfrabosi/Term-Project/blob/main/docs/griddle.PNG)

Figure 6. The griddle

There's really not much else for this one. It's a griddle.


## SUPPORT STRUCTURE
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

![support structure](https://github.com/jfrabosi/Term-Project/blob/main/docs/supportstructure.PNG)

Figure 7. The support structure

Purchasing aluminum extrusions and L-brackets, laser-cutting the plywood
on-campus, and 3D-printing the risers allowed us to keep costs low,
reduced our manufacturing time (as opposed to machining metal), and
allowed for rapid prototyping and design changes (of which there were many)!


## BATTER DISPENSER
Time for moving parts!

This component is the "0.5" axis of our 2.5 axis plotter. It dispenses batter
at a constant rate when told to by the microcontroller, and is made up of a
syringe for holding batter, an endstop for securing the syringe, a plunger
mechanism for pushing the batter, a motor and lead screw for creating linear
dispensing motion, and a PVC tube for moving batter to the nozzle holder.

![extruder](https://github.com/jfrabosi/Term-Project/blob/main/docs/extruder.PNG)

Figure 8. The extruder mechanism

## TRANSVERSE MOTION
To move the location at which batter dispenses (essentially, the location of the
nozzle), we used two axes of motion: transverse (parallel to the syringe) and
radial (rotational about a center axis).

For the transverse motion, we used a belt-driven mechanism that began at our nozzle
carrier. The nozzle carrier has two rectangular slots for the two ends of the belt
to slot into, then two L-brackets slip into the same slots and can be tightened
to fix the belts in position and tension our entire belt system.

![nozzle carrier](https://github.com/jfrabosi/Term-Project/blob/main/docs/nozzlecarrier.PNG)

Figure 9. The nozzle carrier

At either end of the aluminum extrusion there are two 3D-printed parts that slot
into the extrusion ends using careful geometry. The far end piece has three uses:
one, it is used as a pulley for the transverse motion belt; two, it is used as a
load-bearing wheel to ride along the wooden support rail; and three, it holds a limit
switch for the transverse axis. 

![far end stop](https://github.com/jfrabosi/Term-Project/blob/main/docs/farendstop.PNG)

Figure 10. The far end stopper

The other end stop also has multiple uses: one, it holds the transverse axis motor
which drives the belt mechanism; and two, it interfaces with the power transmission
block for the rotational motion motor.

![close end stop](https://github.com/jfrabosi/Term-Project/blob/main/docs/closeendstop.PNG)

Figure 11. The close end stopper

The belt then slides between the slots in the aluminum extrusion. In practice, we
found that this design produced a lot of friction within the transverse axis and
our motor had difficulties providing enough torque to move the nozzle carrier
reliably.


## ROTATIONAL MOTION
For the rotational axis of motion, we used a power transmission block that was
3D-printed (using resin/SLA printing as opposed to the "normal" plastic/FDM 
printing used elsewhere in the project). We used resin printing due to the tight
tolerance requirements associated with this axis of motion; a small bit of backlash
at the rotational motor would amplify over the nearly 14" aluminum extrusion. This
block slotted onto the D-shaft of our high-torque rotational axis motor, and the
edges of the cube then slotted into a tight-fitting cavity on the close end stopper
in the previous section.

![transmission system](https://github.com/jfrabosi/Term-Project/blob/main/docs/transmission.PNG)

Figure 12. The rotational power transmission system

The DC motor then slotted into a 3D-printed housing that interfaced with an
aluminum extrusion part of the support system. This component was ultimately our
worst-performing component: after lots of testing, the power transmission cube
and housing began to show severe signs of wear and produced very large amounts of
backlash into our system.

![rotational motor housing](https://github.com/jfrabosi/Term-Project/blob/main/docs/rotmotor.PNG)

Figure 13. The rotational motor and housing


## LIMIT SWITCHES AND "ZEROING"
To figure out where all of our motors were at the beginning of each "print", we
devised a system using limit switches to trigger when each axis was at its "zero"
position. For the transverse axis, we positioned the limit switch at the far end
of the aluminum extrusion as part of the far end stopper part. For the rotational
axis, we positioned the limit switch at the furthest-right position on the wooden
support rail, as part of a 3D-printed weight supporter.

![rotational limit switch](https://github.com/jfrabosi/Term-Project/blob/main/docs/rotswitch.PNG)

Figure 14. The rotational limit switch

We created a unified limit-switch holder based on the geometry of the limit switches
we purchased (listed in the BOM). The geometry is very precise and thus required
all of the limit switch holders to be 3D-printed in resin. For the transverse axis,
the entire end stopper was printed in resin so this wasn't an issue. However, for
the rotational axis, you can see a small part sitting atop the larger structure.
The large structure is FDM, while the small part is resin.

For the batter extrusion axis, we took a slightly different approach. Instead of
zeroing this axis at the start of each print, we positioned a limit switch between
the plunger and the syringe housing so it would be activated when the plunger was
fully closed (and therefore there was no more batter to dispense). This part was
resin printed and used an L-bracket to attach to the rail.

![batter limit switch](https://github.com/jfrabosi/Term-Project/blob/main/docs/batswitch.PNG)

Figure 15. The batter extrusion limit switch

## SOFTWARE ADDENDUM

Our task diagram and two motor FSMs (radial and transverse) can be seen below.

![task diagram](https://github.com/jfrabosi/Term-Project/blob/main/Images/Task_Diagram.jpg)

Figure 16. Task diagram 

![rad FSM](https://github.com/jfrabosi/Term-Project/blob/main/Images/Rad_MotorFSM.jpg)

Figure 17. Radial motor FSM

![trans FSM](https://github.com/jfrabosi/Term-Project/blob/main/Images/Trans_MotorFSM.jpg)

Figure 18. Transverse motor FSM


## RESULTS
After assembling the pancake plotter and uploading the code to the Nucleo STM 32,
our group was able to successfully plot a square using a marker and g-code created 
by taking points on an image and converting them to polar corrdinates using a cartesian 
to polar converting script. When implementing the pancake batter and syringe into the 
system, the team ran into issues with the amount of torque transmitted by the radial 
axis motor. The torque required to accurately recreate the square pattern we had achieved 
with the marker required a much higher torque than our motor and fixture could apply.
The pancake  batter and syringe added too much weight on the cantilever beam which after 
much testing resulted in our mechanism transferring power from the motor to the shaft 
shattering. Despite not being able to implement the pancake batter, the team found 
success in being able to plot a shape given the cartesian coordinates with a reasonable 
degree of accuracy, proving that our concept worked through the use of our designed 
hardware and corresponding code. 