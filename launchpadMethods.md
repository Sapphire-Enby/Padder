
# Launchpad_py ref
## META - Non methods
### XY Mapping
+---+---+---+---+---+---+---+---+ 
|200|201|202|203|204|205|206|207| < or 0..7 with LedCtrlAutomap()
+---+---+---+---+---+---+---+---+   

+---+---+---+---+---+---+---+---+  +---+
|  0|...|   |   |   |   |   |  7|  |  8|
+---+---+---+---+---+---+---+---+  +---+
| 16|...|   |   |   |   |   | 23|  | 24|
+---+---+---+---+---+---+---+---+  +---+
| 32|...|   |   |   |   |   | 39|  | 40|
+---+---+---+---+---+---+---+---+  +---+
| 48|...|   |   |   |   |   | 55|  | 56|
+---+---+---+---+---+---+---+---+  +---+
| 64|...|   |   |   |   |   | 71|  | 72|
+---+---+---+---+---+---+---+---+  +---+
| 80|...|   |   |   |   |   | 87|  | 88|
+---+---+---+---+---+---+---+---+  +---+
| 96|...|   |   |   |   |   |103|  |104|
+---+---+---+---+---+---+---+---+  +---+
|112|...|   |   |   |   |   |119|  |120|
+---+---+---+---+---+---+---+---+  +---+
### Raw Indexing
  0   1   2   3   4   5   6   7      8   
+---+---+---+---+---+---+---+---+ 
|0/0|1/0|   |   |   |   |   |   |         0
+---+---+---+---+---+---+---+---+ 

+---+---+---+---+---+---+---+---+  +---+
|0/1|   |   |   |   |   |   |   |  |   |  1
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |   |   |   |   |  |   |  2
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |   |5/3|   |   |  |   |  3
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |   |   |   |   |  |   |  4
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |   |   |   |   |  |   |  5
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |4/6|   |   |   |  |   |  6
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |   |   |   |   |  |   |  7
+---+---+---+---+---+---+---+---+  +---+
|   |   |   |   |   |   |   |   |  |8/8|  8
+---+---+---+---+---+---+---+---+  +---+
## Sources Dependencies and Setup
[Source Link:](https://github.com/FMMT666/launchpad.py) link to launchpad_py
[Dependencies:] pygame

>[!Info] Setup:
`pip3 install pygame`
`pip3 install launchpad_py`

    pip3 is used in terminal not python
    these need to be done before main is run 
    if not done before
## Launchpad Model Independant
[In Depth Explanation Link](https://github.com/FMMT666/launchpad.py?tab=readme-ov-file#detailed-description-of-common-launchpad-methods) 
___
>[!abstract] Device control functions
Open( [name], [number], [template (*1*)] )
Close()
==Reset()==
  > Quickly resets the pad and clears lights
ButtonFlush()

>[!abstract] Utility functions
ListAll( [searchString] )
EventRaw()z
## Launchpad Model Specific
[in Depth Explanation Link](https://github.com/FMMT666/launchpad.py?tab=readme-ov-file#detailed-description-of-common-launchpad-methods)
___
>[!abstract]LED functions
LedGetColor( red, green )
  > red and green 0:3
  > returns custom Launchpad color code
  > matching in value
LedCtrlRaw( number, red, green )
  > controls LED via its *number*
LedCtrlXY( x, y, red, green )
  > controls LED via its *coordinates*
LedCtrlRawRapid( allLeds )
  > use bytes to assign multiple pads at once
  > holds placement
LedCtrlRawRapidHome()
  > returns placement to home for led ctrl raw wrap
LedCtrlAutomap( number, red, green )
  > control the top row (legacy?)
LedAllOn()
LedCtrlChar( char, red, green, offsx = 0, offsy = 0 )
LedCtrlString( str, red, green, dir = 0 )

>[!abstract] Button functions
ButtonChanged()
ButtonStateRaw()
ButtonStateXY()
ButtonFlush()
  > do this to avoid lagging, change delay and mem overflow
# END NOTES
if all nodes are going to hold their own color as planned earlier, 
the indexing wont be an issue 
use ==LedCtrlRawRapid== and ==LedGetColor==
also pygame and midi controller will need a dict
to translate the nodes color sting.
with gui:
  1. Select Node to color
  2. Prompt Red Green or Amber or None
  3. store string in cell data
  when updating 
    pygame: get cell boundaries and use cell color as key
    in translation dictionary. for every cell
  4. midi: color dict should return LedGetColor for each colors r and g value
  generate a list of dicts results for all nodes, pass indo ledCtrlRawRapid, rehome.

    red (3,0) green (0,3), amber (3,3)  
  we can decide color with gui ( stick to reg green amber for now)
  

or, when cell click prompt color, draw immedately then adjust x and y pos for midi controlling
literally just add 1 to ypos. but we could save layouts with the previous method
