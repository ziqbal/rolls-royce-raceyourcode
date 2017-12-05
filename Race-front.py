
AimForLane( 1.5 )
Speed( 100 )

WaitForGo( )

while Globals.running :

    WaitForWaypoint( 2 )
    AimForLane( 1.5 )
    Speed( 100 )

    WaitForSeconds( 0.01 )
    pass

