# Dataset description
This dataset describes a simulation of sensors in the patient's room.
  
  Time : this feature indicates the real time. 
  
  Room Temperature : indicates the inside temperature of the room. According to the standards \cite{chambremalade}, it must be between 18 and 20 degrees whatever the season. 
  
  Outdoor temperature : measures the instantaneous temperature of the exterior.
  
  Room brightness : gives the interior brightness of the room. This value can be between 0 and 100.
  
  state_window : The window can be categorized into two possible states: either closed (value between [0..1]) or open (value between [1..2]).
  
  The bed's state : the bed has three different states: either completely low (between[0.1]), intermediate (between[1.2]) or completely high (between[2.3]).
  
  real_action : indicates the real action that the intelligent assistant should take for a given situation.

The file "8actions_DS.csv" is the dataset used for training the model. The two files "Test2.csv" and "Test_DS" are used for test.
