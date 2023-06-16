# nine_mens_checker
it is a two player game with 9 pawns with each user
alternatively the users must place their pawns.

after placing the 9 pawns of both the user, user can now move the pawn by specifying 
the adress of current and target position.

pawns can be moved only in straight line on the nodes with only one jump to the very adjacent node.
to remember:

  if opponents pawn is just beside our pawn and the next node along the straight line 
  
    if empty: 
            can jump over to that position and take over that opponents pawn , weakening opponents strength,
            
    if not empty:
            cannot move our pawn in that direction.
 
 
 
how to win!....

-a user wins if he captures all the pawns of the opponents.
or
-if he blocks the opponent by making no place to move his pawn. 
